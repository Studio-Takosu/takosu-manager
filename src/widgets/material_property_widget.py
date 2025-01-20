from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

class MaterialPropertyWidget(QWidget):
    def __init__(self, property_name, property_value, parent=None):
        super().__init__(parent)
        
        # Main layout for the widget
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 5, 5, 10)

        # Property name label
        self.property_name_label = QLabel(property_name)
        # set size policy, so widget on uses as much space as needed
        self.property_name_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.property_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        self.property_name_label.setStyleSheet("color: white;")
        layout.addWidget(self.property_name_label)
        
        if property_name.lower().endswith('color'):
            self.setToolTip("Click to copy Hex Color to clipboard")
        else:
            self.setToolTip(f"Click to copy {property_name} to clipboard")
        
        # Property value
        if isinstance(property_value, list):
            # If the value is a list, create a horizontal layout to visualize it
            count = 0
            # 3 elements per layout row
            for value in property_value:
                if count == 0:
                    value_layout = QHBoxLayout()
                    value_layout.setContentsMargins(0, 0, 0, 0)
                count += 1
                value_label = QLabel(f"{value}")
                value_label.setStyleSheet("""color: white; font: 500 10pt 'Exo Medium';""")
                # value_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                value_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
                value_layout.addWidget(value_label)
                value_label.adjustSize()
                if count > 2:
                    layout.addLayout(value_layout)
                    count = 0
        else:
            # Otherwise, display it as a single label
            if property_name.lower() == 'density':
                property_value = f"{property_value} kg/m³"
            self.property_value_label = QLabel(f"{property_value}")
            self.property_value_label.setStyleSheet("""color: white; font: 500 10pt 'Exo Medium';""")
            self.property_value_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            layout.addWidget(self.property_value_label)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.setMaximumWidth(320)
        # self.setMinimumHeight(75)
        self.adjustSize()