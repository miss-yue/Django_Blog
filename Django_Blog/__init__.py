# coding: utf-8
import pymysql

# django 中的mysql 只支持 MySQLdb, 而python3 没有MySQLdb这个包，这里我们用pymysql代替
pymysql.install_as_MySQLdb()