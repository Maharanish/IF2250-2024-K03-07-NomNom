from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from controller.controller import *

def create_dinner(parent, stackedWidgetMenu):
    db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
    controller = Controller(db_path)

    AddDinWin = QWidget()
    AddDinWin.setObjectName("AddDinWin")
    verticalLayout_8 = QVBoxLayout(AddDinWin)
    verticalLayout_8.setObjectName("verticalLayout_8")
    greetAddDin = QLabel(AddDinWin)
    greetAddDin.setObjectName("greetAddDin")
    font7 = QFont()
    font7.setFamilies([u"Century Gothic"])
    font7.setPointSize(14)
    font7.setBold(True)
    greetAddDin.setFont(font7)
    greetAddDin.setStyleSheet("color: rgb(0, 143, 110);")

    verticalLayout_8.addWidget(greetAddDin)

    verticalSpacer_16 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_8.addItem(verticalSpacer_16)

    labelMealDin = QLabel(AddDinWin)
    labelMealDin.setObjectName("labelMealDin")
    font8 = QFont()
    font8.setFamilies([u"Century Gothic"])
    font8.setPointSize(10)
    labelMealDin.setFont(font8)
    labelMealDin.setStyleSheet("color: rgb(126, 126, 126);")

    verticalLayout_8.addWidget(labelMealDin)

    lineEdit_MealDin = QLineEdit(AddDinWin)
    lineEdit_MealDin.setObjectName("lineEdit_MealDin")
    lineEdit_MealDin.setMinimumSize(QSize(0, 30))
    lineEdit_MealDin.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                    "border-radius:10px;")

    verticalLayout_8.addWidget(lineEdit_MealDin)

    verticalSpacer_14 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_8.addItem(verticalSpacer_14)

    labelDescDin = QLabel(AddDinWin)
    labelDescDin.setObjectName("labelDescDin")
    labelDescDin.setFont(font8)
    labelDescDin.setStyleSheet("color: rgb(126, 126, 126);")

    verticalLayout_8.addWidget(labelDescDin)

    lineEdit_DescDin = QLineEdit(AddDinWin)
    lineEdit_DescDin.setObjectName("lineEdit_DescDin")
    lineEdit_DescDin.setMinimumSize(QSize(0, 30))
    lineEdit_DescDin.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                    "border-radius:10px;")

    verticalLayout_8.addWidget(lineEdit_DescDin)

    verticalSpacer_17 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_8.addItem(verticalSpacer_17)

    labelRecipeDin = QLabel(AddDinWin)
    labelRecipeDin.setObjectName("labelRecipeDin")
    labelRecipeDin.setFont(font8)
    labelRecipeDin.setStyleSheet("color: rgb(126, 126, 126);")

    verticalLayout_8.addWidget(labelRecipeDin)

    textEdit_RecipeDin = QTextEdit(AddDinWin)
    textEdit_RecipeDin.setObjectName("textEdit_RecipeDin")
    textEdit_RecipeDin.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                    "border-radius:10px;")

    verticalLayout_8.addWidget(textEdit_RecipeDin)

    verticalSpacer_13 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_8.addItem(verticalSpacer_13)

    labelIngredDin = QLabel(AddDinWin)
    labelIngredDin.setObjectName("labelIngredDin")
    labelIngredDin.setFont(font8)
    labelIngredDin.setStyleSheet("color: rgb(126, 126, 126);")

    verticalLayout_8.addWidget(labelIngredDin)

    textEdit_IngredDin = QTextEdit(AddDinWin)
    textEdit_IngredDin.setObjectName("textEdit_IngredDin")
    textEdit_IngredDin.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                    "border-radius:10px;")

    verticalLayout_8.addWidget(textEdit_IngredDin)

    verticalSpacer_15 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_8.addItem(verticalSpacer_15)

    groupbtnSaveBackDin = QWidget(AddDinWin)
    groupbtnSaveBackDin.setObjectName("groupbtnSaveBackDin")
    horizontalLayout_11 = QHBoxLayout(groupbtnSaveBackDin)
    horizontalLayout_11.setObjectName("horizontalLayout_11")
    horizontalSpacer_7 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_11.addItem(horizontalSpacer_7)

    btnSaveAddDin = QPushButton(groupbtnSaveBackDin)
    btnSaveAddDin.setObjectName("btnSaveAddDin")
    btnSaveAddDin.setMinimumSize(QSize(70, 35))
    font2 = QFont()
    font2.setFamilies([u"Century Gothic"])
    font2.setPointSize(10)
    font2.setBold(True)
    btnSaveAddDin.setFont(font2)
    btnSaveAddDin.setStyleSheet("QPushButton{\n"
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
    btnSaveAddDin.setCheckable(True)
    btnSaveAddDin.setAutoExclusive(True)

    horizontalLayout_11.addWidget(btnSaveAddDin)

    btnbBackAddDin = QPushButton(groupbtnSaveBackDin)
    btnbBackAddDin.setObjectName("btnbBackAddDin")
    btnbBackAddDin.setMinimumSize(QSize(70, 35))
    btnbBackAddDin.setFont(font2)
    btnbBackAddDin.setStyleSheet("QPushButton{\n"
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
    btnbBackAddDin.setCheckable(True)
    btnbBackAddDin.setAutoExclusive(True)

    horizontalLayout_11.addWidget(btnbBackAddDin)

    horizontalSpacer_8 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_11.addItem(horizontalSpacer_8)

    verticalLayout_8.addWidget(groupbtnSaveBackDin)
    greetAddDin.setText(QCoreApplication.translate("MainWindow", "What should we have for Dinner ?", None))
    labelMealDin.setText(QCoreApplication.translate("MainWindow", "Meal Name", None))
    labelDescDin.setText(QCoreApplication.translate("MainWindow", "Description", None))
    labelRecipeDin.setText(QCoreApplication.translate("MainWindow", "Recipe", None))
    labelIngredDin.setText(QCoreApplication.translate("MainWindow", "Ingredients", None))
    btnSaveAddDin.setText(QCoreApplication.translate("MainWindow", "SAVE", None))
    btnbBackAddDin.setText(QCoreApplication.translate("MainWindow", "BACK", None))

    def add_Din():
            meal_name = lineEdit_MealDin.text()
            meal_desc = lineEdit_DescDin.text()
            meal_recipe = textEdit_RecipeDin.toPlainText()
            ingredients_text = textEdit_IngredDin.toPlainText()
            
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
                QMessageBox.warning(AddDinWin, "Input Error", "Please fill all fields")
                return
            
            # schedulePage = stackedWidgetMenu.widget(0)
            # schedulePage.update()
                
            stackedWidgetMenu.setCurrentIndex(0)

    def back_Din():
        stackedWidgetMenu.setCurrentIndex(0)

    # CLICKED ACTION
    btnbBackAddDin.clicked.connect(back_Din)
    btnSaveAddDin.clicked.connect(add_Din)


    return AddDinWin