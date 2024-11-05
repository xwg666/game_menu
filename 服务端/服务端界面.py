import datetime
import os
import time
from http import HTTPStatus
import PySide6
import dashscope
import redis
from PyQt6.QtWidgets import QProgressDialog
from PySide6 import QtWidgets, QtCore

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QThread, Signal)
from PyQt6.QtCore import QThread, QObject, pyqtSignal
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget, QMenu, QMessageBox, QListWidget, QListWidgetItem, QAbstractItemView, QLabel,
                               QTextEdit)
from dashscope import Generation
import pymysql as sql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1419, 832)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 1400, 800))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(-10, 3, 181, 71))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/YTY.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 331, 31))
        font1 = QFont()
        font1.setItalic(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(350, 20, 61, 31))
        self.pushButton_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 20, 75, 31))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.pushButton_2.setFont(font2)
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(360, 20, 75, 31))
        self.pushButton_3.setFont(font2)
        self.pushButton_10 = QPushButton(self.frame_6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(180, 20, 75, 31))

        self.horizontalLayout.addWidget(self.frame_6)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(9)
        self.frame_3.setFont(font3)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 0, 201, 701))
        self.frame_7.setFont(font3)
        self.frame_7.setStyleSheet(u"\n"
                                   "background-color: rgb(0, 148, 222);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 40, 81, 31))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.listWidget = QListWidget(self.frame_8)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(40, 80, 121, 171))
        font5 = QFont()
        font5.setPointSize(10)
        self.listWidget.setFont(font5)
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(60, 30, 81, 31))
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.frame_10)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(50, 30, 101, 31))
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(200, 0, 1201, 701))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 1200, 701))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.pushButton_14 = QPushButton(self.frame_15)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(950, 40, 81, 31))
        self.pushButton_15 = QPushButton(self.frame_15)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(1080, 40, 81, 31))
        self.pushButton_16 = QPushButton(self.frame_15)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(950, 130, 81, 31))
        self.label_2 = QLabel(self.frame_15)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(950, 180, 221, 31))
        # self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_17 = QPushButton(self.frame_15)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(950, 260, 75, 24))
        self.pushButton_18 = QPushButton(self.frame_15)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(1080, 260, 75, 24))
        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(940, 300, 231, 351))
        self.frame_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(950, 0, 211, 31))
        # self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.frame_15)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(950, 90, 211, 31))
        # self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_19 = QPushButton(self.frame_15)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(1010, 220, 81, 31))

        # -----------------------------------------------------------
        # -----------------------------------------------------------
        self.tableWidget = QTableWidget(self.frame_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(200, 0, 1201, 701))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Raised)
        # 设置点击选取整行
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 新建一个tablewidget2
        self.tableWidget2 = QtWidgets.QTableWidget(self.frame_15)
        self.tableWidget2.setGeometry(QtCore.QRect(0, 0, 901, 701))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget2.setFrameShape(QFrame.StyledPanel)
        self.tableWidget2.setFrameShadow(QFrame.Raised)
        # 设置点击选取整行
        self.tableWidget2.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 给frame_14添加一个tablewidget3
        self.tableWidget3 = QtWidgets.QTableWidget(self.frame_15)
        self.tableWidget3.setGeometry(QtCore.QRect(940, 300, 231, 351))
        self.tableWidget3.setObjectName("tableWidget2")
        self.tableWidget3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget3.setFrameShape(QFrame.StyledPanel)
        self.tableWidget3.setFrameShadow(QFrame.Raised)
        # 设置点击选取整行
        self.tableWidget3.setSelectionBehavior(QAbstractItemView.SelectRows)

        # self.tableWidget3 = QTableWidget(self.frame_14)
        # self.tableWidget3.setObjectName(u"tableWidget3")
        # self.tableWidget3.setGeometry(QRect(940, 300, 231, 351))
        # # self.tableWidget3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        # self.tableWidget3.setFrameShape(QFrame.StyledPanel)
        # self.tableWidget3.setFrameShadow(QFrame.Raised)
        # # 在textedit中添加可以选择的表格
        # self.tableWidget3.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置主窗口固定，不可伸缩
        MainWindow.setFixedSize(1410, 830)
        # 窗口最小化
        self.pushButton_2.clicked.connect(MainWindow.showMinimized)
        ##绑定函数
        self.pushButton_3.clicked.connect(self.close)

        # 设置pushbutton_4的点击事件
        self.pushButton_4.clicked.connect(self.home_page)
        # 设置pushbutton_5的点击事件
        self.pushButton_5.clicked.connect(self.dir_list)
        # 设置pushbutton_6的点击事件
        self.pushButton_6.clicked.connect(self.client)
        # self.pushButton_6.clicked.connect(self.tableWidget.hide)
        self.pushButton_7.clicked.connect(self.keyReleaseEvent)
        self.pushButton_10.clicked.connect(self.save_data)
        self.pushButton_14.clicked.connect(self.addpath)
        self.pushButton_15.clicked.connect(self.deletepath)
        self.pushButton_16.clicked.connect(self.update)
        self.pushButton_17.clicked.connect(self.del_only_diff)
        self.pushButton_19.clicked.connect(self.diff_file)

        # 设置frame_13的背景色为白色
        # self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        # 设置输入框的placeholder
        self.lineEdit.setPlaceholderText(u"\u5728\u6b64\u641c\u7d22\u6e38\u620f")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        # 绑定函数
        self.lineEdit.textChanged.connect(self.keyReleaseEvent)
        self.listWidget.itemClicked.connect(self.game_type)


        # # # 右键菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.contextMenuEvent)

        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6613\u817e\u4e91\u83dc\u5355", None))
        # self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u641c\u7d22\u6e38\u620f", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5316", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u9996\u9875", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u6e38\u620f", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5355\u673a\u6e38\u620f", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u6e38\u620f", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"steam\u6e38\u620f", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u6e38\u620f", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u5f55\u5217\u8868", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6237\u7aef\u7ba1\u7406", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u8def\u5f84", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u8def\u5f84", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u6e38\u620f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u" \u4ee5\u4e0b\u4e3a\u6570\u636e\u5e93\u548c\u672c\u5730\u6587\u4ef6\u5bf9\u6bd4\u60c5\u51b5\uff1a",
                                                        None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5220\u9664", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5220\u9664", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u" \u7528\u6765\u6dfb\u52a0\u548c\u5220\u9664\u6e38\u620f\u76ee\u5f55\u8def\u5f84\u7684\uff1a",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u" \u7528\u6765\u66f4\u65b0\u6e38\u620f\u76ee\u5f55\u4e0b\u7684\u6267\u884c\u6587\u4ef6\uff1a",
                                                        None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5bf9\u6bd4", None))
    # retranslateUi


    def dir_list(self):
        self.tableWidget.hide()
        self.tableWidget2.show()
        self.frame_15.setVisible(True)
        self.gamepath_list()

    def client(self):
        #设置frame_14和frame_15的不可见
        self.frame_15.setVisible(False)
        self.tableWidget.hide()


    def keyReleaseEvent(self, event):
        #显示tablewidget
        self.tableWidget.show()
        # 获取键盘每次释放后的文本内容
        key = self.lineEdit.text()
        print(key)
        self.search_game(key)


    def sheet_format(self):
        # 清空frame_13的表格
        self.tableWidget.clearContents()
        # self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(11)
        # 设置表格头
        self.tableWidget.setHorizontalHeaderLabels(
            ['id', '游戏名称', '游戏路径', '游戏状态', '备注', '全拼', '缩写', '启动路径', '点击次数', '游戏类型','图标路径'])
        # 设置表格宽度
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 120)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 180)
        self.tableWidget.setColumnWidth(8, 80)
        self.tableWidget.setColumnWidth(9, 100)
        self.tableWidget.setColumnWidth(10, 150)

        #设置滑动条为灰色
        self.tableWidget.setStyleSheet("QScrollBar{background:gray;}")

    def home_page(self):
        #启动右键菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 设置frame_13放在顶层
        self.frame_15.hide()
        self.tableWidget.show()

        # 设置frame_15的不可见
        self.search_game()

    def search_game(self, key=''):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()
        self.sheet_format()
        # 查询数据库
        if len(key) == 0:
            cursor.execute("select id,name,path,state,remark,spell,short,start,click,types,icon from game")
        else:
            cursor.execute(
                f"select id,name,path,state,remark,spell,short,start,click,types,icon from game where name like '%{key}%' or spell like '%{key}%' or short like '%{key}%'")
        data = cursor.fetchall()
        # 设置表格内容
        try:
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
                    # 设置表格内容居中
                    self.tableWidget.item(i, j).setTextAlignment(Qt.AlignCenter)
                    # # 设置表格内容不可编辑
                    # self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled)
                    # 设置表格内容可以复制
                    self.tableWidget.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    # 设置表格内容可以点击
                    # self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)





        except:
            pass
        cursor.close()
        connect.close()

    def contextMenuEvent(self, event):
        menu = QMenu(self.tableWidget)
        menu.setFont(QFont('宋体', 10))
        menu.setStyleSheet(
            'QMenu{margin:10px;}QMenu::item{padding:10px 30px 10px 30px;}QMenu::item:selected{background-color:rgb(0, 170, 255);}')
        item1 = menu.addAction("打开目录")
        item2 = menu.addAction("删除记录")
        item3 = menu.addAction("启动游戏")
        item4 = menu.addAction("修改信息")
        action = menu.exec(self.tableWidget.mapToGlobal(event))
        # self.tableWidget.setContextMenuPolicy(Qt.NoContextMenu)
        if action is None:
            return
        row = self.tableWidget.currentRow()
        selected_item = self.tableWidget.item(row, 1).text()
        print('selected_item：', selected_item)
        if selected_item is None:
            return
        # 获取点击事件的name
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        # 获取路径
        cursor = connect.cursor()
        if action == item1:
            cursor.execute(f'select name,path from game where name="{selected_item}"')
            path = cursor.fetchone()
            path = path[1] + f'\\{path[0]}\\'
            # 打开文件夹
            if os.path.exists(path):
                os.startfile(path)
                return
            else:
                # 文件夹不存在，弹窗提示
                box = QtWidgets.QMessageBox()
                box.setWindowTitle('提示：')
                box.setText(f'{path} 文件夹不存在！')
                box.setStandardButtons(QMessageBox.Ok)
                box.button(QMessageBox.Ok).setText('确定')
                button = box.exec()
                if button == QMessageBox.Ok:
                    return

        if action == item2:
            # 提示是否删除
            box = QtWidgets.QMessageBox()
            box.setWindowTitle('提示：')
            box.setText(f'是否删除 {selected_item}？')
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            box.button(QMessageBox.Yes).setText('确定')
            box.button(QMessageBox.No).setText('取消')
            button = box.exec()
            if button == QMessageBox.No:
                return
            cursor.execute(f'delete from game where name="{selected_item}"')
            connect.commit()
            self.tableWidget.removeRow(row)
            # 提示
            box = QtWidgets.QMessageBox()
            box.setWindowTitle('提示：')
            box.setText(f'删除 {selected_item} 成功！')
            box.setStandardButtons(QMessageBox.Ok)
            box.button(QMessageBox.Ok).setText('确定')
            button = box.exec()
            if button == QMessageBox.Ok:
                return

        if action == item3:
            cursor.execute(f'select start from game where name="{selected_item}"')
            start = cursor.fetchone()
            start = start[0]
            # 判断是否存在start文件
            if not os.path.exists(start):
                box = QtWidgets.QMessageBox()
                box.setWindowTitle('提示：')
                box.setText(f'{start} 文件不存在！')
                box.setStandardButtons(QMessageBox.Ok)
                box.button(QMessageBox.Ok).setText('确定')
                button = box.exec()
                if button == QMessageBox.Ok:
                    return
            box = QtWidgets.QMessageBox()
            box.setWindowTitle('提示：')
            box.setText(f'是否启动 {selected_item}？')
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            box.button(QMessageBox.Yes).setText('确定')
            box.button(QMessageBox.No).setText('取消')
            button = box.exec()
            if button == QMessageBox.No:
                return
            # 使用Qthread启动exe
            self.thread = QThread()
            self.worker = Worker(start)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()

        if action == item4:
            # 使当前选中的行单元格可编辑
            currentRow = self.tableWidget.currentRow()
            column = self.tableWidget.columnCount()
            for currentColumn in range(column):
                currentItem = self.tableWidget.item(currentRow, currentColumn)
                currentItem.setFlags(currentItem.flags() | Qt.ItemIsEditable)
            #     data1.append(currentItem.text())
            # print('data1', data1)
            # self.tableWidget.itemClicked.connect(self.save_data(currentRow, data1,tableWidget=self.tableWidget))
        cursor.close()
        connect.close()

    def save_data(self):
        # 使用thread进行连接row()函数
        if self.tableWidget.currentRow() == -1:
            return
        data = []
        # 获取当前行数
        currentRow = self.tableWidget.currentRow()
        for i in range(self.tableWidget.columnCount()):
            data.append(self.tableWidget.item(currentRow, i).text())

        # 提示是否保存
        box = QtWidgets.QMessageBox()
        box.setWindowTitle('提示：')
        box.setText(f'是否保存 {data[1]}？')
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.button(QMessageBox.Yes).setText('确定')
        box.button(QMessageBox.No).setText('取消')
        button = box.exec()
        if button == QMessageBox.No:
            for i in range(self.tableWidget.columnCount()):
                currentItem = self.tableWidget.item(currentRow, i)
                currentItem.setFlags(currentItem.flags() & ~Qt.ItemIsEditable)

            return
        # 修改数据库
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()
        try:
            path = data[2].replace('\\', '\\\\')
            start = data[7].replace('\\', '\\\\')
            icon = data[10].replace('\\', '\\\\')
            print(path, start, icon)
            cursor.execute(
                f'update game set id="{data[0]}",name="{data[1]}",path="{path}",state="{data[3]}",remark="{data[4]}",spell="{data[5]}",short="{data[6]}", start="{start}",click={data[8]},types="{data[9]}",icon="{icon}" where id={data[0]}')
            connect.commit()
        except Exception as e:
            print(e)
        # 取消当前表格可编辑状态
        for i in range(self.tableWidget.columnCount()):
            currentItem = self.tableWidget.item(currentRow, i)
            currentItem.setFlags(currentItem.flags() & ~Qt.ItemIsEditable)
        return
        # class Worker1(QThread):
        #     finished = pyqtSignal()
        #
        #     def __init__(self, parent=None):
        #         super(Worker1, self).__init__(parent)
        #         self.tableWidget = tableWidget
        #
        #     def run(self):
        #         self.row()
        #         self.finished.emit()
        #
        #     def loop(self):
        #         data = []
        #         while True:
        #             # 获取当前行数
        #             currentRow1 = self.tableWidget.currentRow()
        #             currentRow1_data = self.tableWidget.item(currentRow1, 0).text()
        #             print('currentRow1', currentRow1, 'currentRow1_data', currentRow1_data)
        #             print('currentRow', currentRow, 'currentRow_data', currentRow_data)
        #             #获取点击空白处
        #
        #             if currentRow1 == currentRow and currentRow1_data ==currentRow_data:
        #                 try:
        #                     for i in range(self.tableWidget.columnCount()):
        #                         if len(data) == 0:
        #                             data.append(self.tableWidget.item(currentRow, i).text())
        #                         else:
        #                             continue
        #                 except:
        #                     print('data error')
        #                     return data
        #             else:
        #                 return data

        #     def row(self):
        #         # 获取currentRow行所有数据
        #         # data = []
        #         # for i in range(self.tableWidget.columnCount()):
        #         #     data.append(self.tableWidget.item(currentRow, i).text())
        #         data=self.loop()
        #         print('000',data)
        #         # 修改数据库
        #         connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
        #                               database='python')
        #         cursor = connect.cursor()
        #         try:
        #             path = data[2].replace('\\', '\\\\')
        #             start = data[7].replace('\\', '\\\\')
        #             icon = data[10].replace('\\', '\\\\')
        #             print(path, start, icon)
        #             cursor.execute(
        #                 f'update game set id="{data[0]}",name="{data[1]}",path="{path}",state="{data[3]}",remark="{data[4]}",spell="{data[5]}",short="{data[6]}", start="{start}",click={data[8]},types="{data[9]}",icon="{icon}" where id={data[0]}')
        #             connect.commit()
        #         except Exception as e:
        #             print(e)
        #         # 取消当前表格可编辑状态
        #         for i in range(self.tableWidget.columnCount()):
        #             currentItem = self.tableWidget.item(currentRow, i)
        #             currentItem.setFlags(currentItem.flags() & ~Qt.ItemIsEditable)
        #         return
        #
        # # 创建 Worker 实例并启动
        # self.worker = Worker1()
        # self.worker.start()

    def update(self):

        box = QMessageBox()
        box.setWindowTitle('提示')
        box.setText('是否更新？')
        box.setStandardButtons(QMessageBox.No | QMessageBox.Yes )
        box.setDefaultButton(QMessageBox.Yes)
        result = box.exec()
        if result == QMessageBox.Yes:
            self.thread = QThread()
            self.worker = Worker2()
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.finished.connect(self.thread.deleteLater)
            self.thread.start()



    def get_file(self):

        # 获取数据
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        # 获取路径
        cursor = connect.cursor()
        cursor.execute(f'select path,number from gamepath')
        data = cursor.fetchall()
        print(data)
        for i in range(len(data)):
            n = 0
            paths = data[i][0]
            number = data[i][1]
            print(paths, number)
            try:
                files = os.listdir(paths)
            except:
                #提示
                print('路径不存在')
                continue
            # 获取文件名，并写入到mysql中
            for file in files:
                if 'mystream' in paths or 'Haosiji' in paths:
                    # 判断路径下文件是否存在
                    exepath = f'{paths}' + f'\\{file}' + '\\storygame.exe'
                    print(exepath)
                elif '网络游戏' in paths or '单机游戏' in paths or '对战平台' in paths:
                    exepath = f'{paths}' + f'\\{file}' + '\\Rungame.exe'
                    print(exepath)
                else:  # 寻找新增路径下的exe
                    newpath = f'{paths}' + f'\\{file}'
                    # 获取newpath下的exe文件
                    try:
                        files = os.listdir(newpath)
                    except:
                        continue
                    for f in files:
                        if '.exe' in f:
                            exepath = newpath + '\\' + f
                            print(exepath)

                icon_file = os.listdir(f'{paths}' + f'\\{file}')
                ls = []  # 存储图标文件
                for f in icon_file:
                    if '.icon' in f:
                        ls.append(f)
                if len(ls) > 1:
                    # 获取图标大小比较大的文件
                    icon = ls[0]
                    for k in ls:
                        if os.path.getsize(f'{paths}' + f'\\{file}' + '\\' + k) < os.path.getsize(f'{paths}' + f'\\{file}' + '\\' + icon):
                            icon = k
                    iconpath = f'{paths}' + f'\\{file}' + '\\' + icon
                elif len(ls) == 1:
                    iconpath = f'{paths}' + f'\\{file}' + '\\' + ls[0]
                else:
                    iconpath = ''

                # 判断游戏类型
                if 'mystream' in paths and '免费版' in file:
                    types = 'steam免费版'
                elif 'mystream' in paths and '免费版' not in file:
                    types = 'steam'

                elif '网络游戏' in paths:
                    types = '网络游戏'

                elif '单机游戏' in paths:
                    types = '单机游戏'

                elif '对战平台' in paths:
                    types = '对战平台'
                else:
                    types = '其他'

                # 获取mysql中的name，判断是否存在
                cursor.execute(f'select path from game where name="{file}"')
                if cursor.fetchone() == None:
                    newpath = paths.replace('\\', '\\\\')
                    exepath = exepath.replace('\\', '\\\\')
                    iconpath = iconpath.replace('\\', '\\\\')

                    tone_map = {
                        'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a',
                        'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
                        'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
                        'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o',
                        'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
                        'ǖ': 'ü', 'ǘ': 'ü', 'ǚ': 'ü', 'ǜ': 'ü'
                    }
                    question = f'对下面名称进行全拼与缩略词：例如：名称：英雄联盟，全拼：yingxionglianmeng，缩写：yxlm。\n 名称：{file}。输出全拼和缩写：\n全拼：\n缩写：\n'
                    py = self.qianwen(question, 0)
                    try:
                        spell = py.split('全拼：')[1].split('缩写：')[0].replace('，', '').strip()
                        # 去掉声调与空格
                        spell = spell.lower().translate(str.maketrans(tone_map)).replace(' ', '').replace("'",
                                                                                                          '').strip()

                        short = py.split('缩写：')[1].replace('。', '').strip()
                        short = short.lower().translate(str.maketrans(tone_map)).replace(' ', '').replace("'",
                                                                                                          '').strip()
                        print(spell, short)
                    except:
                        spell = ''
                        short = ''

                    cursor.execute(
                        f'insert into game(name,path,spell,short,start,types,icon) values("{file}","{newpath}","{spell}","{short}","{exepath}","{types}","{iconpath}")')
                    connect.commit()
                else:
                    pass
                n += 1
            cursor.execute(f'update gamepath set number="{n}" where path="{paths}"')
            connect.commit()
        self.count_game()
        self.gamepath_list()
        cursor.close()
        connect.close()

    def count_game(self):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()
        cursor.execute('select path from gamepath')
        path_list = cursor.fetchall()
        for i in path_list:
            path = i[0].replace('\\', '\\\\')
            cursor.execute(f'select count(*) from game where path="{path}"')
            num = cursor.fetchone()[0]
            print(path,'游戏数量：',num)
            cursor.execute(f'update gamepath set number="{num}" where path="{path}"')
            connect.commit()
        cursor.close()
        connect.close()


    def addpath(self):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()
        self.gamepath_list()
        # 选择路径
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "./")
        path = path.replace('/', '\\\\')
        if path == '':
            return
        # 判断路径是否已存在
        cursor.execute(f'select path from gamepath where path="{path}"')
        paths = cursor.fetchone()
        print(paths)
        if paths == None:
            # 写入数据库
            cursor.execute(f'insert into gamepath (path) values("{path}")')
            connect.commit()
            # 提示
            box = QtWidgets.QMessageBox()
            box.setWindowTitle('提示：')
            box.setText('路径:' + path + '添加成功！')
            box.setStandardButtons(QMessageBox.Ok)
            box.button(QMessageBox.Ok).setText('确定')
            button = box.exec()
            if button == QMessageBox.Ok:
                cursor.close()
                connect.close()
                self.gamepath_list()
                return

        else:
            box = QtWidgets.QMessageBox()
            # 设置窗口大小
            box.setFixedSize(300, 200)

            box.setWindowTitle('提示：')
            box.setText('路径:' + path + '路径已存在！')
            box.setStandardButtons(QMessageBox.Ok)
            box.button(QMessageBox.Ok).setText('确定')
            button = box.exec()
            if button == QMessageBox.Ok:
                cursor.close()
                connect.close()
                self.gamepath_list()
                return

    def deletepath(self):
        # 获取选中的行
        row = self.tableWidget2.currentRow()
        print(row)
        # 获取路径
        path = self.tableWidget2.item(row, 0).text()
        path = path.replace('\\', '\\\\')
        print(path)
        # 确认是否删除
        box = QtWidgets.QMessageBox()
        box.setWindowTitle('提示：')
        box.setText(f'是否删除 {path} 文件路径？')
        box.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        box.button(QMessageBox.Yes).setText('是')
        box.button(QMessageBox.No).setText('否')
        button = box.exec()
        if button == QMessageBox.No:
            return
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()
        # 游戏路径列表
        cursor.execute(f'delete from gamepath where path="{path}"')
        connect.commit()
        # 刷新列表
        self.gamepath_list()
        cursor.close()
        connect.close()

    def gamepath_list(self):
        # 关闭右键菜单
        self.tableWidget.setContextMenuPolicy(Qt.NoContextMenu)

        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()
        # 游戏路径列表
        cursor.execute(f'select path,number from gamepath')
        data = cursor.fetchall()
        self.tableWidget2.setRowCount(len(data))
        self.tableWidget2.setColumnCount(len(data[0]))
        # 只保留两列
        self.tableWidget2.setColumnWidth(0, 200)
        self.tableWidget2.setColumnWidth(1, 100)
        # 设置列标签名，带黑色框
        self.tableWidget2.setHorizontalHeaderLabels(['游戏路径', '游戏数量'])

        # 设置表格内容
        for i in range(len(data)):
            path = data[i][0]
            number = data[i][1]
            self.tableWidget2.setItem(i, 0, QTableWidgetItem(str(path)))
            self.tableWidget2.setItem(i, 1, QTableWidgetItem(str(number)))
            # 设置表格内容居中
            self.tableWidget2.item(i, 0).setTextAlignment(Qt.AlignCenter)
            self.tableWidget2.item(i, 1).setTextAlignment(Qt.AlignCenter)
            # 设置不可编辑
            self.tableWidget2.item(i, 0).setFlags(Qt.ItemIsEnabled)
            self.tableWidget2.item(i, 1).setFlags(Qt.ItemIsEnabled)
            self.tableWidget2.item(i, 0).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.tableWidget2.item(i, 1).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)


        cursor.close()
        connect.close()
    def diff_file(self):
        #清除tableWidget3
        self.tableWidget3.clearContents()
        self.tableWidget3.setRowCount(0)
        # self.frame_15.show()
        self.tableWidget.hide()
        self.tableWidget3.show()

        # 关闭右键菜单
        # self.tableWidget.setContextMenuPolicy(Qt.NoContextMenu)

        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()
        # 游戏路径列表
        cursor.execute(f'select name from game')
        data = cursor.fetchall()
        ls1,ls2,ls3=[],[],[]
        #数据库的游戏名称
        for i in range(len(data)):
            ls1.append(data[i][0])

        #本地目录的名称
        cursor.execute(f'select path from gamepath')
        path_list = cursor.fetchall()
        for i in path_list:
            try:
                path=os.listdir(i[0])
            except:
                ls3.append(i[0])
                continue
            for j in path:
                if j not in ls1:
                    ls2.append(j)
        #本地存在的游戏名称
        diff=list(set(ls1)-set(ls2))
        # self.textEdit_2.setText('【本地不存在的路径】：\n'+'\n'.join(set(ls3))+'\n\n'+'【本地不存在的游戏】：\n'+'\n'.join(diff))
        #设置1列，列宽200
        #初始化表格
        self.tableWidget3.setColumnCount(1)
        self.tableWidget3.setColumnWidth(0, 200)
        #设置行数，不设置默认行数为0
        self.tableWidget3.setRowCount(len(diff)+len(ls3)+3)
        # 设置列标签名，带黑色框
        self.tableWidget3.setHorizontalHeaderLabels(['游戏名称'])

        # 设置表格内容居中
        self.tableWidget3.setItem(0, 0, QTableWidgetItem('-本地不存在的路径-'))
        self.tableWidget3.item(0, 0).setFont(QFont('Times', 12, QFont.Bold))
        self.tableWidget3.item(0, 0).setTextAlignment(Qt.AlignCenter)
        self.tableWidget3.item(0, 0).setFlags(Qt.ItemIsEnabled)
        n=0
        for i in range(1,len(ls3)+1):
            self.tableWidget3.setItem(i, 0, QTableWidgetItem(str(ls3[i-1])))
            self.tableWidget3.item(i, 0).setTextAlignment(Qt.AlignCenter)
            self.tableWidget3.item(i, 0).setFlags(Qt.ItemIsEnabled)
            self.tableWidget3.item(i, 0).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            n=i
        self.tableWidget3.setItem(n+1, 0, QTableWidgetItem(''))
        self.tableWidget3.setItem(n+2, 0, QTableWidgetItem('-本地不存在的游戏-'))
        #设置字体粗黑
        self.tableWidget3.item(n+2, 0).setFont(QFont('Times', 12, QFont.Bold))
        self.tableWidget3.item(n+2, 0).setTextAlignment(Qt.AlignCenter)
        #设置此列不可选
        self.tableWidget3.item(n+1, 0).setFlags(Qt.ItemIsEnabled)
        self.tableWidget3.item(n+2, 0).setFlags(Qt.ItemIsEnabled)

        for j in range(n+3,n+3+len(diff)):
            self.tableWidget3.setItem(j, 0, QTableWidgetItem(str(diff[j-n-3])))
            self.tableWidget3.item(j, 0).setTextAlignment(Qt.AlignCenter)
            self.tableWidget3.item(j, 0).setFlags(Qt.ItemIsEnabled)
            self.tableWidget3.item(j, 0).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        cursor.close()
        connect.close()
    def del_only_diff(self):
        # 获取tablewidget3选中的行
        data = ''
        try:
            row = self.tableWidget3.currentRow()
            print(row)
            data = self.tableWidget3.item(row, 0).text()
        except:
            # 提示未选中
            box = QMessageBox()
            box.setWindowTitle('提示')
            box.setText('未选中数据')
            box.setStandardButtons(QMessageBox.Ok)
            box.button(QMessageBox.Ok).setText('确定')
            button = box.exec()
            if button == QMessageBox.Ok:
                return
            #确认是否删除
        box=QMessageBox()
        box.setWindowTitle('提示')
        box.setText(f'是否删除{data}？')
        box.setStandardButtons(QMessageBox.No | QMessageBox.Yes )
        box.button(QMessageBox.Yes).setText('是')
        box.button(QMessageBox.No).setText('否')
        button = box.exec()
        if button == QMessageBox.No:
            return
        #判断是否存在':'和'\'
        if ':' in data and '\\' in data:
            data=data.replace('\\', '\\\\')
            print('删除路径1',data)
            #删除本地不存在的路径
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='python')
            cursor = connect.cursor()
            cursor.execute(f'delete from gamepath where path="{data}"')
            connect.commit()
            cursor.close()
            connect.close()
            #更新tablewidget3
            self.diff_file()
            self.dir_list()

        else:
            #删除本地不存在的游戏
            print('删除游戏2',data)
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='python')
            cursor = connect.cursor()
            cursor.execute(f'delete from game where name="{data}"')
            connect.commit()
            cursor.close()
            connect.close()
            #更新tablewidget3
            self.diff_file()

    def all_del(self):
        #确认是否删除
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('提示')
        msg_box.setText('是否删除所有游戏？')
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        # 设置默认按钮
        msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
        result = msg_box.exec()
        if result == QtWidgets.QMessageBox.No:
            return
        #遍历tablewidget3所有行
        for i in range(self.tableWidget3.rowCount()):
            data=self.tableWidget3.item(i,0).text()
            if '不存在的游戏' in data or '不存在的路径' in data or '' in data:
                continue
            #判断是否存在':'和'\'
            if ':' in data and '\\' in data:
                data=data.replace('\\', '\\\\')
                print('删除路径1',data)
                #删除本地不存在的路径
                connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                      database='python')
                cursor = connect.cursor()
                cursor.execute(f'delete from gamepath where path="{data}"')
                connect.commit()
                cursor.close()
                connect.close()
            else:
                #删除本地不存在的游戏
                connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                      database='python')
                cursor = connect.cursor()
                cursor.execute(f'delete from game where name="{data}"')
                connect.commit()
                cursor.close()
                connect.close()

        #更新tablewidget3
        self.diff_file()

    def close(self):
        # 确认是否关闭
        box = PySide6.QtWidgets.QMessageBox()
        box.setWindowTitle('请确认：')
        box.setText('是否关闭程序？')
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.button(QMessageBox.Yes).setText('是')
        box.button(QMessageBox.No).setText('否')
        button = box.exec()
        if button == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def game_type(self):
        self.tableWidget.show()
        self.tableWidget2.hide()

        # 设置frame_14和frame_15的不可见
        self.frame_15.setVisible(False)
        # 设置新的右键菜单选项
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()
        # 获取Qlistwidget选中的值,默认为全部
        game_type = self.listWidget.currentItem()
        if game_type == None:
            game_type = '全部'
        else:
            game_type = game_type.text()

        game_type = game_type.replace('游戏', '')
        if '全部' in game_type:
            cursor.execute(f'select * from game')
        else:
            cursor.execute(f'select * from game where types like "%{game_type}%"')
        data = cursor.fetchall()
        self.sheet_format()
        # 设置表格内容
        try:
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))
                    # 设置表格内容居中
                    self.tableWidget.item(i, j).setTextAlignment(Qt.AlignCenter)
                    # 设置表格内容不可编辑
                    self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled)
                    # 设置表格内容可以点击
                    self.tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

        except:
            pass
        cursor.close()
        connect.close()

    def qianwen(self, question, n):
        # model_dic= random.choice([{"turbo":"sk-d6eea5e1f4cd44a09ff9ad6e7a10700e"},{"plus":"sk-b492103a85ea48bc8d85264a53887da9"},{"max":"sk-b492103a85ea48bc8d85264a53887da9"}])
        # #获取dict的key,value值
        # model_type=list(model_dic.keys())[0]
        # dashscope.api_key=list(model_dic.values())[0]
        #
        # if 'turbo'in model_type:
        #     model=Generation.Models.qwen_turbo
        # elif 'plus'in model_type:
        #     model=Generation.Models.qwen_plus
        # else:
        #     model=Generation.Models.qwen_max
        dashscope.api_key = 'sk-b492103a85ea48bc8d85264a53887da9'

        def data():
            full_content = ''
            if n == 0:
                messages = [
                    {'role': 'user', 'content': question}]
            else:
                messages = question

            responses = Generation.call(
                Generation.Models.qwen_plus,
                messages=messages,
                result_format='message',  # set the result to be "message" format.
                stream=True,
                incremental_output=True  # get streaming output incrementally
            )
            # with incrementally we need to merge output.
            for response in responses:
                if response.status_code == HTTPStatus.OK:
                    full_content += response.output.choices[0]['message']['content']
                    # yield full_content

                else:
                    print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                        response.request_id, response.status_code,
                        response.code, response.message
                    ))
            print('【提问时间】：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '\n')
            print('【用户问题】：', question, '\n')
            print('【千问回答】：', full_content, '\n')
            return full_content

        # return flask.Response(data(), mimetype="text/event-stream; charset=utf-8")
        return data()


    def update_icon(self):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='python')
        cursor = connect.cursor()

        # 查询数据库
        cursor.execute("select name,path from game limit 10")

        # 获取查询结果
        data = cursor.fetchall()
        for i in data:
            print(i[0], i[1])
            path = i[1] + '\\' + i[0]
            print(path)
            # 获取路径下带icon的文件
            try:
                file_list = os.listdir(path)
                print(file_list)
                ls = []
                for j in file_list:
                    if 'icon' in j:
                        ls.append(j)

                if len(ls) > 1:
                    # 获取图标大小比较大的文件
                    icon = ls[0]
                    for k in ls:
                        if os.path.getsize(path + '\\' + k) > os.path.getsize(path + '\\' + icon):
                            icon = k
                    print(icon)

                    # 获取图标文件路径
                    icon_path = path + '\\' + icon
                    icon_path = icon_path.replace('\\', '\\\\')
                    print(icon_path)
                    cursor.execute(
                        f"update game set icon='{icon_path}' where name='{i[0]}'")
                    connect.commit()
                elif len(ls) == 1:
                    # 获取图标文件路径
                    icon_path = path + '\\' + ls[0]
                    icon_path = icon_path.replace('\\', '\\\\')
                    print(icon_path)
                    cursor.execute(
                        f"update game set icon='{icon_path}' where name='{i[0]}'")
                    connect.commit()
            except:
                pass

        cursor.close()
        connect.close()

    def sql2redis(self):  # 数据库数据同步到Redis
        # 下载并缓存ico图标
        print('111')
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...', database='python')
        cursor = connect.cursor()
        cursor.execute("select name,spell,short,icon,images from game")
        data = cursor.fetchall()
        print(data[0][4])

        # 连接到Redis
        redis_client = redis.Redis(host='192.168.0.248', port=6379, db=0, password='xwg31415926...')
        for i in data:
            name = i[0]
            spell = i[1]
            short = i[2]
            path = i[3]
            image = i[4]
            if image is None:
                continue
            # name转为小写
            # name = name.lower()
            # 图标路径icon
            # 检查Redis中是否存在该图标
            print('000')
            if redis_client.exists(name) and redis_client.get(name) is not None:
                # 如果存在，pass
                print(f'{name + "(" + spell + "," + short + ")"} 缓存命中')
            else:
                # 缓存二进制图标image
                redis_client.set(name + "(" + spell + "," + short + ")", image)
                print(f'{name + "(" + spell + "," + short + ")"} 缓存成功')
        # 关闭数据库连接
        cursor.close()
        connect.close()

        # 关闭Redis连接
        redis_client.close()

class Worker(QObject):  # 继承自QObject来实现moveToThread
    finished = pyqtSignal()

    def __init__(self, start, parent=None):
        super().__init__(parent)
        self.start = start

    def run(self):
        # 使用subprocess来启动进程，而不是os.system
        os.system('start /b ' + self.start)
        self.finished.emit()

class Worker2(QObject):
    finished = Signal(str)

    def run(self):
        data=ui.get_file()
        self.finished.emit(data)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.search_game()
    MainWindow.show()
    sys.exit(app.exec())
