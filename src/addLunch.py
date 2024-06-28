from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from controller.controller import *
     
def create_lunch(parent, stackedWidgetMenu):
    db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
    controller = Controller(db_path)

    AddLunchWin = QWidget()
    AddLunchWin.setObjectName("AddLunchWin")
    verticalLayout_7 = QVBoxLayout(AddLunchWin)
    verticalLayout_7.setObjectName("verticalLayout_7")
    greetAddLunch = QLabel(AddLunchWin)
    greetAddLunch.setObjectName("greetAddLunch")
    font7 = QFont()
    font7.setFamilies([u"Century Gothic"])
    font7.setPointSize(14)
    font7.setBold(True)
    greetAddLunch.setFont(font7)
    greetAddLunch.setStyleSheet("color: rgb(0, 143, 110);")

    verticalLayout_7.addWidget(greetAddLunch)

    verticalSpacer_11 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_7.addItem(verticalSpacer_11)

    labelMealLunch = QLabel(AddLunchWin)
    labelMealLunch.setObjectName("labelMealLunch")
    font8 = QFont()
    font8.setFamilies([u"Century Gothic"])
    font8.setPointSize(10)
    labelMealLunch.setFont(font8)
    labelMealLunch.setStyleSheet("color: rgb(126, 126, 126);")

    verticalLayout_7.addWidget(labelMealLunch)

    lineEdit_MealLunch = QLineEdit(AddLunchWin)
    lineEdit_MealLunch.setObjectName("lineEdit_MealLunch")
    lineEdit_MealLunch.setMinimumSize(QSize(0, 30))
    lineEdit_MealLunch.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                    "border-radius:10px;")

    verticalLayout_7.addWidget(lineEdit_MealLunch)

    verticalSpacer_9 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_7.addItem(verticalSpacer_9)

    labelDescLunch = QLabel(AddLunchWin)
    labelDescLunch.setObjectName("labelDescLunch")
    labelDescLunch.setFont(font8)
    labelDescLunch.setStyleSheet("color: rgb(126, 126, 126);")

    verticalLayout_7.addWidget(labelDescLunch)

    lineEdit_DescLunch = QLineEdit(AddLunchWin)
    lineEdit_DescLunch.setObjectName("lineEdit_DescLunch")
    lineEdit_DescLunch.setMinimumSize(QSize(0, 30))
    lineEdit_DescLunch.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                    "border-radius:10px;")

    verticalLayout_7.addWidget(lineEdit_DescLunch)

    verticalSpacer_12 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_7.addItem(verticalSpacer_12)

    labelRecipeLunch = QLabel(AddLunchWin)
    labelRecipeLunch.setObjectName("labelRecipeLunch")
    labelRecipeLunch.setFont(font8)
    labelRecipeLunch.setStyleSheet("color: rgb(126, 126, 126);")

    verticalLayout_7.addWidget(labelRecipeLunch)

    textEdit_RecipeLunch = QTextEdit(AddLunchWin)
    textEdit_RecipeLunch.setObjectName("textEdit_RecipeLunch")
    textEdit_RecipeLunch.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                        "border-radius:10px;")

    verticalLayout_7.addWidget(textEdit_RecipeLunch)

    verticalSpacer_8 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_7.addItem(verticalSpacer_8)

    labelIngredLunch = QLabel(AddLunchWin)
    labelIngredLunch.setObjectName("labelIngredLunch")
    labelIngredLunch.setFont(font8)
    labelIngredLunch.setStyleSheet("color: rgb(126, 126, 126);")

    verticalLayout_7.addWidget(labelIngredLunch)

    textEdit_IngredLunch = QTextEdit(AddLunchWin)
    textEdit_IngredLunch.setObjectName("textEdit_IngredLunch")
    textEdit_IngredLunch.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                        "border-radius:10px;")

    verticalLayout_7.addWidget(textEdit_IngredLunch)

    verticalSpacer_10 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_7.addItem(verticalSpacer_10)

    groupbtnSaveBackLunch = QWidget(AddLunchWin)
    groupbtnSaveBackLunch.setObjectName("groupbtnSaveBackLunch")
    horizontalLayout_10 = QHBoxLayout(groupbtnSaveBackLunch)
    horizontalLayout_10.setObjectName("horizontalLayout_10")
    horizontalSpacer_5 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_10.addItem(horizontalSpacer_5)

    btnSaveAddLunch = QPushButton(groupbtnSaveBackLunch)
    btnSaveAddLunch.setObjectName("btnSaveAddLunch")
    btnSaveAddLunch.setMinimumSize(QSize(70, 35))
    font2 = QFont()
    font2.setFamilies([u"Century Gothic"])
    font2.setPointSize(10)
    font2.setBold(True)
    btnSaveAddLunch.setFont(font2)
    btnSaveAddLunch.setStyleSheet("QPushButton{\n"
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
    btnSaveAddLunch.setCheckable(True)
    btnSaveAddLunch.setAutoExclusive(True)

    horizontalLayout_10.addWidget(btnSaveAddLunch)

    btnbBackAddLunch = QPushButton(groupbtnSaveBackLunch)
    btnbBackAddLunch.setObjectName("btnbBackAddLunch")
    btnbBackAddLunch.setMinimumSize(QSize(70, 35))
    btnbBackAddLunch.setFont(font2)
    btnbBackAddLunch.setStyleSheet("QPushButton{\n"
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
    btnbBackAddLunch.setCheckable(True)
    btnbBackAddLunch.setAutoExclusive(True)

    horizontalLayout_10.addWidget(btnbBackAddLunch)

    horizontalSpacer_6 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_10.addItem(horizontalSpacer_6)


    verticalLayout_7.addWidget(groupbtnSaveBackLunch)

    greetAddLunch.setText(QCoreApplication.translate("MainWindow", "What should we have for Lunch ?", None))
    labelMealLunch.setText(QCoreApplication.translate("MainWindow", "Meal Name", None))
    labelDescLunch.setText(QCoreApplication.translate("MainWindow", "Description", None))
    labelRecipeLunch.setText(QCoreApplication.translate("MainWindow", "Recipe", None))
    labelIngredLunch.setText(QCoreApplication.translate("MainWindow", "Ingredients", None))
    btnSaveAddLunch.setText(QCoreApplication.translate("MainWindow", "SAVE", None))
    btnbBackAddLunch.setText(QCoreApplication.translate("MainWindow", "BACK", None))

    def add_Lunch():
            meal_name = lineEdit_MealLunch.text()
            meal_desc = lineEdit_DescLunch.text()
            meal_recipe = textEdit_RecipeLunch.toPlainText()
            ingredients_text = textEdit_IngredLunch.toPlainText()
            
            controller.save_meal(meal_name,meal_desc,meal_recipe,ingredients_text)
            # controller.cursor.execute("SELECT * FROM meal")
            # c=controller.cursor

            # # # fetch all the rows from the result set
            # rows = controller.cursor.fetchall()
            # for row in rows:
            #     print(row)
            
            # c.execute("SELECT * FROM jadwal_makanan_has_meal")

            # # # fetch all the rows from the result set
            # rows = c.fetchall()
            # for row in rows:
            #     print(row)
            

            # c.execute("SELECT * FROM jadwalmakanan")

            # # # fetch all the rows from the result set
            # rows = c.fetchall()
            # for row in rows:
            #     print(row)


            if not meal_name or not meal_desc or not meal_recipe or not ingredients_text:
                QMessageBox.warning(AddLunchWin, "Input Error", "Please fill all fields")
                return
            
            # schedulePage = stackedWidgetMenu.widget(0)
            # schedulePage.update()
                
            stackedWidgetMenu.setCurrentIndex(0)

    def back_Lunch():
        stackedWidgetMenu.setCurrentIndex(0)

    # CLICKED ACTION
    btnbBackAddLunch.clicked.connect(back_Lunch)
    btnSaveAddLunch.clicked.connect(add_Lunch)


    return AddLunchWin