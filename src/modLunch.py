from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from controller.controller import *
     
def create_modLunch(parent, stackedWidgetMenu):
    ModLunchWin = QWidget()
    ModLunchWin.setObjectName("ModLunchWin")
    verticalLayout_9 = QVBoxLayout(ModLunchWin)
    verticalLayout_9.setObjectName("verticalLayout_9")
    verticalLayout_Mod = QVBoxLayout()
    verticalLayout_Mod.setObjectName("verticalLayout_Mod")
    greetModLunch = QLabel(ModLunchWin)
    greetModLunch.setObjectName("greetModLunch")
    font4 = QFont()
    font4.setFamilies([u"Century Gothic"])
    font4.setPointSize(16)
    font4.setBold(True)
    greetModLunch.setFont(font4)
    greetModLunch.setStyleSheet("color: rgb(0, 143, 110);\n"
    "margin-bottom:30px;\n"
    "margin-top:20px;")

    verticalLayout_9.addWidget(greetModLunch)

    label_ModLunch = QLabel(ModLunchWin)
    label_ModLunch.setObjectName("label_ModLunch")
    font9 = QFont()
    font9.setFamilies([u"Century Gothic"])
    font9.setPointSize(12)
    font9.setBold(True)
    label_ModLunch.setFont(font9)
    label_ModLunch.setStyleSheet("background-color:#fce8e9;\n"
    "color:#FF5E6A;\n"
    "border-top-right-radius:15px;\n"
    "border-top-left-radius:15px;")
    label_ModLunch.setMargin(20)
    label_ModLunch.setIndent(10)

    verticalLayout_9.addWidget(label_ModLunch)

    db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
    controller = Controller(db_path)
    meals = controller.get_all_meal()
    listWidget_ModLunch = QListWidget(ModLunchWin)
    listWidget_ModLunch.setObjectName("listWidget_ModLunch")
    listWidget_ModLunch.setMinimumSize(QSize(0, 300))
    listWidget_ModLunch.setStyleSheet("color:#FF5E6A;\n")
    font5 = QFont()
    font5.setFamilies([u"Century Gothic"])
    listWidget_ModLunch.setFont(font5)

    for meal in meals:
        item = QListWidgetItem(meal.name_meal)
        listWidget_ModLunch.addItem(item)

    verticalLayout_9.addWidget(listWidget_ModLunch)

    groupbtnChooseLunch = QWidget(ModLunchWin)
    groupbtnChooseLunch.setObjectName("groupbtnChooseLunch")
    horizontalLayout_13 = QHBoxLayout(groupbtnChooseLunch)
    horizontalLayout_13.setObjectName("horizontalLayout_13")
    horizontalSpacer_11 = QSpacerItem(404, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_13.addItem(horizontalSpacer_11)

    btnChooseLunch = QPushButton(groupbtnChooseLunch)
    btnChooseLunch.setObjectName("btnChooseLunch")
    btnChooseLunch.setMinimumSize(QSize(100, 35))
    font2 = QFont()
    font2.setFamilies([u"Century Gothic"])
    font2.setPointSize(10)
    font2.setBold(True)
    btnChooseLunch.setFont(font2)
    btnChooseLunch.setStyleSheet("QPushButton{\n"
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
    btnChooseLunch.setCheckable(True)
    btnChooseLunch.setAutoExclusive(True)

    horizontalLayout_13.addWidget(btnChooseLunch)

    btnbBackModLunch = QPushButton(groupbtnChooseLunch)
    btnbBackModLunch.setObjectName("btnbBackModLunch")
    btnbBackModLunch.setMinimumSize(QSize(100, 35))
    btnbBackModLunch.setFont(font2)
    btnbBackModLunch.setStyleSheet("QPushButton{\n"
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
    btnbBackModLunch.setCheckable(True)
    btnbBackModLunch.setAutoExclusive(True)

    horizontalLayout_13.addWidget(btnbBackModLunch)

    horizontalSpacer_12 = QSpacerItem(404, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_13.addItem(horizontalSpacer_12)

    verticalLayout_9.addWidget(groupbtnChooseLunch)

    greetModLunch.setText(QCoreApplication.translate("MainWindow", "Choose meal to replace!", None))  
    label_ModLunch.setText(QCoreApplication.translate("MainWindow", "List of Meal", None))
    btnChooseLunch.setText(QCoreApplication.translate("MainWindow", "CHOOSE", None))
    btnbBackModLunch.setText(QCoreApplication.translate("MainWindow", "BACK", None))
    
    def back_modLunch():
        stackedWidgetMenu.setCurrentIndex(0)

    def choose_item_Lunch():
        selected_items = listWidget_ModLunch.selectedItems()
        if not selected_items:
            QMessageBox.information(ModLunchWin, "No Selection", "Please select an item to replace.")
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
    btnbBackModLunch.clicked.connect(back_modLunch)
    btnChooseLunch.clicked.connect(choose_item_Lunch)

    return ModLunchWin