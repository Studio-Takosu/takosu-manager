# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PySide6.QtGui import QIcon
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from ui_main_window import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # GLOBAL VARIABLES -----------------------------------------------------
        # selected menu style
        self.SELECTED_MENU_STYLE = """
        /* background-position: left center; */
        border-left: 2px solid #FF79C6;
        /* background-color: rgb(40, 44, 52); */
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
        
        # Set Home button as active
        self.home_btn.parent().setStyleSheet( self.selectMenu( self.home_btn.parent().styleSheet() ) )
        
        
        
        # SHOW APP -------------------------------------------------------------
        self.show()

    def on_button_clicked(self):
        # Get button that was clicked
        btn = self.sender()
        btn_name = btn.objectName()
        
        # Apply the style to the parent QFrame
        btn_parent = btn.parent()
        btn_parent_name = btn_parent.objectName()
        
        # SHOW HOME PAGE
        if btn_name == "home_btn":
            # self.stackedWidget.setCurrentIndex(0) # set current page
            self.resetStyle(btn_parent_name) # Reset button styles
            updatedStyle = self.selectMenu(btn_parent.styleSheet()) # Get updated button style
            btn_parent.setStyleSheet(updatedStyle) # Apply updated style
            print(btn_parent.styleSheet())
        # SHOW ASSET PAGE
        elif btn_name == "asset_btn":
            # self.stackedWidget.setCurrentIndex(1)
            self.resetStyle(btn_parent_name) # Reset button styles
            updatedStyle = self.selectMenu(btn_parent.styleSheet()) # Get updated button style
            btn_parent.setStyleSheet(updatedStyle) # Apply updated style
            print(btn_parent.styleSheet())
        # SHOW PBR PAGE
        elif btn_name == "pbr_btn":
            # self.stackedWidget.setCurrentIndex(2)
            self.resetStyle(btn_parent_name) # Reset button styles
            updatedStyle = self.selectMenu(btn_parent.styleSheet()) # Get updated button style
            btn_parent.setStyleSheet(updatedStyle) # Apply updated style
            print(btn_parent.styleSheet())
        elif btn_name == "toggleBtn":
            self.toggleMenu(True)
        
        # Apply the active style to the clicked button
        # btn.setStyleSheet(self.active_style)
        
        # PRINT BTN NAME
        print("Updating stylesheet for:", btn_parent_name)
        print(f'Button "{btn_name}" pressed!')
        
    
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
    
    def selectStandardMenu(self, widgetName):
        """
        Selects the standard menu for the given widget.

        Parameters:
        - widget: The widget to select the standard menu for.

        Returns:
        None
        """
        print("Updating stylesheet for:", widgetName)
        for widget in self.topMenu.findChildren(QFrame):
            if widget.objectName == widgetName:
                updatedStyle = self.selectMenu(widget.styleSheet())
                widget.setStyleSheet(updatedStyle)
    
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
        
    def toggleMenu(self, enabled):
        """
        Toggles the menu based on the given `enabled` parameter.

        Parameters:
        - enabled: The boolean value to determine if the menu should be enabled.

        Returns:
        - None
        """
        originalWidth = 60
        if enabled:
            pass
            width = self.leftMenuBg.width()
            expandedWidth = self.EXPANDED_MENU_WIDTH
            
            if width == originalWidth:
                # set expanded width
                newWidth = expandedWidth
            else:
                # set original width
                newWidth = originalWidth
                
            # animate the menu
            self.animation = QPropertyAnimation(self.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(self.ANIMATION_DURATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
