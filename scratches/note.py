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
print("\n".join(map(str, list)))
리스트 출력 숫자 제거
print(' '.join(list))
숫자 각각을 원소로 하는 리스트
e = list(map(int, list(str(d))))
리스트 중복 제거
ex_list = list(set(ex_list))
리스트 오름차순
a.sort()
a.sort(reverse=True) - 내림차순

소수점 표현
"%0.3f" %
대소문자 변환
대문자 변환 a.upper(i)
소문자 변환 a.lower(i)