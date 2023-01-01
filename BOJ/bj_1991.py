import sys
N = int(sys.stdin.readline())
# tree와 왼쪽 오른쪽 자식노드 저장할 배열
tree = [0]*(N+1)
ch1 = [0]*(N+1)
ch2 = [0]*(N+1)

# 알파벳을 인덱스(숫자)로 변환해주기 위한 함수
def a_to_num(x):
    return ord(x)-ord('A')+1

for _ in range(N):
    v, l, r = sys.stdin.readline().split()
    # A : 1, B : 2, C : 3 ...
    idx = a_to_num(v)
    # tree 해당 인덱스에 알파벳 저장
    tree[idx] = v
    # 왼쪽 자식 해당 인덱스에 알파벳 인덱스 저장
    if l != '.':
        ch1[idx] = a_to_num(l)
    # 오른쪽 자식 해당 인덱스에 알파벳 인덱스 저장
    if r != '.':
        ch2[idx] = a_to_num(r)

# 전위 순회
def pre_order(v):
    print(tree[v], end='')
    if ch1[v]:
        pre_order(ch1[v])
    if ch2[v]:
        pre_order(ch2[v])

# 중위 순회
def in_order(v):
    if ch1[v]:
        in_order(ch1[v])
    print(tree[v], end='')
    if ch2[v]:
        in_order(ch2[v])

# 후위 순회
def post_order(v):
    if ch1[v]:
        post_order(ch1[v])
    if ch2[v]:
        post_order(ch2[v])
    print(tree[v], end='')

pre_order(1)
print()
in_order(1)
print()
post_order(1)