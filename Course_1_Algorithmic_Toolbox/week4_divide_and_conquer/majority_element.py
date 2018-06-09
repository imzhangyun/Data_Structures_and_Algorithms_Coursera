# Uses python3
import sys

def get_majority_element(a):
    dic = {}
    for element in a:
        if element in dic:
            dic[element] = dic[element] + 1
        else:
            dic[element] = 1
    if any(x > len(a) / 2 for x in list(dic.values())):
        return(1)
    else:
        return(0)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #if get_majority_element(a, 0, n) != -1:
        #print(1)
    #else:
        #print(0)
    print(get_majority_element(a))
