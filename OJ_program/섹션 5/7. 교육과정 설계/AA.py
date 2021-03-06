from collections import deque
# 문제점 : 필수 과목 순서가 일부 맞지만, 일부 필수 과목을 중복수강해서 생기는 문제.
# 해결 : 

tmp = input()
N = int(input())

for i in range(1, N + 1):
    necessary = deque(list(tmp))
    a = deque(list(input()))
    
    for j in range(len(a)):
        if (necessary[0] == a[0]):
            necessary.popleft()
            a.popleft()
        else:
            if a[0] in necessary:
                break
            a.append(a.popleft())
        if (len(necessary) == 0):
            break
        
    print("#", i, end=' ')
    if(len(necessary) != 0):
        print("NO")
    else:
        print("YES")