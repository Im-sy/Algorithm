W, H = map(int, input().split())

# 3 1 = 3/3
# 3 2 = 4/6
# 3 3 = 3/9
# 3 4 = 6/12
# 3 5 = 7/15
# 3 6 = 6/18

# 4 1 = 4/4
# 4 2 = 4/8
# 4 3 = 6/12
# 4 4 = 4/16
# 4 5 = 8/20

# 8 12 = 16/80
# 2 3 = 4/6


ans = 0
for i in range(1, W):
    ans += (H*i)//W
print(ans*2)

# (W//gcd + H//gcd - 1)*gcd

import math
print(W*H - (W+H-math.gcd(W, H)))

