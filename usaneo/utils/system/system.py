import os 



class Os_File:
    def __init__(self, path, file):
        path_file = file
        flags = os.O_RDWR | os.O_CREAT
        mode = 0o666
        fd = os.open(path, flags, mode)