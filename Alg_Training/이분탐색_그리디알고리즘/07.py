import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
L = int(input())
a = list(map(int, input().split()))
M = int(input())

def find(a, value):
    res = -1
    for i in range(L):
        if(a[i] == value):
            res = i
    return res

a.sort()
for _ in range(M):
    maxI = find(a, max(a))
    minI = find(a, min(a))
    
    a[minI] += 1
    a[maxI] -= 1
    
print(max(a) - min(a))
'''
###################################################################
L = int(input())
a = list(map(int, input().split()))
M = int(input())

a.sort()
for _ in range(M):
    a[0] += 1
    a[L - 1] -= 1
    
    a.sort()

print(a[L - 1] - a[0])