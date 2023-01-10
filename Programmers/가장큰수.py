# 시간 초과
# from itertools import permutations
#
#
# def solution(numbers):
#     nums = list(permutations(numbers))
#     max_num = 0
#     for num in nums:
#         num = ''.join(list(map(str, num)))
#         max_num = max(max_num, int(num))
#     return str(max_num)


# https://minnnne.tistory.com/73 참고

def solution(numbers):
    answer = ''
    nums = []
    for number in numbers:
        nums.append([str(number)*3, str(number)])
    nums.sort(reverse=True)
    for num in nums:
        answer += str(num[1])
    for i in answer:
        if i != '0':
            return answer
    return '0'

# 다른 사람 풀이.. 새롭다
# import functools
#
# def comparator(a,b):
#     t1 = a+b
#     t2 = b+a
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
#
# def solution(numbers):
#     n = [str(x) for x in numbers]
#     n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
#     answer = str(int(''.join(n)))
#     return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([1000, 0, 0, 0]))