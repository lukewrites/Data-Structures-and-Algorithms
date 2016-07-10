# Uses python3
import sys

def get_fibonacci_last_digit(n):
    fibs = [0, 1]
    for i in range(1, n):
        fibs.append((fibs[i] + fibs[i-1]) % 10)
    return fibs[n]

# coursera boilerplate
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(get_fibonacci_last_digit(n))
