from Connect import cursor
from Connect import conn

import mainui
def deleting():
    selectall()
    deleteno = eval(input("请选择你要删除的号码"))
    cursor.execute('DELETE FROM DestInfoSheet WHERE DestNo=%d',deleteno)
    conn.commit()
    selectall()

    
def updating():
    print("当前进入更新窗格")
    while True:
        selectall()
        c = input("请选择你要更改的线路的编号,输入quit退出当前模块")
        if c is 'quit':
            mainui.uiDisplay()
        else:
            c = (eval)(c)
            item = ['1.线路信息','2.线路花费','3.线路介绍','4.线路路径']
            for w in item:
                print(w)
            c2 = eval(input("请选择你要更改的信息"))
            if c2==1:
                newinfo = input("请输入新的线路信息：")
                cursor.execute('UPDATE DestInfoSheet SET Name = %s WHERE DestNo = %d',(newinfo,c))
            elif c2==2:
                newfee = eval(input("请输入新的线路花费"))
                cursor.execute('UPDATE DestInfoSheet SET Cost = %d WHERE DestNo = %d',(newfee,c))
            elif c2==3:
                newintro = input("请输入线路介绍：")
                cursor.execute('UPDATE DestInfoSheet SET Intro = %s WHERE DestNo = %d',(newintro,c))
            elif c2==4:
                newpath = input("请输入新的线路路径")
                cursor.execute('UPDATE DestInfoSheet SET Graph = %s WHERE DestNo = %d',(newpath,c))
            conn.commit()
def add():
     
    roadinfo = str(input("请输入线路信息："))
    roadfee = eval(input("请输入线路花费："))
    roadintro = str(input("请输入线路介绍："))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    roadgraph = str(input("请输入线路 路径："))
    roadno = eval(input("线路编号："))
    cursor.execute('INSERT INTO DestInfoSheet VALUES (%s,%d,%s,%s,%d)',(roadinfo,roadfee,roadintro,roadgraph,roadno))
    conn.commit()

def selectall():
    
    cursor.execute('SELECT * FROM DestInfoSheet')
    row = cursor.fetchone()
    print("线路信息\t\t\t线路花费\t\t\t线路介绍\t\t\t线路路径\t\t\t线路编号")
    while row:
        i = 0
        while i<5:
            print((str)(row[i])+"\t\t\t",end='')
            i = i + 1
        print("\n")
        row = cursor.fetchone()

def selectinfo():
    #按照线路信息的盲搜模块
    #这里是字符串的输入
    info = input("请输入相关线路信息")
    info = "%" + (str)(info) + "%"
    cursor.execute('SELECT * FROM DestInfoSheet WHERE Name LIKE %s',info)
    row = cursor.fetchone()
    print("线路信息\t\t\t线路花费\t\t\t线路介绍\t\t\t线路路径\t\t\t线路编号")
    while row:
        i = 0
        while i<5:
            print((str)(row[i])+"\t\t\t",end='')
            i = i + 1
        print("\n")
        row = cursor.fetchone()

def main():    
    while True: 
        print("当前是线路信息管理窗格")
        menuList = ['增加','修改','删除','查询','退出模块','自定义SQL语句']
        count = 1
        for words in menuList:
            print((str)(count)+":"+words)
            count = count + 1
        choose = eval(input("请选择你需要的功能:"))
        if choose==1:
           add()

        elif choose==2: 
           updating()
        elif choose==3:
           deleting()
        elif choose==4:
            a = eval(input("1.查询所有 2.按线路信息盲搜\n"))
            if a==1:
                selectall()
            elif a==2:
                selectinfo()
        elif choose==5:
                mainui.uiDisplay()
        
        




 