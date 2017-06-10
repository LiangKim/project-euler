#coding=utf-8
from functools import reduce

#辗转相除求最大公约数
def gcd(a, b):
    if a<b:
        return gcd(b,a)
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

solve = reduce(lambda x,y:x*y/gcd(x,y), range(1,20))
print(solve)