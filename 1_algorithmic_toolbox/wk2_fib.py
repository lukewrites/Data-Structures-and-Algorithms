# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        fibs = [0, 1]
        for number in range(1, n):
            fibs.append(fibs[number] + fibs[number-1])
    return fibs[n]

# This is coursera boilerplate that isn't necessary outside of there.
# n = int(input())
# print(calc_fib(n))
