#coding=utf-8
from functools import reduce

def solve(max):
    res = reduce(lambda x,y:x+y,getSet(max))
    print(res)

def getSet(max):
    li = list(range(3, max, 3))
    li.extend(list(range(5, max, 5)))
    return set(li)

solve(1000)