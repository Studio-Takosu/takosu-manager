# This Python file uses the following encoding: utf-8
import sys
from typing import Any
from urllib.parse import quote_from_bytes
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PySide6.QtGui import QIcon
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QObject, QSize, QTimer
from ui_main_window import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # GLOBAL VARIABLES -----------------------------------------------------
        # selected menu style
        self.SELECTED_MENU_STYLE = """
        border-left: 2px solid #FF79C6;
        background-color: #44475A;
        """
        
        # expanded menu widths
        self.EXPANDED_MENU_WIDTH = 240
        self.LEFT_BOX_WIDTH = 240
        self.RIGHT_BOX_WIDTH = 240
        self.ANIMATION_DURATION = 500
        
        # APP NAME -------------------------------------------------------------
        title = "Takosu Manager"
        self.setWindowTitle(title)
        
        # Frameless window title
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        
        
        # APP MIN/MAX/CLOSE BUTTONS --------------------------------------------
        self.closeAppBtn.clicked.connect(self.close)
        self.minimizeAppBtn.clicked.connect(self.showMinimized)
        self.maximizeRestoreAppBtn.clicked.connect(self.toggle_maximize_restore)
        self.closeAppBtn.hide()
        self.minimizeAppBtn.hide()
        self.maximizeRestoreAppBtn.hide()
        
        
        
        # MENU BUTTONS ---------------------------------------------------------
        # Connect button signals to the method
        self.asset_btn.clicked.connect(self.on_button_clicked)
        self.home_btn.clicked.connect(self.on_button_clicked)
        self.pbr_btn.clicked.connect(self.on_button_clicked)
        self.toggleBtn.clicked.connect(self.on_button_clicked)
        self.settingsTopBtn.clicked.connect(self.on_button_clicked)
        
        
        # Timer to simulate the animation by changing alignment over time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_resizeContentFrame)
        
        # Set Home button as active and set the Home page to active
        self.home_btn.parent().setStyleSheet( self.selectMenu( self.home_btn.parent().styleSheet() ) )
        self.contentStackedWidget.setCurrentIndex(0)
        
        
        
        # SHOW APP -------------------------------------------------------------
        self.show()
    
        
        # apply the new width and height to the pagesContainer QFrame
        self.pagesContainer.resize(
            self.contentFrame.width(), 
            self.contentFrame.height()
        )
        
        self.settingsRightBox.setMinimumSize(self.settingsRightBox.width(), self.contentFrame.height())
        self.settingsRightBox.move(self.contentFrame.width() - self.settingsRightBox.width(), 0)
        # print(f"Settings Right Box Pos X: {self.contentFrame.width() - self.settingsRightBox.width()}")
        
    def resizeEvent(self, event):
        # get the current width of the content QFrame
        self.resizeContentFrame()
        
        # call the parent resizeEvent
        super(MainWindow, self).resizeEvent(event)
    

    def on_button_clicked(self):
        # Get button that was clicked
        btn = self.sender()
        btn_name = btn.objectName()
        
        # Apply the style to the parent QFrame
        btn_parent = btn.parent()
        btn_parent_name = btn_parent.objectName()
        
        # SHOW HOME PAGE
        if btn_name == "home_btn":
            self.contentStackedWidget.setCurrentIndex(0) # set current page
            self.resetStyle(btn_parent_name) # Reset button styles
            updatedStyle = self.selectMenu(btn_parent.styleSheet()) # Get updated button style
            btn_parent.setStyleSheet(updatedStyle) # Apply updated style
            # Update titleRightInfo text
            self.titleRightInfo.setText(btn.text())
        
        # SHOW PBR PAGE
        elif btn_name == "pbr_btn":
            self.contentStackedWidget.setCurrentIndex(1)
            self.resetStyle(btn_parent_name) # Reset button styles
            updatedStyle = self.selectMenu(btn_parent.styleSheet()) # Get updated button style
            btn_parent.setStyleSheet(updatedStyle) # Apply updated style
            # Update titleRightInfo text
            self.titleRightInfo.setText(btn.text())
        
        # SHOW ASSET PAGE
        elif btn_name == "asset_btn":
            self.contentStackedWidget.setCurrentIndex(2)
            self.resetStyle(btn_parent_name) # Reset button styles
            updatedStyle = self.selectMenu(btn_parent.styleSheet()) # Get updated button style
            btn_parent.setStyleSheet(updatedStyle) # Apply updated style
            # Update titleRightInfo text
            self.titleRightInfo.setText(btn.text())
        
        # LEFT MENU TOGGLE BUTTON
        elif btn_name == "toggleBtn":
            self.toggleMainMenu(True)
            
            
        elif btn_name == "settingsTopBtn":
            self.toggleRightMenu(True)
        
        # Apply the active style to the clicked button
        # btn.setStyleSheet(self.active_style)
        
        # PRINT BTN NAME
        # print("Updating stylesheet for:", btn_parent_name)
        # print(f'Button "{btn_name}" pressed!')
        
    
    def toggle_maximize_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def selectMenu(self, getStyle):
        """
        Selects a menu style based on the given `getStyle` parameter and the `active_style` attribute.

        Parameters:
        - getStyle: The style to be selected.

        Returns:
        - selectedStyle: The selected menu style.

        """
        selectedStyle = getStyle + self.SELECTED_MENU_STYLE
        selectedStyle = self.SELECTED_MENU_STYLE
        return selectedStyle
        
    def deselectMenu(self, getStyle):
        """
        Deselects the menu by replacing the active style with an empty string.

        Parameters:
        - getStyle: The current style of the menu.

        Returns:
        - defaultStyle: The style of the menu after deselecting.

        """
        defaultStyle = getStyle.replace(self.SELECTED_MENU_STYLE, "")
        defaultStyle = ""
        return defaultStyle
    
    def resetStyle(self, widgetName):
        """
        Resets the style of all QPushButton widgets in the topMenu, except for the specified widget.

        Parameters:
        - widget: The QPushButton widget to exclude from style reset.

        Returns:
        - None
        """
        
        # loop through all
        for widget in self.topMenu.findChildren(QFrame):
            if widget.objectName() != widgetName:
                resetStyle = self.deselectMenu(widget.styleSheet())
                widget.setStyleSheet(resetStyle)
        
    def toggleMainMenu(self, enabled):
        """
        Toggles the menu based on the given `enabled` parameter.

        Parameters:
        - enabled: The boolean value to determine if the menu should be enabled.

        Returns:
        - None
        """
        
        def activeToggleStyle():
            updatedStyle = """
            background-image: url(:/icons/images/icons/cil-chevron-left.png);
            """
            return updatedStyle
        
        def defaultToggleStyle():
            defaultStyle = """
            background-image: url(:/icons/images/icons/cil-chevron-right.png);
            """
            return defaultStyle
        
        originalWidth = 60
        if enabled:
            width = self.leftMenuBg.width() # current width of the menu
            expandedWidth = self.EXPANDED_MENU_WIDTH
            pos = self.toggleBtn.pos() # current position of the toggle button
            
            if width == originalWidth:
                # set expanded width
                newWidth = expandedWidth
                newPos = QPoint(180, 0)
                newToggleStyle = activeToggleStyle()
                toggleDuration = self.ANIMATION_DURATION
            else:
                # set original width
                newWidth = originalWidth
                newPos = QPoint(0, 0)
                newToggleStyle = defaultToggleStyle()
                toggleDuration = 300
            
            # setup the menu animation
            self.sizeAnim = self.create_menu_animation(
                self.leftMenuBg,
                b"minimumWidth",
                width,
                newWidth,
                self.ANIMATION_DURATION
            )
            
            # setup toggle button anumation for layout alignment
            self.toggleAnimation = self.create_menu_animation(
                self.toggleBtn, 
                b"pos",
                pos,
                newPos,
                toggleDuration
            )
            
            # self.leftMenuBg.resizeEvent
            
            
            # start the animation
            self.sizeAnim.start()
            self.toggleAnimation.start()
            self.toggleBtn.setStyleSheet(newToggleStyle)
            self.timer.start(1)
            
            # new timer to stop the self.timer animation after 500ms
            QTimer.singleShot(500, lambda: self.timer.stop())
        
    
    def toggleRightMenu(self, enabled):
        # self.RIGHT_BOX_WIDTH = 240
        height = self.settingsRightBox.height()
        initialSize = QSize(0, height)
        
        
        if enabled:
            currentSize = self.settingsRightBox.size()
            expandedSize = QSize(self.RIGHT_BOX_WIDTH, height)
            currentPos = self.settingsRightBox.pos()
            closedPos = QPoint(self.contentFrame.width(), currentPos.y())
            openPos = QPoint(self.contentFrame.width() - self.RIGHT_BOX_WIDTH, currentPos.y())
            
            
            if currentSize.width() == initialSize.width():
                # Open the settingsRightBox
                self.settingsRightBox.raise_()  # Raise settingsRightBox to be on top
                updatedSize = expandedSize
                updatedPos = openPos
                animDuration = self.ANIMATION_DURATION
            else:
                # Close the settingsRightBox
                # self.settingsRightBox.lower()  # Lower settingsRightBox to be behind pagesContainer
                updatedSize = initialSize
                updatedPos = closedPos
                animDuration = 300
            
            self.sizeAnim = self.create_menu_animation(
                self.settingsRightBox,
                b"size",
                currentSize,
                updatedSize,
                self.ANIMATION_DURATION
            )
            self.minSizeAnim = self.create_menu_animation(
                self.settingsRightBox,
                b"minimumSize",
                currentSize,
                updatedSize,
                self.ANIMATION_DURATION
            )
            self.posAnim = self.create_menu_animation(
                self.settingsRightBox,
                b"pos",
                currentPos,
                updatedPos,
                animDuration
            )
            
            
            self.sizeAnim.start()
            self.minSizeAnim.start()
            self.posAnim.start()
            
            self.resizeContentFrame()
    
    def resizeContentFrame(self):
        # get the current width of the content QFrame
        contentWidth = self.contentFrame.width()
        contentHeight = self.contentFrame.height()
        # print ("contentWidth: ", contentWidth)
        
        # apply the new width and height to the pagesContainer QFrame
        self.pagesContainer.setMinimumSize(contentWidth, contentHeight)
        self.pagesContainer.resize(contentWidth, contentHeight)
        
        # apply the new width and height to the settingsRightBox QFrame
        self.settingsRightBox.setMinimumSize(self.settingsRightBox.width(), contentHeight)
        self.settingsRightBox.resize(self.settingsRightBox.width(), contentHeight)
        
        
        # Absolute positioning for settingsRightBox (positioned on top of pagesContainer)
        self.settingsRightBox.move(contentWidth - self.settingsRightBox.width(), 0)
        
        # self.homePage.setStyleSheet("""
        #     background-image: url(:/images/takosu-lrg);
        #     background-position: center;
        #     background-repeat: no-repeat;
        # """)
        # self.homePage.update()
        # self.homePage.repaint()
    
    def timer_resizeContentFrame(self):
        self.resizeContentFrame()
    
    def create_menu_animation(self, widget:QObject, property:str, startValue:Any, endValue:Any, duration:int = 500):
        animation = QPropertyAnimation(widget, property)
        animation.setDuration(duration)
        animation.setStartValue(startValue)
        animation.setEndValue(endValue)
        animation.setEasingCurve(QEasingCurve.InOutQuart)
        return animation


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
    