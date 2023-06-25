# def findMinDifference(timePoints):
#     minutes = [(int(s[:2]) * 60 + int(s[3:])) for s in timePoints]
#     minutes = sorted(minutes)
#     minimum = float('inf')
#     for i in range(len(minutes) - 1):
#         j = i + 1
#         difference = minutes[j] - minutes[i]
#         minimum = min(minimum, difference, 1440 - minutes[j] + minutes[i])

#     last = len(minutes) - 1

#     minimum = min(minimum, minutes[last] - minutes[0],
#                   1440 - minutes[last] + minutes[0])
#     return minimum

def findMinDifference(timePoints):
    time_seen = [False] * 1440
    for time in timePoints:
        minutes = int(time[:2]) * 60 + int(time[3:])
        if time_seen[minutes]:
            return 0
        time_seen[minutes] = True

    first, prev = -1, -1
    minimum = float('inf')
    for i in range(1440):
        if time_seen[i]:
            if first == -1:
                first, prev = i, i
            else:
                minimum = min(minimum, i - prev, 1440 - i + prev)
                prev = i

    minimum = min(minimum, 1440 - prev + first)
    return minimum


print(findMinDifference(["23:59", "00:00"]))
print(findMinDifference(["12:12", "12:13"]))
print(findMinDifference(["00:00", "04:00", "22:00"]))
print(findMinDifference(["12:12", "00:13"]))
