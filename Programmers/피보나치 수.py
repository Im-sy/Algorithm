def solution(n):
    ## 시간 초과
    # def fibo(num):
    #     if num == 0:
    #         return 0
    #     if num == 1:
    #         return 1
    #     return fibo(num-2) + fibo(num-1)
    # answer = fibo(n) % 1234567
    fibo = [0]*(n+1)
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-2] + fibo[i-1]
    answer = fibo[-1] % 1234567
    return answer


print(solution(3))
print(solution(5))