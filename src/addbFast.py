from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from controller.controller import *
     
def create_bfast(parent, stackedWidgetMenu):
        db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
        controller = Controller(db_path)

        AddBfastWin = QWidget()
        AddBfastWin.setObjectName("AddBfastWin")
        verticalLayout_6 = QVBoxLayout(AddBfastWin)
        verticalLayout_6.setObjectName("verticalLayout_6")
        greetAddBfast = QLabel(AddBfastWin)
        greetAddBfast.setObjectName("greetAddBfast")
        font7 = QFont()
        font7.setFamilies(["Century Gothic"])
        font7.setPointSize(14)
        font7.setBold(True)
        greetAddBfast.setFont(font7)
        greetAddBfast.setStyleSheet("color: rgb(0, 143, 110);")

        verticalLayout_6.addWidget(greetAddBfast)

        verticalSpacer_7 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_6.addItem(verticalSpacer_7)

        labelMealBfast = QLabel(AddBfastWin)
        labelMealBfast.setObjectName("labelMealBfast")
        font8 = QFont()
        font8.setFamilies(["Century Gothic"])
        font8.setPointSize(10)
        labelMealBfast.setFont(font8)
        labelMealBfast.setStyleSheet("color: rgb(126, 126, 126);")

        verticalLayout_6.addWidget(labelMealBfast)

        lineEdit_MealBfast = QLineEdit(AddBfastWin)
        lineEdit_MealBfast.setObjectName("lineEdit_MealBfast")
        lineEdit_MealBfast.setMinimumSize(QSize(0, 30))
        lineEdit_MealBfast.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                         "border-radius:10px;\n")

        verticalLayout_6.addWidget(lineEdit_MealBfast)

        verticalSpacer_6 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_6.addItem(verticalSpacer_6)

        labelDescBfast = QLabel(AddBfastWin)
        labelDescBfast.setObjectName("labelDescBfast")
        labelDescBfast.setFont(font8)
        labelDescBfast.setStyleSheet("color: rgb(126, 126, 126);")

        verticalLayout_6.addWidget(labelDescBfast)

        lineEdit_DescBfast = QLineEdit(AddBfastWin)
        lineEdit_DescBfast.setObjectName("lineEdit_DescBfast")
        lineEdit_DescBfast.setMinimumSize(QSize(0, 30))
        lineEdit_DescBfast.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                          "border-radius:10px;")

        verticalLayout_6.addWidget(lineEdit_DescBfast)

        verticalSpacer_5 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_6.addItem(verticalSpacer_5)

        labelRecipeBfast = QLabel(AddBfastWin)
        labelRecipeBfast.setObjectName("labelRecipeBfast")
        labelRecipeBfast.setFont(font8)
        labelRecipeBfast.setStyleSheet("color: rgb(126, 126, 126);")

        verticalLayout_6.addWidget(labelRecipeBfast)

        textEdit_RecipeBfast = QTextEdit(AddBfastWin)
        textEdit_RecipeBfast.setObjectName("textEdit_RecipeBfast")
        textEdit_RecipeBfast.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                            "border-radius:10px;")

        verticalLayout_6.addWidget(textEdit_RecipeBfast)

        verticalSpacer_3 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_6.addItem(verticalSpacer_3)

        labelIngredBfast = QLabel(AddBfastWin)
        labelIngredBfast.setObjectName("labelIngredBfast")
        labelIngredBfast.setFont(font8)
        labelIngredBfast.setStyleSheet("color: rgb(126, 126, 126);")

        verticalLayout_6.addWidget(labelIngredBfast)

        textEdit_IngredBfast = QTextEdit(AddBfastWin)
        textEdit_IngredBfast.setObjectName("textEdit_IngredBfast")
        textEdit_IngredBfast.setStyleSheet("background-color: rgb(213, 213, 213);\n"
                                            "border-radius:10px;")

        verticalLayout_6.addWidget(textEdit_IngredBfast)

        verticalSpacer_4 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_6.addItem(verticalSpacer_4)

        groupbtnSaveBackBfast = QWidget(AddBfastWin)
        groupbtnSaveBackBfast.setObjectName("groupbtnSaveBackBfast")
        horizontalLayout_9 = QHBoxLayout(groupbtnSaveBackBfast)
        horizontalLayout_9.setObjectName("horizontalLayout_9")
        horizontalSpacer_3 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        horizontalLayout_9.addItem(horizontalSpacer_3)

        btnSaveAddBfast = QPushButton(groupbtnSaveBackBfast)
        btnSaveAddBfast.setObjectName("btnSaveAddBfast")
        btnSaveAddBfast.setMinimumSize(QSize(70, 35))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(10)
        font2.setBold(True)
        btnSaveAddBfast.setFont(font2)
        btnSaveAddBfast.setStyleSheet("QPushButton{\n"
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
        btnSaveAddBfast.setCheckable(True)
        btnSaveAddBfast.setAutoExclusive(True)

        horizontalLayout_9.addWidget(btnSaveAddBfast)

        btnbBackAddBfast = QPushButton(groupbtnSaveBackBfast)
        btnbBackAddBfast.setObjectName("btnbBackAddBfast")
        btnbBackAddBfast.setMinimumSize(QSize(70, 35))
        btnbBackAddBfast.setFont(font2)
        btnbBackAddBfast.setStyleSheet("QPushButton{\n"
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
        btnbBackAddBfast.setCheckable(True)
        btnbBackAddBfast.setAutoExclusive(True)

        horizontalLayout_9.addWidget(btnbBackAddBfast)

        horizontalSpacer_4 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        horizontalLayout_9.addItem(horizontalSpacer_4)


        verticalLayout_6.addWidget(groupbtnSaveBackBfast)

        #verticalLayout_7.addLayout(verticalLayout_6)
        greetAddBfast.setText(QCoreApplication.translate("MainWindow", "What should we have for Breakfast ?", None))
        labelMealBfast.setText(QCoreApplication.translate("MainWindow", "Meal Name", None))
        labelDescBfast.setText(QCoreApplication.translate("MainWindow", "Description", None))
        labelRecipeBfast.setText(QCoreApplication.translate("MainWindow", "Recipe", None))
        labelIngredBfast.setText(QCoreApplication.translate("MainWindow", "Ingredients", None))
        btnSaveAddBfast.setText(QCoreApplication.translate("MainWindow", "SAVE", None))
        btnbBackAddBfast.setText(QCoreApplication.translate("MainWindow", "BACK", None))

        def add_Bfast():
            meal_name = lineEdit_MealBfast.text()
            meal_desc = lineEdit_DescBfast.text()
            meal_recipe = textEdit_RecipeBfast.toPlainText()
            ingredients_text = textEdit_IngredBfast.toPlainText()
            
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
                QMessageBox.warning(AddBfastWin, "Input Error", "Please fill all fields")
                return
            
            # schedulePage = stackedWidgetMenu.widget(0)
            # schedulePage.update()
                
            stackedWidgetMenu.setCurrentIndex(0)

        def back_Bfast():
            stackedWidgetMenu.setCurrentIndex(0)

        # CLICKED ACTION
        btnbBackAddBfast.clicked.connect(back_Bfast)
        btnSaveAddBfast.clicked.connect(add_Bfast)


        return AddBfastWin