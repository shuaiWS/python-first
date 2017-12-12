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

        self.__initui()
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
        Entry(self.root,textvariable=self.worn, font=('楷体',14),width=20,background='#96b97d').grid(row=4,columnspan=2, column=0, sticky=W, padx=60, pady=5)
        #信息框
        # sb = Scrollbar(self.root)  # 在 root 初始旷 上面插入一 插入一个滚动条 .
        # sb.pack(side=RIGHT, fill=Y)  # 设置滚动条的位置 .
        self.info = Text(self.root, font=('楷体',12),width=60, height=20).grid(row=5,columnspan=3, column=0, sticky=W, padx=10,ipadx=10, pady=5)

        #初始化
        self.newExcel.set(1)
    def setWorn(self,info):
        self.worn.set(info)

    def setInfo(self,info):
        self.info.insert(END,info)

    def search(self):
        pass

    def start(self):
        pass

    def mainloop(self):
        mainloop()

# tk = setTkinter()
# tk.mainloop()