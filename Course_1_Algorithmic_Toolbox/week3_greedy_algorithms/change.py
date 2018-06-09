# Uses python3
import sys

def get_change(m):
    count = 0
    while m >= 10:
        m     = m - 10
        count = count + 1
        if m == 0:
            return(count)
    while m >=5 :
        m     = m - 5
        count = count + 1
        if m == 0:
            return(count)
    count = count + m
    return (count)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
