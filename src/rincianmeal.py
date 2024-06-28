from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from controller.controller import *
     
def create_rincianMeal(parent, stackedWidgetMenu):
    RincianMealWin = QWidget()
    RincianMealWin.setObjectName("RincianMealWin")
    verticalLayout_14 = QVBoxLayout(RincianMealWin)
    verticalLayout_14.setObjectName("verticalLayout_14")
    MealName = QLabel(RincianMealWin)
    MealName.setObjectName("MealName")
    font4 = QFont()
    font4.setFamilies([u"Century Gothic"])
    font4.setPointSize(16)
    font4.setBold(True)
    MealName.setFont(font4)
    MealName.setStyleSheet("color: rgb(0, 143, 110);\n"
    "margin-bottom:30px;\n"
    "margin-top:20px;")

    verticalLayout_14.addWidget(MealName)
    
    #ambil database
    db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
    controller = Controller(db_path)
    

    MealDesc = QLabel(RincianMealWin)
    MealDesc.setObjectName("MealDesc")
    font3 = QFont()
    font3.setFamilies([u"Century Gothic"])
    font3.setPointSize(11)
    font3.setBold(False)
    MealDesc.setFont(font3)
    MealDesc.setStyleSheet("color: rgb(0, 143, 110);\n"
    "margin-bottom:10px;")

    verticalLayout_14.addWidget(MealDesc)

    horizontalLayout_15 = QHBoxLayout()
    horizontalLayout_15.setObjectName("horizontalLayout_15")
    horizontalSpacer_17 = QSpacerItem(758, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_15.addItem(horizontalSpacer_17)

    btnAddToCart = QPushButton(RincianMealWin)
    btnAddToCart.setObjectName("btnAddToCart")
    btnAddToCart.setMinimumSize(QSize(100, 25))
    font2 = QFont()
    font2.setFamilies(["Century Gothic"])
    font2.setPointSize(10)
    font2.setBold(True)
    btnAddToCart.setFont(font2)
    btnAddToCart.setStyleSheet("QPushButton{\n"
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
    icon9.addFile(u":/images/addW.png", QSize(), QIcon.Normal, QIcon.Off)
    btnAddToCart.setIcon(icon9)
    btnAddToCart.setCheckable(True)
    btnAddToCart.setAutoExclusive(True)

    horizontalLayout_15.addWidget(btnAddToCart)

    verticalLayout_14.addLayout(horizontalLayout_15)

    horizontalLayout_16 = QHBoxLayout()
    horizontalLayout_16.setSpacing(50)
    horizontalLayout_16.setObjectName("horizontalLayout_16")
    verticalLayout_12 = QVBoxLayout()
    verticalLayout_12.setSpacing(0)
    verticalLayout_12.setObjectName("verticalLayout_12")
    label_MealRecipe = QLabel(RincianMealWin)
    label_MealRecipe.setObjectName("label_MealRecipe")
    font9 = QFont()
    font9.setFamilies([u"Century Gothic"])
    font9.setPointSize(12)
    font9.setBold(True)
    label_MealRecipe.setFont(font9)
    label_MealRecipe.setStyleSheet("background-color:#fce8e9;\n"
    "color:#FF5E6A;\n"
    "border-top-right-radius:15px;\n"
    "border-top-left-radius:15px;")
    label_MealRecipe.setAlignment(Qt.AlignCenter)
    label_MealRecipe.setMargin(20)
    label_MealRecipe.setIndent(0)

    verticalLayout_12.addWidget(label_MealRecipe)

    MealRecipe = QTextEdit(RincianMealWin)
    MealRecipe.setObjectName("MealRecipe")
    MealRecipe.setMinimumSize(QSize(0, 0))
    MealRecipe.setReadOnly(True)
    MealRecipe.setStyleSheet("color:black;\n")

    verticalLayout_12.addWidget(MealRecipe)

    horizontalLayout_16.addLayout(verticalLayout_12)

    verticalLayout_13 = QVBoxLayout()
    verticalLayout_13.setSpacing(0)
    verticalLayout_13.setObjectName("verticalLayout_13")
    label_MealIngred = QLabel(RincianMealWin)
    label_MealIngred.setObjectName("label_MealIngred")
    label_MealIngred.setFont(font9)
    label_MealIngred.setStyleSheet("background-color:#fce8e9;\n"
    "color:#FF5E6A;\n"
    "border-top-right-radius:15px;\n"
    "border-top-left-radius:15px;")
    label_MealIngred.setAlignment(Qt.AlignCenter)
    label_MealIngred.setMargin(20)
    label_MealIngred.setIndent(10)

    verticalLayout_13.addWidget(label_MealIngred)

    listWidget_MealIngred = QListWidget(RincianMealWin)

    listWidget_MealIngred.setObjectName("listWidget_MealIngred")
    listWidget_MealIngred.setStyleSheet("color:black;\n")

    verticalLayout_13.addWidget(listWidget_MealIngred)

    horizontalLayout_16.addLayout(verticalLayout_13)

    verticalLayout_14.addLayout(horizontalLayout_16)

    groupbtnBackMeal = QWidget(RincianMealWin)
    groupbtnBackMeal.setObjectName("groupbtnBackMeal")
    verticalLayout_18 = QVBoxLayout(groupbtnBackMeal)
    verticalLayout_18.setObjectName("verticalLayout_18")
    horizontalLayout_7 = QHBoxLayout()
    horizontalLayout_7.setObjectName("horizontalLayout_7")
    horizontalSpacer_15 = QSpacerItem(278, 32, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

    horizontalLayout_7.addItem(horizontalSpacer_15)

    btnbBackMeal = QPushButton(groupbtnBackMeal)
    btnbBackMeal.setObjectName("btnbBackMeal")
    btnbBackMeal.setMinimumSize(QSize(100, 35))
    btnbBackMeal.setFont(font2)
    btnbBackMeal.setStyleSheet("QPushButton{\n"
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
    btnbBackMeal.setCheckable(True)
    btnbBackMeal.setAutoExclusive(True)

    horizontalLayout_7.addWidget(btnbBackMeal)

    btnbBackMeal_2 = QPushButton(groupbtnBackMeal)
    btnbBackMeal_2.setObjectName("btnbBackMeal_2")
    btnbBackMeal_2.setMinimumSize(QSize(100, 35))
    btnbBackMeal_2.setFont(font2)
    btnbBackMeal_2.setStyleSheet("QPushButton{\n"
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
    btnbBackMeal_2.setCheckable(True)
    btnbBackMeal_2.setAutoExclusive(True)

    horizontalLayout_7.addWidget(btnbBackMeal_2)

    horizontalSpacer_16 = QSpacerItem(298, 32, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

    horizontalLayout_7.addItem(horizontalSpacer_16)

    verticalLayout_18.addLayout(horizontalLayout_7)

    verticalLayout_14.addWidget(groupbtnBackMeal)

    

    # MealName.setText(QCoreApplication.translate("MainWindow", meal.name_meal, None))
    # MealDesc.setText(QCoreApplication.translate("MainWindow", meal.description_meal, None))
    btnAddToCart.setText(QCoreApplication.translate("MainWindow", "Add to cart", None))
    label_MealRecipe.setText(QCoreApplication.translate("MainWindow", "Recipe", None))
    label_MealIngred.setText(QCoreApplication.translate("MainWindow", "Ingredients", None))
    btnbBackMeal.setText(QCoreApplication.translate("MainWindow", "BACK", None))
    btnbBackMeal_2.setText(QCoreApplication.translate("MainWindow", "REFRESH", None))

    meal = controller.get_all_selected_meal()
    # Add To Cart
    def addToCart():
            selected_items = listWidget_MealIngred.selectedItems()
            if not selected_items:
                QMessageBox.information(RincianMealWin, "No Selection", "Please select an ingredient to add.")
                return
            reply = QMessageBox.question(RincianMealWin, 'Confirm Removal', "Are you sure you want to add this ingredient?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                print(selected_items[0].text())
                controller.update_status_ingredients_to_shoppingcart(selected_items[0].text())
                
                    
    
    #controller.update_status_meal_to_default(meal.name_meal)
    def refresh():
        meal = controller.get_all_selected_meal()
        if meal:
            print(meal.name_meal)
            print()
            print(meal.id_meal)
        else:
            print("No meal found.")
            return RincianMealWin
        print("masuk")
        ingredients = controller.display_ingredient(meal.id_meal)
        for ingredient in ingredients:
            #print(ingredient.name_ingredient)
            item = QListWidgetItem(ingredient.name_ingredient)
            listWidget_MealIngred.addItem(item)
        MealName.setText(QCoreApplication.translate("MainWindow", meal.name_meal, None))
        MealDesc.setText(QCoreApplication.translate("MainWindow", meal.description_meal, None))
        MealRecipe.setText(QCoreApplication.translate("MainWindow", meal.recipe_meal, None))
        controller.update_status_meal_to_default(meal.name_meal)

    def back_rincianMeal():
        #controller.update_status_meal_to_default(meal.name_meal)
        listWidget_MealIngred.clear()
        stackedWidgetMenu.setCurrentIndex(0)
        


    # CLICKED ACTION
    btnbBackMeal.clicked.connect(back_rincianMeal)
    btnbBackMeal_2.clicked.connect(refresh)
    btnAddToCart.clicked.connect(addToCart)
    

    return RincianMealWin