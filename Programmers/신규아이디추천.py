import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^-_.a-z0-9]', '', new_id)
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # new_id = re.sub(r'\.+', '.', new_id)
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    # new_id = re.sub('^[.]|[.]$', '', new_id)
    if len(new_id) == 0:
        new_id += 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))