from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from controller.controller import *
     
def create_modDinner(parent, stackedWidgetMenu):
    ModDinWin = QWidget()
    ModDinWin.setObjectName("ModDinWin")
    verticalLayout_11 = QVBoxLayout(ModDinWin)
    verticalLayout_11.setObjectName("verticalLayout_11")
    verticalLayout_Mod = QVBoxLayout()
    verticalLayout_Mod.setObjectName("verticalLayout_Mod")
    greetModDin_2 = QLabel(ModDinWin)
    greetModDin_2.setObjectName("greetModDin_2")
    font4 = QFont()
    font4.setFamilies([u"Century Gothic"])
    font4.setPointSize(16)
    font4.setBold(True)
    greetModDin_2.setFont(font4)
    greetModDin_2.setStyleSheet("color: rgb(0, 143, 110);\n"
    "margin-bottom:30px;\n"
    "margin-top:20px;")

    verticalLayout_11.addWidget(greetModDin_2)

    label_ModDin_2 = QLabel(ModDinWin)
    label_ModDin_2.setObjectName("label_ModDin_2")
    font9 = QFont()
    font9.setFamilies([u"Century Gothic"])
    font9.setPointSize(12)
    font9.setBold(True)
    label_ModDin_2.setFont(font9)
    label_ModDin_2.setStyleSheet("background-color:#fce8e9;\n"
    "color:#FF5E6A;\n"
    "border-top-right-radius:15px;\n"
    "border-top-left-radius:15px;")
    label_ModDin_2.setMargin(20)
    label_ModDin_2.setIndent(10)

    verticalLayout_11.addWidget(label_ModDin_2)

    db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
    controller = Controller(db_path)
    meals = controller.get_all_meal()

    listWidget_ModDin_2 = QListWidget(ModDinWin)
    listWidget_ModDin_2.setObjectName("listWidget_ModDin_2")
    listWidget_ModDin_2.setMinimumSize(QSize(0, 300))
    listWidget_ModDin_2.setStyleSheet("color:#FF5E6A;\n")
    font5 = QFont()
    font5.setFamilies([u"Century Gothic"])
    listWidget_ModDin_2.setFont(font5)

    for meal in meals:
        item = QListWidgetItem(meal.name_meal)
        listWidget_ModDin_2.addItem(item)

    verticalLayout_11.addWidget(listWidget_ModDin_2)

    groupbtnChooseDin_2 = QWidget(ModDinWin)
    groupbtnChooseDin_2.setObjectName("groupbtnChooseDin_2")
    horizontalLayout_14 = QHBoxLayout(groupbtnChooseDin_2)
    horizontalLayout_14.setObjectName("horizontalLayout_14")
    horizontalSpacer_13 = QSpacerItem(404, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_14.addItem(horizontalSpacer_13)

    btnChooseDin_2 = QPushButton(groupbtnChooseDin_2)
    btnChooseDin_2.setObjectName("btnChooseDin_2")
    btnChooseDin_2.setMinimumSize(QSize(100, 35))
    font2 = QFont()
    font2.setFamilies([u"Century Gothic"])
    font2.setPointSize(10)
    font2.setBold(True)
    btnChooseDin_2.setFont(font2)
    btnChooseDin_2.setStyleSheet("QPushButton{\n"
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
    btnChooseDin_2.setCheckable(True)
    btnChooseDin_2.setAutoExclusive(True)

    horizontalLayout_14.addWidget(btnChooseDin_2)

    btnbBackAddDin_2 = QPushButton(groupbtnChooseDin_2)
    btnbBackAddDin_2.setObjectName("btnbBackAddDin_2")
    btnbBackAddDin_2.setMinimumSize(QSize(100, 35))
    btnbBackAddDin_2.setFont(font2)
    btnbBackAddDin_2.setStyleSheet("QPushButton{\n"
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
    btnbBackAddDin_2.setCheckable(True)
    btnbBackAddDin_2.setAutoExclusive(True)

    horizontalLayout_14.addWidget(btnbBackAddDin_2)

    horizontalSpacer_14 = QSpacerItem(404, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_14.addItem(horizontalSpacer_14)

    verticalLayout_11.addWidget(groupbtnChooseDin_2)

    verticalLayout_11.addLayout(verticalLayout_Mod)

    greetModDin_2.setText(QCoreApplication.translate("MainWindow", "Choose meal to replace!", None))
    label_ModDin_2.setText(QCoreApplication.translate("MainWindow", "List of Meal", None))
    btnChooseDin_2.setText(QCoreApplication.translate("MainWindow", "CHOOSE", None))
    btnbBackAddDin_2.setText(QCoreApplication.translate("MainWindow", "BACK", None))

    def back_modDin():
        stackedWidgetMenu.setCurrentIndex(0)

    def choose_item_Din():
        selected_items = listWidget_ModDin_2.selectedItems()
        if not selected_items:
            QMessageBox.information(ModDinWin, "No Selection", "Please select an item to replace.")
            return

        selected_meal = controller.get_all_modify_meal()
        
        for item in selected_items:
            item_str = item.text()  
            selected = controller.get_meal_by_name(item_str)
            controller.update_meal_in_jadwal_makanan(selected_meal.id_meal, selected.id_meal)
            stackedWidgetMenu.setCurrentIndex(0)

        

        controller.cursor.execute("SELECT * FROM meal")
        c=controller.cursor
    
        # # fetch all the rows from the result set
        rows = controller.cursor.fetchall()
        for row in rows:
            print(row)
            
        c.execute("SELECT * FROM jadwal_makanan_has_meal")

        # # fetch all the rows from the result set
        rows = c.fetchall()
        for row in rows:
            print(row)
            

        c.execute("SELECT * FROM jadwalmakanan")

         # # fetch all the rows from the result set
        rows = c.fetchall()
        for row in rows:
            print(row)

    # CLICKED ACTION
    btnbBackAddDin_2.clicked.connect(back_modDin)
    btnChooseDin_2.clicked.connect(choose_item_Din)

    return ModDinWin