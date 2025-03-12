# represents file system with directories and files

class FileSystem:
    def __init__(self, name, isDir=False, subDirs=None, files=None):
        self.name = name
        self.isDir = isDir
        self.subDirs = subDirs if subDirs else []
        self.files = files if files else []
        
    def add_file(self, dir, subdir, file):
        pass
    
    def del_file(self, dir, subdir, file):
        pass