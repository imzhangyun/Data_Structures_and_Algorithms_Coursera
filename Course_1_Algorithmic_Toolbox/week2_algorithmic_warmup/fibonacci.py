# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        l = [0,1]
        for i in range(2, n+1):
            k = l[i - 1] + l[i - 2]
            l.append(k)           
    return (l[n])

n = int(input())
print(calc_fib(n))
