from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget, QMessageBox,QScrollArea,QLayout,QCalendarWidget,QGroupBox,QPlainTextEdit,QDialog)

# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.controller import *

def meal_hist(parent):
        font1 = QFont()
        font1.setFamilies(["Century Gothic"])
        font1.setPointSize(16)
        font1.setBold(True)
        meal_hist = QWidget()
        meal_hist.setObjectName("meal_hist")


        mh_hello = QLabel(meal_hist)
        mh_hello.setObjectName("mh_hello")
        mh_hello.setEnabled(True)
        mh_hello.setGeometry(QRect(11, 11, 1140, 32))
        mh_hello.setFont(font1)
        mh_hello.setStyleSheet("color: rgb(0, 143, 110);")

        font2 = QFont()
        font2.setFamilies(["Century Gothic"])
        font2.setPointSize(11)

        mh_here = QLabel(meal_hist)
        mh_here.setObjectName("mh_here")
        mh_here.setGeometry(QRect(11, 50, 1140, 21))
        mh_here.setFont(font2)
        mh_here.setStyleSheet("color: rgb(0, 143, 110);")

        layoutWidget = QWidget(meal_hist)
        layoutWidget.setObjectName("layoutWidget")
        layoutWidget.setGeometry(QRect(10, 90, 1101, 41))
        horizontalLayout_5 = QHBoxLayout(layoutWidget)
        horizontalLayout_5.setObjectName("horizontalLayout_5")
        horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        mh_date = QLabel(layoutWidget)
        
        mh_date.setObjectName("mh_date")
        mh_date.setStyleSheet("color: rgb(0, 143, 110);")
        
        
        mh_horizontalspacer1 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding)
        mh_horizontalspacer2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed)

        

        mh_calendar_button = QPushButton(layoutWidget, clicked = lambda: show_calendar())
        mh_calendar_button.setGeometry(QRect(50, 100, 1101, 41))

        mh_calendar_button.setObjectName("mh_calendar_button")

        font4 = QFont()
        font4.setFamilies(["Century Gothic"])
        font4.setPointSize(8)
        font4.setBold(True)
        
        
        mh_calendar_button.setStyleSheet("QPushButton{\n"
"background-color:white;\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:#FF5E6A;\n"
"height:35px;\n"
"width:150px\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"border-color:#fce8e9;\n"
"}")
        
        horizontalLayout_5.addWidget(mh_date)
        horizontalLayout_5.addItem(mh_horizontalspacer1)
        horizontalLayout_5.addItem(mh_horizontalspacer2)
        horizontalLayout_5.addWidget(mh_calendar_button)
        
        
        

        icon8 = QIcon()
        icon8.addFile(":/images/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        mh_calendar_button.setIcon(icon8)
        # mh_calendar_button.setCheckable(True)
        # mh_calendar_button.setAutoDefault(False)
        # mh_calendar_button.setFlat(False)
        # mh_calendar_button.clicked.connect(show_calendar)


        calendarWidget = QCalendarWidget()
        calendarWidget.hide()

        notes_window = QMainWindow()
        notes_window.setWindowTitle("Notes")
        notes_window.setFixedSize(400,300)

        notes_dialog = QDialog()
        notes_layout = QVBoxLayout(notes_dialog)

        groupBox = QGroupBox("Notes")
        # groupBox.setObjectName("groupBox_notes")
        # groupBox.setGeometry(QRect(480, 700, 371, 271))
        # groupBox.hide()

        notes_layout2 = QVBoxLayout(groupBox)

        plainTextEdit = QPlainTextEdit()
        # plainTextEdit.setObjectName("plainTextEdit")
        # plainTextEdit.setPlainText
        # plainTextEdit.setGeometry(QRect(30, 50, 311, 151))
        plainTextEdit.setOverwriteMode(False)

        save_button = QPushButton("Save")
        # save_button.setObjectName("save_button")
        # save_button.setGeometry(QRect(70, 220, 93, 28))
        cancel_button = QPushButton("Cancel")
        # cancel_button.setObjectName("cancel_button")
        # cancel_button.setGeometry(QRect(210, 220, 93, 28))

        save_button.clicked.connect(notes_dialog.accept)
        cancel_button.clicked.connect(notes_dialog.reject)

        notes_layout2.addWidget(plainTextEdit)
        notes_layout2.addWidget(save_button)
        notes_layout2.addWidget(cancel_button)

        notes_layout.addWidget(groupBox)

        verticalLayoutWidget = QWidget(meal_hist)
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        verticalLayoutWidget.setGeometry(QRect(10, 140, 1101, 481))
        verticalLayout_7 = QVBoxLayout(verticalLayoutWidget)
        verticalLayout_7.setSpacing(1)
        verticalLayout_7.setObjectName("verticalLayout_7")
        verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        mh_Breakfast_label_6 = QLabel(verticalLayoutWidget)
        mh_Breakfast_label_6.setObjectName("mh_Breakfast_label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mh_Breakfast_label_6.sizePolicy().hasHeightForWidth())
        mh_Breakfast_label_6.setSizePolicy(sizePolicy)
        mh_Breakfast_label_6.setFont(font2)
        mh_Breakfast_label_6.setStyleSheet("background-color:#fce8e9;\n"
"color:#FF5E6A;\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"heigth:50px;")
        mh_Breakfast_label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        mh_Breakfast_label_6.setMargin(10)

        verticalLayout_7.addWidget(mh_Breakfast_label_6)

        listWidget_2 = QListWidget(verticalLayoutWidget)
        listWidget_2.setObjectName("listWidget_2")

        verticalLayout_7.addWidget(listWidget_2)

        verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        verticalLayout_7.addItem(verticalSpacer_4)

        mh_Breakfast_label_7 = QLabel(verticalLayoutWidget)
        mh_Breakfast_label_7.setObjectName("mh_Breakfast_label_7")
        sizePolicy.setHeightForWidth(mh_Breakfast_label_7.sizePolicy().hasHeightForWidth())
        mh_Breakfast_label_7.setSizePolicy(sizePolicy)
        mh_Breakfast_label_7.setFont(font2)
        mh_Breakfast_label_7.setStyleSheet("background-color:#fce8e9;\n"
"color:#FF5E6A;\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"heigth:50px;")
        mh_Breakfast_label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        mh_Breakfast_label_7.setMargin(10)

        verticalLayout_7.addWidget(mh_Breakfast_label_7)

        listWidget_3 = QListWidget(verticalLayoutWidget)
        listWidget_3.setObjectName("listWidget_3")

        verticalLayout_7.addWidget(listWidget_3)

        verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        verticalLayout_7.addItem(verticalSpacer_6)

        mh_Breakfast_label_8 = QLabel(verticalLayoutWidget)
        mh_Breakfast_label_8.setObjectName("mh_Breakfast_label_8")
        sizePolicy.setHeightForWidth(mh_Breakfast_label_8.sizePolicy().hasHeightForWidth())
        mh_Breakfast_label_8.setSizePolicy(sizePolicy)
        mh_Breakfast_label_8.setFont(font2)
        mh_Breakfast_label_8.setStyleSheet("background-color:#fce8e9;\n"
"color:#FF5E6A;\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"heigth:50px;")
        mh_Breakfast_label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        mh_Breakfast_label_8.setMargin(10)

        verticalLayout_7.addWidget(mh_Breakfast_label_8)

        listWidget_4 = QListWidget(verticalLayoutWidget)
        listWidget_4.setObjectName("listWidget_4")

        verticalLayout_7.addWidget(listWidget_4)
        
        


        def show_notes(id):
                id_mh = int(id)
                db_path= os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
                controller = Controller(db_path)
                prev_text = controller.get_notes_mealhistory_by_id(id_mh)
                plainTextEdit.setPlainText(prev_text)
                print("text : "+prev_text)
                result = notes_dialog.exec()
                if result == QDialog.Rejected:
                        plainTextEdit.setPlainText(prev_text)
                else:
                        controller.add_notes_mealhistory(str(id_mh),plainTextEdit.toPlainText())


        def show_calendar():
                # mh_calendar_button.setEnabled(False)
                # Create a new calendar widget
                calendarWidget.activateWindow()
                calendarWidget.setGeometry(720, 150, 392, 236)
                # calendarWidget.setStyleSheet("background-color: white; color: black;")
                # Connect the clicked signal to the date_selected function
                calendarWidget.clicked.connect(date_selected)

                # Set up layout and add the calendar widget
                # layout = QVBoxLayout()
                # meal_hist.addWidget(calendarWidget)
                # setLayout(layout)
                calendarWidget.show()

        def date_selected():
                selected_date = calendarWidget.selectedDate()
                yy = selected_date.year()
                mm = selected_date.month()
                dd = selected_date.day()
                mh_date.setText(f"{dd:02d}-{mm:02d}-{yy:04d}")
                calendarWidget.hide()
                # mh_calendar_button.setEnabled(True)
                add_mh(f'{yy:04d}-{mm:02d}-{dd:02d}')



        def add_mh(date):
                print("display_mh flag")
                db_path= os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
                controller = Controller(db_path)
                print("date : "+date)
                mh_list = controller.get_mealhistory_by_date(date)
                print("mh_list flag : \n"+str(mh_list))
                listWidget_2.clear()
                listWidget_3.clear()
                listWidget_4.clear()
                for mh in mh_list:
                        listwItem = QListWidgetItem()
                        print("mh : "+str(mh))
                        match mh[2]:
                                case 'breakfast':
                                        print("flag bfast")
                                        count = listWidget_2.count()+1
                                        item = make_mh(mh[1],count,mh[0])
                                        listwItem.setSizeHint(item.sizeHint())
                                        listWidget_2.addItem(listwItem)
                                        listWidget_2.setItemWidget(listwItem,item)
                                case'lunch':
                                        print("flag lunch")
                                        count = listWidget_3.count()+1
                                        item = make_mh(mh[1],count,mh[0])
                                        listwItem.setSizeHint(item.sizeHint())
                                        listWidget_3.addItem(listwItem)
                                        listWidget_3.setItemWidget(listwItem,item)
                                case 'dinner':
                                        print("flag dinna")
                                        
                                        count = listWidget_4.count()+1
                                        item = make_mh(mh[1],count,mh[0])
                                        listwItem.setSizeHint(item.sizeHint())
                                        listWidget_4.addItem(listwItem)
                                        listWidget_4.setItemWidget(listwItem,item)


        
        def make_mh(meal_name,n,id):
                # listwItem = QListWidgetItem()
                item = QWidget()

                layout = QHBoxLayout(item)

                label = QLabel()
                label.setText(str(n) +"). "+(meal_name))
                label.setStyleSheet("color:black;")
                icon_button = QPushButton(item,clicked = lambda: show_notes(id))
                icon_button.setStyleSheet("background-color: #fce8e9;")
                icon8 = QIcon()
                icon8.addFile(":/images/modifyW.png", QSize(24, 24), QIcon.Normal)
                icon_button.setIcon(icon8)
                icon_button.setIconSize(QSize(24, 24))
                icon_button.setFixedSize(30, 30)
                # icon_button.setStyleSheet("border: none;")  # Remove button border
                # icon_button.clicked.connect(icon_button_clicked)
                spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                layout.addWidget(label)
                layout.addItem(spacer)
                layout.addWidget(icon_button)

                # listwItem.setSizeHint(item.sizeHint())
                
                return item







        mh_hello.setText(QCoreApplication.translate("MainWindow", "Hello, Nana!", None))
        mh_here.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p>Here is your <span style=\" font-weight:600;\">meal history</span></p></body></html>", None))
        mh_date.setText(QCoreApplication.translate("MainWindow", "DD-MM-YY", None))
        mh_calendar_button.setText(QCoreApplication.translate("MainWindow", "  SELECT DATE", None))
        mh_Breakfast_label_6.setText(QCoreApplication.translate("MainWindow", "Breakfast", None))
        mh_Breakfast_label_7.setText(QCoreApplication.translate("MainWindow", "Lunch", None))
        mh_Breakfast_label_8.setText(QCoreApplication.translate("MainWindow", "Dinner", None))
        

        return meal_hist