import sys
sys.stdin = open('swea_1232.txt')

def post_order(n):
    if n <= N:
        # 재귀 최대깊이 한도 때문에 한 번 걸러줘야 함
        if ch1[n]:
            post_order(ch1[n])
        if ch2[n]:
            post_order(ch2[n])
        cal = tree[n]
        l = tree[ch1[n]]
        r = tree[ch2[n]]
        if cal == '+':
            tree[n] = l + r
        elif cal == '-':
            tree[n] = l - r
        elif cal == '*':
            tree[n] = l * r
        elif cal == '/':
            tree[n] = l / r

for tc in range(1, 11):
    N = int(input())
    # 값 저장
    tree = [0] * (N + 1)
    # 자식노드 저장
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    arrs = [list(input().split()) for _ in range(N)]
    # 연산자는 str, 피연산자는 int 주의
    for arr in arrs:
        if len(arr) == 4:
            tree[int(arr[0])] = arr[1]
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
        else:
            tree[int(arr[0])] = int(arr[1])
    post_order(1)
    print(f'#{tc} {int(tree[1])}')