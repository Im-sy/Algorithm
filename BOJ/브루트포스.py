#220106

### 2798 : 블랙잭
#N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
'''
n, m = map(int, input().split(" "))
n_list = list(map(int, input().split(" ")))
total=0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if n_list[i]+n_list[j]+n_list[k] > m:
#                 pass
#             else :
#                 total=max(total, n_list[i]+n_list[j]+n_list[k])
# print(total)
from itertools import combinations
for i in combinations(n_list, 3):
    tmp_total=sum(i)
    if total<tmp_total<=m:
        total=tmp_total
print(total)
'''


### 2231 : 분해합
#어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미
#어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
#자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
'''
n=int(input())
n_digit=1
m=n
while 1:
    if m//10==0:
        break
    else:
        m=m//10
        n_digit+=1
m=n-9*n_digit
for i in range(m, n+1):
    m_sum=i+sum(map(int, str(i)))
    if m_sum==n:
        print(i)
        break
    elif i==n:
        print(0)
'''

### 7568 : 덩치
#어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다.
#두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"
#만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1
#학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력해야 한다.
'''
n=int(input())
n_list=[]
for i in range(n):
    n_list.append(list(map(int, input().split(" "))))
def dungchi(*arg):
    if arg[0][0]>arg[1][0] and arg[0][1]>arg[1][1]:
        return 0
    elif arg[1][0]>arg[0][0] and arg[1][1]>arg[0][1]:
        return 1
#print(n_list)
win_list=[1]*n
#print(win_list)
for i in range(n):
    for j in range(i+1,n):
        if dungchi(n_list[i],n_list[j])==0:
            win_list[j]+=1
        elif dungchi(n_list[i],n_list[j])==1:
            win_list[i]+=1
for i in win_list:
    print(i, end=" ")
'''


### 1018 : 체스판 다시 칠하기
# M×N 크기의 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
# 당연히 8*8 크기는 아무데서나 골라도 된다. 다시 칠해야 하는 정사각형의 최소 개수
'''
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
count = []
for i in range(N-7):
    for j in range(M-7):
        W_cnt = 0 # W로 시작할 때
        B_cnt = 0 # B로 시작할 때
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2:
                    if board[k][l] != 'B':
                        W_cnt += 1
                    if board[k][l] != 'W':
                        B_cnt += 1
                else:
                    if board[k][l] != 'W':
                        W_cnt += 1
                    if board[k][l] != 'B':
                        B_cnt += 1
        count.append(min(W_cnt, B_cnt))
print(min(count))
'''


### 1436 : 영화감동 숌
# 종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다.
# 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, 과 같다
# N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램
'''
n = int(input())
nth = 666
cnt = 0
while 1:
    if '666' in str(nth):
        cnt += 1
    if cnt == n:
        print(nth)
        break
    nth += 1
'''