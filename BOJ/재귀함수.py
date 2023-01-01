#22/01/02

### 10872
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
'''
def factorial(n):
    if n==0:
        result=1
    if n>=1:
        result=n*factorial(n-1)
    return result

x=int(input())
print(factorial(x))
'''
###10870
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''
def fib(n):
    if n==0:
        result=0
    if n==1:
        result=1
    if n>=2:
        result=fib(n-1)+fib(n-2)
    return result

x=int(input())
print(fib(x))
'''

###2447
# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
'''
def star(n,lst):
    result=[]
    if n==3:
        return lst
    else:
        for i in lst:
            result.append(i*3)
        for i in lst:
            result.append(i+' '*len(lst)+i)
        for i in lst:
            result.append(i*3)
        return star(n//3, result)

x=int(input())
first=['***','* *','***']
for i in star(x,first):
    print(i)
'''

###11729
#세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다.
#한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
#쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
#이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

def hanoi(n, start, to, end):
    if n==1:
        print("{} {}".format(start, end))
    else:
        hanoi(n-1, start, end, to)
        print("{} {}".format(start, end))
        hanoi(n-1, to, start, end)

x=int(input())
print(2**x-1)
hanoi(x, 1, 2, 3)