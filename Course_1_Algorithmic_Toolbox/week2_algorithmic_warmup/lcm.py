# Uses python3
import sys
def gcd(a, b):
    if a  < b:
        a, b = b, a
    if b == 0:
        return(a)
    else:
        aa = a % b
        return gcd(b, aa)

def lcm(a, b):
    return (int(a * b // gcd(a, b)))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

