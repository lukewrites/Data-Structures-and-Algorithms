# Uses python3
import sys

def get_change(m):
    coins = 0
    if m % 10 != 0:
        pass
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
