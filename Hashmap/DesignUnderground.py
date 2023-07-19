class UndergroundSystem:

    def __init__(self):
        self.startDict = {}  # id -> (startStation, startTime)
        self.routes = {}  # (start, end) -> [time1, time2, ...]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startDict[id] = (stationName, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation = self.startDict[id][0]
        startTime = self.startDict[id][1]

        route = (startStation, endStation)
        timeTaken = t - startTime
        if route not in self.routes:
            self.routes[route] = [timeTaken]
        else:
            self.routes[route].append(timeTaken)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        totalTime = 0
        for time in self.routes[route]:
            totalTime += time
        numPeople = len(self.routes[route])
        return totalTime / numPeople

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
