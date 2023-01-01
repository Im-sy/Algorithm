N = int(input())

def star(n, lst):
    res = []
    if n == 3:
        return lst
    else:
        for i in lst:
            res.append(' '*len(lst)+i+' '*len(lst))
        for i in lst:
            res.append(i+' '+i)
        return star(n//2, res)

first = ['  *  ', ' * * ', '*****']
ans = star(N, first)
for x in ans:
    print(x)