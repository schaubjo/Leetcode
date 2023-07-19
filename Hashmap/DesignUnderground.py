class UndergroundSystem:

    def __init__(self):
        self.startDict = {}  # id -> (startStation, startTime)
        self.routes = {}  # (start, end) -> [timeSum, numTimes]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startDict[id] = (stationName, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation = self.startDict[id][0]
        startTime = self.startDict[id][1]

        route = (startStation, endStation)
        timeTaken = t - startTime
        if route not in self.routes:
            self.routes[route] = [timeTaken, 1]
        else:
            self.routes[route][0] += timeTaken
            self.routes[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.routes[route][0] / self.routes[route][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
