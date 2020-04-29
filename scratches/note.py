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
print(' '.join(map(str, list)))
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


순열 구하기
1. 재귀 이용
iterable = [1, 2,3, 4, 5]
visited=[False]*5
def get_permutations(_currentIndex, _permutation):
    if _currentIndex == 5:
        print(_permutation)
        return
    for index, value in enumerate(iterable):
        if not visited[index]:
            visited[index], _permutation[_currentIndex] = True, value
            get_permutations(_currentIndex+1, _permutation)
            visited[index] = False

if __name__ == '__main__':
    get_permutations(0, [None]*5)
2. itertools이용
import itertools
iterable = [1,2,3,4,5]
result = itertools.permutations(iterable)
for i in result:
    print(i)

조합 구하기
import itertools
a = [1, 2, 3, 4, 5]
print(itertools.combinations(a, 3))
혹은
from itertools import combinations
a = [1, 2, 3, 4, 5]
print(combinations(a, 3))