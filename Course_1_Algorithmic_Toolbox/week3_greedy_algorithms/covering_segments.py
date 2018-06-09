# Uses python3
import sys
from collections import namedtuple
import numpy as np

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    for s in segments:
        points.append(s.start)
        points.append(s.end)

    time   = []
    points = np.array(points).reshape((int(len(points) / 2), 2))
    k      = points.shape[0]
    for _ in range(k):
        min_end = min(points[:, 1])
        i       = np.where(points[:,0] <= min_end)[0]
        time.append(max(points[i,0]))
        
        if points.shape[0] == i.shape[0]:
            break
        else:
            points = np.delete(points, i, 0)
    return(time)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
