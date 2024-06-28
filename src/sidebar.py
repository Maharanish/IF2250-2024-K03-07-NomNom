from cobapisah import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        
        self.icon_name_widget.setHidden(True)
        
        self.schedule_1.clicked.connect(self.switch_to_schedule)
        self.schedule_2.clicked.connect(self.switch_to_schedule)
        
        self.cart_1.clicked.connect(self.switch_to_shopcart)
        self.cart_2.clicked.connect(self.switch_to_shopcart)
        
        self.mealhist_1.clicked.connect(self.switch_to_mealhistory)
        self.mealhist_2.clicked.connect(self.switch_to_mealhistory)

        self.shophist_1.clicked.connect(self.switch_to_shophistory)
        self.shophist_2.clicked.connect(self.switch_to_shophistory)
       

    def switch_to_schedule(self):
        self.stackedWidgetMenu.setCurrentIndex(0)

    def switch_to_shopcart(self):
        self.stackedWidgetMenu.setCurrentIndex(8)

    def switch_to_mealhistory(self):
        self.stackedWidgetMenu.setCurrentIndex(9)

    def switch_to_shophistory(self):
        self.stackedWidgetMenu.setCurrentIndex(10)