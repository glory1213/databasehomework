import pymssql

conn = pymssql.connect(server = '127.0.0.1' , database = "touristagency")
cursor = conn.cursor()

def main():
    print("数据库连接成功")

    
    