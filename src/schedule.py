from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from controller.controller import *
from datetime import datetime
     
def create_schedule(parent, stackedWidgetMenu):
        db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
        controller = Controller(db_path)

        schedule = QWidget()
        schedule.setObjectName("schedule")
        label_8 = QLabel(schedule)
        label_8.setObjectName("label_8")
        label_8.setGeometry(QRect(20, 67, 721, 25))
        font3 = QFont()
        font3.setFamilies(["Century Gothic"])
        font3.setPointSize(11)
        font3.setBold(False)
        label_8.setFont(font3)
        label_8.setStyleSheet("color: rgb(0, 143, 110);")
        label_6 = QLabel(schedule)
        label_6.setObjectName("label_6")
        label_6.setGeometry(QRect(20, 20, 721, 38))
        font4 = QFont()
        font4.setFamilies(["Century Gothic"])
        font4.setPointSize(16)
        font4.setBold(True)
        label_6.setFont(font4)
        label_6.setStyleSheet("color: rgb(0, 143, 110);")
        widget_2 = QWidget(schedule)
        widget_2.setObjectName("widget_2")
        widget_2.setGeometry(QRect(20, 120, 1051, 47))
        widget_2.setStyleSheet("border-radius:15px;\n"
"background-color:white;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:#8b8b8b;")
        horizontalLayout_5 = QHBoxLayout(widget_2)
        horizontalLayout_5.setObjectName("horizontalLayout_5")
        btnMon = QPushButton(widget_2,clicked = lambda : switchday(0))
        btnMon.setObjectName("btnMon")
        font5 = QFont()
        font5.setFamilies(["Century Gothic"])
        btnMon.setFont(font5)
        btnMon.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color:#8b8b8b\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:#FF5E6A;\n"
"font-weight:bold;\n"
"}")
        btnMon.setCheckable(True)
        btnMon.setAutoExclusive(True)

        horizontalLayout_5.addWidget(btnMon)

        btnTues = QPushButton(widget_2,clicked = lambda : switchday(1))
        btnTues.setObjectName("btnTues")
        btnTues.setFont(font5)
        btnTues.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color:#8b8b8b\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:#FF5E6A;\n"
"font-weight:bold;\n"
"}")
        btnTues.setCheckable(True)
        btnTues.setAutoExclusive(True)

        horizontalLayout_5.addWidget(btnTues)

        btnWed = QPushButton(widget_2,clicked = lambda : switchday(2))
        btnWed.setObjectName("btnWed")
        btnWed.setFont(font5)
        btnWed.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color:#8b8b8b\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:#FF5E6A;\n"
"font-weight:bold;\n"
"}")
        btnWed.setCheckable(True)
        btnWed.setAutoExclusive(True)

        horizontalLayout_5.addWidget(btnWed)

        btnThurs = QPushButton(widget_2,clicked = lambda : switchday(3))
        btnThurs.setObjectName("btnThurs")
        btnThurs.setFont(font5)
        btnThurs.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color:#8b8b8b\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:#FF5E6A;\n"
"font-weight:bold;\n"
"}")
        btnThurs.setCheckable(True)
        btnThurs.setAutoExclusive(True)

        horizontalLayout_5.addWidget(btnThurs)

        btnFri = QPushButton(widget_2,clicked = lambda : switchday(4))
        btnFri.setObjectName("btnFri")
        btnFri.setFont(font5)
        btnFri.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color:#8b8b8b\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:#FF5E6A;\n"
"font-weight:bold;\n"
"}")
        btnFri.setCheckable(True)
        btnFri.setAutoExclusive(True)

        horizontalLayout_5.addWidget(btnFri)

        btnSat = QPushButton(widget_2,clicked = lambda : switchday(5))
        btnSat.setObjectName("btnSat")
        btnSat.setFont(font5)
        btnSat.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color:#8b8b8b\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:#FF5E6A;\n"
"font-weight:bold;\n"
"}")
        btnSat.setCheckable(True)
        btnSat.setAutoExclusive(True)

        horizontalLayout_5.addWidget(btnSat)

        btnSun = QPushButton(widget_2,clicked = lambda : switchday(6))
        btnSun.setObjectName("btnSun")
        btnSun.setFont(font5)
        btnSun.setStyleSheet("QPushButton{\n"
"border:none;\n"
"color:#8b8b8b\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:#FF5E6A;\n"
"font-weight:bold;\n"
"}")
        btnSun.setCheckable(True)
        btnSun.setAutoExclusive(True)

        horizontalLayout_5.addWidget(btnSun)

        widget_3 = QWidget(schedule)
        widget_3.setObjectName("widget_3")
        widget_3.setGeometry(QRect(20, 180, 741, 48))
        horizontalLayout_6 = QHBoxLayout(widget_3)
        horizontalLayout_6.setObjectName("horizontalLayout_6")
        iconCalendar = QLabel(widget_3)
        iconCalendar.setObjectName("iconCalendar")
        iconCalendar.setMinimumSize(QSize(30, 30))
        iconCalendar.setMaximumSize(QSize(30, 30))
        iconCalendar.setPixmap(QPixmap(":/images/calendar.png"))
        iconCalendar.setScaledContents(True)


        # label_date = QLabel(widget_3)
        # label_date.setText("YYYY-MM-DD")
        horizontalLayout_6.addWidget(iconCalendar)

        labelDate = QLabel(widget_3)
        labelDate.setObjectName("labelDate")
        font6 = QFont()
        font6.setFamilies(["Century Gothic"])
        font6.setPointSize(9)
        labelDate.setFont(font6)
        labelDate.setStyleSheet("color:#FF5E6A")

        horizontalLayout_6.addWidget(labelDate)

        layoutWidget = QWidget(schedule)
        layoutWidget.setObjectName("layoutWidget")
        layoutWidget.setGeometry(QRect(20, 240, 1091, 471))
        horizontalLayout_8 = QHBoxLayout(layoutWidget)
        horizontalLayout_8.setObjectName("horizontalLayout_8")
        horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        Bfast = QWidget(layoutWidget)
        Bfast.setObjectName("Bfast")
        listWidget_Bfast = QListWidget(Bfast)
        listWidget_Bfast.setObjectName("listWidget_Bfast")
        listWidget_Bfast.setGeometry(QRect(10, 110, 311, 200))
        listWidget_Bfast.setStyleSheet("font: 12pt 'Century Gothic'; color: black;")
        # meals = controller.get_jadwalmakanan_by_category("breakfast")
        # print("meals check : "+str(meals))
        #ingredients = ["bakso", "ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam","ayam"]
        # date_today
        # date_today = datetime.now()
        def switchday(index: int):
                date = controller.get_current_week_dates()
                meals_bfast = controller.get_jadwalmakanan_by_category("breakfast")
                #print("meals check : "+str(meals))   
                global date_today
                date_today = date[index]
                labelDate .setText(date_today.strftime("%d-%m-%Y"))
                listWidget_Bfast.clear()
                for meal in meals_bfast[index]:
                        print("bfast id : "+str(index)+" mn : "+str(meal.name_meal))
                        itemBfast = QListWidgetItem(meal.name_meal) 
                        itemBfast.setWhatsThis(str(meal.id_meal))
                        listWidget_Bfast.addItem(itemBfast)                         


                meals_lunch = controller.get_jadwalmakanan_by_category("lunch")
                #print("meals check : "+str(meals))   
                listWidget_Lunch.clear()
                for meal_lunch in meals_lunch[index]:
                        print("lunch id : "+str(index)+" mn : "+str(meal_lunch.name_meal))
                        itemLunch = QListWidgetItem(meal_lunch.name_meal) 
                        itemLunch.setWhatsThis(str(meal_lunch.id_meal))
                        listWidget_Lunch.addItem(itemLunch)        


                meals_dinner = controller.get_jadwalmakanan_by_category("dinner")
                #print("meals check : "+str(meals))   
                listWidget_Dinner.clear()
                for meal_din in meals_dinner[index]:
                        print("dinner id : "+str(index)+" mn : "+str(meal_din.name_meal))
                        itemDinner = QListWidgetItem(meal_din.name_meal) 
                        itemDinner.setWhatsThis(str(meal_din.id_meal))
                        listWidget_Dinner.addItem(itemDinner)               



        widget_4 = QWidget(Bfast)
        widget_4.setObjectName("widget_4")
        widget_4.setGeometry(QRect(10, 10, 221, 41))
        label_Bfast = QLabel(Bfast)
        label_Bfast.setObjectName("label_Bfast")
        label_Bfast.setGeometry(QRect(10, 50, 311, 61))
        label_Bfast.setFont(font3)
        label_Bfast.setStyleSheet("background-color:#fce8e9;\n"
"color:#FF5E6A;\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;")
        label_Bfast.setAlignment(Qt.AlignCenter)
        bfastDel = QPushButton(Bfast)
        bfastDel.setObjectName("bfastDel")
        bfastDel.setGeometry(QRect(280, 20, 31, 23))
        bfastDel.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(":/images/deleteW.png", QSize(), QIcon.Normal, QIcon.Off)
        bfastDel.setIcon(icon8)
        bfastDel.setCheckable(True)
        bfastDel.setAutoExclusive(True)
        bfastAdd = QPushButton(Bfast, clicked = lambda: add_item_Bfast(date_today))
        bfastAdd.setObjectName("bfastAdd")
        bfastAdd.setGeometry(QRect(200, 20, 31, 23))
        bfastAdd.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(":/images/addW.png", QSize(), QIcon.Normal, QIcon.Off)
        bfastAdd.setIcon(icon9)
        bfastAdd.setCheckable(True)
        bfastAdd.setAutoExclusive(True)
        bfastDaftar = QPushButton(Bfast)
        bfastDaftar.setObjectName("bfastDaftar")
        bfastDaftar.setGeometry(QRect(160, 20, 31, 23))
        bfastDaftar.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(":/images/content_paste.png", QSize(), QIcon.Normal, QIcon.Off)
        bfastDaftar.setIcon(icon10)
        bfastDaftar.setCheckable(True)
        bfastDaftar.setAutoExclusive(True)
        bfastMod = QPushButton(Bfast)
        bfastMod.setObjectName("bfastMod")
        bfastMod.setGeometry(QRect(240, 20, 31, 23))
        bfastMod.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(":/images/modifyW.png", QSize(), QIcon.Normal, QIcon.Off)
        bfastMod.setIcon(icon11)
        bfastMod.setCheckable(True)
        bfastMod.setAutoExclusive(True)

        horizontalLayout_8.addWidget(Bfast)

        Lunch = QWidget(layoutWidget)
        Lunch.setObjectName("Lunch")
        listWidget_Lunch = QListWidget(Lunch)
        listWidget_Lunch.setObjectName("listWidget_Lunch")
        listWidget_Lunch.setGeometry(QRect(20, 110, 291, 200))
        listWidget_Lunch.setStyleSheet("font: 12pt 'Century Gothic'; color:black;")
        label_Lunch = QLabel(Lunch)
        label_Lunch.setObjectName("label_Lunch")
        label_Lunch.setGeometry(QRect(20, 50, 291, 61))
        label_Lunch.setFont(font3)
        label_Lunch.setStyleSheet("background-color:#fce8e9;\n"
"color:#FF5E6A;\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;")
        label_Lunch.setAlignment(Qt.AlignCenter)
        widget_8 = QWidget(Lunch)
        widget_8.setObjectName("widget_8")
        widget_8.setGeometry(QRect(30, 10, 221, 41))
        lunchDel = QPushButton(Lunch)
        lunchDel.setObjectName("lunchDel")
        lunchDel.setGeometry(QRect(270, 20, 31, 23))
        lunchDel.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        lunchDel.setIcon(icon8)
        lunchDel.setCheckable(True)
        lunchDel.setAutoExclusive(True)
        lunchDaftar = QPushButton(Lunch)
        lunchDaftar.setObjectName("lunchDaftar")
        lunchDaftar.setGeometry(QRect(150, 20, 31, 23))
        lunchDaftar.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        lunchDaftar.setIcon(icon10)
        lunchDaftar.setCheckable(True)
        lunchDaftar.setAutoExclusive(True)
        lunchAdd = QPushButton(Lunch, clicked = lambda: add_item_Lunch(date_today))
        lunchAdd.setObjectName("lunchAdd")
        lunchAdd.setGeometry(QRect(190, 20, 31, 23))
        lunchAdd.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        lunchAdd.setIcon(icon9)
        lunchAdd.setCheckable(True)
        lunchAdd.setAutoExclusive(True)
        lunchMod = QPushButton(Lunch)
        lunchMod.setObjectName("lunchMod")
        lunchMod.setGeometry(QRect(230, 20, 31, 23))
        lunchMod.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        lunchMod.setIcon(icon11)
        lunchMod.setCheckable(True)
        lunchMod.setAutoExclusive(True)

        horizontalLayout_8.addWidget(Lunch)

        Dinner = QWidget(layoutWidget)
        Dinner.setObjectName("Dinner")
        
        listWidget_Dinner = QListWidget(Dinner)
        listWidget_Dinner.setObjectName("listWidget_Dinner")
        listWidget_Dinner.setGeometry(QRect(10, 110, 291, 200))
        listWidget_Dinner.setStyleSheet("font: 12pt 'Century Gothic'; color:black;")
        label_Dinner = QLabel(Dinner)
        label_Dinner.setObjectName("label_Dinner")
        label_Dinner.setGeometry(QRect(10, 50, 291, 61))
        label_Dinner.setFont(font3)
        label_Dinner.setStyleSheet("background-color:#fce8e9;\n"
"color:#FF5E6A;\n"
"border-top-right-radius:15px;\n"
"border-top-left-radius:15px;")
        label_Dinner.setAlignment(Qt.AlignCenter)
        widget_9 = QWidget(Dinner)
        widget_9.setObjectName("widget_9")
        widget_9.setGeometry(QRect(10, 10, 221, 41))
        dinDel = QPushButton(Dinner)
        dinDel.setObjectName("dinDel")
        dinDel.setGeometry(QRect(260, 20, 31, 23))
        dinDel.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        dinDel.setIcon(icon8)
        dinDel.setCheckable(True)
        dinDel.setAutoExclusive(True)
        dinDaftar = QPushButton(Dinner)
        dinDaftar.setObjectName("dinDaftar")
        dinDaftar.setGeometry(QRect(140, 20, 31, 23))
        dinDaftar.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        dinDaftar.setIcon(icon10)
        dinDaftar.setCheckable(True)
        dinDaftar.setAutoExclusive(True)
        dinAdd = QPushButton(Dinner, clicked = lambda: add_item_Dinner(date_today))
        dinAdd.setObjectName("dinAdd")
        dinAdd.setGeometry(QRect(180, 20, 31, 23))
        dinAdd.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        dinAdd.setIcon(icon9)
        dinAdd.setCheckable(True)
        dinAdd.setAutoExclusive(True)
        dinMod = QPushButton(Dinner)
        dinMod.setObjectName("dinMod")
        dinMod.setGeometry(QRect(220, 20, 31, 23))
        dinMod.setStyleSheet("QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")
        dinMod.setIcon(icon11)
        dinMod.setCheckable(True)
        dinMod.setAutoExclusive(True)
        

        horizontalLayout_8.addWidget(Dinner)
        
        
# ADD FUNCTIONS TO BUTTON
        # ADD
        def add_item_Bfast(date_today):
                controller.add_meal_to_jadwalmakanan(date_today,"breakfast")
                stackedWidgetMenu.setCurrentIndex(1)
                
        
        def add_item_Lunch(date_today):
                controller.add_meal_to_jadwalmakanan(date_today,"lunch")
                controller.cursor.execute("SELECT * FROM jadwalmakanan")

                # # fetch all the rows from the result set
                rows = controller.cursor.fetchall()
                for row in rows:
                        print(row)
                stackedWidgetMenu.setCurrentIndex(2)
            
        def add_item_Dinner(date_today):
                controller.add_meal_to_jadwalmakanan(date_today,"dinner")
                controller.cursor.execute("SELECT * FROM jadwalmakanan")

                # # fetch all the rows from the result set
                rows = controller.cursor.fetchall()
                for row in rows:
                        print(row)
                stackedWidgetMenu.setCurrentIndex(3)

            
        
        # REMOVE
        def remove_selected_items_Bfast():
                selected_items = listWidget_Bfast.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to remove.")
                        return
                reply = QMessageBox.question(schedule, 'Confirm Removal', "Are you sure you want to remove the selected items?",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                        for item in selected_items:
                                listWidget_Bfast.takeItem(listWidget_Bfast.row(item))
                                deleted_item = controller.get_meal_by_name(item.text())
                                controller.delete_meal_from_jadwalmakanan(deleted_item.id_meal)
        
        def remove_selected_items_Lunch():
                selected_items = listWidget_Lunch.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to remove.")
                        return
                reply = QMessageBox.question(schedule, 'Confirm Removal', "Are you sure you want to remove the selected items?",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                        for item in selected_items:
                                listWidget_Lunch.takeItem(listWidget_Lunch.row(item))
                                deleted_item = controller.get_meal_by_name(item.text())
                                controller.delete_meal_from_jadwalmakanan(deleted_item.id_meal)
                    
        def remove_selected_items_Dinner():
                selected_items = listWidget_Dinner.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to remove.")
                        return
                reply = QMessageBox.question(schedule, 'Confirm Removal', "Are you sure you want to remove the selected items?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                        for item in selected_items:
                                listWidget_Dinner.takeItem(listWidget_Dinner.row(item))
                                deleted_item = controller.get_meal_by_name(item.text())
                                controller.delete_meal_from_jadwalmakanan(deleted_item.id_meal)

        # Modify
        def mod_item_Bfast():
                controller.revert_modify_meal()
                selected_items = listWidget_Bfast.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to modify.")
                        return
                
                for item in selected_items:
                        print(item.whatsThis())
                        controller.send_modify_meal((item.whatsThis()))
                        stackedWidgetMenu.setCurrentIndex(4)
        
        def mod_item_Lunch():
                controller.revert_modify_meal()
                selected_items = listWidget_Lunch.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to modify.")
                        return
                
                for item in selected_items:
                        print(item.whatsThis())
                        controller.send_modify_meal((item.whatsThis()))
                        stackedWidgetMenu.setCurrentIndex(5)
            
        def mod_item_Dinner():
                controller.revert_modify_meal()
                selected_items = listWidget_Dinner.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to modify.")
                        return
                
                for item in selected_items:
                        print(item.whatsThis())
                        controller.send_modify_meal((item.whatsThis()))
                        stackedWidgetMenu.setCurrentIndex(6)

        # RincianMeal
        def rincianbFast():
                selected_items = listWidget_Bfast.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to remove.")
                        return
                
                controller.update_selected_meal(selected_items[0].text())
                stackedWidgetMenu.setCurrentIndex(7)
        
        def rincianLunch():
                selected_items = listWidget_Lunch.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to remove.")
                        return
                
                controller.update_selected_meal(selected_items[0].text())
                stackedWidgetMenu.setCurrentIndex(7)
                        
        def rincianDinner():
                selected_items = listWidget_Dinner.selectedItems()
                if not selected_items:
                        QMessageBox.information(schedule, "No Selection", "Please select an item to remove.")
                        return
                controller.update_selected_meal(selected_items[0].text())
                stackedWidgetMenu.setCurrentIndex(7)
        
        
        # CLICKED ACTIONBfast
        bfastDel.clicked.connect(remove_selected_items_Bfast)
        lunchDel.clicked.connect(remove_selected_items_Lunch)
        dinDel.clicked.connect(remove_selected_items_Dinner)
        # bfastAdd.clicked.connect(add_item_Bfast(date_today))
        bfastMod.clicked.connect(mod_item_Bfast)
        lunchMod.clicked.connect(mod_item_Lunch)
        dinMod.clicked.connect(mod_item_Dinner)
        bfastDaftar.clicked.connect(rincianbFast)
        lunchDaftar.clicked.connect(rincianLunch)
        dinDaftar.clicked.connect(rincianDinner)
        # btnMon.clicked.connect(switchday(0))
        # btnTues.clicked.connect(switchday(1))
        # btnWed.clicked.connect(switchday(2))
        # btnThurs.clicked.connect(switchday(3))
        # btnFri.clicked.connect(switchday(4))
        # btnSat.clicked.connect(switchday(5))
        # btnSun.clicked.connect(switchday(6))

        
        
        # SET TEXT
        label_8.setText(QCoreApplication.translate("MainWindow", u"What are we eating today?", None))
        label_6.setText(QCoreApplication.translate("MainWindow", u"Hello, Nana!", None))
        btnMon.setText(QCoreApplication.translate("MainWindow", u"Monday", None))
        btnTues.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None))
        btnWed.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None))
        btnThurs.setText(QCoreApplication.translate("MainWindow", u"Thursday", None))
        btnFri.setText(QCoreApplication.translate("MainWindow", u"Friday", None))
        btnSat.setText(QCoreApplication.translate("MainWindow", u"Saturday", None))
        btnSun.setText(QCoreApplication.translate("MainWindow", u"Sunday", None))
        iconCalendar.setText("")
        labelDate.setText("DD-MM-YYYY")
        label_Bfast.setText(QCoreApplication.translate("MainWindow", u"Breakfast", None))
        bfastDel.setText("")
        bfastAdd.setText("")
        bfastDaftar.setText("")
        bfastMod.setText("")
        label_Lunch.setText(QCoreApplication.translate("MainWindow", u"Lunch", None))
        lunchDel.setText("")
        lunchDaftar.setText("")
        lunchAdd.setText("")
        lunchMod.setText("")
        dinDel.setText("")
        dinAdd.setText("")
        dinMod.setText("")
        dinDaftar.setText("")
        label_Dinner.setText(QCoreApplication.translate("MainWindow", u"Dinner", None))

        return schedule