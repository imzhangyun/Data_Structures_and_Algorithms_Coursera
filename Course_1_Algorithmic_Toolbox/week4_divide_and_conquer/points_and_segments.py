# Uses python3
import sys
import numpy as np


def fast_count_segments(starts, ends, points):

    A = []
    for l in starts:
        A.append([l, "a"])
    for r in ends:
        A.append([r, "c"])
    for p in points:
        A.append([p, "b"])
    A.sort()
    
    segments = 0
    result   = {}

    for j in A:
        if j[1]   == "b":
            result[j[0]] = segments
        elif j[1] == "a":
            segments += 1
        elif j[1] == "c":
            segments -= 1
  
    return (result)

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in points:
        print(cnt[x], end=' ')
