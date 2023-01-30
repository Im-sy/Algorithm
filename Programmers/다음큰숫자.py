def get_binary(num):
    bin_num = ''
    while num>0:
        bin_num += str(num % 2)
        num //= 2
    return bin_num.count('1')

def solution(n):
    answer = n
    n_binary = get_binary(n)
    while True:
        answer += 1
        if n_binary == get_binary(answer):
            break
    return answer


print(solution(78))
print(solution(15))