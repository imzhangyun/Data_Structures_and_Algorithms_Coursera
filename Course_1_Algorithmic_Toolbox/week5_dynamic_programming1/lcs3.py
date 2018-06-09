#Uses python3

import sys
import numpy as np

def lcs3(a, b, c):
    a_len  = len(a)
    b_len  = len(b)
    c_len  = len(c)
    matrix = np.zeros((a_len + 1, b_len + 1, c_len + 1))
    
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            for k in range(1, c_len + 1):
            
                unmatch1 = matrix[i - 1, j    , k]
                unmatch2 = matrix[i - 1, j - 1, k]               
                unmatch3 = matrix[i - 1, j    , k - 1]
                unmatch4 = matrix[i - 1, j - 1, k - 1]
                unmatch5 = matrix[i    , j - 1, k]
                unmatch6 = matrix[i    , j - 1, k - 1]
                unmatch7 = matrix[i    , j    , k - 1]
                
                

                if a[i - 1] == b[j - 1] == c[k - 1]:
                    matrix[i, j, k] = max(unmatch1, unmatch2, unmatch3, unmatch4,
                                      unmatch5, unmatch6, unmatch7 + 1)

                else:
                    matrix[i, j, k] = max(unmatch1, unmatch2, unmatch3, unmatch4,
                                      unmatch5, unmatch6, unmatch7)
                
    return (int(matrix[a_len, b_len, c_len]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
