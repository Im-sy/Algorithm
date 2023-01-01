# 1. 각 줄의 높이만 알면 됨
# 2. 나보다 오른쪽에 있으면서 높이가 낮으면 낙차 +1
# 3. 모든 열에 대해 낙차 계산
# 4. 그 중 가장 큰 값이 정답

# input ex : 7 4 2 0 0 6 0 7 0
boxes = list(map(int, input().split()))
# 입력이 제대로 되었는지 확인
# sum, max, min, count 금지
cnt_max = 0 # 굳이 list 만들어서 append 하지말자..
for i in range(len(boxes)):
    cnt = 0
    for j in range(i+1, len(boxes)):
        if boxes[i] > boxes[j]:
            cnt += 1
    if cnt_max < cnt:
        cnt_max = cnt
print(cnt_max)