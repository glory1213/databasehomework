from Connect import cursor
from Connect import conn
# from main import uiDisplay as uiDisplay2
import mainui
def deleting():
    selectall()
    deleteno = eval(input("请选择你要删除的号码"))
    cursor.execute('DELETE FROM TeamInfoSheet WHERE TeamNo=%d',deleteno)
    conn.commit()
    selectall()

    
def updating():
    print("当前进入更新窗格")
    while True:
        selectall()
        c = input("请选择你要更改的团队编号,输入quit退出当前模块")
        if c is 'quit':
            mainui.uiDisplay()
        else:
            c = (eval)(c)
            item = ['团队编号','目的地编号','团队人数','出发日期','返程日期']
            count = 1
            for w in item:
                print((str)(count)+":"+w)
                count = count + 1
            c2 = eval(input("请选择你要更改的信息"))
            if c2==1:
                newdestno = eval(input("请输入团队编号"))
                cursor.execute('UPDATE TeamInfoSheet SET DestNo = %d WHERE TeamNo = %d',(newdestno,c))
            elif c2==2:
                newteamno = eval(input("请输入目的地编号"))
                cursor.execute('UPDATE TeamInfoSheet SET TeamNo = %d WHERE TeamNo = %d',(newteamno,c))
            elif c2==3:
                newname = input("请输入团队人数")
                cursor.execute('UPDATE TeamInfoSheet SET Name = %s WHERE TeamNo = %d',(newname,c))
            elif c2==4:
                newsex = input("请输入出发日期")
                cursor.execute('UPDATE TeamInfoSheet SET Sex = %s WHERE TeamNo = %d',(newsex,c))
            elif c2==5:
                newtel = input("请输入返程日期")
                cursor.execute('UPDATE TeamInfoSheet SET Tel = %s WHERE TeamNo = %d',(newtel,c))

            conn.commit()
def add():

    printf("目前状态")
    selectall()
    teamno = eval(input("请输入团队编号"))
    destno = eval(input("请输入目的地编号"))
    teamnum = eval(input("请输入团队人数"))
    teamleave = eval(input("请输入出发日期"))
    teamreturn = eval(input("请输入返程日期"))
    
    
    cursor.execute('INSERT INTO TeamInfoSheet VALUES (%d,%d,%d,%d,%d)',(teamno,destno,teamnum,teamleave,teamreturn)) 
    conn.commit()

def selectall():
    
    cursor.execute('SELECT * FROM TeamInfoSheet')
    row = cursor.fetchone()
    print("团队编号\t\t\t目的地编号\t\t\t团队人数\t\t\t出发日期\t\t\t返程日期")
    while row:
        i = 0
        while i<5:
            print((str)(row[i])+"\t\t\t",end='')
            i = i + 1
        print("\n")
        row = cursor.fetchone()

def main():    
    while True: 
        print("当前是排团信息管理窗格")
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
             selectall()
         
        elif choose==5:
            mainui.uiDisplay()