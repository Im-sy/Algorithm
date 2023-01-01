T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    for i in range(len(arr)-1):
        if arr[i] == '(' and arr[i+1] == ')':
            arr[i] = '!'
            arr[i+1] = '?'
    tmp_stick = cnt_stick = cnt_damage = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            cnt_stick += 1
            tmp_stick += 1
        if arr[i] == '!':
            cnt_damage += tmp_stick
        if arr[i] == ')':
            tmp_stick -= 1
    print(f'#{tc} {cnt_damage + cnt_stick}')