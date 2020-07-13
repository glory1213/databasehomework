from Connect import cursor
from Connect import conn
# from main import uiDisplay
import mainui
def deleting():
    selectall()
    deleteno = eval(input("请选择你要删除的号码"))
    cursor.execute('DELETE FROM MemInfoSheet WHERE DestNo=%d',deleteno)
    conn.commit()
    selectall()

    
def updating():
    print("当前进入更新窗格")
    while True:
        selectall()
        c = input("请选择你要更改的团员编号,输入quit退出当前模块")
        if c is 'quit':
            mainui.uiDisplay()
        else:
            c = (eval)(c)
            item = ['目的地编号','团队编号','团员编号','姓名','性别','电话','地址','身份证号码','是否支付','备注']
            count = 1
            for w in item:
                print((str)(count)+":"+w)
                count = count + 1
            c2 = eval(input("请选择你要更改的信息"))
            if c2==1:
                newdestno = eval(input("请输入目的地编号："))
                cursor.execute('UPDATE MemInfoSheet SET DestNo = %d WHERE MemNo = %d',(newdestno,c))
            elif c2==2:
                newteamno = eval(input("请输入新的团队编号："))
                cursor.execute('UPDATE MemInfoSheet SET TeamNo = %d WHERE MemNo = %d',(newteamno,c))
            elif c2==3:
                newname = input("请输入新的姓名")
                cursor.execute('UPDATE MemInfoSheet SET Name = %s WHERE MemNo = %d',(newname,c))
            elif c2==4:
                newsex = input("请输入新的性别")
                cursor.execute('UPDATE MemInfoSheet SET Sex = %s WHERE MemNo = %d',(newsex,c))
            elif c2==5:
                newtel = input("请输入新的电话")
                cursor.execute('UPDATE MemInfoSheet SET Tel = %s WHERE MemNo = %d',(newtel,c))
            elif c2==6:
                newadd = input("请输入新的地址")
                cursor.execute('UPDATE MemInfoSheet SET Address = %s WHERE MemNo = %d',(newadd,c))

            elif c2==7:
                newidcardnum = input("请输入新的身份证号码")
                cursor.execute('UPDATE MemInfoSheet SET IdcardNum = %s WHERE MemNo = %d',(newidcardnum,c))

            elif c2==8:
                newispaid = input("请输入是否支付")
                cursor.execute('UPDATE MemInfoSheet SET IsPaid = %s WHERE MemNo = %d',(newispaid,c))

            elif c2==9:
                newtips = input("请输入备份")
                cursor.execute('UPDATE MemInfoSheet SET tips = %s WHERE MemNo = %d',(newtips,c))
            conn.commit()
def add():


    memno = eval(input("请输入成员编号"))
    memname = input("请输入姓名")
    memsex = input("请输入性别")
    memtel = input("请输入电话")
    memaddress = input("请输入地址")
    memidcardnum = input("请输入身份证号码")
    memispaid = input("是否支付 ?请输入是或否")
    memtips = input("请输入备注")
    cursor.execute('SELECT * FROM DestInfoSheet WHERE Name LIKE %s',info)
    row = cursor.fetchone()
    print("线路信息\t\t\t线路花费\t\t\t线路介绍\t\t\t线路路径\t\t\t线路编号")
    memdestno = eval(input("请输入目的地编号"))
    
    cursor.execute('INSERT INTO MemInfoSheet VALUES (%d,%s,%s,%s,%s,%s,%s,%s,%d)',(memno,memname,memsex,memtel,memaddress,memidcardnum,memispaid,memtips,memdestno)) 
    conn.commit()

def selectall():
    
    cursor.execute('SELECT * FROM MemInfoSheet')
    row = cursor.fetchone()
    print("目的地编号\t\t\t团队号码\t\t\t成员编号\t\t\t姓名\t\t\t性别\t\t\t电话\t\t\t地址\t\t\t身份证号码\t\t\t是否交费\t\t\t备注")
    while row:
        i = 0
        while i<10:
            print((str)(row[i])+"\t\t\t",end='')
            i = i + 1
        print("\n")
        row = cursor.fetchone()

def selectinfo():
    #按照线路信息的盲搜模块
    #这里是字符串的输入
    info = input("请输入相关姓名")
    info = "%" + (str)(info) + "%"
    cursor.execute('SELECT * FROM DestInfoSheet WHERE Name LIKE %s',info)
    row = cursor.fetchone()
    print("目的地编号\t\t\t团队号码\t\t\t成员编号\t\t\t姓名\t\t\t性别\t\t\t电话\t\t\t地址\t\t\t身份证号码\t\t\t是否交费\t\t\t备注")
    while row:
        i = 0
        while i<10:
            print((str)(row[i])+"\t\t\t",end='')
            i = i + 1
        print("\n")
        row = cursor.fetchone()

def main():    
    while True: 
        print("当前是游客信息管理窗格")
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
            a = eval(input("1.查询所有 2.按姓名盲搜\n"))
            if a==1:
                selectall()
            elif a==2:
                selectinfo()
        elif choose==5:
                mainui.uiDisplay()
        


    
