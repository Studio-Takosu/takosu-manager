from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout, QSizePolicy, QScrollArea, QFrame, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QEvent, QSize, Signal
from PySide6.QtGui import QMouseEvent, QPixmap, QFont, QPalette, QColor


class GridViewItem(QWidget):
    # Signal to notify when an item is selected/clicked
    selected = Signal(QWidget)
    
    def __init__(self, image_path, item_name, parent=None):
        super().__init__(parent)

        self.is_selected = False
        self.item_name = item_name
        # self.backgroundColor = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(33, 35, 45, 255), stop:1 rgba(24, 26, 33, 255));"
        self.backgroundColor = "background-color: rgba(35, 35, 35, 255);"
        self.normalStyle = f"border: 4px solid transparent; border-radius: 4px; {self.backgroundColor}"
        self.hoveredStyle = f"border: 4px solid rgb(45,45,45); border-radius: 10px; {self.backgroundColor}"
        self.selectedStyle = f"border: 4px solid rgba(255, 121, 198, 255); border-radius: 10px; {self.backgroundColor}"

        # Set up the main frame (the container for the image and label)
        self.frame = QFrame(self)
        self.frame.setLayout(QVBoxLayout())
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame.setStyleSheet(f"{self.normalStyle}")
        self.frame.layout().setAlignment(Qt.AlignCenter)
        self.frame.layout().setContentsMargins(0, 0, 0, 0)
        # self.frame.setMaximumSize(275, 250)
        self.frame.setMinimumSize(275, 250)
        
        # Create a QGraphicsDropShadowEffect
        # shadow = QGraphicsDropShadowEffect()
        # shadow.setBlurRadius(2)  # The blur radius of the shadow
        # shadow.setColor(QColor(150, 150, 150, 255))  # Shadow color with transparency (ARGB)
        # shadow.setOffset(5, 5)  # Horizontal and vertical offset of the shadow

        # # Apply the shadow to the frame
        # self.frame.setGraphicsEffect(shadow)
        

        # QLabel to hold the material image
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(200, 200)  # Adjust the size as needed
        self.image_label.setScaledContents(True)
        self.image_label.setStyleSheet("border: none; border-radius: 10px; background-color: transparent;")
        self.image_label.setAlignment(Qt.AlignCenter)

        # QLabel to hold the material name (hidden by default)
        self.name_label = QLabel(self)
        self.name_label.setAlignment(Qt.AlignLeft)
        self.name_label.setStyleSheet("color: white; font-size: 16px; border: none; background-color: transparent;")
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
            if not self.is_selected:
                self.frame.setStyleSheet(f"{self.hoveredStyle}")
            self.name_label.setText(self.item_name)
        
        elif event.type() == QEvent.Leave:
            # Remove border and hide name when not hovering
            if not self.is_selected:
                self.frame.setStyleSheet(f"{self.normalStyle}")
            self.name_label.setText('')

        return super().eventFilter(obj, event)
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Detect when the item is clicked and emit the selected signal."""
        self.selected.emit(self)
        return super().mousePressEvent(event)
    
    def set_selected(self, selected: bool):
        """Set the selected state of the item."""
        self.is_selected = selected
        if selected:
            self.frame.setStyleSheet(f"{self.selectedStyle}")
        else:
            self.frame.setStyleSheet(f"{self.normalStyle}")


class GridView(QWidget):
    # Signal to notify when an item is selected/clicked
    selected = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_item = None

        # Set up the grid layout
        self.items = None
        self.item_widgets = []
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setVerticalSpacing(8)
        self.grid_layout.setHorizontalSpacing(8)
        self.grid_layout.setContentsMargins(25, 35, 25, 35)
        
    def set_items(self, items: dict):
        """Set the items to be displayed in the grid."""
        self.items = items
        self.create_item_widgets()  # Create item widgets only once

    def create_item_widgets(self):
        """Create GridViewItem widgets but don't populate them in the layout yet."""
        for key, value in self.items.items():
            item_widget = GridViewItem(value['image'], key)
            item_widget.selected.connect(self.on_item_selected)
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
                
    def on_item_selected(self, selected_widget):
        """Handle the selection of an item."""
        if self.selected_item:
            # Deselect the previously selected item
            self.selected_item.set_selected(False)
        # Set the new item as selected
        self.selected_item = selected_widget
        self.selected_item.set_selected(True)
        self.selected.emit(self.selected_item.item_name)
        # print("Selected item:", self.selected_item.item_name)


class ScrollableGridView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a QScrollArea for scrolling
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        
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
        self.columns = 3  # Default columns
        
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