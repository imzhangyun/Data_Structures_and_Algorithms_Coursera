#Uses python3

import sys
import numpy as np

def compare(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)):
        return(a)
    else:
        return(b)

def largest_number(D):
    answer = ''
    while D:
        max_d = 0
        for d in D:
            max_d = compare(d, max_d)
        answer = answer + str(max_d)
        D.remove(max_d)
    return(int(answer))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
