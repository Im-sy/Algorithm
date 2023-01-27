from collections import Counter


def solution(want, number, discount):
    answer = 0
    wants = dict(zip(want, number))
    for i in range(len(discount)-9):
        disc = dict(Counter(discount[i:i+10]))
        if wants == disc:
            answer += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))