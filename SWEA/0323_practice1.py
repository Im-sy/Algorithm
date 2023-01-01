# 0000000111100000011000000111100110000110000111100111100111111001100111
arr = list(map(int, input()))
for i in range(0, len(arr), 7):
    tmp = 0
    cnt = 6
    for j in range(i, i+7):
        tmp += arr[j] * 2**cnt
        cnt -= 1
    print(tmp)