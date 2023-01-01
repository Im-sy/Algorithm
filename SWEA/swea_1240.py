import sys
sys.stdin = open('swea_1240.txt')

num = {'0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for r in range(N):
        for c in range(M-1, -1, -1):
            if arr[r][c]=='1':
                cr, cc = r, c
                break
    password = arr[cr][cc-55:cc+1]
    # print(password)
    result = ''
    for i in range(0, len(password), 7):
        result += num[password[i:i+7]]
    # print(result)
    ans = 0
    for i in range(7):
        if i%2:
            ans += int(result[i])
        else:
            ans += int(result[i])*3
    ans += int(result[7])

    if ans%10:
        print(f'#{tc} 0')
    else:
        total = 0
        for i in range(8):
            total += int(result[i])
        print(f'#{tc} {total}')