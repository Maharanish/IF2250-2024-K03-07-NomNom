from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


def create_Home(parent, stackedWidgetMenu):
    WelcomeWin = QWidget()
    WelcomeWin.setObjectName("WelcomeWin")
    verticalLayout_17 = QVBoxLayout(WelcomeWin)
    verticalLayout_17.setObjectName("verticalLayout_17")
    verticalLayout_16 = QVBoxLayout()
    verticalLayout_16.setObjectName("verticalLayout_16")
    verticalSpacer_18 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_16.addItem(verticalSpacer_18)

    horizontalLayout_17 = QHBoxLayout()
    horizontalLayout_17.setObjectName("horizontalLayout_17")
    horizontalSpacer_18 = QSpacerItem(218, 28, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_17.addItem(horizontalSpacer_18)

    verticalLayout_15 = QVBoxLayout()
    verticalLayout_15.setObjectName("verticalLayout_15")
    label_10 = QLabel(WelcomeWin)
    label_10.setObjectName("label_10")
    font10 = QFont()
    font10.setFamilies(["Century Gothic"])
    font10.setPointSize(25)
    font10.setBold(True)
    label_10.setFont(font10)
    label_10.setStyleSheet("color: rgb(0, 143, 110);")
    label_10.setAlignment(Qt.AlignCenter)

    verticalLayout_15.addWidget(label_10)

    label_11 = QLabel(WelcomeWin)
    label_11.setObjectName("label_11")
    font11 = QFont()
    font11.setFamilies(["Century Gothic"])
    font11.setPointSize(20)
    font11.setBold(False)
    label_11.setFont(font11)
    label_11.setStyleSheet("color: rgb(0, 143, 110);")
    label_11.setAlignment(Qt.AlignCenter)

    verticalLayout_15.addWidget(label_11)

    label_12 = QLabel(WelcomeWin)
    label_12.setObjectName("label_12")
    label_12.setPixmap(QPixmap(":/images/logo2.png"))
    label_12.setScaledContents(True)
    label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

    verticalLayout_15.addWidget(label_12)

    btnSaveAddBfast_2 = QPushButton(WelcomeWin)
    btnSaveAddBfast_2.setObjectName("btnSaveAddBfast_2")
    btnSaveAddBfast_2.setMinimumSize(QSize(70, 35))
    font2 = QFont()
    font2.setFamilies([u"Century Gothic"])
    font2.setPointSize(10)
    font2.setBold(True)
    btnSaveAddBfast_2.setFont(font2)
    btnSaveAddBfast_2.setStyleSheet(
        "QPushButton{"
        "background-color:#FF5E6A;"
        "border-radius:10px;"
        "color:white;"
        "}"
        "QPushButton:checked{"
        "border-style:solid;"
        "border-width:2px;"
        "border-color:#fce8e9;"
        "}"
    )
    btnSaveAddBfast_2.setCheckable(True)
    btnSaveAddBfast_2.setAutoExclusive(True)

    verticalLayout_15.addWidget(btnSaveAddBfast_2)

    horizontalLayout_17.addLayout(verticalLayout_15)

    horizontalSpacer_19 = QSpacerItem(218, 28, QSizePolicy.Expanding, QSizePolicy.Minimum)

    horizontalLayout_17.addItem(horizontalSpacer_19)

    verticalLayout_16.addLayout(horizontalLayout_17)

    verticalSpacer_19 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

    verticalLayout_16.addItem(verticalSpacer_19)

    verticalLayout_17.addLayout(verticalLayout_16)
    
    label_10.setText(QCoreApplication.translate("MainWindow", "Hello, Nana!", None))
    label_11.setText(QCoreApplication.translate("MainWindow", "how are you feeling today?", None))
    label_12.setText("")
    btnSaveAddBfast_2.setText(QCoreApplication.translate("MainWindow", "GET STARTED", None))
    
    def started(self):
        stackedWidgetMenu.setCurrentIndex(0)

    btnSaveAddBfast_2.clicked.connect(started)

    return WelcomeWin