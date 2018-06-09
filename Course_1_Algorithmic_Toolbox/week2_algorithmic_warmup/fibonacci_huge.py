# Uses python3
import sys
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        l = [0, 1]
        for i in range(2, n+1):
            k = l[i - 1] + l[i - 2]
            l.append(k)           
    return (l[n])

def get_fibonacci_huge(n, m):
    previous = 0
    current  = 1
    for i in range(n):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            length = i + 1
            return(calc_fib(n % length) % m)
            break
    return(calc_fib(n) % m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
