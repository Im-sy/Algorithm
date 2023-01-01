import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    # 중요도 담을 리스트
    imp = list(map(int, sys.stdin.readline().split()))
    # 중요도의 인덱스 담을 리스트
    # imp, num은 함께 append, pop 해주기
    num = [_ for _ in range(N)]
    # 몇 번 수행 해야하는지 저장할 변수
    cnt = 1
    while imp:
        # 만약 첫 번째 값이 가장 큰 값이면
        if imp[0] == max(imp):
            # 알고자 하는 문서의 순서와 같은 인덱스값일 때 출력
            if num[0] == M:
                print(cnt)
                break
            # 아니라면 dequeue해서 나머지 값들에 대해 다시 반복
            else:
                imp.pop(0)
                num.pop(0)
                cnt += 1
        # 첫 번째 값이 가장 큰 게 아니라면 뽑아서 가장 끝으로 넣어주기
        else:
            imp.append(imp.pop(0))
            num.append(num.pop(0))

