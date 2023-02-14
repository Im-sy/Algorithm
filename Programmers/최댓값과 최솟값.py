def solution(s):
    lst = list(map(int, s.split()))
    answer = f'{str(min(lst))} {str(max(lst))}'
    return answer


print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))
print(solution('-1 -1'))