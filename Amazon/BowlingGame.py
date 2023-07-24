def isWinner(player1, player2):
    pins1, pins2 = 0, 0
    N = len(player1)
    for i in range(N):
        doubled1 = False
        doubled2 = False
        if i > 0:
            if player1[i - 1] == 10:
                pins1 += player1[i] * 2
                doubled1 = True

            if player2[i - 1] == 10:
                pins2 += player2[i] * 2
                doubled2 = True

        if i > 1:
            if player1[i - 2] == 10 and not doubled1:
                pins1 += player1[i] * 2
                doubled1 = True

            if player2[i - 2] == 10 and not doubled2:
                pins2 += player2[i] * 2
                doubled2 = True

        if not doubled1:
            pins1 += player1[i]
        if not doubled2:
            pins2 += player2[i]

    if pins1 > pins2:
        return 1
    elif pins2 > pins1:
        return 2
    else:
        return 0


print(isWinner(player1=[4, 10, 7, 9], player2=[6, 5, 2, 3]))
print(isWinner(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2]))
print(isWinner(player1=[2, 3], player2=[4, 1]))
print(isWinner([7, 8, 8, 5, 2], [10, 1, 4, 2, 6]))
