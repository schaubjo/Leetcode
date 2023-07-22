def checkStraightLine(coordinates):
    def getSlope(c1, c2):
        # edge case: divide by zero error; vertical slope
        if c2[0] - c1[0] == 0:
            return float('inf')
        return (c2[1] - c1[1]) / (c2[0] - c1[0])

    # iterate through all coordinates, if slope ever changes, return false
    currSlope = getSlope(coordinates[0], coordinates[1])
    for i in range(2, len(coordinates)):
        if currSlope != getSlope(coordinates[i - 1], coordinates[i]):
            return False

    return True


print(checkStraightLine([[0, 0], [0, 1], [0, -1]]))
print(checkStraightLine(coordinates=[
      [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(checkStraightLine(coordinates=[
      [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
