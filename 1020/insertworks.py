# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:51:55 2022

@author: USER
"""

import db

print("新增工作項目")

items = input("請輸入工作項目: ")

info = input("請輸入工作詳述: ")

employeeid = int(input("請對應的員工編號: "))

sql = "insert into works (items,info,employeeid) values('{}','{}','{}')".format(items,info,employeeid)

cursor = db.conn.cursor()

cursor.execute(sql)

db.conn.commit()

db.conn.close()

