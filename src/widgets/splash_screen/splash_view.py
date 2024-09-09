# splash_screen.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QSizePolicy, QFrame
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QSize, QRect

class SplashView(QWidget):
    def __init__(self):
        super().__init__()
        self.gifSize = QSize(200, 200)
        
        # Set up the splash screen layout
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setFixedSize(600, 400)
        
        # Create the main splash layout
        self.splashLayout = QVBoxLayout(self)
        self.splashLayout.setObjectName("splashLayout")
        
        # Layout to hold loading movie
        self.splashTop = QVBoxLayout(self)
        self.splashTop.setObjectName("splashTop")
        
        # Layout to hold status text and progress bar
        self.splashBottom = QVBoxLayout(self)
        self.splashBottom.setObjectName("splashBottom")
        self.splashBottom.setAlignment(Qt.AlignCenter)
        
        # Add the Top | Bottom layouts to the main layout
        self.splashLayout.addLayout(self.splashTop)
        self.splashLayout.addLayout(self.splashBottom)
        
        # Label to hold the animation
        self.label_animation = QLabel(self)
        self.label_animation.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.label_animation.setScaledContents(True)
        self.label_animation.setMaximumSize(self.gifSize)
        
        # Load the GIF and set scaling properties
        self.movie = QMovie("src\widgets\splash_screen\loading_animation.gif")  # Load your animation GIF
        self.movie.setScaledSize(self.gifSize)  # Set a default scaled size
        self.label_animation.setMovie(self.movie)
        self.movie.start()

        # Status text
        self.label_status = QLabel("Loading...", self)
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.label_status.setStyleSheet("color: white; font-size: 12px; padding-bottom: 20px;")
        
        # Progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(50)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setMaximumSize(QSize(400, 10))
        # self.label_animation.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        # self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #44475A;
                border-radius: 5px;
                background-color: #222;
            }
            QProgressBar::chunk {
                background-color: #FF79C6;
                border: 5px solid transparent;
                border-radius: 5px;
                width: 20px;
            }
        """)

        self.splashTop.addWidget(self.label_animation)
        self.splashTop.layout().setAlignment(Qt.AlignCenter)
        self.splashBottom.layout().addWidget(self.progress_bar)
        self.splashBottom.layout().addWidget(self.label_status)
        
    def resizeEvent(self, event):
        """ Adjust the GIF size based on the window size """
        super(SplashView, self).resizeEvent(event)
        new_size = QSize(self.width() * 0.5, self.height() * 0.5)  # Resize to 50% of the window size
        self.movie.setScaledSize(new_size)
    
    def set_loading_status(self, message):
        """ Update the status text on the splash screen. """
        splash_status = f"Loading... {message}"
        self.label_status.setText(splash_status)

    def set_progress(self, value):
        """ Update the progress bar. """
        self.progress_bar.setValue(value)
