# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a) - 1
    for _ in range(len(a) + 1):
        if a[(right + left) // 2] == x:
            return((right + left) // 2)
        elif right == left:
            return(-1)
        elif a[(right + left) // 2] > x:
            left, right = left, (right + left) // 2
        else:
            left, right = (right + left) // 2 + 1, right

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
