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
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_PbrReferenceWidget(object):
    def setupUi(self, PbrReferenceWidget):
        if not PbrReferenceWidget.objectName():
            PbrReferenceWidget.setObjectName(u"PbrReferenceWidget")
        PbrReferenceWidget.resize(1220, 645)
        PbrReferenceWidget.setMinimumSize(QSize(0, 0))
        PbrReferenceWidget.setStyleSheet(u"/* ////////////////////////////////////////////////////////////\n"
"MATERIAL REFERENCE */\n"
".QLabel {\n"
"	\n"
"	font: 600 12pt \"Exo SemiBold\";\n"
"}\n"
"\n"
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
"}\n"
"\n"
"/* ///////////////////////////////"
                        "////////// \n"
"Material List Frame */\n"
"#materialPropFrame {\n"
"	background-color: #44475A;\n"
"	border-right: 4px solid #BD93F9;\n"
"}\n"
"\n"
"#propertiesTitleFrame {\n"
"	background-color: rgb(98, 114, 164);\n"
"	border-bottom: 0px solid #282A36;\n"
"	margin-right: 4px;\n"
"	padding-left: 10px;\n"
"}\n"
"#propertiesTitleFrame .QPushButton {\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	background-color: rgb(75, 75, 75);\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#propertiesTitleFrame .QPushButton:hover { \n"
"	background-color: rgb(90, 90, 90);\n"
"	border-style: solid; \n"
"	color: rgb(170, 0, 0);\n"
"}\n"
"#propertiesTitleFrame .QPushButton:pressed { \n"
"	background-color: #BD93F9; \n"
"	border-style: solid; \n"
"}")
        self.verticalLayout_11 = QVBoxLayout(PbrReferenceWidget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.PbrStackedWidget = QStackedWidget(PbrReferenceWidget)
        self.PbrStackedWidget.setObjectName(u"PbrStackedWidget")
        self.pbrMainPage = QWidget()
        self.pbrMainPage.setObjectName(u"pbrMainPage")
        self.verticalLayout = QVBoxLayout(self.pbrMainPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.materialTopFrame = QFrame(self.pbrMainPage)
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
        self.cancelSearchBtn.setStyleSheet(u"/* background-image : url(:/icons/resources/icons/icon_close_24.svg); */\n"
"image: url(:/icons/resources/icons/icon_close_24.svg);\n"
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


        self.verticalLayout.addWidget(self.materialTopFrame)

        self.materialBotFrame = QWidget(self.pbrMainPage)
        self.materialBotFrame.setObjectName(u"materialBotFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.materialBotFrame.sizePolicy().hasHeightForWidth())
        self.materialBotFrame.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.materialBotFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.materialPropFrame = QFrame(self.materialBotFrame)
        self.materialPropFrame.setObjectName(u"materialPropFrame")
        self.materialPropFrame.setMinimumSize(QSize(320, 0))
        self.materialPropFrame.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.materialPropFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.propertiesTitleFrame = QFrame(self.materialPropFrame)
        self.propertiesTitleFrame.setObjectName(u"propertiesTitleFrame")
        self.propertiesTitleFrame.setMinimumSize(QSize(0, 60))
        self.propertiesTitleFrame.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.propertiesTitleFrame)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.propsCloseButton = QPushButton(self.propertiesTitleFrame)
        self.propsCloseButton.setObjectName(u"propsCloseButton")
        self.propsCloseButton.setMinimumSize(QSize(24, 24))
        self.propsCloseButton.setMaximumSize(QSize(24, 24))
        self.propsCloseButton.setStyleSheet(u"/* background-image : url(:/icons/resources/icons/icon_close_24.svg); */\n"
"image: url(:/icons/resources/icons/icon_close_24.svg);")

        self.horizontalLayout.addWidget(self.propsCloseButton)

        self.propertiesLabel = QLabel(self.propertiesTitleFrame)
        self.propertiesLabel.setObjectName(u"propertiesLabel")
        sizePolicy.setHeightForWidth(self.propertiesLabel.sizePolicy().hasHeightForWidth())
        self.propertiesLabel.setSizePolicy(sizePolicy)
        self.propertiesLabel.setStyleSheet(u"")
        self.propertiesLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.propertiesLabel)


        self.verticalLayout_2.addWidget(self.propertiesTitleFrame)

        self.matLibraryListWidget = QListWidget(self.materialPropFrame)
        self.matLibraryListWidget.setObjectName(u"matLibraryListWidget")
        self.matLibraryListWidget.setMaximumSize(QSize(16777215, 16777215))
        self.matLibraryListWidget.setStyleSheet(u"")
        self.matLibraryListWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.matLibraryListWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.matLibraryListWidget.setAutoScroll(False)
        self.matLibraryListWidget.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.matLibraryListWidget.setAlternatingRowColors(False)
        self.matLibraryListWidget.setResizeMode(QListView.ResizeMode.Fixed)
        self.matLibraryListWidget.setUniformItemSizes(True)
        self.matLibraryListWidget.setSelectionRectVisible(True)
        self.matLibraryListWidget.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.matLibraryListWidget)


        self.horizontalLayout_2.addWidget(self.materialPropFrame)

        self.materialDashFrame = QFrame(self.materialBotFrame)
        self.materialDashFrame.setObjectName(u"materialDashFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.materialDashFrame.sizePolicy().hasHeightForWidth())
        self.materialDashFrame.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.materialDashFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.materialDashFrame)


        self.verticalLayout.addWidget(self.materialBotFrame)

        self.PbrStackedWidget.addWidget(self.pbrMainPage)
        self.splashPage = QWidget()
        self.splashPage.setObjectName(u"splashPage")
        self.verticalLayout_10 = QVBoxLayout(self.splashPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.splashFrame = QFrame(self.splashPage)
        self.splashFrame.setObjectName(u"splashFrame")
        self.verticalLayout_3 = QVBoxLayout(self.splashFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.splashFrame)

        self.PbrStackedWidget.addWidget(self.splashPage)

        self.verticalLayout_11.addWidget(self.PbrStackedWidget)


        self.retranslateUi(PbrReferenceWidget)

        self.PbrStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PbrReferenceWidget)
    # setupUi

    def retranslateUi(self, PbrReferenceWidget):
        PbrReferenceWidget.setWindowTitle(QCoreApplication.translate("PbrReferenceWidget", u"Form", None))
        self.searchBtn.setText("")
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("PbrReferenceWidget", u"Search", None))
        self.cancelSearchBtn.setText("")
        self.propsCloseButton.setText("")
        self.propertiesLabel.setText(QCoreApplication.translate("PbrReferenceWidget", u"Properties", None))
    # retranslateUi

