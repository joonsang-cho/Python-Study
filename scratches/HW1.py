def sum(n):
    a=n
    b=10*n+a
    c=100*n+b
    return a+b+c
if __name__ == '__main__':
    n=int(input())
    if 0<n<10:
        print(sum(n))
    else:
        print("error")
