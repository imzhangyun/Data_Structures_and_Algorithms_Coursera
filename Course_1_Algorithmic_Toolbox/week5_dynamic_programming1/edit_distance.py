# Uses python3

import numpy as np
def edit_distance(s, t):
    s_len = len(s)
    t_len = len(t)
    
    matrix = np.zeros((s_len + 1, t_len + 1))
    matrix[0, :] = range(t_len + 1)
    matrix[:, 0] = range(s_len + 1)
    
    
    for i in range(1, s_len + 1):
        for j in range(1, t_len + 1):
            deletion  = matrix[i - 1, j] + 1
            insertion = matrix[i, j - 1] + 1
            mismatch  = matrix[i - 1, j - 1] + 1
            match     = matrix[i - 1, j - 1]
            
            if s[i - 1] == t[j - 1]:
                matrix[i, j] = min(deletion, insertion, match)
            else:
                matrix[i, j] = min(deletion, insertion, mismatch)
    return(int(matrix[s_len, t_len]))

if __name__ == "__main__":
    print(edit_distance(input(), input()))
