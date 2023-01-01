T = int(input())
def f(i, j):   # i~j 사이의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

# 1 vs 2 => 2
# 1 vs 3 => 1
# 2 vs 3 => 3
def win(left, right):
    l = arr[left]
    r = arr[right]
    if abs(l-r) == 1:
        result = left if l>r else right
        return result
    elif abs(l-r) == 2:
        result = left if l<r else right
        return result
    else:
        return left

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {f(0, N-1)+1}')
