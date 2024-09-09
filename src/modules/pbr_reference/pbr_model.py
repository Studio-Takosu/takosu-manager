# pbr_model.py

import sys
sys.path.append('./src/modules/utils')
import os
import json
from ..utils.worker import Worker
from ..interfaces import ModelInterface
from PySide6.QtCore import QObject, Slot, Signal


class PBRModel(QObject):
    def __init__(self, threadpool):
        super(PBRModel, self).__init__()  # Call QObject constructor
        self.material_names = []
        self.materials_data = {}
        self.percent_loaded = 0
        self.threadpool = threadpool  # Threadpool for managing worker threads
        
        # Initialize the worker thread for loading data
        self.worker = Worker(self._load_data_worker)
        # Connect signals from the worker thread
        self.signals = self.worker.signals

    def load_data(self):
        """ Initialize material data loading in a worker thread """
        # worker = Worker(self._load_data_worker)
        # worker.signals.progress.connect(self.report_progress)
        # worker.signals.result.connect(self.on_data_loaded)
        # worker.signals.finished.connect(self.on_finished_loading)
        
        # self.threadpool.start(worker)
        self.threadpool.start(self.worker)

    def _load_data_worker(self, progress_callback):
        """ Worker function to load the data, called by the worker thread """
        # Get the root directory of the project
        project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        dirPath = os.path.join(project_dir, 'data', 'pbr_reference', 'materials')
        
        # Get the names of the folders in the materials directory
        self.material_names = [f for f in os.listdir(dirPath) if os.path.isdir(os.path.join(dirPath, f))]
        
        num_materials = len(self.material_names)
        materials_data = {}

        # Load the JSON files from each folder
        for index, materialName in enumerate(self.material_names):
            # print("Loading material:", materialName)
            matDirPath = os.path.join(dirPath, materialName)
            for file in os.listdir(matDirPath):
                filepath = os.path.join(matDirPath, file)
                if file.endswith('.json'):
                    # print('Loading json:', file)
                    with open(os.path.join(filepath), 'r') as f:
                        materials_data[materialName] = json.load(f)
                        materials_data[materialName]['image'] = os.path.join(matDirPath, f'{materialName}.jpeg')
                # else:
                    # print('Loading image:', filepath)
                    # materials_data[materialName]['image'] = filepath
                
            # Report progress with additional information
            progress_callback.emit(int((index + 1) / num_materials * 100), materialName)
        
        self.materials_data = materials_data
        # [print(f"Material: {k}, Data: {v}\n") for k, v in materials_data.items()]
        return materials_data
    
    def get_material_data(self, material_name):
        """ Get the data for a specific material """
        return self.materials_data.get(material_name, None)