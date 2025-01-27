import os, sys, random

# This imports from a file that will be present in the
# grading system. No need to alter for local testing -
# if the file isn't present then these lines are skipped
try:
    from compile_with_soln import grader_stub

    grader = grader_stub()
except:
    pass


# ----------------------------------------
# This function (which will be compiled with our code
# when it is submitted to the grading system) takes
# a list of values of x and returns a list of
# values of f(x) for all of them.

# If you pass it a list of length more than K,
# you'll only get back the first K answers.
# If you call it more than R times, you'll start to
# get back empty lists.
# If you pass any values of x outside [0,1], you'll
# get back corresponding values of -1.

# grader.call_grader(x)
# ----------------------------------------

# For testing on your own system, you can call
# this function instead. It uses an array of length 100
# with values 0, 100, 200, 8300, 8400, 8300, 8200, ...
# Don't forget to switch your code back to calling
# grader.call_grader() before submitting.
def getSystemGrader(x):
    return grader.call_grader(x)

    # result = []
    # for i in range(len(x)):
    #     result.append(1.0 - abs(x[i] - 0.8400))
    # return result

def generateRandomValue(K):
    return [random.random() for _ in range(K)]

def calcValue(K, getSystemGrader):
    xValueSet = generateRandomValue(K)
    yValueSet = getSystemGrader(xValueSet)
    return xValueSet, yValueSet

def updateBestValue(best, x, y):
    if y > best:
        bestYValue = y
        bestXValue = x
        return bestYValue, bestXValue
    return best, None

def calcPreciseXValue(K, R, getSystemGrader):
    bestYValue = -float('inf')
    bestXValue = 0.5

    for z in range(R):
        xValueSet, yValueSet = calcValue(K, getSystemGrader)

        for x, y in zip(xValueSet, yValueSet):
            if y == -1:
                continue
            newBest, newXValue = updateBestValue(bestYValue, x, y)
            if newXValue is not None:
                bestYValue = newBest
                bestXValue = newXValue

    return bestXValue

def main():
    # Values for K and R are set in the grading system
    # through environment variables, if present.
    # If these aren't present, the default values are K = 4, R = 7

    try:
        K = int(os.environ["K"])
        R = int(os.environ["R"])
    except:
        K = 4
        R = 7

    result = calcPreciseXValue(K, R, getSystemGrader)

    print(result)

if __name__ == "__main__":
    main()