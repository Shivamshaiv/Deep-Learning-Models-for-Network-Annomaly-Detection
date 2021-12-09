import pandas
import glob
import os

class IDSDataset(object):
    def __init__(self,root_folder,extentions):
        self.root_folder = root_folder
        self.extentions = extentions

    def get_data_paths(self):
        all_files = []
        for ext in self.extentions:
            datapath = os.join.path(f"{self.root_folder}",f"*.{ext}")
            for file in glob.glob(datapath):
                all_files.append(file)
        return all_files

class CIC2017Dataset(IDSDataset):
    def __init__(self,root_folder,extentions = ['csv']):
        super().__init__(root_folder,extentions)
        self.attacks = []
