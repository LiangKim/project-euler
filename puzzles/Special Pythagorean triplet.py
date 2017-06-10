#coding=utf-8

#0<a<334
#a<b<500-a/2

for a in range(1,334):
    #500.1是为了避免获得整数
    for b in range(a+1, int(500.1-a/2)):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a=%d, b=%d, c=%d, product=%d" % (a,b,c,a*b*c))
