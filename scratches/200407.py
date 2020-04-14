for i in range(2+2, 10, 2):
    print(i)

a = int(input())


소수 관련 문제
def hash(a):
    for i in range(a*2, 10000+1, a):
        yield i

sosuu = []
pool = [0]*(10000+1)
pool[1] = 1
pool[0] = 1
for j in range(2, 10000+1):
    if pool[j] ==1:
        continue
    for k in hash(j):
        pool[k] = 1

def sosu(w):
    basket = []
    for x in range(int(w/2)+1):
        y  = w-x
        if pool[x] == 0:
            if pool[y] ==0:
                basket.append(x)
    print(max(basket), w-max(basket))

a = int(input())
for i in range(a):
    b= int(input())
    sosu(b)