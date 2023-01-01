import sys
sys.setrecursionlimit(10**6)

# 전위 순회 입력 받기
pre_order = []
while True:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break
# print(pre_order)

# 전위 -> 후위 순회 처리
# 리스트의 시작점과 끝점을 기준으로
# 전위 순회에서 루트 노트는 가장 첫번째 점(시작점)
# 이진 검색 트리이므로 루트 노드보다 큰 값이 나오는 인덱스 구하기
# (구할 때 큰 원소 없을 경우 고려해야 함)
# (큰 원소 없을 경우 start end 반전되면서 return)
# 그 인덱스 기준 왼쪽은 왼쪽 자식, 오른쪽은 오른쪽 자식
# 왼쪽 자식들 리스트, 오른쪽 자식 리스트 재귀 돌리기
# 후위 순회로 마무리
def pre_to_post(start, end):
    if start > end:
        return
    root = pre_order[start]
    idx = end + 1
    for i in range(start+1, end+1):
        if pre_order[i] > root:
            idx = i
            break
    # idx = start + 1
    # while idx <= end:
    #     if pre_order[idx] > root:
    #         break
    #     idx += 1

    pre_to_post(start+1, idx-1)
    pre_to_post(idx, end)
    print(root)

pre_to_post(0, len(pre_order)-1)
