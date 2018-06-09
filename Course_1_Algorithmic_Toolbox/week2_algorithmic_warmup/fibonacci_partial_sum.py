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


def fibonacci_sum(n):
    ll       =[0, 1]
    sum_list =[0, 1]
    for i in range(2, n + 1):
        kk = calc_fib(i) % 10
        ll.append(kk)
        sum_list.append(sum(ll) % 10)
        if (sum_list[i] == 1 ) and (sum_list[i - 1] == 0):
            period = sum_list[0: -2]
            length = len(period)
            return(period[n % length])
            break
    return(sum(ll[0: n+1]) % 10)

def fibonacci_partial_sum(from_, to):
    out=(fibonacci_sum(to)-fibonacci_sum(from_-1)+10)%10
    return(out)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
