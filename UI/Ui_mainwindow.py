# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Java\Java program\pyprogram\accountbook\UI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 700)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        MainWindow.setMaximumSize(QtCore.QSize(2400, 1200))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mwico/g8.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 221, 40))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(250, 60, 191, 41))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_money = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_money.setFont(font)
        self.label_money.setObjectName("label_money")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_money)
        self.lineEdit_money = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_money.setFont(font)
        self.lineEdit_money.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_money.setInputMask("")
        self.lineEdit_money.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_money.setClearButtonEnabled(False)
        self.lineEdit_money.setObjectName("lineEdit_money")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_money)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(450, 10, 391, 40))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lineEdit_use = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit_use.setFont(font)
        self.lineEdit_use.setCursorPosition(0)
        self.lineEdit_use.setObjectName("lineEdit_use")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_use)
        self.label_use = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_use.setFont(font)
        self.label_use.setObjectName("label_use")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_use)
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(270, 12, 169, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.formLayoutWidget_4.setFont(font)
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.comboBox_category = QtWidgets.QComboBox(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_category.setFont(font)
        self.comboBox_category.setObjectName("comboBox_category")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_category)
        self.label_category = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_category.setFont(font)
        self.label_category.setObjectName("label_category")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_category)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(20, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_query = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_query.setGeometry(QtCore.QRect(20, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_query.setFont(font)
        self.pushButton_query.setObjectName("pushButton_query")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(20, 260, 81, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_delete.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet("background-color:rgb(255, 170, 127)")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(450, 60, 191, 41))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.lineEdit_money_she = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_money_she.setFont(font)
        self.lineEdit_money_she.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_money_she.setInputMask("")
        self.lineEdit_money_she.setObjectName("lineEdit_money_she")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_money_she)
        self.label_money_she = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_money_she.setFont(font)
        self.label_money_she.setObjectName("label_money_she")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_money_she)
        self.tableWidget_main = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_main.setGeometry(QtCore.QRect(110, 140, 731, 521))
        self.tableWidget_main.setAutoFillBackground(False)
        self.tableWidget_main.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_main.setAlternatingRowColors(False)
        self.tableWidget_main.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_main.setRowCount(15)
        self.tableWidget_main.setColumnCount(8)
        self.tableWidget_main.setObjectName("tableWidget_main")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_main.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_main.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_main.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_main.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_main.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_main.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_main.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_main.setHorizontalHeaderItem(7, item)
        self.tableWidget_main.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_main.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_main.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_main.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_main.verticalHeader().setVisible(False)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(18, 13, 241, 33))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 14), QtCore.QTime(8, 30, 0)))
        self.dateTimeEdit.setTime(QtCore.QTime(8, 30, 0))
        self.dateTimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2021, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.groupBox_day = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_day.setGeometry(QtCore.QRect(850, 10, 195, 211))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_day.setFont(font)
        self.groupBox_day.setObjectName("groupBox_day")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_day)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox_day)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_day_input = QtWidgets.QLabel(self.groupBox_day)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_day_input.setFont(font)
        self.label_day_input.setText("")
        self.label_day_input.setObjectName("label_day_input")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_day_input)
        self.label_2 = QtWidgets.QLabel(self.groupBox_day)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_day_output = QtWidgets.QLabel(self.groupBox_day)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_day_output.setFont(font)
        self.label_day_output.setText("")
        self.label_day_output.setObjectName("label_day_output")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_day_output)
        self.label_3 = QtWidgets.QLabel(self.groupBox_day)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_day_lirun = QtWidgets.QLabel(self.groupBox_day)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_day_lirun.setFont(font)
        self.label_day_lirun.setText("")
        self.label_day_lirun.setObjectName("label_day_lirun")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_day_lirun)
        self.label_4 = QtWidgets.QLabel(self.groupBox_day)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_day_shezhang = QtWidgets.QLabel(self.groupBox_day)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_day_shezhang.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_day_shezhang.setFont(font)
        self.label_day_shezhang.setText("")
        self.label_day_shezhang.setObjectName("label_day_shezhang")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_day_shezhang)
        self.verticalLayout.addLayout(self.formLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_day_info = QtWidgets.QPushButton(self.groupBox_day)
        self.pushButton_day_info.setObjectName("pushButton_day_info")
        self.verticalLayout.addWidget(self.pushButton_day_info)
        self.pushButton_queryall = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_queryall.setGeometry(QtCore.QRect(20, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_queryall.setFont(font)
        self.pushButton_queryall.setObjectName("pushButton_queryall")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionfind = QtWidgets.QAction(MainWindow)
        self.actionfind.setObjectName("actionfind")
        self.menu.addAction(self.actionclose)
        self.menu_2.addAction(self.actionfind)
        self.menu_3.addAction(self.actionabout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.actionclose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "记账软件"))
        self.label_name.setText(_translate("MainWindow", "姓名："))
        self.lineEdit_name.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">必须填，不填会报错</span></p></body></html>"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "必填"))
        self.label_money.setText(_translate("MainWindow", "金额："))
        self.lineEdit_money.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">必须填，不填会报错</span></p></body></html>"))
        self.lineEdit_money.setPlaceholderText(_translate("MainWindow", "必填"))
        self.lineEdit_use.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">必须填，不填会报错</span></p></body></html>"))
        self.lineEdit_use.setPlaceholderText(_translate("MainWindow", "(必填)洗车，修车等等"))
        self.label_use.setText(_translate("MainWindow", "作用："))
        self.comboBox_category.setToolTip(_translate("MainWindow", "<html><head/><body><p>必须选则正确，不然账本会混乱</p><p>收钱===收入</p><p>花钱===支出</p></body></html>"))
        self.comboBox_category.setItemText(0, _translate("MainWindow", "收入"))
        self.comboBox_category.setItemText(1, _translate("MainWindow", "支出"))
        self.label_category.setText(_translate("MainWindow", "类型："))
        self.pushButton_add.setToolTip(_translate("MainWindow", "添加一笔记录"))
        self.pushButton_add.setText(_translate("MainWindow", "添加记录"))
        self.pushButton_query.setToolTip(_translate("MainWindow", "选择查询日期"))
        self.pushButton_query.setText(_translate("MainWindow", "选日期查询"))
        self.pushButton_delete.setToolTip(_translate("MainWindow", "<html><head/><body><p>慎重选择，删除后不可恢复</p></body></html>"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除"))
        self.lineEdit_money_she.setToolTip(_translate("MainWindow", "<html><head/><body><p>只有赊账和记账时填写。</p><p>例子1：</p><p>比如应该付500，实际付30元</p><p>金额就填500，实收填30</p><p><br/></p><p><br/></p></body></html>"))
        self.lineEdit_money_she.setPlaceholderText(_translate("MainWindow", "选填"))
        self.label_money_she.setText(_translate("MainWindow", "赊账："))
        item = self.tableWidget_main.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_main.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "日期"))
        item = self.tableWidget_main.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时间"))
        item = self.tableWidget_main.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "类别"))
        item = self.tableWidget_main.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_main.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "作用"))
        item = self.tableWidget_main.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "金额"))
        item = self.tableWidget_main.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "赊账"))
        self.dateTimeEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>最好自己检查一下时间对不对</p></body></html>"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd H:mm"))
        self.groupBox_day.setToolTip(_translate("MainWindow", "<html><head/><body><p>当天状况：</p><p>营收=收入-支出，所以可能是负数</p></body></html>"))
        self.groupBox_day.setTitle(_translate("MainWindow", "当日信息："))
        self.label.setText(_translate("MainWindow", "收入："))
        self.label_2.setText(_translate("MainWindow", "支出："))
        self.label_3.setText(_translate("MainWindow", "营收："))
        self.label_4.setText(_translate("MainWindow", "赊账:"))
        self.pushButton_day_info.setText(_translate("MainWindow", "查询当天信息"))
        self.pushButton_queryall.setToolTip(_translate("MainWindow", "添加一笔记录"))
        self.pushButton_queryall.setText(_translate("MainWindow", "当月记录"))
        self.menu.setTitle(_translate("MainWindow", "程序"))
        self.menu_2.setTitle(_translate("MainWindow", "查找记录"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.actionclose.setText(_translate("MainWindow", "退出程序"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionfind.setText(_translate("MainWindow", "查询"))
import ico.ico_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())