import json
from storeConfig import StorefrontConfig

class FileController:
    @staticmethod
    # file_name (str): path to json file
    def read_file(file_name):
        with open(file_name) as f:
            data = json.load(f)
            return StorefrontConfig(data)

    @staticmethod
    def write_file(obj, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(obj, json_file)
