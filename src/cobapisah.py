# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from shop_hist import ShoppingHist
import shop_cart
import resources_rc
import schedule
import addbFast
import addLunch
import addDinner
import modbFast
import modDinner
import modLunch
import meal_hist
import rincianmeal
import welcomeWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200,620)
        MainWindow.setMinimumSize(QSize(1200,620))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(247, 255, 249);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget) 
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.316, y1:0.267, x2:1, y2:1, stop:0 rgba(0, 188, 161, 255), stop:1 rgba(100, 200, 120, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"color:white;\n"
"text-align: left;\n"
"height:40px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color:white;\n"
"color:#00D493\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 188, 161);")
        self.label_2.setPixmap(QPixmap(u":/images/logonom.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(11)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 188, 161);")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.schedule_2 = QPushButton(self.icon_name_widget)
        self.schedule_2.setObjectName(u"schedule_2")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setBold(True)
        self.schedule_2.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/images/icon_jadwal.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/icon_jadwal2.png", QSize(), QIcon.Normal, QIcon.On)
        self.schedule_2.setIcon(icon)
        self.schedule_2.setCheckable(True)
        self.schedule_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.schedule_2)

        self.cart_2 = QPushButton(self.icon_name_widget)
        self.cart_2.setObjectName(u"cart_2")
        self.cart_2.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/images/icon_cart.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/images/icon_cart2.png", QSize(), QIcon.Normal, QIcon.On)
        self.cart_2.setIcon(icon1)
        self.cart_2.setCheckable(True)
        self.cart_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.cart_2)

        self.mealhist_2 = QPushButton(self.icon_name_widget)
        self.mealhist_2.setObjectName(u"mealhist_2")
        self.mealhist_2.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/images/icon_histmeal.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/icon_histmeal2.png", QSize(), QIcon.Normal, QIcon.On)
        self.mealhist_2.setIcon(icon2)
        self.mealhist_2.setCheckable(True)
        self.mealhist_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.mealhist_2)

        self.shophist_2 = QPushButton(self.icon_name_widget)
        self.shophist_2.setObjectName(u"shophist_2")
        self.shophist_2.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/images/icon_histshop.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/icon_histshop2.png", QSize(), QIcon.Normal, QIcon.On)
        self.shophist_2.setIcon(icon3)
        self.shophist_2.setCheckable(True)
        self.shophist_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.shophist_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 305, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_11 = QPushButton(self.icon_name_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 0))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"color:white;\n"
"text-align: center;\n"
"height:40px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color:white;\n"
"color:#00D493\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/logout2.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_11)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.316, y1:0.267, x2:1, y2:1, stop:0 rgba(0, 188, 161, 255), stop:1 rgba(100, 200, 120, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"color:white;\n"
"height:40px;\n"
"border:none;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color:white;\n"
"color:#00D493\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setStyleSheet(u"background-color: rgb(0, 188, 161);")
        self.label.setPixmap(QPixmap(u":/images/logonom.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.schedule_1 = QPushButton(self.icon_only_widget)
        self.schedule_1.setObjectName(u"schedule_1")
        self.schedule_1.setIcon(icon)
        self.schedule_1.setCheckable(True)
        self.schedule_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.schedule_1)

        self.cart_1 = QPushButton(self.icon_only_widget)
        self.cart_1.setObjectName(u"cart_1")
        self.cart_1.setIcon(icon1)
        self.cart_1.setCheckable(True)
        self.cart_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cart_1)

        self.mealhist_1 = QPushButton(self.icon_only_widget)
        self.mealhist_1.setObjectName(u"mealhist_1")
        self.mealhist_1.setIcon(icon2)
        self.mealhist_1.setCheckable(True)
        self.mealhist_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.mealhist_1)

        self.shophist_1 = QPushButton(self.icon_only_widget)
        self.shophist_1.setObjectName(u"shophist_1")
        self.shophist_1.setIcon(icon3)
        self.shophist_1.setCheckable(True)
        self.shophist_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.shophist_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 305, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout_1 = QPushButton(self.icon_only_widget)
        self.logout_1.setObjectName(u"logout_1")
        icon5 = QIcon()
        icon5.addFile(u":/images/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_1.setIcon(icon5)
        self.logout_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.logout_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.gridLayout_2 = QGridLayout(self.main_menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/images/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QSize(20, 20))
        self.pushButton_10.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_10)

        self.horizontalSpacer = QSpacerItem(439, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/images/icon_back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(20, 20))
        self.pushButton_9.setCheckable(True)


        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(0, 143, 110);")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidgetMenu = QStackedWidget(self.main_menu)
        self.stackedWidgetMenu.setObjectName(u"stackedWidgetMenu")
        self.stackedWidgetMenu.setStyleSheet(u"background-color:white;")

        
        self.stackedWidgetMenu.addWidget(schedule.create_schedule(self, self.stackedWidgetMenu)) #0

        def switch_to_home():
            self.stackedWidgetMenu.setCurrentIndex(11)
        
        self.pushButton_9.clicked.connect(switch_to_home)

        self.stackedWidgetMenu.addWidget(addbFast.create_bfast(self,self.stackedWidgetMenu)) #1
        self.stackedWidgetMenu.addWidget(addLunch.create_lunch(self,self.stackedWidgetMenu)) #2
        self.stackedWidgetMenu.addWidget(addDinner.create_dinner(self,self.stackedWidgetMenu)) #3

        self.stackedWidgetMenu.addWidget(modbFast.create_modbFast(self,self.stackedWidgetMenu)) #4
        self.stackedWidgetMenu.addWidget(modLunch.create_modLunch(self,self.stackedWidgetMenu)) #5
        self.stackedWidgetMenu.addWidget(modDinner.create_modDinner(self,self.stackedWidgetMenu)) #6

        self.stackedWidgetMenu.addWidget(rincianmeal.create_rincianMeal(self,self.stackedWidgetMenu)) #7

        self.stackedWidgetMenu.addWidget(shop_cart.create_shop_cart(self)) #8

        
        self.stackedWidgetMenu.addWidget(meal_hist.meal_hist(self)) #9
        self.shop_hist = ShoppingHist()
        self.stackedWidgetMenu.addWidget(self.shop_hist) #10
        self.stackedWidgetMenu.addWidget(welcomeWindow.create_Home(self,self.stackedWidgetMenu)) #11

        self.gridLayout_2.addWidget(self.stackedWidgetMenu, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_10.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_10.toggled.connect(self.icon_name_widget.setVisible)
        self.shophist_1.toggled.connect(self.shophist_2.setChecked)
        self.mealhist_1.toggled.connect(self.mealhist_2.setChecked)
        self.cart_1.toggled.connect(self.cart_2.setChecked)
        self.schedule_1.toggled.connect(self.schedule_2.setChecked)
        self.schedule_2.toggled.connect(self.schedule_1.setChecked)
        self.cart_2.toggled.connect(self.cart_1.setChecked)
        self.mealhist_2.toggled.connect(self.mealhist_1.setChecked)
        self.shophist_2.toggled.connect(self.shophist_1.setChecked)
        self.logout_1.toggled.connect(MainWindow.close)
        self.pushButton_11.toggled.connect(MainWindow.close)

        self.stackedWidgetMenu.setCurrentIndex(11)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NomNom", None))
        self.schedule_2.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.cart_2.setText(QCoreApplication.translate("MainWindow", u"Shop Cart", None))
        self.mealhist_2.setText(QCoreApplication.translate("MainWindow", u"Meal History", None))
        self.shophist_2.setText(QCoreApplication.translate("MainWindow", u"Shop History", None))
        self.pushButton_11.setText("")
        self.label.setText("")
        self.schedule_1.setText("")
        self.cart_1.setText("")
        self.mealhist_1.setText("")
        self.shophist_1.setText("")
        self.logout_1.setText("")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home", None))
    # retranslateUi