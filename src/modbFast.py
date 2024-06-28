from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from controller.controller import *
     
def create_modbFast(parent, stackedWidgetMenu):
    ModBfastWin = QWidget()
    ModBfastWin.setObjectName("ModBfastWin")
    verticalLayout_10 = QVBoxLayout(ModBfastWin)
    verticalLayout_10.setObjectName("verticalLayout_10")
    verticalLayout_Mod = QVBoxLayout()
    verticalLayout_Mod.setObjectName("verticalLayout_Mod")
    greetModBfast = QLabel(ModBfastWin)
    greetModBfast.setObjectName("greetModBfast")
    font4 = QFont()
    font4.setFamilies([u"Century Gothic"])
    font4.setPointSize(16)
    font4.setBold(True)
    greetModBfast.setFont(font4)
    greetModBfast.setStyleSheet("color: rgb(0, 143, 110);\n"
    "margin-bottom:30px;\n"
    "margin-top:20px;")

    verticalLayout_Mod.addWidget(greetModBfast)

    label_ModBfast = QLabel(ModBfastWin)
    label_ModBfast.setObjectName("label_ModBfast")
    font9 = QFont()
    font9.setFamilies(["Century Gothic"])
    font9.setPointSize(12)
    font9.setBold(True)
    label_ModBfast.setFont(font9)
    label_ModBfast.setStyleSheet("background-color:#fce8e9;\n"
    "color:#FF5E6A;\n"
    "border-top-right-radius:15px;\n"
    "border-top-left-radius:15px;")
    label_ModBfast.setMargin(20)
    label_ModBfast.setIndent(10)

    verticalLayout_Mod.addWidget(label_ModBfast)

    db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
    controller = Controller(db_path)
    meals = controller.get_all_meal()
    
    listWidget_ModBfast = QListWidget(ModBfastWin)
    listWidget_ModBfast.setObjectName("listWidget_ModBfast")
    listWidget_ModBfast.setMinimumSize(QSize(0, 300))
    listWidget_ModBfast.setStyleSheet("color:#FF5E6A;\n")
    font5 = QFont()
    font5.setFamilies([u"Century Gothic"])
    listWidget_ModBfast.setFont(font5)

    for meal in meals:
        item = QListWidgetItem(meal.name_meal)
        listWidget_ModBfast.addItem(item)

    verticalLayout_Mod.addWidget(listWidget_ModBfast)

    groupbtnChooseBfast = QWidget(ModBfastWin)
    groupbtnChooseBfast.setObjectName("groupbtnChooseBfast")
    horizontalLayout_12 = QHBoxLayout(groupbtnChooseBfast)
    horizontalLayout_12.setObjectName("horizontalLayout_12")
    horizontalSpacer_9 = QSpacerItem(351, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_12.addItem(horizontalSpacer_9)

    btnChooseBfast = QPushButton(groupbtnChooseBfast)
    btnChooseBfast.setObjectName("btnChooseBfast")
    btnChooseBfast.setMinimumSize(QSize(100, 35))
    font2 = QFont()
    font2.setFamilies([u"Century Gothic"])
    font2.setPointSize(10)
    font2.setBold(True)
    btnChooseBfast.setFont(font2)
    btnChooseBfast.setStyleSheet("QPushButton{\n"
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
    btnChooseBfast.setCheckable(True)
    btnChooseBfast.setAutoExclusive(True)

    horizontalLayout_12.addWidget(btnChooseBfast)

    btnbBackModBfast = QPushButton(groupbtnChooseBfast)
    btnbBackModBfast.setObjectName("btnbBackModBfast")
    btnbBackModBfast.setMinimumSize(QSize(100, 35))
    btnbBackModBfast.setFont(font2)
    btnbBackModBfast.setStyleSheet("QPushButton{\n"
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
    btnbBackModBfast.setCheckable(True)
    btnbBackModBfast.setAutoExclusive(True)

    horizontalLayout_12.addWidget(btnbBackModBfast)

    horizontalSpacer_10 = QSpacerItem(351, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_12.addItem(horizontalSpacer_10)

    verticalLayout_Mod.addWidget(groupbtnChooseBfast)

    verticalLayout_10.addLayout(verticalLayout_Mod)

    greetModBfast.setText(QCoreApplication.translate("MainWindow", "Choose meal to replace!", None))
    label_ModBfast.setText(QCoreApplication.translate("MainWindow", "List of Meal", None))
    btnChooseBfast.setText(QCoreApplication.translate("MainWindow", "CHOOSE", None))
    btnbBackModBfast.setText(QCoreApplication.translate("MainWindow", "BACK", None))

    def back_modBFast():
        stackedWidgetMenu.setCurrentIndex(0)
    

    def choose_item_Bfast():
        selected_items = listWidget_ModBfast.selectedItems()
        if not selected_items:
            QMessageBox.information(ModBfastWin, "No Selection", "Please select an item to replace.")
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
    btnbBackModBfast.clicked.connect(back_modBFast)
    btnChooseBfast.clicked.connect(choose_item_Bfast)

    return ModBfastWin