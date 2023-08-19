def platesBetweenCandles(s, queries):
    candleDict = {}  # candle index -> number of plates before candle
    plateCount = 0

    # initialize candleDict
    for i in range(len(s)):
        if s[i] == '*':
            plateCount += 1
        else:
            candleDict[i] = plateCount

    # find leftmost candle in query
    def findLeftmostCandle(l, r):
        while l <= r:
            if l in candleDict:
                return l
            l += 1

        # return -1 if no candles found in range
        return -1

    # find rightmost candle in query
    def findRightmostCandle(l, r):
        while r >= l:
            if r in candleDict:
                return r
            r -= 1

        # return -1 if no candles found in range
        return -1

    res = []
    for query in queries:
        # get index of leftmost candle in query
        lCandle = findLeftmostCandle(query[0], query[1])

        if lCandle == -1:
            res.append(0)
            continue

        # get index of rightmost candle in query
        rCandle = findRightmostCandle(lCandle + 1, query[1])

        if rCandle == -1:
            res.append(0)
            continue

        platesBetween = candleDict[rCandle] - candleDict[lCandle]
        res.append(platesBetween)

    return res


print(platesBetweenCandles(s="**|**|***|", queries=[[2, 5], [5, 9]]))
print(platesBetweenCandles(s="***|**|*****|**||**|*",
      queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
