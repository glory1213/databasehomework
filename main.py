#author:liuliu

import UserInfo #导入用户管理模块
import Connect #数据库连接模块
import mainui
       
if __name__ == "__main__":
       #程序入口
    Connect.main()
    a = UserInfo.login()
    if a == 1:
    
        mainui.uiDisplay()
    else:
        exit()
    

    
    
    
