#coding=utf-8
import sqlite3
import math

class Prime:
    #构造函数，初始化质数堆的容量
    def __init__(self):
        conn = sqlite3.connect("E:\database\prime.db")
        cur = conn.cursor()
        #初始化表
        res = cur.execute("SELECT COUNT(1) FROM sqlite_master "
        + "WHERE type='table' AND name='prime_list'")
        exists = res.fetchone()[0]
        if exists ==0:
            cur.execute("CREATE TABLE prime_list(id INTEGER PRIMARY KEY autoincrement, value int)")
            conn.commit()

        #初始化容量
        res = cur.execute("SELECT IFNULL(MAX(id),0) FROM prime_list")
        self.size = res.fetchone()[0]
        cur.close()
        conn.close()

    #插入新的素数
    def insert(self,new):
        conn = sqlite3.connect("E:\database\prime.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO prime_list(value) VALUES(%d)" % (new))
        conn.commit()
        cur.close()
        conn.close()
        
    #扩展
    def extend(self):
        #获取上一位素数
        conn = sqlite3.connect("E:\database\prime.db")
        cur = conn.cursor()
        res = cur.execute("SELECT IFNULL(MAX(value),0) FROM prime_list")
        last = res.fetchone()[0]
        if last == 0:
            self.insert(2)
            self.size = self.size + 1
            return 
        new = last+1
        while not self.is_prime(new):
            new = new + 1
        self.insert(new)
        self.size = self.size + 1

    #判断某数是否为素数
    def is_prime(self,number):
        if type(number) != type(1):
            return False
        if number < 2:
            return False
        for i in range(2,int(math.sqrt(number))+1):
            if number%i==0:
                return False
        return True
            
    #获取第n个素数
    def get(self,n):
        #如果对应素数还未生成，则先进行扩容
        while self.size < n:
            self.extend()
        conn = sqlite3.connect("E:\database\prime.db")
        cur = conn.cursor()
        res = cur.execute("SELECT IFNULL(value,0) FROM prime_list WHERE id=%d" % (n))
        tar = res.fetchone()[0]
        return tar
        
