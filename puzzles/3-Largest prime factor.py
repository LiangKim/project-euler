#coding=utf-8
import math
#计算某数的最大质因数
def largest_prime_factor(tar):
    #先生成素数表
    pList = prime_list(int(math.sqrt(tar))+1)
    #从高位开始遍历
    while len(pList)>0:
        curr = pList.pop(len(pList)-1)
        if tar%curr==0:
            return curr
    return tar #tar本身就是质数


#生成从2->tar的素数表
def prime_list(tar):
    list = []
    list.append(2)
    list.append(3)

    for i in range(5,tar+1,2):
        if is_prime(i):
            list.append(i)

    return list

#判断tar是否为素数
def is_prime(tar):
    if type(tar)!=type(1) or tar<0 or tar==1:
        return False

    for i in range(2,int(math.sqrt(tar))+1):
        if tar%i==0:
            return False

    return True

#最终结果
print(largest_prime_factor(600851475143))
