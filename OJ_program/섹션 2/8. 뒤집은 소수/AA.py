def reverse(x):
    itos = str(x)
    stoi = ""
    for i in range(len(itos) - 1, -1, -1):
        stoi += itos[i]
    return int(stoi)

def reverse_1(x):
    # x = 9010 -> 0109
    res = 0
    dec = 1
    while(x > 0):
        t = x % 10
        res += dec * t
    return res
    

def isPrime(x):
    if(x == 1):
        return False
    cnt = [0] * (x + 1)
    for i in range(2, x):
        if(cnt[i] == 0):
            for j in range(i, x + 1, i):
                if(j == x):
                    return False
                cnt[j] = 1
    else:
        return True

N = int(input())
a = list(map(int, input().split()))

for e in a:
    r = reverse_1(e)
    # r = reverse(e)
    if(isPrime(r)):
        print(r, end=' ')
#######################################################################
