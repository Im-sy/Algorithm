def solution(arr1, arr2):
    answer = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*arr2)] for A_row in arr1]
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

# 1 4   3 3
# 3 2   3 3
# 4 1
