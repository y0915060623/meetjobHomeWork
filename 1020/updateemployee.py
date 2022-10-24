# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:09:30 2022

@author: USER
"""

import db

print("修改員工資料: ")

sql = "select id from employee"

cursor = db.conn.cursor()

cursor.execute(sql)

db.conn.commit()

result = cursor.fetchall()

print("員工編號: ")
for row in result:
    print(row[0])
    
no = input("請輸入欲修改的員工編號: ")

name = input("請輸入欲修改的員工姓名: ")

tel = input("請輸入欲修改的員工電話: ")

sex = input("請輸入欲修改的員工性別: ")

sql = "update employee set name='{}',tel='{}',sex='{}' where id='{}'".format(name,tel,sex,no)

cursor.execute(sql)

db.conn.commit()        
