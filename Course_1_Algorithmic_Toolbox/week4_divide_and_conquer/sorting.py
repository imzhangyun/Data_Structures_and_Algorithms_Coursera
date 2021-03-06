# Uses python3
import sys
import random

def partition3(a, l, r):

    x = a[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            k = k + 1
            j = j + 1

            a[k], a[j], a[i] = a[i], a[k], a[j]

    a[l: j + 1] = a[l: j+1][::-1]

    return (j)


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
        
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end = ' ')
     
