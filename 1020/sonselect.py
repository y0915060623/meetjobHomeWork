# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:56:03 2022

@author: USER
"""

import db

print("查詢員工資料: ")

no = input("請輸入欲查詢的員工編號: ")

sql = "select employee.name,works.items,works.info from employee,works where employee.id='{}'".format(no)
cursor = db.conn.cursor()

cursor.execute(sql)

db.conn.commit()

result = cursor.fetchall()


for row in result:
    print("員工姓名:",row[0])
    print("工作項目:",row[1])
    print("工作詳述:",row[2])
    
    