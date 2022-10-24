# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:09:30 2022

@author: USER
"""

import db

print("查詢員工資料: ")

no = input("請輸入欲查詢的員工編號: ")

sql = "select * from employee where id='{}'".format(no)

cursor = db.conn.cursor()

cursor.execute(sql)

db.conn.commit()

result = cursor.fetchall()


for row in result:
    print("員工編號:",row[0])
    print("員工姓名:",row[1])
    print("員工性別:",row[2])
    print("員工電話:",row[3])
    print("修改日期:",row[4])
    