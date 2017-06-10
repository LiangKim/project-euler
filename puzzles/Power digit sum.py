#coding=utf-8

#eval函数真神奇
def solve():
    return eval("+".join(str(2**1000)))

print(solve())