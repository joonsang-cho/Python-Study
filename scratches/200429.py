# 백준1018 체스판 문제
y, x = map(int, input().split())
board = []
for z in range(y):
    board.append(input())
list_B = ['BWBWBWBW', 'WBWBWBWB']*4
list_W = ['WBWBWBWB', 'BWBWBWBW']*4
#list B와 비교
B_count=[]
for a in range(y-7):
    for b in range(x-7):
        num = 0
        for i in range(8):
            for j in range(8):
                if board[a+j][b+i] != list_B[j][i]:
                    num += 1
        B_count.append(num)
#list_W와 비교
W_count=[]
for a in range(y-7):
    for b in range(x-7):
        num = 0
        for i in range(8):
            for j in range(8):
                if board[a+j][b+i] != list_W[j][i]:
                    num += 1
        W_count.append(num)
print(min(min(B_count), min(W_count)))