# Uses python3
import sys
import itertools

def partition3(A):
    if sum(A) % 3 != 0 :
        return(0)
    else:
        target = int(sum(A) / 3)
        A.sort(reverse = True)
        
        check = 0
        for _ in [1, 2, 3]:
            if len(A) == 0:
                break
                
            else:
                candidate = {0: [0]}
                for i in A:
                    tmp = {}
                    for element in candidate:
                        tmp[element + i] = candidate[element] + [i]
                        tmp[i]           = [i]
                    candidate = {**tmp, **candidate}
                    if target in candidate:
                        for a in candidate[target]:
                            A.remove(a)
                        check = check +1 
                        break

        if check == 3 :
            return(1)
        else: return(0)  

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

