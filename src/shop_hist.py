from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QFont
from controller.controller import *

class ShoppingHist(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.verticalLayout_6 = QVBoxLayout(self)
        self.label_6 = QLabel(self)
        font3 = QFont()
        font3.setFamilies(["Century Gothic"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet("color: rgb(0, 143, 110);")
        self.label_6.setText("Hello, Nana!")

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_8 = QLabel(self)
        font4 = QFont()
        font4.setFamilies(["Century Gothic"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet("color: rgb(0, 143, 110);")
        self.label_8.setText("Here is your shopping history!")

        self.verticalLayout_6.addWidget(self.label_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalSpacer_3 = QSpacerItem(538, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(":/images/deleteW.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setText("Remove")
        self.horizontalLayout_5.addWidget(self.pushButton_2)

        refreshbtn1 = QPushButton(self)
        refreshbtn1.setObjectName(u"refreshbtn1")
        refreshbtn1.setStyleSheet(u"QPushButton{\n"
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
        
        refreshbtn1.setText("Refresh")
        refreshbtn1.setCheckable(True)
        self.horizontalLayout_5.addWidget(refreshbtn1)

        def remove_selected_items():
            selected_items = self.listWidget_2.selectedItems()
            if not selected_items:
                QMessageBox.information(self, "No Selection", "Please select an item to remove.")
                return
            reply = QMessageBox.question(self, 'Confirm Removal', "Are you sure you want to remove the selected items?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                for item in selected_items:
                    self.listWidget_2.takeItem(self.listWidget_2.row(item))
                    controller.update_status_shoppinghistory_to_default(selected_items[0].text())
            

        self.pushButton_2.clicked.connect(remove_selected_items)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.label_10 = QLabel(self)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet("background-color:#fce8e9;\n"
                                    "color:#FF5E6A;\n"
                                    "border-top-right-radius:15px;\n"
                                    "border-top-left-radius:15px;\n"
                                    "height:50px;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setMargin(10)
        self.label_10.setText("Ingredients")

        self.verticalLayout_6.addWidget(self.label_10)

        db_path= os.path.join(os.path.dirname(__file__), 'database', 'nomnom.db')
        controller = Controller(db_path)
        ingredients = controller.get_all_shopping_history()
        self.listWidget_2 = QListWidget(self)
        self.listWidget_2.setStyleSheet("font: 12pt \"Century Gothic\";\n"
                                        "border-top-right-radius:15px;\n"
                                        "border-top-left-radius:15px;\n"
                                        "color: black")

        for ingredient in ingredients:
            print(ingredient.name_ingredient)
            print()
            item = QListWidgetItem(ingredient.name_ingredient)
            self.listWidget_2.addItem(item)
        self.verticalLayout_6.addWidget(self.listWidget_2)

        def refresh():
            self.listWidget_2.clear()
            ingredients = controller.get_all_shopping_history()
            for ingredient in ingredients:
                item = QListWidgetItem(ingredient.name_ingredient)
                self.listWidget_2.addItem(item)

        refreshbtn1.clicked.connect(refresh)

    def retranslateUi(self):
        self.label_6.setText("Hello, Nana!")
        self.label_8.setText("Here is your shopping history!")
        self.pushButton_2.setText("Remove")
        font3 = QFont()
        font3.setFamilies(["Century Gothic"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_10.setFont(font3)
        self.label_10.setText("Ingredients")