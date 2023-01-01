N = int(input())
length = len(str(N))
M = N-9*length
while M < N:
    tmp_M = M
    tmp_sum = M
    while tmp_M>0:
        tmp_sum += tmp_M%10
        tmp_M //= 10
    if tmp_sum == N:
        print(N)
        break
    M += 1
else:
    print(0)

# for i in range(1, N):
#     tmp_sum = i + sum(map(int, str(i)))
#     if tmp_sum == N:
#         print(i)
#         break
# else:
#     print(0)