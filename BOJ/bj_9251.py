# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence

import sys
input = sys.stdin.readline
A = ' '+input().strip()
B = ' '+input().strip()
LCS = [[0]*len(B) for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B)):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(LCS[len(A)-1][len(B)-1])