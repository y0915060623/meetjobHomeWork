# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:51:55 2022

@author: USER
"""

import db

print("新增員工資料: ")

name = input("請輸入員工姓名: ")

sex = input("請輸入性別: ")

tel = input("請輸入電話: ")

sql = "insert into employee (name,sex,tel) values('{}','{}','{}')".format(name,sex,tel)

cursor = db.conn.cursor()

cursor.execute(sql)

db.conn.commit()

db.conn.close()

