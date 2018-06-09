# Uses python3
import sys

def optimal_summands(n):
    if n == 1:
        return([1])
    for i in range(1, n+1):
        if i > n:          
            out     = list(range(1, i))[:i]
            out[-1] = out[-1] + n
            return(out)
        n = n - i
        
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
