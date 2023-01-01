import sys
# 재귀 최대 깊이한도 지정 필요
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

# 중위후위 -> 전위
# in_l, in_r : 중위순회배열의 첫번째, 마지막 인덱스
# post_l, post_r : 후위순회배열의 첫번째, 마지막 인덱스
def inpost_to_pre(in_l, in_r, post_l, post_r):
    # 첫번째, 마지막 인덱스 서로 반전 시 return
    if in_l > in_r or post_l > post_r:
        return
    # 후위순회배열에서 가장 마지막 요소가 루트노드
    root = post_order[post_r]
    
    # 중위순회배열에서 루트노드 기준 왼쪽 자식 노드, 오른쪽 자식 노드 나뉨
    # mid : 중위순회배열에서 루트노드 인덱스 
    # index()함수 시간초과ㅠㅠ
    # 따로 딕셔너리 만들어서 불러오기
    # mid = in_order.index(root)
    mid = idx_dict[root]
    
    # 전위순회 (루트노드 먼저)
    print(root, end=' ')
    
    # 중위순회에서 왼쪽자식노드 수
    l_length = mid - in_l - 1
    # 중위순회에서 오른쪽자식노드 수
    r_length = in_r - mid - 1
    
    # 재귀 접근 시 인덱스 설정 조심!
    # 중위순회는 mid로 접근하면 되지만
    # 후위순회는 l_length와 r_length로 접근해야함
    inpost_to_pre(in_l, mid-1, post_l, post_l+l_length)
    inpost_to_pre(mid+1, in_r, post_r-r_length-1, post_r-1)
    
    # 인덱싱, 슬라이싱 시 시간초과 ㅠㅠ
    # if postorder:
    #     root = postorder[-1]
    #     mid = inorder.index(root)
    #     print(root, end=' ')
    #     inpost_to_pre(inorder[:mid], postorder[:mid])
    #     inpost_to_pre(inorder[mid+1:], postorder[mid:-1])

# 인덱스와 값 따로 딕셔너리에 저장해두고 쓰면 빠르다
idx_dict = {}
for k, v in enumerate(in_order):
    idx_dict[v] = k
inpost_to_pre(0, N-1, 0, N-1)