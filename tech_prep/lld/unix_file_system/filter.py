from abc import ABC, abstractmethod

# abstract base class for filter
class Filter(ABC):
    @abstractmethod
    def match(self, file):
        pass
    
class NameFilter(Filter):
    def __init__(self, name):
        self.name = name
        
    def match(self, file):
        return file.get_name() == self.name
    
class SizeFilter(Filter):
    def __init__(self, props):
        self.size = props[0]
        self.operator = props[1]
        
    def match(self, file):
        return eval(f'{file.get_size()} {self.operator} {self.size}')
    
class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension
        
    def match(self, file):
        return file.get_extension() == self.extension