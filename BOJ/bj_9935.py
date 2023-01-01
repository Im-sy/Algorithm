import sys
input = sys.stdin.readline

arr = input().rstrip()
boom = input().rstrip()
# while boom in arr:
#     arr = arr.replace(boom, '')

length = len(boom)
stack = []
for x in arr:
    stack.append(x)
    if ''.join(stack[-length:]) == boom:
        for _ in range(length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")