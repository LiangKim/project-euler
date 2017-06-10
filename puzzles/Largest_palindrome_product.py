#coding=utf-8
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#我的思路是从大数开始遍历。
#分为两个主要方法。1：获取下一个回文数。2.判断该回文数是否能分解为两个三位数之积。

#获取下一个回文数
def next(number):
    string = str(number)
    gap = narrow(number)
    high = string[0]
    low = string[len(string)-1]
    if gap==0:
        if high>low:
            return number-int(low)+int(high)
        else:
            if high=='1':
                return 10**len(string)-1
            else:
                return (int(high))*10**(len(string)-1)-1-9+int(high)
    else:
        # if symm(number):
        #     return int(high+str(next(gap))+high)
        # elif high==low:
        pass

#掐头去尾拿到中间的数字
def narrow(before):
    if len(before)<2:
        return 0
    return int(before[1:len(before)-1])

#

