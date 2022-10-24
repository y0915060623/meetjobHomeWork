# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 20:51:46 2022

@author: USER
"""

import pymysql

dbsetting = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"123456789",
    "db":"jobs",
    "charset":"utf8"
    }

conn = pymysql.connect(**dbsetting)