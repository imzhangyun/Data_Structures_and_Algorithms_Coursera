# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    if len(weights) == 1:
        if capacity > weights[0]:
            return(values[0])
        else:
            return(value + values[0] * capacity / weights[0])

    else:
        rate = []
        for a, b in zip(weights, values):
            rate.append(b / a)
        while capacity > 0:
            if len(rate) == 0:
                return(value)

            else:
                i = rate.index(max(rate))
                if weights[i] >= capacity:
                    return(value + values[i] * capacity / weights[i])
                else:
                    value    = value + values[i]
                    capacity = capacity - weights[i]
                    rate.pop(i)
                    weights.pop(i)
                    values.pop(i)
        return(value)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
