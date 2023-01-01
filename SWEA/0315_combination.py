arr = [2, 5, 7, 1, 9, 10, 2, 3, 6]
N = 9
K = 4
# idx : 조합 포함여부 결정할 idx 번째 요소
# selected : 조합 포함여부 표시
# cnt : 조합에 포함된 요소 개수 (K 넘어갈 수 없음)
def solve(idx, selected, cnt):
    if cnt == K: # 조합이 완성됨
        print(selected)
        return
    if idx == N: # 모든 요소를 다 결정했다고 해서 결과가 나온 건 아님
        # 연산 필요 X
        return
    selected[idx] = 1
    solve(idx+1, selected, cnt+1)
    selected[idx] = 0
    solve(idx + 1, selected, cnt)

solve(0, [0]*N, 0)