record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = []
nick = {}
# 112.92 48.4
id = []
for rec in record:
    arr = list(rec.split())
    if arr[0] == 'Enter':
        answer.append(arr[2]+"Enter")
        nick[arr[1]] = arr[2]
        id.append(arr[1])
    elif arr[0] == 'Leave':
        answer.append(nick[arr[1]]+"Leave")
        id.append(arr[1])
    else:
        nick[arr[1]] = arr[2]
# print(answer)
# print(nick)
# print(id)
for i in range(len(id)):
    if answer[i][-5:] == "Enter":
        answer[i] = nick[id[i]]+"님이 들어왔습니다."
    else:
        answer[i] = nick[id[i]]+"님이 나갔습니다."
print(answer)


# 107.36 55.5
for rec in record:
    arr = list(rec.split())
    if arr[0] == 'Enter':
        answer.append(arr[1]+" Enter")
        nick[arr[1]] = arr[2]
    elif arr[0] == 'Leave':
        answer.append(arr[1]+" Leave")
    else:
        nick[arr[1]] = arr[2]
for i in range(len(answer)):
    id, t = answer[i].split()
    if t == "Enter":
        answer[i] = nick[id]+"님이 들어왔습니다."
    else:
        answer[i] = nick[id]+"님이 나갔습니다."