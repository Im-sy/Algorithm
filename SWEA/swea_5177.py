T = int(input())

# 힙에 넣어주는 함수
# 들어온 값이 트리의 가장 마지막 값이 되고
# 부모 노드가 있고, 부모 노드와 비교했을 때 자식이 더 작은 경우 부모와 자식 change
def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p>=1 and tree[p]>tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    last = 0
    arr = list(map(int, input().split()))
    for x in arr:
        enq(x)
    # 가장 마지막 노드(포함X)의 조상 노드들의 합 구하기
    tmp_sum = 0
    while last>0:
        last = last//2
        tmp_sum += tree[last]
    print(f'#{tc} {tmp_sum}')