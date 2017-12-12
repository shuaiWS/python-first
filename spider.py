#coding=utf-8
import sys
import os
import html.parser
import sqlite3
from win32crypt import CryptUnprotectData
from urllib import request
from bs4 import BeautifulSoup
import re
import time
import _thread
import qichacha as qcc
import cookie as coo
import headers as hd
from tkinter import *

# 导入tkinter模块的所有内容
class setTkinter:
    def __init__(self,**arguments):
        self.root = Tk()
        self.root.title('欢迎使用！')
        self.companyName = StringVar() #公司名称
        self.excelPath = StringVar() #Excel路径
        self.sNum = StringVar() # 右边序号范围
        self.bNum = StringVar() # 左边序号范围
        self.worn = StringVar() #警告
        self.newExcel = StringVar() # 是否生成新Excel
        self.isLogin = True

        self.__initui()
        self.setUrlCookie()
    def __initui(self):
        #第一行
        Label(self.root,text='企业名称/人名(以空格隔开)：').grid(row=0,column=0, padx=20)
        Entry(self.root, textvariable=self.companyName).grid(row=0, column=1, sticky=W,ipadx=5, padx=10, pady=5)  # 公司名称
        Button(self.root, text='查询', width=10, command=self.search).grid(row=0, column=2, sticky=W, padx=10, pady=5)
        #第二行
        Label(self.root,text='输入需要导入的Excel路径：').grid(row=1,column=0, padx=20)
        Entry(self.root, textvariable=self.excelPath).grid(row=1, column=1, sticky=W, ipadx=5,padx=10, pady=5)    #Excel路径
        #第三行
        Label(self.root,text='范围操作(序号范围)：').grid(row=2, column=0, sticky=W, padx=20, pady=5)
        Entry(self.root, textvariable=self.sNum,width=5).grid(row=2,  column=1, sticky=W,padx=10, pady=5)
        Label(self.root,text='-').grid(row=2,column=1, sticky=W, padx=60, pady=5)
        Entry(self.root, textvariable=self.bNum,width=5).grid(row=2, column=1, sticky=W,padx=80)
        #第四行
        Radiobutton(self.root, text='操作原Excel', variable=self.newExcel, value=0).grid(row=3, column=0, padx=5, pady=5)
        Radiobutton(self.root, text='生成新Excel', variable=self.newExcel, value=1).grid(row=3, column=1,  padx=5, pady=5)
        Button(self.root, text="开始", width=10, command=self.start).grid(row=3, column=2, sticky=W, padx=10, pady=5)
        #告警框
        Entry(self.root,textvariable=self.worn, font=('楷体',12),width=40,background='#96b97d').grid(row=4,columnspan=2, column=0, sticky=W, padx=60, pady=5)
        #信息框
        # sb = Scrollbar(self.root)  # 在 root 初始旷 上面插入一 插入一个滚动条 .
        # sb.pack(side=RIGHT, fill=Y)  # 设置滚动条的位置 .
        self.info = Text(self.root, font=('楷体',12),width=60, height=20)
        self.info.grid(row=5,columnspan=3, column=0, sticky=W, padx=10,ipadx=10, pady=5)

        #初始化
        self.newExcel.set(1)

    def setWorn(self,info):
        self.worn.set(info)

    def setInfo(self,info):
        self.info.insert(END,info)

    def delInfo(self):
        self.info.delete(0.0, END)

    def setUrlCookie(self):
        str = ''
        cookie = dict(coo.GetCookie('www.qichacha.com').get(), **coo.GetCookie('.qichacha.com').get())
        if (len(cookie) == 0):
            self.setWorn('请先用谷歌浏览器登录企查查网站！')
            self.isLogin = False
            return
        for item in cookie:
            str += '%s=%s; ' % (item, cookie[item])
        hd.Cookie(str)
        self.setWorn('登录企查查网站成功！')

    def search(self):
        data = {}
        list = []
        self.delInfo()
        if self.isLogin == False:
            self.setUrlCookie()

        company = self.companyName.get()
        if len(company) == 0:
            self.setWorn("请输入企业名称/人名(以空格隔开)")
            return
        clist = company.split(' ')
        for i in range(len(clist)):
            if clist[i] != '':
                list.append(clist[i])
        for i in range(len(list)):
            self.setWorn("正在查询第%s条信息，总共%s条信息" % (i + 1, len(list)))
            info = qcc.Qichacha(list[i],self.setWorn).getInfoDist()
            if len(info) == 0:
                self.setWorn("企查查登录已经过期，请重新登录！")
                return

            data[list[i]] = info
            for key in info:
                self.setInfo('%s:%s\n' %(key ,info[key]))
            self.setWorn("查询完毕，总共%s条信息" % len(list))
            self.setInfo('\n===============================================\n')

    def start(self):
        self.setWorn('现在还特么不能用！')

    def mainloop(self):
        mainloop()

setTkinter().mainloop()

