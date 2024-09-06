# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pbr_reference.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_PbrReferenceWidget(object):
    def setupUi(self, PbrReferenceWidget):
        if not PbrReferenceWidget.objectName():
            PbrReferenceWidget.setObjectName(u"PbrReferenceWidget")
        PbrReferenceWidget.resize(1220, 645)
        PbrReferenceWidget.setMinimumSize(QSize(940, 560))
        PbrReferenceWidget.setStyleSheet(u"/* //////////////////// \n"
"MATERIAL REFERENCE */\n"
"#materialTopFrame { background-color: rgb(44, 49, 58); }\n"
"\n"
"#searchContainer {\n"
"	background-color: rgb(40, 42, 54);\n"
"	border-radius: 1em;\n"
"}\n"
"#searchContainer:hover {\n"
"	border: 2px solid rgb(50, 52, 64);\n"
"}\n"
"#searchContainer  .QLineEdit {\n"
"	color: #ffffff;\n"
"	background-color: rgb(40, 42, 54);\n"
"	border: none;\n"
"	\n"
"}\n"
"\n"
"#searchContainer .QPushButton {\n"
"	/* background-color: rgb(40, 42, 54); */\n"
"	border-radius: 12px;\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#searchContainer .QPushButton:hover { \n"
"	background-color: rgb(144, 149, 157); \n"
"	border-style: solid; \n"
"	color: rgb(170, 0, 0);\n"
"}\n"
"#searchContainer .QPushButton:pressed { \n"
"	background-color: rgb(139, 233, 253); \n"
"	border-style: solid; \n"
"}")
        self.verticalLayout_3 = QVBoxLayout(PbrReferenceWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.materialTopFrame = QFrame(PbrReferenceWidget)
        self.materialTopFrame.setObjectName(u"materialTopFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materialTopFrame.sizePolicy().hasHeightForWidth())
        self.materialTopFrame.setSizePolicy(sizePolicy)
        self.materialTopFrame.setMinimumSize(QSize(0, 80))
        self.verticalLayout_27 = QVBoxLayout(self.materialTopFrame)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.searchFrame = QFrame(self.materialTopFrame)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(0, 55))
        self.searchFrame.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(30, 10, 30, 10)
        self.searchContainer = QFrame(self.searchFrame)
        self.searchContainer.setObjectName(u"searchContainer")
        self.searchContainer.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.searchContainer.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.searchContainer)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(15, 0, 15, 0)
        self.searchBtn = QPushButton(self.searchContainer)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(24, 24))
        self.searchBtn.setMaximumSize(QSize(24, 24))
        self.searchBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchBtn.setStyleSheet(u"background-image: url(:/icons/resources/icons/cil-magnifying-glass.png);\n"
"border: none;\n"
"")
        self.searchBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.searchBtn)

        self.searchLineEdit = QLineEdit(self.searchContainer)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setEnabled(False)
        self.searchLineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_13.addWidget(self.searchLineEdit)

        self.cancelSearchBtn = QPushButton(self.searchContainer)
        self.cancelSearchBtn.setObjectName(u"cancelSearchBtn")
        self.cancelSearchBtn.setMinimumSize(QSize(24, 24))
        self.cancelSearchBtn.setMaximumSize(QSize(24, 24))
        self.cancelSearchBtn.setStyleSheet(u"background-image: url(:/icons/resources/icons/icon_close_24.svg);\n"
"border: none;")
        self.cancelSearchBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_13.addWidget(self.cancelSearchBtn)


        self.horizontalLayout_12.addWidget(self.searchContainer)


        self.verticalLayout_27.addWidget(self.searchFrame)

        self.filterFrame = QFrame(self.materialTopFrame)
        self.filterFrame.setObjectName(u"filterFrame")
        self.filterFrame.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_6 = QHBoxLayout(self.filterFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout_27.addWidget(self.filterFrame)


        self.verticalLayout_3.addWidget(self.materialTopFrame)

        self.materialBotFrame = QWidget(PbrReferenceWidget)
        self.materialBotFrame.setObjectName(u"materialBotFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.materialBotFrame.sizePolicy().hasHeightForWidth())
        self.materialBotFrame.setSizePolicy(sizePolicy1)
        self.verticalLayout_26 = QVBoxLayout(self.materialBotFrame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.matLabel = QLabel(self.materialBotFrame)
        self.matLabel.setObjectName(u"matLabel")
        self.matLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.matLabel)


        self.verticalLayout_3.addWidget(self.materialBotFrame)


        self.retranslateUi(PbrReferenceWidget)

        QMetaObject.connectSlotsByName(PbrReferenceWidget)
    # setupUi

    def retranslateUi(self, PbrReferenceWidget):
        PbrReferenceWidget.setWindowTitle(QCoreApplication.translate("PbrReferenceWidget", u"Form", None))
        self.searchBtn.setText("")
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("PbrReferenceWidget", u"Search", None))
        self.cancelSearchBtn.setText("")
        self.matLabel.setText(QCoreApplication.translate("PbrReferenceWidget", u"Material Reference Page", None))
    # retranslateUi

