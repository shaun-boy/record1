# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from service import controller
from .Ui_Login import Ui_MainWindow


class LoginWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, mainwindow=None,database=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__()
        self.setupUi(self)


        self.mainwindow = mainwindow
        self.mydb = database

    @pyqtSlot()
    def on_pushButton_launch_clicked(self):
        account = self.LineEdit_account.text()
        pwd = self.LineEdit_password.text()
        if controller.validation(account,self.mydb.account) and controller.validation(pwd, self.mydb.pwd):
            self.mainwindow.show()
            self.close()
        else:
            QMessageBox.warning(self,"warning","账号或密码错误")
