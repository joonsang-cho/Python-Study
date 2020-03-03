숫자 여러개 입력받기
1. a, b = map(int, input().split())
2.
import sys
number = int(input())
for i in range(number):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

리스트 출력 개행
print(1, 2, 3, sep='\n')
리스트 출력 숫자 제거
print(' '.join(ans))