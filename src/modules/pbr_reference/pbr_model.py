# pbr_model.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from interfaces import ModelInterface

class PBRModel(ModelInterface):
    def __init__(self):
        self.materials_data = {}

    def load_data(self):
        """Simulated loading data"""
        self.materials_data = {
            "metal": {"roughness": 0.5, "specularity": 1.0},
            "wood": {"roughness": 0.9, "specularity": 0.2},
        }

    def get_material_data(self, material_name):
        return self.materials_data.get(material_name, {})