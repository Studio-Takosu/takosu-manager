# src/modules/pbr_reference/pbr_view.py

import os
import sys
# -----------------------------------------------------------------------------
moduleDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
srcDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
uiDir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(moduleDir)
sys.path.append(srcDir)
# sys.path.append(uiDir)
# -----------------------------------------------------------------------------
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
# from interfaces import ViewInterface
from widgets import *
from .ui import Ui_PbrReferenceWidget

class PBRView(QWidget):
    def __init__(self, parent=None):
      QWidget.__init__(self)
      self.parent = parent
      # self.ui = None  # Reference to the UI setup
      self.ui = Ui_PbrReferenceWidget()
      self.ui.setupUi(self)
      
      # ----------------------------------------------------------------------------
      # PBR MATERIAL REFERENCE PAGE ------------------------------------------------
      # Hide the placeholder searchLineEdit
      self.ui.searchLineEdit.hide()
      
      # Add CustomSearchLineEdit to the searchContainer
      # Replacing the placeholder searchLineEdit
      self.ui.searchLineEdit = CustomSearchLineEdit()
      self.ui.searchLineEdit.setPlaceholderText("Search")
      self.ui.searchLineEdit.setStyleSheet("""
          color: #ffffff;
          background-color: rgb(40, 42, 54);
          border: none;
      """)
      self.ui.searchContainer.layout().addWidget(self.ui.searchLineEdit)
      
      
      # reset parent for the cancel button
      # otherwise it will appear on the left side of the searchLineEdit
      self.ui.cancelSearchBtn.setParent(None)
      self.ui.searchContainer.layout().addWidget(self.ui.cancelSearchBtn)
      
      
      # ----------------------------------------------------------------------------
      # Set up the splash screen ---------------------------------------------------
      self.ui.splash_screen = SplashView()
      self.ui.splashFrame.layout().addWidget(self.ui.splash_screen)
      self.ui.PbrStackedWidget.setCurrentIndex(1)
      # self.ui.matLibraryListWidget.clear()
      
      # ----------------------------------------------------------------------------
      # Set up the Grid View -------------------------------------------------------
      self.ui.gridWidget = ScrollableGridView()
      self.ui.materialDashFrame.layout().addWidget(self.ui.gridWidget)
      
      
      # Create a QGraphicsDropShadowEffect
      shadow = QGraphicsDropShadowEffect( self.ui.materialPropFrame )
      shadow.setBlurRadius(45)
      shadow.setColor(QColor(0, 0, 0, 50))
      shadow.setOffset(15, 5)
      
      
      # # Apply the shadow to the materialPropFrame
      self.ui.materialPropFrame.setGraphicsEffect(shadow)
      self.ui.materialPropFrame.raise_()
      
      shadow = QGraphicsDropShadowEffect( self.ui.materialPropFrame )
      shadow.setBlurRadius(45)
      shadow.setColor(QColor(0, 0, 0, 50))
      shadow.setOffset(0, 5)
      self.ui.propertiesTitleFrame.setGraphicsEffect(shadow)
      self.ui.propertiesTitleFrame.raise_()
    
    def display_material(self, material_data):
        """Update the UI with material data."""
        print(f"Displaying material: {material_data}")