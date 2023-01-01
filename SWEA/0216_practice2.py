# ord('0') == 48 문자의 아스키 코드 반환
# chr(48) == '0' 아스키 코드에 해당하는 문자 반환

# 숫자를 문자로 만들기
def itoa(integer):
    result = ''
    while integer > 0:
        r = integer % 10
        result = chr(r + ord('0')) + result
        integer //= 10
    return result
print([itoa(123)])