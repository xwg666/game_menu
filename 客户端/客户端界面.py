import io
import os
import socket
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser

import psutil
import requests
from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QMetaObject, QPoint, QRect, QSize, Qt, QUrl, QThread, Signal)
from PySide6.QtGui import (QFont, QIcon, QAction, QPixmap, QDesktopServices, QMovie)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMenu,
                               QMessageBox, QListWidget, QListWidgetItem, QLabel, QTabWidget, QListView, QTextEdit,
                               QSystemTrayIcon, QMainWindow)
import pymysql as sql


class activation_thread(QThread):
    finished = Signal(str)

    def run(self):
        try:
            self.finished.emit('ACTIVATE')

        except Exception as e:
            print(e)
            self.finished.emit()
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.icon_dict = {}
        # self.steam = {}
        # self.console = {}
        # self.online = {}
        # self.vs = {}
        # self.other = {}
        self.ai_api = []
        self.server_running = True
        self.server = None
        self.server_thread = threading.Thread(target=self.start_server)
        self.server_thread.daemon = True
        self.server_thread.start()
        self.all_data = ()
        self.steam_data = ()
        self.all_item = 50
        self.steam_item = 50
        self.icon_state = 0

    def hideEvent(self, event):
        if self.tray_icon.isVisible():
            MainWindow.hide()

    def onTrayIconActivated(self, reason):
        # 当托盘图标被激活时
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            print('托盘图标被激活')
            MainWindow.showNormal()
            MainWindow.show()
            MainWindow.raise_()
            MainWindow.activateWindow()

    def activate_window(self):
        print('开始激活窗口')
        MainWindow.showNormal()
        MainWindow.show()
        MainWindow.raise_()
        MainWindow.activateWindow()
        print('激活窗口完成')

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            retries = 5
            while retries > 0:
                try:
                    self.server.bind(('localhost', port))
                    self.server.listen(1)
                    print(f"服务器正在监听端口 {port}")
                    break
                except OSError as e:
                    print(f"Failed to bind server: {e}, retrying...")
                    retries -= 1
                    time.sleep(1)
            if retries == 0:
                print(f"无法绑定端口 {port}，退出")
                return

            while self.server_running:
                try:
                    conn, addr = self.server.accept()
                    data = conn.recv(1024)
                    print('data', data)
                    if data == b'ACTIVATE':
                        # self.activate_window()
                        act_thread = activation_thread()
                        act_thread.finished.connect(self.activate_window)
                        act_thread.start()
                    conn.close()
                    print('接受完成')
                except OSError as e:
                    print('接受异常:', e)
                    break
        except OSError as e:
            state = subprocess.run(['netstat', '-ano', '|', 'findstr', str(port)], capture_output=True,
                                   text=True).returncode
            print(state)
            if state == 1:
                # 获取pid
                pid = os.popen('netstat -ano | findstr ' + str(port)).read().split(' ')[-1].strip()
                print(pid)
                subprocess.run(['taskkill', '/PID', str(pid), '/F'], check=True)
            print('绑定异常:', e)
            self.server_running = False
        finally:
            self.server.close()

    def closeEvent(self, event):
        # 如果端口存在，则获取PID，杀死进程
        try:
            self.server_running = False
            self.server.close()
            self.server_thread.join()
            event.accept()
            # except:
            # 无CMD界面执行
            state = subprocess.run(['netstat', '-ano', '|', 'findstr', str(port)], capture_output=True,
                                   shell=True,
                                   text=True).returncode
            print(state)
            if state == 1:
                # 获取pid
                pid = os.popen('netstat -ano | findstr ' + str(port)).read().split(' ')[-1].strip()
                print(pid)
                subprocess.run(['taskkill', '/PID', str(pid), '/F'], check=True)
        finally:
            # 关闭主窗口
            sys.exit(0)

    # --------------------------------------------------------------
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"YiTengYunMenu")
        MainWindow.setWindowTitle(u"易腾云游戏菜单")
        MainWindow.resize(1400, 899)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1400, 901))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"QWidget#widget\n"
                                  "{\n"
                                  "border-radius: 20px;\n"
                                  "}")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1401, 110))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 30, 101, 41))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(0,170,255);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;")

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 30, 341, 41))
        font1 = QFont()
        font1.setItalic(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;")
        self.lineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(480, 40, 75, 24))
        font2 = QFont()
        font2.setFamilies([u"\u6977\u4f53"])
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(0,170,255);\n"
                                        "border-radius: 10px;")

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 40, 41, 28))
        icon = QIcon()
        # 获取打包资源文件路径
        path1 = os.path.join(resource_path, '1.png')
        icon.addFile(path1, QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))
        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(80, 40, 41, 28))
        icon1 = QIcon()
        path2 = os.path.join(resource_path, '2.png')
        icon1.addFile(path2, QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 110, 175, 801))
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 40, 151, 721))
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 0, 111, 21))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(170, 110, 1231, 791))
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        self.frame_8.setFont(font4)
        self.frame_8.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame_8)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 0, 1171, 761))
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        font5 = QFont()
        font5.setBold(True)
        self.tab.setFont(font5)
        # 设置tab页面选项边框颜色
        # self.tab.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);")
        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 1171, 741))

        self.listWidget.setStyleSheet(u"""
                    QListWidget {
                        background-color: rgb(255, 255, 255);
                        border: none;
                    }
                    #设置滚动条轨道颜色为白色
                    QListWidget::horizontalScrollBar {
                        background-color: rgb(255, 255, 255);
                    }
                    #设置滚动条滑块颜色为白色
                    QListWidget::horizontalScrollBar::handle {
                        background-color: rgb(0, 170, 255);

                    }
                """)  # 此处已修改，把样式规则组合在一起

        # AI对话框
        self.frame_9 = QFrame(self.tab)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(830, 0, 341, 741))
        self.frame_9.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);border:none;")
        self.lineEdit_2.setGeometry(QRect(10, 60, 281, 41))
        self.textEdit = QTextEdit(self.frame_9)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 110, 321, 611))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 20, 71, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        font6 = QFont()
        font6.setPointSize(12)
        self.label_2.setFont(font6)
        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(290, 60, 41, 41))
        # 设置按钮无边框
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 255, 255);border: none;")
        icon3 = QIcon()
        path3 = os.path.join(resource_path, "send.png")
        icon3.addFile(path3, QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(20, 20))
        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(300, 0, 31, 31))
        icon4 = QIcon()
        path4 = os.path.join(resource_path, "1.png")
        icon4.addFile(path4, QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(20, 20))
        # ------------------------------------------------------------
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.listWidget_2 = QListWidget(self.tab_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(0, 0, 1171, 741))
        self.listWidget_2.setStyleSheet(u"""
QListWidget {
    background-color: rgb(255, 255, 255);
    border: none;
}
QListWidget::verticalScrollBar {
    background: rgb(230, 230, 230);
}
QListWidget::item:hover {
                background-color: lightblue; /* 设置鼠标悬停时的背景颜色 */
            }
""")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.listWidget_3 = QListWidget(self.tab_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(0, 0, 1171, 741))
        self.listWidget_3.setStyleSheet(u"""
QListWidget {
background-color: rgb(255, 255, 255);
border: none;
}
QListWidget::verticalScrollBar {
background: rgb(230, 230, 230);
}
""")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.listWidget_4 = QListWidget(self.tab_4)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setGeometry(QRect(0, 0, 1171, 741))
        self.listWidget_4.setStyleSheet(u"""
QListWidget {
background-color: rgb(255, 255, 255);
border: none;
}
QListWidget::verticalScrollBar {
background: rgb(230, 230, 230);
}
""")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.listWidget_5 = QListWidget(self.tab_5)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setGeometry(QRect(0, 0, 1171, 741))
        self.listWidget_5.setStyleSheet(u"""
QListWidget {
background-color: rgb(255, 255, 255);
border: none;
}
QListWidget::verticalScrollBar {
background: rgb(230, 230, 230);
}
""")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.listWidget_6 = QListWidget(self.tab_6)
        self.listWidget_6.setObjectName(u"listWidget_6")
        self.listWidget_6.setGeometry(QRect(0, 0, 1171, 741))
        self.listWidget_6.setStyleSheet(u"""
QListWidget {
background-color: rgb(255, 255, 255);
border: none;
}
QListWidget::verticalScrollBar {
background: rgb(230, 230, 230);
}
""")
        self.tabWidget.addTab(self.tab_6, "")

        # listWidget_8
        self.listWidget_8 = QListWidget(self.tab)
        self.listWidget_8.setObjectName(u"listWidget_8")
        self.listWidget_8.setGeometry(QRect(0, 0, 1171, 741))
        self.listWidget_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        # 设置滚动条颜色
        self.listWidget_8.setStyleSheet(u"""
           QListWidget {
               background-color: rgb(255, 255, 255);
               border: none;
           }
           QListWidget::verticalScrollBar {
               background: rgb(230, 230, 230);
           }
           """)
        MainWindow.setCentralWidget(self.centralwidget)
        # -------------------------------------------------------------------------------------------
        # 创建一个托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(os.path.join(resource_path, 'yty.ico')))
        self.context_menu = QMenu()
        self.show_action = self.context_menu.addAction("打开")
        self.exit_action = self.context_menu.addAction("退出")
        self.show_action.triggered.connect(self.activate_window)
        # 绑定左键点击图标打开窗口
        self.tray_icon.activated.connect(self.onTrayIconActivated)
        self.exit_action.triggered.connect(self.closeEvent)
        self.tray_icon.setContextMenu(self.context_menu)
        self.tray_icon.show()
        print('托盘图标创建成功')

        # 设置主窗口固定，不可伸缩
        MainWindow.setFixedSize(1399, 900)
        # 设置按住frame4可移动主窗口
        self.frame_4.setMouseTracking(True)
        # 设置滚动条步长
        self.listWidget.verticalScrollBar().setSingleStep(40)
        # 绑定滚动事件
        self.listWidget.verticalScrollBar().valueChanged.connect(self.wheelEvent)
        self.listWidget_2.verticalScrollBar().valueChanged.connect(self.steamEvent)

        self.listWidget_2.verticalScrollBar().setSingleStep(40)
        self.listWidget_3.verticalScrollBar().setSingleStep(40)
        self.listWidget_4.verticalScrollBar().setSingleStep(40)
        self.listWidget_5.verticalScrollBar().setSingleStep(40)
        self.listWidget_6.verticalScrollBar().setSingleStep(40)
        self.listWidget_8.verticalScrollBar().setSingleStep(40)

        # 绑定键盘事件
        self.lineEdit.setPlaceholderText(u"\u641c\u7d22\u5e94\u7528")
        self.lineEdit.textChanged.connect(self.keyReleaseEvent)
        self.lineEdit.setClearButtonEnabled(True)
        # 绑定回车键
        self.lineEdit.returnPressed.connect(self.lineEdit_returnPresse)
        # 设置lineEdit的右键粘贴选项
        self.lineEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.lineEdit.customContextMenuRequested.connect(self.lineEdit_menu)
        # 创建查询定时器
        # self.search_timer = QTimer()
        # self.search_timer.timeout.connect(self.timeout)
        # self.search_timer.setInterval(200)

        # 绑定lineEdit_2的键盘事件
        self.lineEdit_2.setPlaceholderText(u"\u5728\u6b64\u8f93\u5165\u95ee\u9898")
        self.lineEdit_2.setClearButtonEnabled(True)
        # 设置lineEdit_2的右键粘贴选项
        self.lineEdit_2.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.lineEdit_2.customContextMenuRequested.connect(self.lineEdit_2_menu)
        # 窗口最小化
        self.pushButton_2.clicked.connect(MainWindow.showMinimized)
        # 绑定退出按钮
        # self.pushButton_3.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_3.clicked.connect(self.hideEvent)
        # 绑定助手按钮
        self.pushButton_4.clicked.connect(self.ai)
        # 绑定发送按钮
        self.pushButton_5.clicked.connect(self.qa)
        # 发送按钮与回车键绑定
        self.lineEdit_2.returnPressed.connect(self.qa)
        # 绑定退出按钮
        self.pushButton_6.clicked.connect(self.exit)

        # 设置listWidget表格内容
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setSpacing(12)
        self.listWidget.setIconSize(QSize(48, 48))
        self.listWidget.setGridSize(QSize(142, 128))
        # 设置文字自动换行
        self.listWidget.setWordWrap(True)
        # 设置listwidget右键菜单
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(lambda pos: self.menu(pos, self.listWidget))
        # 设置双击启动
        self.listWidget.itemDoubleClicked.connect(lambda QListWidget: self.double_start(self.listWidget))
        # 取消左键点击事件
        self.listWidget.itemClicked.connect(lambda QListWidget: self.unselect(self.listWidget))
        # 绑定tabWidget的切换事件
        self.tabWidget.setCurrentIndex(0)
        # self.tabWidget.currentChanged.connect(self.local_list)
        self.tabWidget.currentChanged.connect(self.redis_list)

        # 设置listWidget_2表格内容
        self.listWidget_2.setViewMode(QListView.IconMode)
        self.listWidget_2.setResizeMode(QListView.Adjust)
        self.listWidget_2.setMovement(QListView.Static)
        self.listWidget_2.setSpacing(12)
        self.listWidget_2.setIconSize(QSize(48, 48))
        self.listWidget_2.setGridSize(QSize(142, 128))
        # 设置文字自动换行
        self.listWidget_2.setWordWrap(True)
        # 设置listwidget右键菜单
        self.listWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_2.customContextMenuRequested.connect(lambda pos: self.menu(pos, self.listWidget_2))
        # 设置双击启动
        self.listWidget_2.itemDoubleClicked.connect(lambda QListWidget: self.double_start(self.listWidget_2))
        # 取消左键点击事件
        self.listWidget_2.itemClicked.connect(lambda QListWidget: self.unselect(self.listWidget_2))
        # 绑定tab_2
        self.tabWidget.setCurrentIndex(1)
        # 绑定切换事件
        self.tabWidget.currentChanged.connect(self.steam_list)

        # 设置listWidget_3表格内容
        self.listWidget_3.setViewMode(QListView.IconMode)
        self.listWidget_3.setResizeMode(QListView.Adjust)
        self.listWidget_3.setMovement(QListView.Static)
        self.listWidget_3.setSpacing(12)
        self.listWidget_3.setIconSize(QSize(48, 48))
        self.listWidget_3.setGridSize(QSize(142, 128))
        # 设置文字自动换行
        self.listWidget_3.setWordWrap(True)
        # 设置listwidget右键菜单
        self.listWidget_3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_3.customContextMenuRequested.connect(lambda pos: self.menu(pos, self.listWidget_3))
        # 设置双击启动
        self.listWidget_3.itemDoubleClicked.connect(lambda QListWidget: self.double_start(self.listWidget_3))
        # 取消左键点击事件
        self.listWidget_3.itemClicked.connect(lambda QListWidget: self.unselect(self.listWidget_3))
        # 绑定tab_3
        self.tabWidget.setCurrentIndex(2)
        # 绑定切换事件
        self.tabWidget.currentChanged.connect(self.console_game)

        # 设置listWidget_4表格内容
        self.listWidget_4.setViewMode(QListView.IconMode)
        self.listWidget_4.setResizeMode(QListView.Adjust)
        self.listWidget_4.setMovement(QListView.Static)
        self.listWidget_4.setSpacing(12)
        self.listWidget_4.setIconSize(QSize(48, 48))
        self.listWidget_4.setGridSize(QSize(142, 128))
        # 设置文字自动换行
        self.listWidget_4.setWordWrap(True)
        # 设置listwidget右键菜单
        self.listWidget_4.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_4.customContextMenuRequested.connect(lambda pos: self.menu(pos, self.listWidget_4))
        # 设置双击启动
        self.listWidget_4.itemDoubleClicked.connect(lambda QListWidget: self.double_start(self.listWidget_4))
        # 取消左键点击事件
        self.listWidget_4.itemClicked.connect(lambda QListWidget: self.unselect(self.listWidget_4))
        # 绑定tab_4
        self.tabWidget.setCurrentIndex(3)
        # 绑定切换事件
        self.tabWidget.currentChanged.connect(self.online_game)

        # 设置listWidget_5表格内容
        self.listWidget_5.setViewMode(QListView.IconMode)
        self.listWidget_5.setResizeMode(QListView.Adjust)
        self.listWidget_5.setMovement(QListView.Static)
        self.listWidget_5.setSpacing(12)
        self.listWidget_5.setIconSize(QSize(48, 48))
        self.listWidget_5.setGridSize(QSize(142, 128))
        # 设置文字自动换行
        self.listWidget_5.setWordWrap(True)
        # 设置listwidget右键菜单
        self.listWidget_5.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_5.customContextMenuRequested.connect(lambda pos: self.menu(pos, self.listWidget_5))
        # 设置双击启动
        self.listWidget_5.itemDoubleClicked.connect(lambda QListWidget: self.double_start(self.listWidget_5))
        # 取消左键点击事件
        self.listWidget_5.itemClicked.connect(lambda QListWidget: self.unselect(self.listWidget_5))
        # 绑定tab_5
        self.tabWidget.setCurrentIndex(4)
        # 绑定切换事件
        self.tabWidget.currentChanged.connect(self.vs_game)

        # 设置listwidget_6表格内容
        self.listWidget_6.setViewMode(QListView.IconMode)
        self.listWidget_6.setResizeMode(QListView.Adjust)
        self.listWidget_6.setMovement(QListView.Static)
        self.listWidget_6.setSpacing(12)
        self.listWidget_6.setIconSize(QSize(48, 48))
        self.listWidget_6.setGridSize(QSize(142, 128))
        # 设置文字自动换行
        self.listWidget_6.setWordWrap(True)
        # 设置listwidget右键菜单
        self.listWidget_6.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_6.customContextMenuRequested.connect(lambda pos: self.menu(pos, self.listWidget_6))
        # 设置双击启动
        self.listWidget_6.itemDoubleClicked.connect(lambda QListWidget: self.double_start(self.listWidget_6))

        # 取消左键点击事件
        self.listWidget_6.itemClicked.connect(lambda QListWidget: self.unselect(self.listWidget_6))
        # 绑定tab_6
        self.tabWidget.setCurrentIndex(5)
        # 绑定切换事件
        self.tabWidget.currentChanged.connect(self.other_game)
        #         self.tabWidget.setStyleSheet("""
        #                     QTabWidget::pane { /* The tab widget frame */
        #                         border: 1px solid #000000; /* Black border around the tab widget */
        #                     }
        #                     QTabBar::tab {
        #                         width: 95px;  /* 设置 tab 的宽度 */
        # #                       height: 50px;  /* 设置 tab 的高度 */
        #                         background: #f0f0f0; /* Light gray background */
        #                         border: 1px solid #000000; /* Black border */
        #                         padding: 10px; /* Padding inside each tab */
        #                         margin: 2px; /* Space between tabs */
        #                     }
        #                     QTabBar::tab:selected {
        #                         background: #c0c0c0; /* Darker gray for selected tab */
        #                     }
        #                     QTabBar::tab:hover {
        #                         background:rgb(0,170,255); /* Slightly darker gray for hover */
        #                     }
        #                 """)
        self.tabWidget.setStyleSheet("""
        QTabBar::tab {
            width: 95px;  /* 设置 tab 的宽度 */
            height: 30px;  /* 设置 tab 的高度 */
            background: rgb(0,170,255);  /* 设置 tab 的背景色 */
            color:black;
        }
         QTabBar::tab:selected, QTabBar::tab:hover {
             background: rgb(255, 255, 255);  /* 设置选中和悬停 tab 的背景色 */
         }
         QTabWidget::pane {
                border: 1px solid black; /* Black border around the tab widget */
            }
    """)

        # self.tabWidget.setStyleSheet(
        #     u"QTabWidget::pane { /* The tab widget frame */ border-top: 2px solid #C2C2C2;position: absolute;top: 0px;}QTabWidget::tab-bar {alignment: Left;}QTabBar::tab {background: lightgray;border: 1px solid #C4C4C3;border-bottom: 0px;border-bottom-color: #C2C2C2; /* same as the pane color */border-top-left-radius: 4px;border-top-right-radius: 4px;min-width: 8ex;padding: 5px;font: bold 12px \"Arial\";}QTabBar::tab:selected, QTabBar::tab:hover {background: #f0f0f0;}QTabBar::tab:selected {border-color: #9B9B9B;border-bottom-color: #C2C2C2; /* same as pane color */}")
        # 创建Qlistwidget_7,热点排行榜
        layout7 = QVBoxLayout(self.frame_7)
        self.listwidget_7 = QListWidget()
        # 禁用 QListWidget 的拖动模式
        self.listwidget_7.setDragDropMode(QListWidget.DragDropMode.NoDragDrop)
        self.listwidget_7.setViewMode(QListWidget.ViewMode.IconMode)
        self.listwidget_7.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.listwidget_7.setFlow(QListWidget.Flow.LeftToRight)
        # 设置图标大小
        self.listwidget_7.setIconSize(QSize(48, 48))
        self.listwidget_7.setGridSize(QSize(120, 70))
        # 设置文字自动换行
        self.listwidget_7.setWordWrap(True)
        # 设置间距
        self.listwidget_7.setSpacing(15)
        # self.listwidget2.setGridSize(QSize(64, 64))
        layout7.addWidget(self.listwidget_7)
        # 设置左键点击事件
        self.listwidget_7.itemClicked.connect(lambda QListWidget: self.unselect(self.listwidget_7))
        # 设置右键菜单
        self.listwidget_7.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listwidget_7.customContextMenuRequested.connect(lambda pos: self.menu(pos, self.listwidget_7))
        # 绑定启动函数
        self.listwidget_7.itemDoubleClicked.connect(lambda QListWidget: self.double_start(self.listwidget_7))

        # 设置listwidget_8表格内容
        self.listWidget_8.setViewMode(QListView.IconMode)
        self.listWidget_8.setIconSize(QSize(48, 48))
        self.listWidget_8.setResizeMode(QListView.Adjust)
        self.listWidget_8.setFlow(QListView.LeftToRight)
        self.listWidget_8.setSpacing(12)
        self.listWidget_8.setIconSize(QSize(48, 48))
        self.listWidget_8.setGridSize(QSize(142, 128))
        # 设置文字自动换行
        self.listWidget_8.setWordWrap(True)
        # 设置listwidget右键菜单
        self.listWidget_8.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_8.customContextMenuRequested.connect(lambda pos: self.menu(pos, self.listWidget_8))
        # 设置双击启动
        self.listWidget_8.itemDoubleClicked.connect(lambda QListWidget: self.double_start(self.listWidget_8))
        # 取消左键点击事件
        self.listWidget_8.itemClicked.connect(lambda QListWidget: self.unselect(self.listWidget_8))
        # 设置textEdit不可编辑，可复制内容
        self.textEdit.setReadOnly(True)
        # 设置textEdit右键菜单
        self.textEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.textEdit.customContextMenuRequested.connect(self.showCustomMenu)

        self.tabWidget.setCurrentIndex(0)
        # 图片左侧区域
        self.draggableFrame0 = DraggableFrame(MainWindow)
        self.draggableFrame0.setGeometry(QRect(680, 1, 80, 108))
        # 图片右侧区域
        self.draggableFrame1 = DraggableFrame(MainWindow)
        self.draggableFrame1.setGeometry(QRect(1140, 1, 40, 108))

        self.draggableFrame2 = DraggableFrame(MainWindow)
        self.draggableFrame2.setGeometry(QRect(1, 1, 300, 108))
        self.draggableFrame3 = DraggableFrame(MainWindow)
        # 搜索框上下
        self.draggableFrame3.setGeometry(QRect(282, 70, 420, 40))
        self.draggableFrame7 = DraggableFrame(MainWindow)
        self.draggableFrame7.setGeometry(QRect(282, 1, 420, 28))
        self.draggableFrame4 = DraggableFrame(MainWindow)
        self.draggableFrame4.setGeometry(QRect(780, 111, 600, 20))
        self.draggableFrame5 = DraggableFrame(MainWindow)
        self.draggableFrame5.setGeometry(QRect(1260, 1, 140, 42))
        self.draggableFrame6 = DraggableFrame(MainWindow)
        self.draggableFrame6.setGeometry(QRect(1260, 64, 140, 50))
        # 小云助手上下区域
        self.draggableFrame8 = DraggableFrame(MainWindow)
        self.draggableFrame8.setGeometry(QRect(1180, 0, 105, 40))
        self.draggableFrame9 = DraggableFrame(MainWindow)
        self.draggableFrame9.setGeometry(QRect(1180, 65, 80, 45))
        # 小云助手右侧区域
        self.draggableFrame10 = DraggableFrame(MainWindow)
        self.draggableFrame10.setGeometry(QRect(1255, 41, 52, 22))

        # # 设置DraggableFrame的背景色为黑色
        # self.draggableFrame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        # 边框颜色为黑色
        self.draggableFrame0.setFrameShadow(QFrame.Raised)
        self.draggableFrame0.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame1.setFrameShadow(QFrame.Raised)
        self.draggableFrame1.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame2.setFrameShadow(QFrame.Raised)
        self.draggableFrame2.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame3.setFrameShadow(QFrame.Raised)
        self.draggableFrame3.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame4.setFrameShadow(QFrame.Raised)
        self.draggableFrame4.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame5.setFrameShadow(QFrame.Raised)
        self.draggableFrame5.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame6.setFrameShadow(QFrame.Raised)
        self.draggableFrame6.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame7.setFrameShadow(QFrame.Raised)
        self.draggableFrame7.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame8.setFrameShadow(QFrame.Raised)
        self.draggableFrame8.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame9.setFrameShadow(QFrame.Raised)
        self.draggableFrame9.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame10.setFrameShadow(QFrame.Raised)
        self.draggableFrame10.setFrameShape(QFrame.StyledPanel)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6613\u817e\u4e91", None))
        # self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5e94\u7528", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u4e91\u52a9\u624b", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u" \u6bcf \u65e5 \u70ed \u699c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5e94\u7528", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"steam\u6e38\u620f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QCoreApplication.translate("MainWindow", u"\u5355\u673a\u6e38\u620f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),
                                  QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u6e38\u620f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),
                                  QCoreApplication.translate("MainWindow", u"\u5bf9\u6218\u5e73\u53f0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6),
                                  QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u4e91\u95ee\u7b54", None))

    # retranslateUi
    def wheelEvent(self, event):
        # 对listwidget原有的图标上继续追加图标
        print('追加图标', self.listWidget.verticalScrollBar().maximum(), self.listWidget.verticalScrollBar().value())
        if self.listWidget.verticalScrollBar().maximum() - self.listWidget.verticalScrollBar().value() < 50:
            # self.listWidget.verticalScrollBar().setValue(self.listWidget.verticalScrollBar().value() + 50)
            start = self.listWidget.count()
            print('start=', start)
            for i in range(start, start + 50):
                if self.all_item >= len(self.all_data):
                    break
                name = self.all_data[i][0]
                spell = self.all_data[i][1]
                short = self.all_data[i][2]
                image = self.icon_dict.get(name + "<" + spell + "," + short + ">")
                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    # for name,icon in self.icon_dict.items():
                    # 如果
                    # 将二进制图标加到item中
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)
                name = name.split('<')[0]
                name = name + '\n' + 28 * ' '

                # 在listwidget原有图标上进行追加
                item1 = QListWidgetItem()
                # 将item设置为固定大小
                item1.setSizeHint(QSize(120, 120))

                # item的图标
                item1.setIcon(QIcon(pic))
                # item的文本
                item1.setText(name)
                # 文本可自动换行居中
                item1.setTextAlignment(Qt.AlignCenter)
                # 禁用拖动功能
                item1.setFlags(item1.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item追加到QListWidget中
                self.listWidget.addItem(item1)
                self.listWidget.viewport().update()
                self.all_item += 1

    def local_list(self):
        self.frame_9.hide()
        self.listWidget_8.hide()
        self.listWidget.show()
        if self.listWidget.count() > 1:
            return
        self.listWidget.clear()
        try:
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='game')
            cursor = connect.cursor()
            # 写入到listWidget_2
            cursor.execute("select name,spell,short,icon from game")
            self.all_data = cursor.fetchall()
            cursor.close()
            connect.close()
            for i in range(50):
                name = self.all_data[i][0]
                spell = self.all_data[i][1]
                short = self.all_data[i][2]
                image = self.all_data[i][3]
                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    # for name,icon in self.icon_dict.items():
                    # 如果
                    # 将二进制图标加到item中
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)
                # name = name.split('<')[0]
                name = name + '\n' + 28 * ' '

                # 在listwidget原有图标上进行追加
                item1 = QListWidgetItem()
                # 将item设置为固定大小
                item1.setSizeHint(QSize(120, 120))

                # item的图标
                item1.setIcon(QIcon(pic))
                # item的文本
                item1.setText(name)
                # 文本可自动换行居中
                item1.setTextAlignment(Qt.AlignCenter)
                # 禁用拖动功能
                item1.setFlags(item1.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item追加到QListWidget中
                self.listWidget.addItem(item1)
                self.listWidget.viewport().update()

        except Exception as e:
            print(e)

    def redis_list(self):
        self.frame_9.hide()
        self.listWidget_8.hide()
        self.listWidget.show()
        if self.listWidget.count() > 1:
            return
        self.listWidget.clear()
        try:
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='game')
            cursor = connect.cursor()
            # 写入到listWidget_2
            cursor.execute("select name,spell,short,icon from game")
            self.all_data = cursor.fetchall()
            cursor.close()
            connect.close()
            # if self.icon_state == 0:
            #
            # else:
            for i in range(50):
                name = self.all_data[i][0]
                spell = self.all_data[i][1]
                short = self.all_data[i][2]
                image = self.icon_dict.get(name + "<" + spell + "," + short + ">")
                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    # for name,icon in self.icon_dict.items():
                    # 如果
                    # 将二进制图标加到item中
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)
                name = name.split('<')[0]
                name = name + '\n' + 28 * ' '
                item1 = QListWidgetItem()
                # 将item设置为固定大小
                item1.setSizeHint(QSize(120, 120))

                # item的图标
                item1.setIcon(QIcon(pic))
                # item的文本
                item1.setText(name)
                # 文本可自动换行居中
                item1.setTextAlignment(Qt.AlignCenter)
                # 禁用拖动功能
                item1.setFlags(item1.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # item添加到QListWidget中
                self.listWidget.addItem(item1)
            self.listWidget.viewport().update()

        except Exception as e:
            print('redis_list', e)

    def steam_list(self):
        self.lineEdit.clear()
        self.listWidget_2.show()
        if self.listWidget_2.count() > 1:
            return
        self.listWidget_2.clear()
        try:
            # if len(self.steam.keys())==0:
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='game')
            cursor = connect.cursor()
            # 写入到listWidget_2
            cursor.execute("select name,spell,short,icon from game where types like '%steam%'")
            self.steam_data = cursor.fetchall()
            for i in range(50):
                name = self.steam_data[i][0]
                spell = self.steam_data[i][1]
                short = self.steam_data[i][2]
                image = self.icon_dict.get(name + "<" + spell + "," + short + ">")
                # self.steam[name] = image  # 将图像数据存储在字典中
                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)
                name = name + '\n' + 28 * ' '

                # 将二进制图标加到item中
                item2 = QListWidgetItem()
                # 将item设置为固定大小
                item2.setSizeHint(QSize(120, 120))
                # 设置item的图标
                item2.setIcon(QIcon(pic))
                # 设置item的文本
                item2.setText(name)
                # 设置文本可自动换行居中
                item2.setTextAlignment(Qt.AlignCenter)
                # 禁用项目的拖动功能
                item2.setFlags(item2.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)

                # 将item添加到QListWidget中
                self.listWidget_2.addItem(item2)
            self.listWidget_2.viewport().update()
            cursor.close()
            connect.close()

        except Exception as e:
            print('steam_list', e)

        return True

    def steamEvent(self, event):
        # 对listwidget_2原有的图标上继续追加图标
        if self.listWidget_2.verticalScrollBar().maximum() - self.listWidget_2.verticalScrollBar().value() < 50:
            # self.listWidget.verticalScrollBar().setValue(self.listWidget.verticalScrollBar().value() + 50)
            start = self.listWidget_2.count()
            print('start=', start)
            for i in range(start, start + 50):
                if self.steam_item >= len(self.all_data):
                    break
                name = self.all_data[i][0]
                spell = self.all_data[i][1]
                short = self.all_data[i][2]
                image = self.icon_dict.get(name + "<" + spell + "," + short + ">")
                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    # for name,icon in self.icon_dict.items():
                    # 如果
                    # 将二进制图标加到item中
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)
                name = name.split('<')[0]
                name = name + '\n' + 28 * ' '

                # 在listwidget原有图标上进行追加
                item1 = QListWidgetItem()
                # 将item设置为固定大小
                item1.setSizeHint(QSize(120, 120))

                # item的图标
                item1.setIcon(QIcon(pic))
                # item的文本
                item1.setText(name)
                # 文本可自动换行居中
                item1.setTextAlignment(Qt.AlignCenter)
                # 禁用拖动功能
                item1.setFlags(item1.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item追加到QListWidget中
                self.listWidget_2.addItem(item1)
                self.listWidget_2.viewport().update()
                self.steam_item += 1

    # def steam_game(self):
    #         self.lineEdit.clear()
    #         if self.listWidget_2.count() > 100:
    #             print(self.listWidget_2.count())
    #             return
    #         self.listWidget_2.clear()
    #         connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
    #                               database='game')
    #         cursor = connect.cursor()
    #         # 写入到listWidget_2
    #         cursor.execute("select name,start,icon from game where types like '%steam%'")
    #         data = cursor.fetchall()
    #         try:
    #             for i in range(len(data)):
    #                 name = data[i][0]
    #                 start = data[i][1]
    #                 icon = data[i][2]
    #                 if os.path.exists(icon) == False:
    #                     icon = resource_path + '\\yty.ico'
    #                 if len(name) < 8:
    #                     n = 15 - len(name)
    #                     name = ' ' * (n // 2) + name + ' ' * (n // 2)
    #
    #                 item2 = QListWidgetItem()
    #                 # 将item设置为固定大小
    #                 item2.setSizeHint(QSize(120, 120))
    #
    #                 # 设置item的图标
    #                 item2.setIcon(QIcon(icon))
    #
    #                 # item2.setData(1002, start)  # 自定义数据存储路径
    #
    #                 # 设置item的文本
    #                 item2.setText(name)
    #
    #                 # 设置文本可自动换行居中
    #                 item2.setTextAlignment(Qt.AlignCenter)
    #
    #                 # 禁用项目的拖动功能
    #                 item2.setFlags(item2.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
    #
    #                 # 将item添加到QListWidget中
    #                 self.listWidget_2.addItem(item2)
    #
    #                 self.listWidget_2.viewport().update()
    #         except:
    #             pass
    #
    #         cursor.close()
    #         connect.close()
    def console_game(self):
        self.lineEdit.clear()
        self.listWidget_3.show()
        if self.listWidget_3.count() > 0:
            return
        self.listWidget_3.clear()
        try:
            # if len(self.console.keys()) == 0:
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='game')
            cursor = connect.cursor()
            # 写入到listWidget_2
            cursor.execute("select name,spell,short from game where types ='单机游戏'")
            data = cursor.fetchall()
            for i in range(len(data)):
                name = data[i][0]
                spell = data[i][1]
                short = data[i][2]
                image = self.icon_dict.get(name + "<" + spell + "," + short + ">")
                # self.console[name] = image  # 将图像数据存储在字典中
                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic.scaled(120, 120, Qt.KeepAspectRatio)
                name = name + '\n' + 28 * ' '

                item3 = QListWidgetItem()
                # 将item设置为固定大小
                item3.setSizeHint(QSize(120, 120))
                # 设置item的图标
                item3.setIcon(QIcon(pic))
                # 设置item的文本
                item3.setText(name)
                # 设置文本可自动换行居中
                item3.setTextAlignment(Qt.AlignCenter)
                # 禁用项目的拖动功能
                item3.setFlags(item3.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item添加到QListWidget中
                self.listWidget_3.addItem(item3)
            self.listWidget_3.viewport().update()
            cursor.close()
            connect.close()

        except Exception as e:
            print("单机游戏列表获取失败", e)

    def online_game(self):
        self.lineEdit.clear()
        self.listWidget_4.show()
        if self.listWidget_4.count() > 1:
            return
        self.listWidget_4.clear()
        try:
            # if len(self.online.keys()) == 0:
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='game')
            cursor = connect.cursor()
            # 写入到listWidget_2
            cursor.execute("select name,spell,short from game where types ='网络游戏'")
            data = cursor.fetchall()
            for i in range(len(data)):
                name = data[i][0]
                spell = data[i][1]
                short = data[i][2]
                image = self.icon_dict.get(name + "<" + spell + "," + short + ">")
                # self.online[name] = image  # 将图像数据存储在字典中

                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'

                else:
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)

                name = name + '\n' + 28 * ' '

                item4 = QListWidgetItem()
                # 将item设置为固定大小
                item4.setSizeHint(QSize(120, 120))
                # 设置item的图标
                item4.setIcon(QIcon(pic))
                # 设置item的文本
                item4.setText(name)
                # 设置文本可自动换行居中
                item4.setTextAlignment(Qt.AlignCenter)

                # 禁用项目的拖动功能
                item4.setFlags(item4.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item添加到QListWidget中
                self.listWidget_4.addItem(item4)
            self.listWidget_4.viewport().update()
            cursor.close()
            connect.close()

        except Exception as e:
            print('网络游戏列表获取失败', e)

    def vs_game(self):
        self.lineEdit.clear()
        self.listWidget_5.show()
        if self.listWidget_5.count() > 1:
            return
        self.listWidget_5.clear()
        try:
            # if len(self.vs.keys()) == 0:
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='game')
            cursor = connect.cursor()
            cursor.execute("select name,spell,short from game where types ='对战平台'")
            data = cursor.fetchall()
            for i in range(len(data)):
                name = data[i][0]
                spell = data[i][1]
                short = data[i][2]
                image = self.icon_dict.get(name + "<" + spell + "," + short + ">")
                # self.vs[name] = image  # 将图像数据存储在字典中
                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)

                name = name + '\n' + 28 * ' '

                item5 = QListWidgetItem()
                # 将item设置为固定大小
                item5.setSizeHint(QSize(120, 120))
                # 设置item的图标
                item5.setIcon(QIcon(pic))
                # 设置item的文本
                item5.setText(name)
                # 设置文本可自动换行居中
                item5.setTextAlignment(Qt.AlignCenter)

                # 禁用项目的拖动功能
                item5.setFlags(item5.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item添加到QListWidget中
                self.listWidget_5.addItem(item5)
            self.listWidget_5.viewport().update()
            cursor.close()
            connect.close()

        except Exception as e:
            print('对战游戏列表获取失败', e)

    def other_game(self):
        self.lineEdit.clear()
        self.listWidget_6.show()
        if self.listWidget_6.count() > 1:
            return
        self.listWidget_6.clear()
        try:
            # if len(self.vs.keys()) == 0:
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='game')
            cursor = connect.cursor()
            cursor.execute("select name,spell,short from game where types ='其他'")
            data = cursor.fetchall()
            for i in range(len(data)):
                name = data[i][0]
                spell = data[i][1]
                short = data[i][2]
                image = self.icon_dict.get(name + "<" + spell + "," + short + ">")
                # self.other[name] = image  # 将图像数据存储在字典中
                if image is None or len(image) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    icon = io.BytesIO(image)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)

                name = name + '\n' + 28 * ' '

                item6 = QListWidgetItem()
                # 将item设置为固定大小
                item6.setSizeHint(QSize(120, 120))
                # 设置item的图标
                item6.setIcon(QIcon(pic))
                # 设置item的文本
                item6.setText(name)
                # 设置文本可自动换行居中
                item6.setTextAlignment(Qt.AlignCenter)

                # 禁用项目的拖动功能
                item6.setFlags(item6.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item添加到QListWidget中
                self.listWidget_6.addItem(item6)
            self.listWidget_6.viewport().update()
            cursor.close()
            connect.close()

        except Exception as e:
            print('其他游戏列表获取失败', e)

    def keyReleaseEvent(self, event):
        # 获取键盘每次释放后的文本内容
        key = self.lineEdit.text()
        key = key.lower()
        # 判断是否在定位到tab1上
        if self.tabWidget.currentIndex() != 0:
            self.tabWidget.setCurrentIndex(0)
            self.lineEdit.setText(key)
        # self.listWidget_8.clear()
        self.listWidget_8.show()
        # 将关键字重新写到lineedit中
        if len(key) == 0:
            print('请输入关键字')
            self.listWidget_8.hide()  # 不隐藏查询listwidget会遮住AI对话框
            self.listWidget.show()
        else:
            self.key_search(key)

    def lineEdit_returnPresse(self):
        key = self.lineEdit.text()
        if len(key) == 0:
            self.listWidget_8.hide()  # 不隐藏查询listwidget会遮住AI对话框
            self.listWidget.show()
        self.tabWidget.setCurrentIndex(0)
        self.listWidget_8.clear()
        self.listWidget_8.show()
        thread = threading.Thread(target=self.key_search, args=(key,))
        thread.start()
        # 等待线程结束
        thread.join()

    def key_search(self, key1):
        self.listWidget_8.show()
        self.listWidget_8.clear()  # 每次写入前清空
        # 获取模糊查询结果
        n = 0
        for key, value in self.icon_dict.items():
            print(key)
            if key1.lower() in key.lower():
                if n > 50:
                    break
                n += 1
                if value is None or len(value) == 0:
                    pic = resource_path + '\\game.ico'
                else:
                    # 将二进制图标加到item中
                    icon = io.BytesIO(value)
                    pic = QPixmap()
                    pic.loadFromData(icon.getvalue())
                    pic = pic.scaled(120, 120, Qt.KeepAspectRatio)
                print(key, key1)
                # 创建QListWidgetItem
                item8 = QListWidgetItem()
                # 设置item的图标
                item8.setIcon(QIcon(pic))
                # 将item设置为固定大小
                item8.setSizeHint(QSize(120, 120))
                # item8.setData(1000, start)  # 自定义数据存储路径
                # 设置item的文本
                key = key.split('<')[0]
                name = key + '\n' + 28 * ' '
                item8.setText(name)
                # 设置文本可自动换行居中
                item8.setTextAlignment(Qt.AlignCenter)
                # 禁用项目的拖动功能
                item8.setFlags(item8.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item添加到QListWidget中
                self.listWidget_8.addItem(item8)
                # 刷新列表
                self.listWidget_8.viewport().update()

        '''connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='game')
        cursor = connect.cursor()
        try:
                cursor.execute(f"select name,spell,short,start,icon from game where name like '%{key}%' or spell like '%{key}%' or short like '%{key}%'")
                data = cursor.fetchall()
                if len(data) == 0:
                        self.listWidget_8.clear()
                        print('没有找到相关游戏')
                        return
                # print('开关状态：',ui.on_off)
                # if ui.on_off==0:
                #     ui.on_off = 1
                self.listWidget_8.clear()  #每次写入前清空
                for i in range(len(data)):
                        name = data[i][0]
                        start = data[i][3]
                        icon = data[i][4]
                        # icon=resource_path+'\\game.ico'
                        if os.path.exists(icon) == False:
                                icon = resource_path + '\\game.ico'

                        if len(name) < 8:
                                n = 15 - len(name)
                                name = ' ' * (n // 2) + name + ' ' * (n // 2)
                        # 创建QListWidgetItem
                        item8 = QListWidgetItem()
                        # 设置item的图标
                        item8.setIcon(QIcon(icon))
                        # 将item设置为固定大小
                        item8.setSizeHint(QSize(120, 120))
                        item8.setData(1000, start)  # 自定义数据存储路径
                        # 设置item的文本
                        item8.setText(name)
                        # 设置文本可自动换行居中
                        item8.setTextAlignment(Qt.AlignCenter)
                        # 禁用项目的拖动功能
                        item8.setFlags(item8.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                        # 将item添加到QListWidget中
                        self.listWidget_8.addItem(item8)
                        # 刷新列表
                        if i // 8 == 0:
                                self.listWidget_8.viewport().update()
                cursor.close()
                connect.close()

        except Exception as e:
                print(e)'''

    def hot_list(self):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='game')
        cursor = connect.cursor()
        # 根据点击数量进行排序
        cursor.execute(f"select name,spell,short,start,click,icon,images from game order by click desc limit 10")
        data = cursor.fetchall()
        try:
            for i in range(len(data)):
                name = data[i][0]
                spell = data[i][1]
                short = data[i][2]
                # 判断是否有这个KEY
                if name + '<' + spell + ',' + short + '>' not in self.icon_dict:
                    pic = resource_path + '\\game.ico'
                else:
                    image = self.icon_dict[name + '<' + spell + ',' + short + '>']
                    if image is None or len(image) == 0:
                        pic = resource_path + '\\game.ico'
                    else:
                        # 将二进制图标加到item中
                        icon = io.BytesIO(image)
                        pic = QPixmap()
                        pic.loadFromData(icon.getvalue())
                        pic = pic.scaled(72, 72, Qt.KeepAspectRatio)

                # 创建QListWidgetItem
                item7 = QListWidgetItem()
                # 设置item的图标
                item7.setIcon(QIcon(pic))
                # 将item设置为固定大小
                item7.setSizeHint(QSize(72, 72))
                # 设置item的文本
                item7.setText(name)
                # 设置鼠标放在图标上显示文字
                item7.setToolTip(name)
                # 设置文本可自动换行居中
                item7.setTextAlignment(Qt.AlignCenter)
                # 禁用项目的拖动功能
                item7.setFlags(item7.flags() & ~Qt.ItemFlag.ItemIsDragEnabled)
                # 将item添加到QListWidget2中
                self.listwidget_7.addItem(item7)
                # 刷新列表
                self.listwidget_7.viewport().update()
            cursor.close()
            connect.close()

        except Exception as e:
            print(e)

    def menu(self, pos, QlistWidget):
        listWidget = QlistWidget
        item = listWidget.itemAt(pos)
        menu = QMenu(listWidget)
        menu.setFont(QFont('宋体', 10))
        # 设置菜单背景色为灰色
        menu.setStyleSheet(
            'QMenu{background-color: rgb(170,255,255);margin:10px;}QMenu::item{padding:10px 20px 10px 20px;}QMenu::item:selected{background-color:rgb(255, 255, 255);}')
        menu.addAction('启动游戏')
        menu.addAction('打开目录')
        # action = menu.exec(QCursor.pos()) #这种方式会在光标当前位置显示菜单
        action = menu.exec(listWidget.mapToGlobal(pos))  # 这种方式会在右键点击的位置显示菜单
        if action == None:
            return
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='game')
        cursor = connect.cursor()
        name = item.text().strip()
        if action.text() == '启动游戏':
            self.game_start(name)

        elif action.text() == '打开目录':
            cursor.execute(f'select name,path from game where name="{name}"')
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
            cursor.close()
            connect.close()
        else:
            return

    def double_start(self, QlistWidget):
        listWidget = QlistWidget
        item = listWidget.currentItem()
        if item == None:
            return
        name = item.text().strip()
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='game')
        cursor = connect.cursor()
        cursor.execute(f'select start from game where name="{name}"')
        start = cursor.fetchone()
        print('name', name, 'start', start)
        start = start[0]
        # 判断是否存在
        if os.path.exists(start):
            os.system('start /b ' + start)
        else:
            box = QMessageBox()
            box.setWindowTitle('提示')
            box.setText(f'游戏{name}不存在')
            box.setIcon(QMessageBox.Warning)
            box.setStandardButtons(QMessageBox.Ok)
            box.exec()
        start = start.replace('\\', '\\\\')
        # 更新数据库点击次数
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='game')
        cursor = connect.cursor()
        # 根据点击数量进行排序
        cursor.execute(f"update game set click=click+1 where start='{start}'")
        connect.commit()
        cursor.close()
        connect.close()

    def game_start(self, name):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='game')
        cursor = connect.cursor()
        cursor.execute(f'select start from game where name="{name}"')
        start = cursor.fetchone()
        start = start[0]

        # 判断是否存在
        if os.path.exists(start):
            os.system('start /b ' + start)
        else:
            box = QMessageBox()
            box.setWindowTitle('提示')
            box.setText(f'游戏{name}不存在')
            box.setIcon(QMessageBox.Warning)
            box.setStandardButtons(QMessageBox.Ok)
            box.exec()
        start = start.replace('\\', '\\\\')
        # 更新数据库点击次数
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='game')
        cursor = connect.cursor()
        # 根据点击数量进行排序
        cursor.execute(f"update game set click=click+1 where start='{start}'")
        connect.commit()
        cursor.close()
        connect.close()

    def unselect(self, listwidget):
        global global_listwidget
        if global_listwidget is not None:
            if global_listwidget != listwidget:
                global_listwidget.clearSelection()
        global_listwidget = listwidget

    def ai(self):
        self.lineEdit.clear()
        # 如何frame_9是隐藏的，就显示，否则隐藏
        if self.frame_9.isHidden():
            self.tabWidget.setCurrentIndex(0)
            self.frame_9.show()
        else:
            self.frame_9.hide()
            self.tabWidget.setCurrentIndex(0)

    def exit(self):
        self.frame_9.hide()

    def qa(self):
        question = self.lineEdit_2.text()
        if question == '':
            print('请输入问题')
            return
        # 使用异步请求
        self.worker = Worker()
        self.worker.start()

    def get_response(self):
        import random
        if len(self.ai_api) == 0:
            connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                                  database='game')
            cursor = connect.cursor()
            cursor.execute('select ai_api from config where id=1')
            data = cursor.fetchone()[0]
            self.ai_api = data.replace('[', '').replace(']', '').replace("'", '').split(',')
            url = random.choice(self.ai_api)
            cursor.close()
            connect.close()
        else:
            print('api', self.ai_api)
            # url = random.choice(['http://xwgchat.cn:3307/gameai?question=','http://xwgchat.cn:3308/gameai?question='])
            url = random.choice(self.ai_api)
        question = self.lineEdit_2.text()
        self.lineEdit_2.clear()
        response = ''
        try:
            response = requests.get(url + question).json()
            print('response', response)
            if len(response) != 0:
                # 将内容添加到textedit
                self.textEdit.append('问题：' + question + '\n' + '答案：\n' + response + '\n\n')
            else:
                self.textEdit.append('返回为空，请重试')
        except:
            self.textEdit.append('网络错误\n')
        return response

    # def move_mouse(self, event):
    #     # 检测鼠标是否滚动
    #     self.listWidget.scrollContentsBy(0, 100)
    #     # 获取滚动后的位置
    #     scroll_position = self.listWidget.verticalScrollBar().value()
    #     print("滚动后的位置：", scroll_position)
    #     # 获取滚动后的最大位置
    #     max_scroll_position = self.listWidget.verticalScrollBar().maximum()
    #     print("滚动后的最大位置：", max_scroll_position)

    def showCustomMenu(self, pos):
        # 创建一个新的菜单
        menu = QMenu(self.textEdit)
        # 设置菜单颜色
        menu.setStyleSheet(
            'QMenu{background-color: rgb(0,170,255);margin:5px;}QMenu::item{padding:5px 7px 5px 7px;}QMenu::item:selected{background-color:rgb(255, 255, 255);}')

        # 创建复制和全选的动作
        actionCopy = QAction("复制", self.textEdit)
        actionSelectAll = QAction("全选", self.textEdit)
        menu.addAction(actionCopy)
        menu.addAction(actionSelectAll)

        # 连接复制和全选的动作
        actionCopy.triggered.connect(self.copyText)
        actionSelectAll.triggered.connect(self.selectAllText)

        # 显示菜单
        menu.exec(self.textEdit.mapToGlobal(pos))

    def copyText(self):
        # 复制文本的槽函数
        self.textEdit.copy()

    def selectAllText(self):
        # 全选文本的槽函数
        self.textEdit.selectAll()

    def lineEdit_menu(self, pos):
        context_menu = QMenu(self.lineEdit)
        # 设置菜单颜色
        context_menu.setStyleSheet(
            'QMenu{background-color: rgb(0,170,255);margin:5px;}QMenu::item:selected{background-color:rgb(255, 255, 255);color:rgb(0, 0, 0);}')

        paste_action = QAction('粘贴', self.lineEdit)
        paste_action.triggered.connect(self.paste_text)

        context_menu.addAction(paste_action)

        # 显示上下文菜单
        context_menu.exec(self.lineEdit.mapToGlobal(pos))

    def paste_text(self):
        self.lineEdit.paste()

    def lineEdit_2_menu(self, pos):
        context_menu = QMenu(self.lineEdit_2)
        # 设置菜单颜色
        context_menu.setStyleSheet(
            'QMenu{background-color: rgb(0,170,255);margin:5px;}QMenu::item:selected{background-color:rgb(255, 255, 255);color:rgb(0, 0, 0);}')
        paste_action = QAction('粘贴', self.lineEdit_2)
        paste_action.triggered.connect(self.paste_text_2)

        context_menu.addAction(paste_action)

        # 显示上下文菜单
        context_menu.exec(self.lineEdit_2.mapToGlobal(pos))

    def paste_text_2(self):
        self.lineEdit_2.paste()

    def ad_img(self):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...', database='game')
        cursor = connect.cursor()
        # 获取ad_link表里的path和link链接地址
        cursor.execute("SELECT ad_link,ad_image FROM config where id=1")
        result = cursor.fetchone()
        link = result[0]
        path = result[1]
        if any(ext in path for ext in ['.png', '.jpg', '.jpeg']):
            self.label_3 = ClickableLabel(self.frame_4)
            self.label_3.setGeometry(70, 5, 370, 100)
            # 加载图片
            self.label_3.setTextFormat(Qt.RichText)
            # 设置超链接
            self.label_3.setLink(link)
            # # 加载广告图片链接
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(path).content)
            self.label_3.setPixmap(pixmap)
            self.label_3.setScaledContents(True)
            self.label_3.setWindowFlags(Qt.WindowStaysOnTopHint)
        elif '.gif' in path:
            self.label_3 = QLabel(self.frame_4)
            self.label_3.setGeometry(70, 5, 370, 100)
            response = requests.get(path)
            temp_file = tempfile.NamedTemporaryFile(delete=False)  # 创建临时文件
            temp_file.write(response.content)
            temp_file.close()  # 关闭文件，确保写入完成
            movie = QMovie(temp_file.name)  # 使用临时文件名初始化 QMovie
            self.label_3.setMovie(movie)
            # 设置鼠标点击事件
            self.label_3.setCursor(Qt.PointingHandCursor)
            self.label_3.mousePressEvent = lambda event: webbrowser.open(link)
            movie.start()

        else:
            self.label_3 = QLabel(self.frame_4)
            self.label_3.setGeometry(70, 5, 370, 100)
            self.label_3.setText(" 广告位招租中，点击联系客服")
            # 设置字体大小
            font = QFont()
            font.setPointSize(20)
            # 字体居中
            font.setBold(True)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
            # 设置鼠标点击事件
            self.label_3.setCursor(Qt.PointingHandCursor)
            self.label_3.mousePressEvent = lambda event: webbrowser.open('http://www.ytydn.com/#/home')

        # 设置关闭按钮
        self.close_btn = QPushButton(self.frame_4)
        self.close_btn.setGeometry(390, 5, 50, 20)
        # 设置关闭按钮的文字
        self.close_btn.setText("关闭窗口")
        # 设置关闭按钮的字体颜色
        self.close_btn.setStyleSheet("color: rgb(255, 255, 255);")
        # 绑定关闭广告的事件
        self.close_btn.clicked.connect(self.close_ad)
        self.label_3.show()
        self.close_btn.show()

    def close_ad(self):
        self.label_3.close()
        self.close_btn.close()
        self.draggableFrame = DraggableFrame(MainWindow)
        self.draggableFrame.setGeometry(QRect(680, 1, 500, 108))
        self.draggableFrame.setFrameShadow(QFrame.Raised)
        self.draggableFrame.setFrameShape(QFrame.StyledPanel)
        self.draggableFrame.show()

    def redis2dict(self):
        import redis
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...', database='game')
        cursor = connect.cursor()
        # 查询数据库
        cursor.execute("select redis_ip,redis_passwd,redis_db from config where id=1")
        data = cursor.fetchone()
        host = data[0]
        passwd = data[1]
        db = data[2]
        cursor.close()
        connect.close()
        print('redis地址：', host, 'redis密码:', passwd, 'redis数据库：', db)
        try:
            if passwd == None or len(passwd) == 0:
                redis_client = redis.Redis(host=host, port=6379, db=db,socket_timeout=1)
            else:
                redis_client = redis.Redis(host=host, port=6379, db=db, password=passwd,socket_timeout=1)
            # redis_client=redis.Redis(host=host, port=6379, db=1, password='xwg31415926...')
            keys = redis_client.keys()
            # global self.icon_dict
            for key in keys:
                value = redis_client.get(key)
                self.icon_dict[key.decode('utf-8')] = value
            redis_client.close()
            return self.icon_dict
        except Exception as e:
            print(e)
            return {}

    def local2dict(self):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...',
                              database='game')
        cursor = connect.cursor()
        # 查询数据库
        cursor.execute("select name,icon from game")
        # 获取查询结果
        data = cursor.fetchall()
        for i in data:
            name=i[0]
            icon=i[1]
            #遍历icon路径
            if os.path.exists(icon):
                with open(icon, 'rb') as f:
                    icon = f.read()
                    self.icon_dict[name] = icon
            else:
                icon = resource_path + '\\game.ico'
                with open(icon, 'rb') as f:
                    icon = f.read()
                    self.icon_dict[name] = icon

        cursor.close()
        connect.close()
        self.icon_state=1
        return self.icon_dict
        
    def redis_btn(self):
        self.thread = redisthread()
        self.thread.start()
        print('redis启动线程')
    def steam_btn(self):
        print('启动steam线程')
        self.thread1 = steamthread()
        self.thread1.start()
        print('steam启动线程')

    def console_btn(self):
        self.thread2 = consolethread()
        self.thread2.start()
        print('console启动线程')

    def online_btn(self):
        self.thread3 = onlinethread()
        self.thread3.start()
        print('online启动线程')

    def vs_btn(self):
        self.thread4 = vsthread()
        self.thread4.start()
        print('vs启动线程')

    def other_btn(self):
        self.thread5 = otherthread()
        self.thread5.start()
        print('other启动线程')

    def game_thread(self):
        # self.thread6 =localthread()
        # self.thread6.start()
        # print('启动local线程')
        self.thread6 = redisthread()
        self.thread6.start()
        print('启动redis线程')

        self.thread7 = steamthread()
        self.thread7.start()
        print('启动steam线程')

        self.thread8 = hotthread()
        self.thread8.start()
        print('启动hot线程')

        self.thread9 = onlinethread()
        self.thread9.start()
        print('启动online线程')

        self.thread10 = consolethread()
        self.thread10.start()
        print('启动console线程')

        self.thread11 = vsthread()
        self.thread11.start()
        print('启动vs线程')

        self.thread12 = otherthread()
        self.thread12.start()
        print('启动other线程')


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class ClickableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOpenExternalLinks(True)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            QDesktopServices.openUrl(QUrl(self.link))

    def setLink(self, link):
        self.link = link


class Worker(QThread):
    # finished = pyqtSignal(str)

    def run(self):
        try:
            text = ui.get_response()
            self.finished.emit(text)

        except Exception as e:
            print(e)
            self.finished.emit()


class DraggableFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()
        self.isDragging = False
        self.dragStartPosition = QPoint()

    def initUI(self):
        self.setFrameShape(QFrame.Shape.StyledPanel)
        layout = QVBoxLayout(self)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.isDragging = True
            self.dragStartPosition = event.globalPosition().toPoint() - self.parentWidget().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.isDragging:
            self.parentWidget().move(event.globalPosition().toPoint() - self.dragStartPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.isDragging = False
            event.accept()


def is_already_running():
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == 65432 and conn.status == 'LISTEN':
            return True
    print('没有运行')
    return False


def send_activation_signal():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('localhost', port))
        s.sendall(b'ACTIVATE')
        s.close()
        print("Activation signal sent")
    except (ConnectionRefusedError, OSError) as e:
        print(f"无法发送激活信号: {e}")


class config:
    def port(self):
        connect = sql.connect(host='xwgchat.cn', port=3306, user='root', password='xwg31415926...', database='game')
        cursor = connect.cursor()
        # 查询数据库
        cursor.execute("select port from config where id=1")
        port = int(cursor.fetchone()[0])
        cursor.close()
        connect.close()
        return port


# ==================================================================\
class localthread(QThread):
    data_loaded = Signal(list)

    def run(self):
        ui.local2dict()
        print('local列表加载完成')
# tab线程启动
class steamthread(QThread):
    # data_loaded = pyqtSignal(list)

    def run(self):
        ui.steam_list()
        print('steam列表加载完成')


class hotthread(QThread):
    # data_loaded = pyqtSignal(list)

    def run(self):
        ui.hot_list()
        print('hot列表加载完成')


class redisthread(QThread):
    # data_loaded = pyqtSignal(list)

    def run(self):
        ui.redis_list()
        print('redis列表加载完成')


class consolethread(QThread):
    # data_loaded = pyqtSignal(list)

    def run(self):
        ui.console_game()
        print('console列表加载完成')


class onlinethread(QThread):
    # data_loaded = pyqtSignal(list)

    def run(self):
        ui.online_game()
        print('online列表加载完成')


class vsthread(QThread):
    # data_loaded = pyqtSignal(list)

    def run(self):
        ui.vs_game()
        print('vs列表加载完成')


class otherthread(QThread):
    # data_loaded = pyqtSignal(list)

    def run(self):
        ui.other_game()
        print('other列表加载完成')


# ==================================================================================

if __name__ == "__main__":
    global_listwidget = None
    all_data = ()
    load_item = 50
    resource_path = os.path.dirname(os.path.abspath(__file__))
    # resource_path = 'E:\python-project\游戏菜单\客户端\\'
    app = QtWidgets.QApplication(sys.argv)
    port = config().port()
    if is_already_running():
        print("已存在运行程序")
        send_activation_signal()
        sys.exit(0)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.sql2dict()
    # ui.redis2dict()
    ui.game_thread()
    ui.ad_img()
    # 设置为无边框
    MainWindow.setWindowFlags(Qt.FramelessWindowHint)
    # MainWindow.show()
    sys.exit(app.exec())


# pyinstaller -D --name=YiTengYunMenu  --noconsole --add-data "yty.ico;."  --add-data "1.png;."  --add-data "2.png;." --add-data "game.ico;." --add-data "send.png;." --icon yty.ico 客户端界面.py --upx-dir E:\python-project\游戏菜单\upx-4.2.4-win64

# nuitka --standalone --mingw64 --enable-plugin=PySide6  --windows-disable-console  --windows-icon-from-ico=E:\python-project\游戏菜单\客户端\yty.ico --output-dir=E:\python-project\游戏菜单\客户端\dist\game.exe E:\python-project\游戏菜单\客户端\客户端界面.py
