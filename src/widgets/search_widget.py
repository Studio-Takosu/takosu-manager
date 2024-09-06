from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

class CustomSearchLineEdit(QLineEdit):
    def __init__(self, parent=None, focus_in_style=None, focus_out_style=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Store the custom styles as instance variables
        self.focus_in_style = focus_in_style or """
          background-color: rgb(40, 42, 54);
          border-radius: 1em;
          border: 2px solid #8BE9FD;  /* Cyan border when focused */
        """
        self.focus_out_style = focus_out_style or ""
        
        # self.focus_out_style = focus_out_style or """
        #   background-color: rgb(40, 42, 54);
        #   border-radius: 1em;
        #   border: 2px solid transparent;  /* Remove border when not focused */
        # """

    def focusInEvent(self, event):
        # When the QLineEdit gets focus, modify the parent (searchContainer) style
        self.parentWidget().setStyleSheet(self.focus_in_style)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        # When the QLineEdit loses focus, revert to the original style
        self.parentWidget().setStyleSheet(self.focus_out_style)
        super().focusOutEvent(event)