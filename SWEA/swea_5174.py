T = int(input())
def order(n):
    # # V L R 순서 (전위 순회)
    # # 순서는 상관 없음
    # global cnt
    # # 0인 경우에는 자식이 없는 경우이므로 할 필요 없음
    # if n == 0:
    #     return
    # # 몇 번째인지 카운트
    # cnt += 1
    # order(ch1[n])
    # order(ch2[n])

    # global 함수 안 쓰는 법
    if n == 0:
        return 0
    return order(ch1[n]) + order(ch2[n]) + 1

for tc in range(1, T+1):
    E, N = map(int, input().split())
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    # 부모 자식 노드 번호 쌍
    arr = list(map(int, input().split()))
    # 트리 나타내기
    for i in range(0, len(arr), 2):
        # a : 부모노드(인덱스), b : 자식노드 번호
        a, b = arr[i], arr[i+1]
        # 왼쪽 자식 먼저 채우기
        if not ch1[a]:
            ch1[a] = b
        # 왼쪽 자식이 차있다면 오른쪽 자식 채우기
        else:
            ch2[a] = b
    # 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수
    # cnt = 0
    # order(N)

    # global 함수 안 쓰는 법
    cnt = order(N)

    print(f'#{tc} {cnt}')
