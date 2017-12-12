#coding=utf-8
# 从谷歌浏览器中获取 登录cookie
import os
import sqlite3
from win32crypt import CryptUnprotectData

class GetCookie:
    def __init__(self,host='.qichacha.com'):
        GetCookie.Cookie = self.__getcookiefromchrome(host)

    def __getcookiefromchrome(self,host):
        cookiepath=os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
        sql="select host_key,name,encrypted_value from cookies where host_key='%s'" % host
        with sqlite3.connect(cookiepath) as conn:
            cu=conn.cursor()
            cookies={
                name:CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()
            }
        return cookies
    def get(self):
        return self.Cookie