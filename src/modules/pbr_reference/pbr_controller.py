# pbr_controller.py

import os
import sys
srcDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(srcDir)
from typing import Any
from interfaces import ControllerInterface
from PySide6.QtCore import QThreadPool, QTimer, Qt, QRectF, QPropertyAnimation, QEasingCurve, QObject, QPoint
from PySide6.QtWidgets import QApplication, QListWidgetItem
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPainterPath
from widgets import MaterialPropertyWidget

class PBRController(ControllerInterface):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.splash_view = self.view.ui.splash_screen
        self.selected_material = None
        
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
        ui.matLibraryListWidget.itemClicked.connect(self.on_material_property_selected)
        
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
        materialName = item
        self.selected_material = materialName
        self.view.ui.matLibraryListWidget.clear()
        
        # Get the material data and add the properies to the list widget
        mat_data = self.model.get_material_data(materialName)
        
        # Update labels for selected material
        self.view.ui.materialNameLabel.setText(materialName)
        self.view.ui.categoryLabel.setText( mat_data['category'][0] )
        
        for property_name, property_value in mat_data['properties'].items():
            if property_name == "complexIor": continue 
            if property_name == "densityRange": continue
            if property_name == 'acousticAbsorption': continue
            if property_name == 'density' and property_value == 0: continue
            
            list_widget_item = QListWidgetItem(property_name)
            property_name = self.format_property_name(property_name)
            print("Property:", property_name, "Value:", property_value)
            
            # Create a custom widget for the property
            property_widget = MaterialPropertyWidget(property_name, property_value)
            
            # Create a QListWidgetItem to hold the custom widget
            # Set the item size to match the custom widget
            list_widget_item.setSizeHint(property_widget.size())
            
            # Add the QListWidgetItem to the QListWidget
            self.view.ui.matLibraryListWidget.addItem(list_widget_item)
            
            # Set the custom widget to be displayed in the QListWidgetItem
            self.view.ui.matLibraryListWidget.setItemWidget(list_widget_item, property_widget)
        
        self.toggle_properties_frame(True)
        
    
    def on_material_property_selected(self, item):
        """Copy the selected property value/s to the clipboard."""
        listWidget = item.listWidget()
        widget = listWidget.itemWidget(item)
        property_name = item.text()
        property_value = ''
        
        # if property_value_label exists, set the property value
        if widget and hasattr(widget, 'property_value_label'):
            property_value = widget.property_value_label.text()
        # lets get the property value the material_data dictionary
        else:
            material_data = self.model.get_material_data(self.selected_material)
            value = material_data['properties'][property_name]
            # if it's a color property
            if len(value) == 3:
                # convert color to hex, pass it as a tuple
                rgb_tuple = (value[0], value[1], value[2])
                property_value = self.linear_rgb_to_hex(rgb_tuple)
                # property_value = rgb_tuple
                # pass
        
        print(f"Property: {property_name} - Value: {property_value} copied to clipboard.")
        # Copy the property value to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(property_value)
        self.view.ui.matLibraryListWidget.clearSelection()
        
        
    def format_property_name(self, property_name):
        # Change the property name to title case and add a space if necessary
        # specularColor -> Specular Color, subsurfaceRadius -> Subsurface Radius
        # transmissionDispersion -> Transmission Dispersion, complexIor -> Complex IOR
        # thinFilmThickness -> Thin Film Thickness, densityRange -> Density Range
        # acousticAbsorption -> Acoustic Absorption
        if property_name == "specularColor":
            property_name = "Specular Color"
        elif property_name == "subsurfaceRadius":
            property_name = "Subsurface Radius"
        elif property_name == "transmissionDispersion":
            property_name = "Transmission Dispersion"
        elif property_name == "complexIor":
            property_name = "Complex IOR"
        elif property_name == "ior":
            property_name = "IOR"
        elif property_name == "thinFilmThickness":
            property_name = "Thin Film Thickness"
        elif property_name == "densityRange":
            property_name = "Density Range"
        elif property_name == "acousticAbsorption":
            property_name = "Acoustic Absorption"
        else:
            property_name = property_name.title()
        
        return property_name
    
    def linear_rgb_to_hex(self, rgb_linear: tuple ) -> str:
        """
        Convert a linear RGB triplet to a hexadecimal color code.
        
        Args:
            rgb_linear (tuple): A tuple of linear RGB values (R, G, B) in decimal format (0.0 to 1.0).
        
        Returns:
            str: A string representing the hexadecimal color code.
        """
        # Step 1: Clamp the RGB values between 0 and 1
        r_clamped = max(0, min(1, rgb_linear[0]))
        g_clamped = max(0, min(1, rgb_linear[1]))
        b_clamped = max(0, min(1, rgb_linear[2]))

        # Step 2: Convert linear RGB values to 8-bit integers (0-255)
        r_int = int(round(r_clamped * 255))
        g_int = int(round(g_clamped * 255))
        b_int = int(round(b_clamped * 255))

        # Step 3: Convert to hex and format with leading zeros if necessary
        hex_value = "#{:02X}{:02X}{:02X}".format(r_int, g_int, b_int)

        return hex_value
    
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