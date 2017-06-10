#coding=utf-8
def solve():
    pass

def fib(index):
    a1,a2,a3 = 0,1,1
    while index > 0:
        yield a3
        a1,a2,a3 = a2, a3, a2+a3
        index-=1


f = fib(100)
sum = 0
for i in f:
    if i>4000000:
        break
    if i%2==0:
        sum+=i
print(sum)
