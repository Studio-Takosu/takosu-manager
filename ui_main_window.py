# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.styleSheet.setStyleSheet(u"/* Dracula Theme */\n"
"\n"
"/* Base Background */\n"
"QWidget {\n"
"    /* background-color: #282A36;\n"
"    color: #F8F8F2; */\n"
"	color: rgb(221, 221, 221);\n"
"	font: 600 10pt \"Exo SemiBold\";\n"
"}\n"
"\n"
"/* Tooltips */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, .180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Background App */\n"
"#bgApp {\n"
"	background-color: #282A36;\n"
"	border: 0px solid #6272A4\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#leftMenuFrame{\n"
""
                        "	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/takosu);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* TOGGLE BUTTON */\n"
"#toggleBtn {\n"
"	background-position: left center;\n"
"  	background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	border-right: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleBtn:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleBtn:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"\n"
"#topMenu #homeBtnFrame, \n"
"#topMenu #pbrBtnFrame, \n"
"#topM"
                        "enu #assetBtnFrame {\n"
"	border: none;\n"
"	border-left: 0px solid #FF79C6;\n"
"	padding-left: 22px;\n"
"}\n"
"\n"
"#topMenu #homeBtnFrame:hover, \n"
"#topMenu #pbrBtnFrame:hover, \n"
"#topMenu #assetBtnFrame:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu #homeBtnFrame:pressed, \n"
"#topMenu #pbrBtnFrame:pressed, \n"
"#topMenu #assetBtnFrame:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"  	background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////"
                        "//////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.bgApp.setLineWidth(1)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(240, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleAppLeft = QLabel(self.topLogoInfo)
        self.titleAppLeft.setObjectName(u"titleAppLeft")
        self.titleAppLeft.setGeometry(QRect(60, 7, 180, 35))
        self.titleAppLeft.setStyleSheet(u"font: 600 16pt \"Exo SemiBold\";")
        self.titleAppLeft.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.verticalLayout_9 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleBtn = QPushButton(self.toggleBox)
        self.toggleBtn.setObjectName(u"toggleBtn")
        self.toggleBtn.setMinimumSize(QSize(0, 45))
        self.toggleBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_9.addWidget(self.toggleBtn)


        self.verticalLayout_3.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.topMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.homeFrame = QFrame(self.topMenu)
        self.homeFrame.setObjectName(u"homeFrame")
        self.homeFrame.setMinimumSize(QSize(0, 45))
        self.homeFrame.setMaximumSize(QSize(16777215, 240))
        self.verticalLayout_10 = QVBoxLayout(self.homeFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.homeBtnFrame = QFrame(self.homeFrame)
        self.homeBtnFrame.setObjectName(u"homeBtnFrame")
        self.homeBtnFrame.setMinimumSize(QSize(0, 45))
        self.verticalLayout_12 = QVBoxLayout(self.homeBtnFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.homeBtnFrame)
        self.home_btn.setObjectName(u"home_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy)
        self.home_btn.setMinimumSize(QSize(0, 45))
        self.home_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);\n"
"border: none;")

        self.verticalLayout_12.addWidget(self.home_btn)


        self.verticalLayout_10.addWidget(self.homeBtnFrame)

        self.homeContainer = QFrame(self.homeFrame)
        self.homeContainer.setObjectName(u"homeContainer")
        self.homeContainer.setMinimumSize(QSize(0, 0))
        self.homeContainer.setMaximumSize(QSize(16777215, 16777215))
        self.homeContainer.setStyleSheet(u"background-color: #44475A;")
        self.verticalLayout_11 = QVBoxLayout(self.homeContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.homeContainer)


        self.verticalLayout_6.addWidget(self.homeFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.pbrFrame = QFrame(self.topMenu)
        self.pbrFrame.setObjectName(u"pbrFrame")
        self.pbrFrame.setMinimumSize(QSize(0, 45))
        self.verticalLayout_13 = QVBoxLayout(self.pbrFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pbrBtnFrame = QFrame(self.pbrFrame)
        self.pbrBtnFrame.setObjectName(u"pbrBtnFrame")
        self.pbrBtnFrame.setMinimumSize(QSize(0, 45))
        self.verticalLayout_16 = QVBoxLayout(self.pbrBtnFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pbr_btn = QPushButton(self.pbrBtnFrame)
        self.pbr_btn.setObjectName(u"pbr_btn")
        sizePolicy.setHeightForWidth(self.pbr_btn.sizePolicy().hasHeightForWidth())
        self.pbr_btn.setSizePolicy(sizePolicy)
        self.pbr_btn.setMinimumSize(QSize(0, 45))
        self.pbr_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pbr_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-circle.png);\n"
"border: none;")

        self.verticalLayout_16.addWidget(self.pbr_btn)


        self.verticalLayout_13.addWidget(self.pbrBtnFrame)


        self.verticalLayout_6.addWidget(self.pbrFrame)

        self.assetFrame = QFrame(self.topMenu)
        self.assetFrame.setObjectName(u"assetFrame")
        self.assetFrame.setMinimumSize(QSize(0, 45))
        self.assetFrame.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.assetFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.assetBtnFrame = QFrame(self.assetFrame)
        self.assetBtnFrame.setObjectName(u"assetBtnFrame")
        self.assetBtnFrame.setMinimumSize(QSize(0, 45))
        self.assetBtnFrame.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.assetBtnFrame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.asset_btn = QPushButton(self.assetBtnFrame)
        self.asset_btn.setObjectName(u"asset_btn")
        sizePolicy.setHeightForWidth(self.asset_btn.sizePolicy().hasHeightForWidth())
        self.asset_btn.setSizePolicy(sizePolicy)
        self.asset_btn.setMinimumSize(QSize(0, 45))
        self.asset_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.asset_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);\n"
"border: none;")

        self.verticalLayout_15.addWidget(self.asset_btn)


        self.verticalLayout_14.addWidget(self.assetBtnFrame)


        self.verticalLayout_6.addWidget(self.assetFrame)


        self.verticalLayout_3.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBtn = QPushButton(self.bottomMenu)
        self.toggleLeftBtn.setObjectName(u"toggleLeftBtn")
        self.toggleLeftBtn.setMinimumSize(QSize(0, 45))
        self.toggleLeftBtn.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")
        self.toggleLeftBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.toggleLeftBtn)


        self.verticalLayout_3.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Exo SemiBold"])
        font.setPointSize(16)
        font.setWeight(QFont.ExtraBold)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setStyleSheet(u"font: 800 16pt \"Exo SemiBold\";")

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rightButtons.sizePolicy().hasHeightForWidth())
        self.rightButtons.setSizePolicy(sizePolicy3)
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.horizontalLayout_6 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.minimizeAppBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.minimizeAppBtn.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.verticalLayout_4 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.horizontalLayout_5 = QHBoxLayout(self.content)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.verticalLayout_8 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.horizontalLayout_5.addWidget(self.pagesContainer)

        self.settingsRightBox = QFrame(self.content)
        self.settingsRightBox.setObjectName(u"settingsRightBox")
        self.settingsRightBox.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.settingsRightBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_5.addWidget(self.settingsRightBox)


        self.verticalLayout_4.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")

        self.horizontalLayout_2.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-size-grip.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right bottom;")
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleAppLeft.setText(QCoreApplication.translate("MainWindow", u"Takosu Manager", None))
        self.toggleBtn.setText("")
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pbr_btn.setText(QCoreApplication.translate("MainWindow", u"PBR Material Reference", None))
        self.asset_btn.setText(QCoreApplication.translate("MainWindow", u"Assets", None))
        self.toggleLeftBtn.setText(QCoreApplication.translate("MainWindow", u"User Settings", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Studio Takosu", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

