# 완전 탐색
# 순열 만들어서 앞뒤 세 개씩 잘라서 run 또는 triplet 인지 검사
# 순열 - 개수가 정해져 있는 경우 반복문으로 순열 생성 가능
arr = list(map(int, input()))
def babygin(arr):
    N = len(arr)
    for i in range(N):
        for j in range(N):
            if i == j: continue
            for k in range(N):
                if k == i or k == j: continue
                for a in range(N):
                    if a == i or a==j or a==k: continue
                    for b in range(N):
                        if b==i or b==j or b==k or b==a: continue
                        for c in range(N):
                            if c==i or c==j or c==k or c==a or c==b: continue
                            # 순열 중 baby-gin 확인
                            result = 0
                            if arr[i]+1 == arr[j] and arr[i]+2 == arr[k]:
                                result += 1
                            elif arr[i] == arr[j] and arr[i] == arr[k]:
                                result += 1
                            if arr[a]+1 == arr[b] and arr[a]+2 == arr[c]:
                                result += 1
                            elif arr[a] == arr[b] and arr[a] == arr[c]:
                                result += 1
                            if result == 2:
                                # print('baby-gin!') # 베이비진임을 확인
                                return True
    return False

print(babygin(arr))

# count 배열 사용하기
def babygin2(arr):
    cnt = [0]*12 # 한번에 run, triplet 인덱스 확인 위해서 (9, 10, 11)
    for i in range(len(arr)):
        cnt[arr[i]] += 1
    run, triplet = 0, 0
    for i in range(10):
        if cnt[i] and cnt[i+1] and cnt[i+2]:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            run += 1
            continue
        if cnt[i] >= 3:
            cnt[i] -= 3
            triplet += 1
            continue
    if run+triplet == 2:
        return True
    else:
        return False

print(babygin2(arr))

lst = [2,7,3,4,7,7]
N = 6
# 재귀함수로 순열 만들기
def make_perm(idx, used, perm):
    if idx == N: # 모든 idx 에 대해 들어갈 요소 결정됨
        print(perm)
        return
    # idx 번째에 들어갈 요소 결정 (다 고려해봐야 함)
    for i in range(N):
        if not used[i]:
            used[i] = 1
            perm[idx] = arr[i]
            make_perm(idx+1, used, perm)
            used[i] = 0
make_perm(0, [0]*N, [0]*N)