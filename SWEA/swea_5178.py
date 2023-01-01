T = int(input())
def post_order(n):
    if n <= N:
        post_order(n*2)
        post_order(n*2+1)
        # 자식 노드가 존재하는지 확인 필요 (인덱스가 N 범위 내에 존재해야함)
        if n*2 <= N:
            tree[n] += tree[n*2]
        if n*2+1 <= N:
            tree[n] += tree[n*2+1]

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    post_order(1)
    print(f'#{tc} {tree[L]}')