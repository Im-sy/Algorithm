N = 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
arr = list(map(int, input().split()))
ch1 = [0]*14
ch2 = [0]*14
for i in range(0, len(arr), 2):
    p = arr[i]
    c = arr[i+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

def pre_order(v):
    if v:
        print(v, end=' ')
        pre_order(ch1[v])
        pre_order(ch2[v])

pre_order(1)