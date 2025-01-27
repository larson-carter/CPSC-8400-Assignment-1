import os, sys

# This imports from a file that will be present in the
# grading system. No need to alter for local testing -
# if the file isn't present then these lines are skipped
try:
    from compile_with_soln import grader_stub

    grader = grader_stub()
except:
    pass


# ----------------------------------------
# This function, grader.call_grader() (which will be
# present with our code when it is submitted to the
# grading system), takes an integer index i and returns
# A[i].

# If you pass an invalid index or call this function
# more than 64 times, you'll get back -1

# grader.call_grader(i)
# ----------------------------------------

# For testing on your own system, you can call
# this function instead. It uses an array of length 100
# with values 0, 100, 200, 8300, 8400, 8300, 8200, ...
# Don't forget to switch your code back to calling
# grader.call_grader() before submitting.
def getSystemGrader(i):
    return grader.call_grader(i)
    #return 8400 - abs(84 - i) * 100

def search(low, high, N, getSystemGrader):
    while high - low > 2:
        midPoint1, midPoint2 = (low + (high - low) // 3), (high - (high - low) // 3)
        pointOne, pointTwo = getSystemGrader(midPoint1), getSystemGrader(midPoint2)
        low, high = (midPoint1, high) if pointOne < pointTwo else (low, midPoint2)

    return low, high

def maxPosition(low, high, getSystemGrader):
    maxValue = -float('inf')
    highestPointIndex = -1

    for i in range(low, high + 1):
        value = getSystemGrader(i)
        if value == -1:
            continue
        if value > maxValue:
            maxValue = value
            highestPointIndex = i

    return maxValue, highestPointIndex

def find_highestPointIndex(N, getSystemGrader):
    low = 0
    high = N - 1
    highestPointIndex = -1
    maxValue = -float('inf')
    low, high = search(low, high, N, getSystemGrader)
    maxValue, highestPointIndex = maxPosition(low, high, getSystemGrader)

    if highestPointIndex == -1:
        highestPointIndex = 0

    return highestPointIndex

def main():
    # Value for N is set in the grading system
    # through an environment variable, if present.
    # If this isn't present, the default values is N = 100

    try:
        N = int(os.environ["N"])
    except:
        N = 100

    solution = find_highestPointIndex(N, getSystemGrader)

    print(solution)

if __name__ == "__main__":
    main()