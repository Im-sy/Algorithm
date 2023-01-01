S = input().upper()
arr = list(set(S))
cnt = []
for x in arr:
    cnt.append(S.count(x))
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(arr[(cnt.index(max(cnt)))])


text = list(input().upper()) #대문자로 받기
alpha = dict()
for i in text:
    if i not in alpha: #문자가 없으면
        alpha[i] = 1 #딕셔너리에 추가
    else: #문자가 이미 있으면
        alpha[i] += 1 #key(문자)에 해당하는 value 1 증가
max = 0
most = ''
for k, v in alpha.items():
    if max < v: #max가 value보다 작으면
        max = v #max를 바꾸고
        most = k #그 value를 가진 key를 저장
    elif max == v: #max가 value와 같으면
        max = v #max는 value로 바꾸고
        most = '?' #most는 물음표로 저장
print(most)

# for x in arr:
#     count = 0
#     for s in S:
#         if x == s:
#             count += 1
#     cnt.append(count)
# cnt_max = max_idx = 0
# for i in range(len(arr)):
#     if cnt_max < arr[i]:
#         max_idx = i
#         cnt_max = arr[i]

