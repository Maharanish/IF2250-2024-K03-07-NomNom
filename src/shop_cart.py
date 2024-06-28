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
    QWidget,QMessageBox)

from controller.controller import *

def create_shop_cart(parent):
    shop_cart = QWidget(parent)
    shop_cart.setObjectName("shop_cart")
    
    verticalLayout_5 = QVBoxLayout(shop_cart)
    verticalLayout_5.setObjectName("verticalLayout_5")
    
    label_5 = QLabel(shop_cart)
    label_5.setObjectName("label_5")
    font3 = QFont()
    font3.setFamilies(["Century Gothic"])
    font3.setPointSize(16)
    font3.setBold(True)
    label_5.setFont(font3)
    label_5.setStyleSheet("color: rgb(0, 143, 110);")
    verticalLayout_5.addWidget(label_5)

    label_7 = QLabel(shop_cart)
    label_7.setObjectName("label_7")
    font4 = QFont()
    font4.setFamilies(["Century Gothic"])
    font4.setPointSize(11)
    font4.setBold(False)
    label_7.setFont(font4)
    label_7.setStyleSheet("color: rgb(0, 143, 110);")
    verticalLayout_5.addWidget(label_7)

    horizontalLayout_4 = QHBoxLayout()
    horizontalLayout_4.setObjectName("horizontalLayout_4")
    horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
    horizontalSpacer_2 = QSpacerItem(538, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    horizontalLayout_4.addItem(horizontalSpacer_2)

    pushButton = QPushButton(shop_cart)
    pushButton.setObjectName("pushButton")
    pushButton.setStyleSheet("QPushButton{\n"
                             "background-color:#FF5E6A;\n"
                             "border-radius:10px;\n"
                             "color:white;\n"
                             "height:35px;\n"
                             "width:100px\n"
                             "}\n"
                             "QPushButton:checked{\n"
                             "border-style:solid;\n"
                             "border-width:2px;\n"
                             "border-color:#fce8e9;\n"
                             "}")
    icon = QIcon()
    icon.addFile(":/images/deleteW.png", QSize(), QIcon.Normal, QIcon.Off)
    pushButton.setIcon(icon)
    pushButton.setCheckable(True)
    horizontalLayout_4.addWidget(pushButton)
    verticalLayout_5.addLayout(horizontalLayout_4)

    refreshbtn = QPushButton(shop_cart)
    refreshbtn.setObjectName(u"refreshbtn")
    refreshbtn.setStyleSheet(u"QPushButton{\n"
"background-color:#FF5E6A;\n"
"border-radius:10px;\n"
"color:white;\n"
"height:35px;\n"
"width:100px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#fce8e9;\n"
"}")

    
    refreshbtn.setText("Refresh")
    refreshbtn.setCheckable(True)
    horizontalLayout_4.addWidget(refreshbtn)

    label_9 = QLabel(shop_cart)
    label_9.setObjectName("label_9")
    label_9.setFont(font3)  # Reusing font3 for simplicity; adjust if a different font is needed
    label_9.setStyleSheet("background-color:#fce8e9;\n"
                          "color:#FF5E6A;\n"
                          "border-top-right-radius:15px;\n"
                          "border-top-left-radius:15px;\n"
                          "height:50px;")  # Fixed typo in 'height'
    label_9.setAlignment(Qt.AlignCenter)
    label_9.setMargin(10)
    verticalLayout_5.addWidget(label_9)

    db_path = os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
    controller = Controller(db_path)
    ingredients = controller.get_all_shopping_cart()
    listWidget = QListWidget(shop_cart)
    listWidget.setObjectName("listWidget")
    listWidget.setStyleSheet("font: 12pt 'Century Gothic';\n"
                             "color:black;\n"
                             "border-top-right-radius:15px;\n"
                             "border-top-left-radius:15px;")
   
    for ingredient in ingredients:
        item = QListWidgetItem(ingredient.name_ingredient)
        listWidget.addItem(item)
    verticalLayout_5.addWidget(listWidget)

    def remove_selected_items():
        selected_items = listWidget.selectedItems()
        if not selected_items:
            QMessageBox.information(shop_cart, "No Selection", "Please select an item to remove.")
            return
        reply = QMessageBox.question(shop_cart, 'Confirm Removal', "Are you sure you want to remove the selected items?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            for item in selected_items:
                listWidget.takeItem(listWidget.row(item))
                controller.update_status_ingredients_to_shoppinghistory(item.text())
    
    def refresh():
        listWidget.clear()
        ingredients = controller.get_all_shopping_cart()
        for ingredient in ingredients:
            item = QListWidgetItem(ingredient.name_ingredient)
            listWidget.addItem(item)

    pushButton.clicked.connect(remove_selected_items)
    refreshbtn.clicked.connect(refresh)


    label_5.setText(QCoreApplication.translate("MainWindow", u"Hello, Nana!", None))
    label_7.setText(QCoreApplication.translate("MainWindow", u"Here is your shopping cart!", None))
    pushButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    label_9.setText(QCoreApplication.translate("MainWindow", u"Ingredients", None)) 

    return shop_cart