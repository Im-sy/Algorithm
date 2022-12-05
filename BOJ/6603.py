import sys
input = sys.stdin.readline
from itertools import combinations

while True:
    S = list(map(int, input().split()))
    k = S[0]
    S = S[1:]
    if k == 0:
        break
    for comb in combinations(S, 6):
        print(*comb)
    print()