import sys
from PyQt5.QtWidgets import QApplication

from UI.mainwindow import MainWindow
from UI.Login import LoginWindow
from dao.mydatabase import MyDatabase
from service.backup import BackUp


BackUp() #防止数据库被意外删除，恢复上次打开的数据库
app = QApplication(sys.argv)
mydb = MyDatabase() #连接数据库 #加载密码
print(mydb.account)
mainwindow = MainWindow(dababase=mydb)  #加载主屏
lw = LoginWindow(mainwindow=mainwindow,database=mydb) #加载登陆密码屏
lw.show()
sys.exit(app.exec_())
