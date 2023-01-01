# 부분 집합
# idx : 부분집합에 포함 여부 결정할 요소 인덱스
# selected : 각 idx 번째 요소가 부분집합에 포함되는지 표시
def solve(idx, selected):
    if idx == N:
        # print(selected)
        group = []
        for i in range(N):
            if selected[i]:
                group.append(arr[i])
        print(group)
        return
    # idx 번째 요소의 부분집합 포함 여부 결정
    # idx+1 번째 요소의 부분집합 포함 여부 결정
    selected[idx] = 0 # 부분집합 포함 X
    solve(idx + 1, selected)
    selected[idx] = 1 # 부분집합 포함 O
    solve(idx + 1, selected)

arr = [1, 2, 3, 4, 5]
N = 5
selected = [0]*N
solve(0, selected)