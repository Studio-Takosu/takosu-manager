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
from PySide6.QtWidgets import QWidget, QMainWindow
# from interfaces import ViewInterface
from widgets import *
# from ui_pbr_reference import Ui_PbrReferenceWidget # type: ignore
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
      # self.ui.matRenderLabel.setPixmap
      
      # self.ui.matLibraryListWidget.setCurrentItem(self.ui.matLibraryListWidget.item(0))
      # self.ui.matLibraryListWidget.item(0).setIcon
    
    def display_material(self, material_data):
        """Update the UI with material data."""
        print(f"Displaying material: {material_data}")