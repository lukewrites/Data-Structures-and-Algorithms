#Uses python3

import sys

def min_dot_product(a, b, n):
    a = sorted(a)
    b = sorted(b, reverse=True)
    res = 0
    for i in range(n):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b, n))
