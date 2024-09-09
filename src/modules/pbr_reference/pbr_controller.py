# pbr_controller.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import Any
from interfaces import ControllerInterface
from PySide6.QtCore import QThreadPool, QTimer, Qt, QRectF, QPropertyAnimation, QEasingCurve, QObject, QPoint
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPainterPath

class PBRController(ControllerInterface):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.splash_view = self.view.ui.splash_screen
        
        self.connect_signals()

    def connect_signals(self):
        """Connect signals between view and model."""
        ui = self.view.ui
        
        # ---------
        # Connect the signals from the model to update the splash screen
        self.model.signals.progress.connect(self.update_progress)
        self.model.signals.finished.connect(self.on_finished_loading)
        # self.model.signals.result.connect
        # ---------
        # Connect the signals from the view
        ui.searchLineEdit.returnPressed.connect(self.on_search_return)
        ui.cancelSearchBtn.clicked.connect(self.on_cancel_search)
        ui.propsCloseButton.clicked.connect(self.toggle_properties_frame)
        ui.gridWidget.grid_widget.selected.connect(self.on_material_selected)
        
        # ui.matLibraryListWidget.itemClicked.connect(self.on_material_selected)
        # ui.searchBtn.installEventFilter(self)
        
    def on_button_clicked(self):
        # Get button that was clicked
        btn = self.sender()
        btn_name = btn.objectName()
        
        # Apply the style to the parent QFrame
        btn_parent = btn.parent()
        btn_parent_name = btn_parent.objectName()
        
        
        if btn_name == "propsCloseButton":
            self.toggle_properties_frame(False)
            
        if btn_name == "grid_widget":
            self.toggle_properties_frame(True)

    def on_search(self):
        """Fetch material data when search is clicked."""
        
        # def eventFilter(self, obj, event):
        #   """Event filter to detect hover events."""
        #   if obj == self.searchBtn:
        #       # print("Event: ", event.type())
        #       if event.type() == 127:
        #           print("Mouse entered")
        #           # self.start_animation(1.0)  # Hover in (move to white)
        #       elif event.type() == 128:
        #           print("Mouse left")
        #           # self.start_animation(0.0)  # Hover out (move to gray)
        #   return super().eventFilter(obj, event)
        pass
    
    def on_search_return(self):
        print(self.view.ui.searchLineEdit.text())
        # remove focus from the searchLineEdit
        self.view.ui.searchLineEdit.clearFocus()
    
    def on_cancel_search(self):
        self.view.ui.searchLineEdit.clear()
        self.view.ui.searchLineEdit.clearFocus()
    
    
    
    def start_loading(self):
        """Starts loading data and shows the splash screen."""
        if self.model.percent_loaded == 100: return
        print("Loading material data...")
        self.splash_view.set_loading_status("")
        self.model.load_data()
    
    def update_progress(self, progress, material_name):
        """Update progress bar on the splash screen."""
        self.splash_view.set_progress(progress)
        self.splash_view.set_loading_status(f"- Finished loading: {material_name}")
        # print(f"Loading progress: {progress}% - Finished loaded: {material_name}")
        
    def on_data_loaded(self, materials_data):
        # self.model.materials_data = materials_data
        print("Material data loaded successfully.")
    
    def on_finished_loading(self):
        """Switch to the main application when loading is done."""
        self.splash_view.set_loading_status("")
        self.model.percent_loaded = 100
        print("Material data loaded successfully.")
        # self.switch_to_main_page()
        QTimer.singleShot(500, self.switch_to_main_page)
    
    def switch_to_main_page(self):
        """ Switch to the main page of the application. """
        self.view.ui.PbrStackedWidget.setCurrentIndex(0)
        self.set_material_library()
    
    def set_material_library(self):
        """Set the material library data in the view."""
        self.view.ui.gridWidget.populate_grid_view(self.model.materials_data)
    
    def on_material_selected(self, item):
        """ Opens the Properties Tab when a material is selected in the grid view. """
        # print("Material selected:", item)
        self.toggle_properties_frame(True)
        
    def create_rounded_pixmap(self, pixmap: QPixmap, radius: int = 10) -> QPixmap:
        """Create a rounded pixmap from a square pixmap."""
        # Create an empty pixmap with the same size as the original
        rounded_pixmap = QPixmap(pixmap.size())
        rounded_pixmap.fill(Qt.transparent)  # Fill with transparency

        # Set up the painter for the new pixmap
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        # Create a rounded rect path
        path = QPainterPath()
        rect = QRectF(pixmap.rect())
        path.addRoundedRect(rect, radius, radius)

        # Set the clip region to the rounded rect and draw the original pixmap
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)

        painter.end()

        return rounded_pixmap
    
    def set_material_selected(self, materialName):
        """Set the selected material in the view."""
        data = self.model.get_material_data(materialName)
        baseImg = QPixmap(data['image'])
        img = self.create_rounded_pixmap(baseImg, 25)
        self.view.ui.matRenderLabel.setPixmap( QIcon(img).pixmap(200, 200) )
        
    def toggle_properties_frame(self, enabled):
        """Toggle the properties frame in the view."""
        expanded_width = 320 # width when expanded
        width = self.view.ui.materialPropFrame.width() # current width of the menu
        
        if enabled:
            if width != expanded_width:
                # set expanded width
                newWidth = expanded_width
                newPos = QPoint(180, 0)
                toggleDuration = 500
                
                # setup the menu animation
                self.sizeAnim = self.create_menu_animation(
                    self.view.ui.materialPropFrame,
                    b"minimumWidth",
                    width,
                    newWidth,
                    toggleDuration
                )
                # start the animation
                self.sizeAnim.start()
        else:
            if width != 0:
                # set original width
                newWidth = 0
                toggleDuration = 300
                
                # setup the menu animation
                self.sizeAnim = self.create_menu_animation(
                    self.view.ui.materialPropFrame,
                    b"minimumWidth",
                    width,
                    newWidth,
                    toggleDuration
                )
                # start the animation
                self.sizeAnim.start()
        
    def create_menu_animation(self, widget:QObject, property:str, startValue:Any, endValue:Any, duration:int = 500):
        animation = QPropertyAnimation(widget, property)
        animation.setDuration(duration)
        animation.setStartValue(startValue)
        animation.setEndValue(endValue)
        animation.setEasingCurve(QEasingCurve.InOutQuart)
        return animation