T = int(input())
def in_order(n):
    global cnt
    if n <= N:
        in_order(n * 2)
        # 중위 순회 하면서 현재 노드가 몇 번째 탐색인지 카운트한 값을 트리에 저장
        tree[n] = cnt
        cnt += 1
        in_order(n * 2 + 1)

for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    cnt = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')