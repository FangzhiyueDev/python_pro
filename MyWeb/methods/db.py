# ! /usr/bin/python
# ! coding=utf-8

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="123", db="test", port=3306, charset="utf8")

cur = conn.cursor()  # 游标对象


def addUser(userName, password):
    sql = "insert into user(name,password) values('" + userName + "','" + password + "')"
    cur.execute(sql)


def userInfoList():
    sql="select * from user"
    cur.execute(sql)
    lines=cur.fetchall()
    return lines
