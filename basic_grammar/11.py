'''
함수 만들기

# C언어처럼 전처리자가 없기 때문에 항상 함수 정의부는 위에 배치 시킬 것.
def add(a, b):
    c = a + b
    print(c)

add(3, 2)
######################################################################################
# 튜플 형태로 리턴하는 함수.
def calc(a, b):
    c = a + b
    d = a - b
    return c, d

a, s = calc(3, 2)
print(a, ",", s)

'''
def isPrime_1(x):
    if any((x%i == 0) for i in range(2, x)):
        return False
    else:
        return True

def isPrime_2(x):
    for i in range(2, x):
        if(x%i == 0):
            return False
    else:
        return True
######################################################################################
a = [12, 13, 7, 9, 19]
for y in a:
    if(isPrime_1(y)):
        print(y, end=' ')
        
######################################################################################
## 주의할 점
################################################################################
'''
전역 변수 vs 지역 변수

* 파이썬에서 변수의 사용은 지역/전역 상관없이 사용 가능하다.         
'''
N = 9

def func1():
    for _ in range(N):
        print("Iteration")
        
'''
하지만, 전역변수를 함수 내부에서 초기화하려면 에러(런타임 에러)가 발생하기 때문에,
사용하려는 변수가 전역 변수임을 알려줘야한다. (global 키워드 사용.)
'''

M = -2147000000
a = [3, 5, 4, -2, -1]

def findMinimum(a):
    global M    # 함수한테 M이 전역변수임을 알려준다. 
    for e in a:
        if(e < M):
            M = e
