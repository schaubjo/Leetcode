def generate(numRows):
    pascal = [[] for _ in range(numRows)]
    pascal[0].append(1)
    for row in range(1, numRows):
        pascal[row].append(1)
        # insert center tiles
        # number of center tiles = row - 1
        for i in range(row - 1):
            pascal[row].append(pascal[row - 1][i] + pascal[row - 1][i + 1])
        pascal[row].append(1)

    return pascal


print(generate(5))
