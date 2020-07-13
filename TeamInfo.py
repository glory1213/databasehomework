from Connect import cursor
from Connect import conn
import mainui
def deleting():
    selectall()
    deleteno = eval(input("请选择你要删除的号码"))
    cursor.execute('DELETE FROM GroupInfoSheet WHERE GroupNo=%d',deleteno)
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
            item = ['该组负责人','人数','日期','出发','费用','盈利']
            count = 1
            for w in item:
                print((str)(count)+":"+w)
                count = count + 1
            c2 = eval(input("请选择你要更改的信息"))
            if c2==1:
                newGroupNo = input("请输入负责人")
                cursor.execute('UPDATE GroupInfoSheet SET GroupNo = %d WHERE GroupNo = %d',(newGroupNo,c))
            elif c2==2:
                newnum = eval(input("请输入人数"))
                cursor.execute('UPDATE GroupInfoSheet SET Name = %s WHERE GroupNo = %d',(newnum,c))
            elif c2==3:
                newdate = input("请输入日期")
                cursor.execute('UPDATE GroupInfoSheet SET Sex = %s WHERE GroupNo = %d',(newdate,c))
            elif c2==4:
                newisleave = input("请输入是否出发")
                cursor.execute('UPDATE GroupInfoSheet SET Tel = %s WHERE GroupNo = %d',(newisleave,c))
            elif c2==5:
                newfee = eval(input("请输入新的费用"))
                cursor.execute('UPDATE GroupInfoSheet SET Tel = %s WHERE GroupNo = %d',(newfee,c))
            elif c2==6:
                newshare = eval(input("请输入盈利金额"))
                cursor.execute('UPDATE GroupInfoSheet SET Tel = %s WHERE GroupNo = %d',(newshare,c))
            conn.commit()
def add():

    printf("目前状态")
    selectall()
    GroupNo = eval(input("请输入组别编号"))
    GroupCharge = input("请输入该组负责人")
    Groupnum = eval(input("请输入该组人数"))
    GroupSetDate = input("请输入建组日期")
    Groupisleave = input("请输入是否出发")
    GroupFee = eval(input("请输入费用"))
    GroupShare = eval(input("请输入盈利数额"))
    
    
    
    cursor.execute('INSERT INTO GroupInfoSheet VALUES (%d,%s,%d,%s,%s,%s,%d,%d)',(GroupNo,GroupCharge,Groupnum,GroupSetDate,Groupisleave,GroupFee,GroupShare)) 
    conn.commit()
    selectall()

def selectall():
    
    cursor.execute('SELECT * FROM GroupInfoSheet')
    row = cursor.fetchone()
    print("组别编号\t\t\t负责人\t\t\t\t该组人数\t\t\t建组日期\t\t\t是否出发\t\t\t费用\t\t\t\t\t盈利数额\t\t\t")
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