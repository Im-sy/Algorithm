import sys
input = sys.stdin.readline

N, M = map(int, input().split())
fact_nums = set(list(map(int, input().split()))[1:])

parties = []
for _ in range(M):
    parties.append(set(list(map(int, input().split()))[1:]))

# 진실을 아는 사람이 포함된 파티에 있는 모든 사람을 진실을 아는 사람으로 취급
for _ in range(M):
    for party in parties:
        if party & fact_nums:
            fact_nums = fact_nums.union(party)
ans = 0
for party in parties:
    if party & fact_nums:
        continue
    ans += 1
print(ans)