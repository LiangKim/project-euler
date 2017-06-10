#coding=utf-8
import math

def countDivisors(num):
    divisors = []
    for d in range(1,int(math.sqrt(num))+1):
        if num%d==0:
            divisors.append(d)
            if d*d!=num:
                divisors.append(num/d)
    return len(divisors)

def getTriangularNum(i):
    return int(i*(i+1)/2)

def solve():
    num = 0
    i = 1
    while True:
        tri = getTriangularNum(i)
        count = countDivisors(tri)
        print("[%d]current triangular number=%d, has %d divisors" % (i,tri,count))
        if count>500:
            num = tri
            break
        i+=1
    return num

print(solve())