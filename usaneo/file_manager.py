import os
import shutil
FILE_MANAGEMENT = os.path.isfile()
PATH = os.path()
=======
class FileManager:
    def __init__(self, base_path):
        self.base_path = base_path

    def read_file(self, filename):
        with open(os.path.join(self.base_path, filename), 'r') as file:
            return file.read()

    def write_file(self, filename, content):
        with open(os.path.join(self.base_path, filename), 'w') as file:
            file.write(content)

    def copy_file(self, src_filename, dest_filename):
        shutil.copy(os.path.join(self.base_path, src_filename), os.path.join(self.base_path, dest_filename))