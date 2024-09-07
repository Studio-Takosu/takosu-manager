# pbr_model.py

import sys
sys.path.append('src/modules/utils')
import os
import json
from worker import Worker

class PBRModel:
    def __init__(self, threadpool):
        self.material_names = []
        self.materials_data = {}
        self.percent_loaded = 0
        self.threadpool = threadpool  # Threadpool for managing worker threads

    def load_data(self):
        """ Initialize material data loading in a worker thread """
        worker = Worker(self._load_data_worker)
        worker.signals.progress.connect(self.report_progress)
        worker.signals.result.connect(self.on_data_loaded)
        worker.signals.finished.connect(self.on_finished_loading)
        self.threadpool.start(worker)

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
            matDirPath = os.path.join(dirPath, materialName)
            for file in os.listdir(matDirPath):
                if file.endswith('.json'):
                    with open(os.path.join(matDirPath, file), 'r') as f:
                        materials_data[materialName] = json.load(f)
                elif file.endswith('.png'):
                    materials_data[materialName] = {'image': os.path.join(matDirPath, file)}
            
            # Report progress
            progress_callback.emit(int((index + 1) / num_materials * 100))

        return materials_data

    def report_progress(self, progress):
        print(f"Loading progress: {progress}%")

    def on_data_loaded(self, materials_data):
        self.materials_data = materials_data
        print("Material data loaded successfully.")

    def on_finished_loading(self):
        print("Material loading finished.")