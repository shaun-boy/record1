import sqlite3


class MyDatabase:

    def __init__(self):
        str = 'record1.db'
        try:
            self.conn = sqlite3.connect(str)
            print("successfully")
        except:
            print("数据库连接失败")
        self.csr = self.conn.cursor()

        accountpwd = self.csr.execute("select * from accountpwd").fetchall()
        self.account = accountpwd[0][0]
        self.pwd = accountpwd[0][1]

        self.recorddata = self.csr.execute("select * from record").fetchall()

    def close(self):
        self.csr.close()
        self.conn.close()
