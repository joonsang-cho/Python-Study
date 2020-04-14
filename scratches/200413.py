# 백준 2447번 별찍기
# 제기랄 개어렵네
def star(n):
    n = int(n)
    if n == 1:
        ans = ["*", "*", "*"]
        return ans
    else:
        temp=[]
        a = star(n / 3)
        for i in range(n):
            if int(i/(n/3)) == 1 :
                temp.append(a[i%int(n/3)]+' '*int(n/3)+a[i%int(n/3)])
            else:
                temp.append(a[i%int(n/3)]*3)
        ans = list(temp)
        temp = list()
        return ans
print('\n'.join(star(int(input()))))