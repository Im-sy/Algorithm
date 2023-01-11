# 효율성 시간 초과
# def solution(phone_book):
#     phone_book.sort(key=lambda x: len(x))
#     for i in range(len(phone_book)):
#         cnt = 0
#         n = len(phone_book[i])
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i] == phone_book[j][:n]:
#                 cnt += 1
#             if cnt > 0:
#                 return False
#     return True


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True


# 해시를 사용한 풀이
# def solution(phone_book):
#     hash_map = {}
#     for num in phone_book:
#         hash_map[num] = 1
#     for num in phone_book:
#         tmp = ""
#         for n in num:
#             tmp += n
#             if tmp in hash_map and tmp != num:
#                 return False
#     return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))