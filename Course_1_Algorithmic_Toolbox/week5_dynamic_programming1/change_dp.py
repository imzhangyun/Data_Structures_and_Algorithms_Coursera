# Uses python3
import sys

def get_change(m):
    #write your code here
    array = [0, 1, 2, 1, 1]
    for i in range(5, m + 1):
        choice = min(array[i - 1], array[i - 3], array[i - 4])
        array.append(choice + 1)
    return (array[m])

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
