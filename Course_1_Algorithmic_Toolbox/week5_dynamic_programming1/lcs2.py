#Uses python3

import sys
import numpy as np
def lcs2(s, t):
    s_len = len(s)
    t_len = len(t)
    
    matrix = np.zeros((s_len + 1, t_len + 1))
    
    for i in range(1, s_len + 1):
        for j in range(1, t_len + 1):
            deletion  = matrix[i - 1, j]
            insertion = matrix[i, j - 1]
            mismatch  = matrix[i - 1, j - 1]
            match     = matrix[i - 1, j - 1] + 1
            
            if s[i - 1] == t[j - 1]:
                matrix[i, j] = max(deletion, insertion, match)

            else:
                matrix[i, j] = max(deletion, insertion, mismatch)

    return(int(matrix[s_len, t_len]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
