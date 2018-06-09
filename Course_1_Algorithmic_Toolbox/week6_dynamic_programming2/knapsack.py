# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    
    bag = [0] * (W + 1)
    if W < min(w):
        return(0)
    elif W in w:
        return(W)
    elif W >= sum(w):
        return(sum(w))
    
    w = [x for x in w if x < W]
    w.sort()
    candidate = [0, w[0]]

    for i in w[1:]:       
        length = len(candidate)
        for index in range(length):
            if candidate[index] + i <= W:
                candidate.append(candidate[index] + i)
            candidate.append(i)

        candidate = list(set(candidate))

    maximun = max(candidate)
    return(maximun)    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
