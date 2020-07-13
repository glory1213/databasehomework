import pymssql #DB-SIG compliant module for communicating with MS SQL servers
from Connect import cursor
from Connect import conn
from getpass import getpass

def main():
    while True: 
        print("当前是用户管理窗格")
        menuList = ['增加用户','修改密码','备份','恢复']
        count = 1
        for words in menuList:
            print((str)(count)+":"+words)
            count = count + 1
        choose = eval(input("请选择你需要的功能"))
        if choose==1:
           username = input("请输入用户名")
           flag = 0
           password = input("请输入密码")
           while flag==0:
                passwordconfirm = input("请再输入一次")
                if password==passwordconfirm:
                    
                    cursor.execute('INSERT INTO UserInfoSheet VALUES (%s,%s)',(username,password)) 
                    conn.commit()
                    flag=1
        elif choose==2:
           cursor.execute('SELECT username FROM UserInfoSheet')
           no = input("请输入要更改密码的用户")
           newpass = input("输入新的密码:")
           while True:
            newpassconfirm = input("请再输入一次：")
            if newpass is newpassconfirm:
               cursor.excute('UPDATE UserInfoSheet Set password = %s WHERE username = %s ',(username,password))
               conn.commit()
               break
        # elif choose==3:
        #     backup()
        # elif choose==4:
        #     recuse()

def backup():
    cursor.execute('Backup Database touristagency To disk = D:\backup.bak')
    conn.commit()
def recuse():
    cursor.execute('Restore database touristagency from disk = D:\backup.bak')
    conn.commit()

def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")

    cursor.execute('select password from UserInfoSheet WHERE UserName = %s',username)
    row = cursor.fetchone()
    if row[0] == password:
        return 1;
    else:
        return 0;



        


