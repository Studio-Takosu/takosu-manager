from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout, QSizePolicy, QScrollArea, QFrame
from PySide6.QtCore import Qt, QEvent, QSize
from PySide6.QtGui import QPixmap, QFont


class GridViewItem(QWidget):
    def __init__(self, image_path, item_name, parent=None):
        super().__init__(parent)

        self.item_name = item_name

        # Set up the main frame (the container for the image and label)
        self.frame = QFrame(self)
        self.frame.setLayout(QVBoxLayout())
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame.setStyleSheet("border: 4px solid transparent; border-radius: 10px; background-color: #282A36;")
        self.frame.layout().setAlignment(Qt.AlignCenter)
        self.frame.layout().setContentsMargins(0, 0, 0, 0)
        # 275, 250
        self.frame.setMaximumSize(275, 250)
        self.frame.setMinimumSize(275, 250)
        

        # QLabel to hold the material image
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(200, 200)  # Adjust the size as needed
        self.image_label.setScaledContents(True)
        self.image_label.setStyleSheet("border: none; border-radius: 10px;")
        self.image_label.setAlignment(Qt.AlignCenter)

        # QLabel to hold the material name (hidden by default)
        self.name_label = QLabel(self)
        self.name_label.setAlignment(Qt.AlignLeft)
        self.name_label.setStyleSheet("color: white; font-size: 16px; border: none;")
        # self.name_label.setFont(QFont('Exo', 12))
        # self.name_label.hide()

        # Add widgets to the layout of the frame
        self.frame.layout().addWidget(self.image_label)
        self.frame.layout().addWidget(self.name_label)
        
        # Add frame to the main layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.frame)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        # Install event filter to detect hover events
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            # Show border and name when hovering
            self.frame.setStyleSheet("border: 4px solid #FF79C6; border-radius: 10px; background-color: #282A36;")
            self.name_label.setText(self.item_name)
            # Print size of frame
            # print("Frame size:", self.frame.size())
        elif event.type() == QEvent.Leave:
            # Remove border and hide name when not hovering
            self.frame.setStyleSheet("border: 4px solid transparent; border-radius: 10px; background-color: #282A36;")
            self.name_label.setText('')

        return super().eventFilter(obj, event)


class GridView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the grid layout
        self.items = None
        self.item_widgets = []
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setVerticalSpacing(2)
        self.grid_layout.setHorizontalSpacing(2)
        
    def set_items(self, items: dict):
        """Set the items to be displayed in the grid."""
        self.items = items
        self.create_item_widgets()  # Create item widgets only once

    def create_item_widgets(self):
        """Create GridViewItem widgets but don't populate them in the layout yet."""
        for key, value in self.items.items():
            item_widget = GridViewItem(value['image'], key)
            self.item_widgets.append(item_widget)

    def populate_grid(self, columns: int):
        """Reposition existing items in the grid based on the column count."""
        if not self.items or not self.item_widgets:
            return

        # Remove only the layout's position references, but keep the widgets
        while self.grid_layout.count() > 0:
            self.grid_layout.takeAt(0)

        # Re-add the widgets based on the new column count
        row, col = 0, 0
        for widget in self.item_widgets:
            self.grid_layout.addWidget(widget, row, col)
            col += 1
            if col == columns:
                col = 0
                row += 1


class ScrollableGridView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a QScrollArea for scrolling
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        # self.scroll_area.setMaximumWidth(1220)
        
        # Disable horizontal scrolling and enable vertical scrolling only
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Create a container widget to hold the grid layout
        self.grid_widget = GridView()
        self.scroll_area.setWidget(self.grid_widget)

        # Set up the main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.scroll_area)
        self.setLayout(layout)
        
        # Initial values
        self.item_width = 285  # Fixed width of grid items
        self.columns = 4  # Default columns
        
    def populate_grid_view(self, items: dict):
        """Populate the grid view with items."""
        self.grid_widget.set_items(items)
        self.grid_widget.populate_grid(self.columns)
        
    def resizeEvent(self, event):
        """Handle the resizing of the widget."""
        if not self.grid_widget.items:
            return

        available_width = self.width()
        self.scroll_area.setMaximumWidth(available_width)
        cols = max(1, available_width // self.item_width)

        if cols != self.columns:
            self.columns = cols
            self.grid_widget.populate_grid(self.columns)
        super().resizeEvent(event)