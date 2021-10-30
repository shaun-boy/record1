# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QDate,Qt
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView

from .Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self,dababase=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__()
        self.setupUi(self)
        self.lineEdit_money.setValidator(QDoubleValidator())
        self.lineEdit_money_she.setValidator(QDoubleValidator())
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.tableWidget_main.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.db = dababase

    @pyqtSlot()
    def on_actionabout_triggered(self):
        QMessageBox.about(self,"关于软件","个人记账软件测试版\n版本：1.0\n设计者：shaun")

    @pyqtSlot()
    def on_actionfind_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_add_clicked(self):
        category = self.comboBox_category.currentText()
        date = self.dateTimeEdit.date().toString("yyyy/MM/dd")
        time = self.dateTimeEdit.time().toString("hh:mm")
        use = self.lineEdit_use.text()
        name = self.lineEdit_name.text()
        money = self.lineEdit_money.text()
        money_she = self.lineEdit_money_she.text()
        if len(use) == 0 or len(name) == 0 or len(money) == 0:
            QMessageBox.critical(self, "信息提示框", "输入不完整，请检查")
        else:
            sql = 'insert into record (类别,日期,时间,姓名,作用,金额,赊账) ' \
                  'values ("{}","{}","{}","{}","{}","{}","{}")'.format(category,date,time,name,use,money,money_she)

            qm = QMessageBox.question(self, "信息提示框", "确定新增记录？Yes/No",
                                      QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if qm == QMessageBox.Yes:
                self.db.csr.execute(sql)
                self.db.conn.commit()
                self.on_pushButton_queryall_clicked()
            else:
                pass
    
    @pyqtSlot()
    def on_pushButton_query_clicked(self):
        selectDate = self.dateTimeEdit.date().toString("yyyy/MM/dd")
        data = self.db.csr.execute("select * from record where 日期 = '{}'".format(selectDate)).fetchall()
        self.tableWidget_main.clearContents()
        for i in range(len(data)):
            for j in range(8):
                temp = data[i][j]
                if temp:
                    shuju = QTableWidgetItem(str(temp))
                    shuju.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget_main.setItem(i, j, shuju)
    
    @pyqtSlot()
    def on_pushButton_delete_clicked(self):
        rowIndex = self.tableWidget_main.currentIndex().row()
        if rowIndex < 0:
            QMessageBox.warning(self,"提示","用鼠标选择想删除的行")
        else:
            selectID = self.tableWidget_main.item(rowIndex,0).text()
            tip = QMessageBox.critical(self,"警告","请检查考虑清楚，数据删除是不可恢复的",
                                 QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if tip == QMessageBox.Yes:
                self.db.csr.execute("DELETE FROM record WHERE ID = {}".format(int(selectID)))
                self.db.conn.commit()
                self.on_pushButton_queryall_clicked()
            else:
                pass
    
    @pyqtSlot()
    def on_pushButton_day_info_clicked(self):
        currentDay = QtCore.QDate.currentDate().toString("yyyy/MM/dd")
        money = self.db.csr.execute("select 类别,金额,赊账 from record where 日期 = '{}'".format(currentDay))
        shouru = 0
        zhichu = 0
        shezhang = 0
        for i in money:
            for j in i:
                if j == "收入":
                    shouru += i[1]
                    if i[2] != "":
                        shezhang += i[2]
                elif j == "支出":
                    zhichu += i[1]
        self.label_day_input.setText(str(shouru))
        self.label_day_shezhang.setText(str(shezhang))
        self.label_day_output.setText(str(zhichu))
        self.label_day_lirun.setText(str(shouru-zhichu))
    
    @pyqtSlot()
    def on_pushButton_queryall_clicked(self):
        day = QDate.currentDate().toString("yyyy/MM")
        data = self.db.csr.execute("select * from record where 日期 glob '{}*'".format(day)).fetchall()
        #rowCount = self.db.csr.execute('select count(*) from record').fetchone()[0]
        rowCount = len(data)
        columnCount = len(data[0])

        self.tableWidget_main.setRowCount(rowCount)
        self.tableWidget_main.setColumnCount(columnCount)

        for i in range(0,rowCount):
            for j in range(0,columnCount):
                temp = data[i][j]
                if temp:
                    shuju = QTableWidgetItem(str(temp))
                    shuju.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget_main.setItem(i, j, shuju)
