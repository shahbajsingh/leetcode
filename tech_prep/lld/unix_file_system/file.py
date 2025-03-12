class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size
        
    def get_name(self):
        return self.name
    
    def get_extension(self):
        return self.extension
    
    def get_size(self):
        return self.size