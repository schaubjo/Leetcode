from functools import cache


def uniquePaths(m, n):
    @cache
    def dfs(r, c):
        if r > m - 1 or c > n - 1:
            return 0

        if r == m - 1 and c == n - 1:
            return 1

        return dfs(r + 1, c) + dfs(r, c + 1)

    return dfs(0, 0)


print(uniquePaths(m=3, n=2))
