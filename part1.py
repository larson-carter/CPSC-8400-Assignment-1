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
# more than 32 times, you'll get back -1

# grader.call_grader(int i)
# ----------------------------------------

# For testing on your own system, you can call
# this function instead.  It uses an array of length 10
# with values 1000, 2000, 3000, ..., 10,000.
# Don't forget to switch your code back to calling
# grader.call_grader() before submitting.
def call_grader_local(i):
    A = [1000, 2000, 3000, 4000, 5000,
         6000, 7000, 8000, 9000, 10000]
    return A[i]

def getSystemGrader(i):
    return grader.call_grader(i)
    #return call_grader_local(i)

def checkLowParam(low, N, T, getSystemGrader, difference, index):
    if low < N:
        lowParam = getSystemGrader(low)
        if lowParam != -1:
            distanceLowParam = abs(lowParam - T)
            if distanceLowParam < difference:
                difference = distanceLowParam
                index = low
    return difference, index

def checkHighParam(high, N, T, getSystemGrader, difference, index):
    if high >= 0:
        highParam = getSystemGrader(high)
        if highParam != -1:
            distanceHighParam = abs(highParam - T)
            if distanceHighParam < difference:
                difference = distanceHighParam
                index = high
    return difference, index

def findNearestValue(N, T):
    low = 0
    high = N - 1
    index = -1
    difference = float('inf')

    while low <= high:
        mid = (low + high) // 2
        value = getSystemGrader(mid)

        if value == -1:
            break

        diff = abs(value - T)

        if diff < difference:
            difference = diff
            index = mid

        # Punch the search pointers based on comparison
        if value < T:
            low = mid + 1
        elif value > T:
            high = mid - 1
        else:
            index = mid
            break

    if difference != 0:
        difference, index = checkLowParam(low, N, T, getSystemGrader, difference, index)
        difference, index = checkHighParam(high, N, T, getSystemGrader, difference, index)

    # No valid index was found
    if index == -1:
        index = 0

    return index

def main():
    # Values for N and T are set in the grading system
    # through environment variables, if present.
    # If these aren't present, the default values are N = 10
    # and T = 8400.

    try:
        N = int(os.environ["N"])
        T = int(os.environ["T"])
    except:
        N = 10
        T = 8400

    index = findNearestValue(N, T)

    print(index)

if __name__ == "__main__":
    main()