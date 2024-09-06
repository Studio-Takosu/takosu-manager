# interfaces.py
from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def load_data(self):
        """Load data into the model."""
        pass

class ViewInterface(ABC):
    @abstractmethod
    def setup_ui(self):
        """Setup the UI for the view."""
        pass

class ControllerInterface(ABC):
    @abstractmethod
    def connect_signals(self):
        """Connect signals between the view and the model."""
        pass