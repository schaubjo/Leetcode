from collections import deque


def secondsToHours(seconds):
    return seconds / 60 / 60


class LogServer:
    def __init__(self, m):
        self.logs = deque()
        self.maxLogs = m

    def recordLog(self, logId, timestamp):
        self.logs.appendleft((timestamp, logId))
        while timestamp - self.logs[-1][0] >= 60 * 60:
            self.logs.pop()

    def getLogs(self):
        start = self.maxLogs - \
            1 if len(self.logs) >= self.maxLogs else len(self.logs) - 1
        end = -1
        while start > end:
            if start > 0:
                print(f"{self.logs[start][1]}, ", end="")
            else:
                print(self.logs[start][1])
                break

            start -= 1
        # count = 0
        # i = len(self.logs) - 1
        # for i in range(len(self.logs) - 1, len(self.logs) - self.maxLogs - 1, -1):
        #     if i > 0:
        #         print(f"{self.logs[i][1]}, ", end="")
        #     else:
        #         print(self.logs[i][1])
        #         break

    def getLogCount(self):
        print(len(self.logs))


def main():
    log = LogServer(-1)
    with open('recordLogsInput.txt', 'r') as file:
        for line_number, line in enumerate(file):
            line = line.strip().split()

            if line_number == 0:
                log.maxLogs = int(line[0])
            elif line_number == 1:
                continue
            else:
                if line[0][0] == 'R':
                    log.recordLog(int(line[1]), int(line[2]))
                elif line[0][0] == 'G':
                    log.getLogs()
                else:
                    log.getLogCount()


main()
