# src/app/__init__.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# GUI FILE
# from ui_main_window import Ui_MainWindow
from .ui.ui_main_window import Ui_MainWindow


"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui')))
import ui.resources_rc
"""