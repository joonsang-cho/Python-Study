# 백준 11021
# import sys
# num = int(input())
# def solving(num):
#     for i in range(1, num+1):
#         a, b = map(int, sys.stdin.readline().split())
#         if a<= 0:
#             print('숫자 오류')
#             break
#         elif b>= 10:
#             print('숫자 오류')
#             break
#         else :
#             print('Case #', i, ': ', a+b, sep='')
# solving(num)

# 백준 2439
# 1. 오른쪽 정렬 rjust
# num = int(input())
# for i in range(1, num+1):
#     a = '*'*i
#     print(a.rjust(num))
#
# 2. 오른쪽 정렬 공백
# num = int(input())
# for i in range(1, num+1):
#     print(' '*(num-i), '*'*i, sep='')