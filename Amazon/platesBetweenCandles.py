def platesBetweenCandles(s, queries):
    platesBeforeCandle = []
    plateCount = 0

    # initialize platesBeforeCandle
    for i in range(len(s)):
        if s[i] == '*':
            plateCount += 1
            platesBeforeCandle.append(-1)
        else:
            platesBeforeCandle.append(plateCount)

    # create list of the leftmost candle to index
    leftmostCandle = [-1 for _ in s]
    leftmost = -1
    for i in range(1, len(s)):
        if s[i] == '|':
            leftmost = i
        leftmostCandle[i] = leftmost

    # create list of the rightmost candle to index
    rightmostCandle = [-1 for _ in s]
    rightmost = -1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '|':
            rightmost = i
        rightmostCandle[i] = rightmost

    res = []
    for query in queries:
        # find rightmost candle of left bound
        rightmost = rightmostCandle[query[0]]
        if rightmost == -1:
            res.append(0)
            continue

        # find leftmost candle of right bound
        leftmost = leftmostCandle[query[1]]
        if leftmost == -1:
            res.append(0)
            continue

        # find candles between rightmost and leftmost
        difference = platesBeforeCandle[leftmost] - \
            platesBeforeCandle[rightmost]

        if difference <= 0:
            res.append(0)
        else:
            res.append(difference)

    return res


print(platesBetweenCandles(s="**|**|***|", queries=[[2, 5], [5, 9]]))
print(platesBetweenCandles(s="***|**|*****|**||**|*",
      queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
print(platesBetweenCandles("||*", [[2, 2]]))
