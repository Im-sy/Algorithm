S = input()
# for i in range(len(S)-1, -1, -1):
#     print(S[i], end='')

n = len(S)
mid = len(S)//2
s_list = list(S)
for i in range(mid):
    s_list[i], s_list[n-1-i] = s_list[n-1-i], s_list[i]
print(''.join(s_list))