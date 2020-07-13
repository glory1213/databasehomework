import pymssql #DB-SIG compliant module for communicating with MS SQL servers
import DestInfo  #导入线路信息模块
import TouristInfo #导入游客信息模块
import ArragementInfo #导入排团信息模块
import TeamInfo  #导入导游信息模块
import UserInfo #导入用户管理模块
def uiDisplay():
    #视图层与逻辑层分离
    while True:
        menuList = ['线路信息管理','游客信息管理','排团信息管理','导游信息管理','用户管理/备份恢复','退出程序']
        print("欢迎使用旅行社信息管理系统")
        count = 1;
        for w in menuList:
            print((str)(count)+":"+w)
            count = count + 1
        choose = eval(input("请输入你想要的功能"))
        if choose==1:
            DestInfo.main()
        elif choose==2:
            TouristInfo.main()
        elif choose==3:
            ArragementInfo.main()
        elif choose==4:
            TeamInfo.main()
        elif choose==5:
            UserInfo.main()
        elif choose==6:
           exit()