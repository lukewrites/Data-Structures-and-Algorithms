# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    # first, I want a list of the values by weight
    value_by_weight = []
    for i in range(0, n):
        value_by_weight.append(values[i]//weights[i])
    while value < capacity:


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
