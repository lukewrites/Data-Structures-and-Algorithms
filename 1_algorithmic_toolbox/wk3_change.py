# Uses python3
import sys

def get_change(m, coins):

    while m:
        if m - 10 >= 0:
            m -= 10
            coins += 1
            return get_change(m, coins)
        if m - 5 >= 0:
            m -= 5
            coins += 1
            return get_change(m, coins)
        if m - 1 >= 0:
            m -= 1
            coins += 1
            return get_change(m, coins)

    return coins

    # The below is a one-line answer...but it isn't greedy!
    # return num % 5+((num-(num % 5)) % 10 // 5) + ((num - (num % 10)) // 10)

if __name__ == '__main__':
    num = int(sys.stdin.read())
    print(get_change(num, 0))
