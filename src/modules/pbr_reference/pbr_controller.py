# pbr_controller.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from interfaces import ControllerInterface

class PBRController(ControllerInterface):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.connect_signals()

    def connect_signals(self):
        """Connect signals between view and model."""
        # Example: Connect a button click to load and display material data
        #self.view.ui.searchBtn.clicked.connect(self.on_search)
        
        ui = self.view.ui
        print(ui)
        
        # ---------
        ui.searchLineEdit.returnPressed.connect(self.on_search_return)
        ui.cancelSearchBtn.clicked.connect(self.on_cancel_search)
        # ui.searchBtn.installEventFilter(self)

    def on_search(self):
        """Fetch material data when search is clicked."""
        pass
    
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
    
    def on_search_return(self):
      print(self.view.ui.searchLineEdit.text())
      # remove focus from the searchLineEdit
      self.view.ui.searchLineEdit.clearFocus()
    
    def on_cancel_search(self):
      self.view.ui.searchLineEdit.clear()
      self.view.ui.searchLineEdit.clearFocus()
    
    