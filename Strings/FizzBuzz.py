def fizzBuzz(n):
    res = [1] * n
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            res[i - 1] = "FizzBuzz"
        elif i % 3 == 0:
            res[i - 1] = "Fizz"
        elif i % 5 == 0:
            res[i - 1] = "Buzz"
        else:
            res[i - 1] = str(i)

    return res


print(fizzBuzz(3))
