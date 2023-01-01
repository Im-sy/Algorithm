N, K = map(int, input().split())
arr = [_ for _ in range(1, N+1)]
i = 0
print('<', end='')
# K 번째 마다 pop
# pop 할 때마다 개수 줄기 때문에 주의
# 하나 남을 때 까지 pop 후 남은 하나는 > 와 함께 출력
while len(arr)>1:
    i = (i+K-1)%N
    print(arr.pop(i), end=', ')
    N -= 1
print(arr.pop(), end='>')