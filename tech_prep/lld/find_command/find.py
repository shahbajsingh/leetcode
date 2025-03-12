from abc import ABC, abstractmethod
from typing import List

# Composite Pattern: Base class for File and Directory
class FileSystemItem(ABC):
    def __init__(self, name: str, size: int = 0, extension: str=''):
        self.name = name
        self.size = size
        self.extension = extension
        
    @abstractmethod
    def isDirectory(self) -> bool:
        pass
    
    @abstractmethod
    def addChild(self, child: 'FileSystemItem'):
        pass
    
    @abstractmethod
    def getChildren(self) -> List['FileSystemItem']:
        pass
    
# File class: leaf node in Composite Pattern
class File(FileSystemItem):
    def __init__(self, name: str, size: int, extension: str = ''):
        super().__init__(name, size, extension)
        
    def isDirectory(self) -> bool:
        return False
    
    def addChild(self, child: 'FileSystemItem'):
        raise NotImplementedError('Cannot add child to file.')
    
    def getChildren(self) -> List['FileSystemItem']:
        return []
    
    def __repr__(self):
        return f"File(name={self.name}, size={self.size}, extension={self.extension})"
    
# Directory class: composite in Composite Pattern
class Directory(FileSystemItem):
    def __init__(self, name: str):
        super().__init__(name)
        self.children = []
        
    def isDirectory(self) -> bool:
        return True
    
    def addChild(self, child: 'FileSystemItem'):
        self.children.append(child)
        
    def getChildren(self) -> List['FileSystemItem']:
        return self.children
    
# Strategy Pattern: Filter interface
class Filter(ABC):
    @abstractmethod
    def apply(self, item: 'FileSystemItem') -> bool:
        pass
    
# Size Filter: Concrete strategy
class SizeFilter(Filter):
    def __init__(self, size: int):
        self.size = size
        
    def apply(self, item: 'FileSystemItem') -> bool:
        return item.size > self.size
    
# Extension Filter: Concrete strategy
class ExtensionFilter(Filter):
    def __init__(self, extension: str):
        self.extension = extension
        
    def apply(self, item: 'FileSystemItem') -> bool:
        return self.extension == item.extension
    
# Iterator Pattern: Directory Iterator
class DirectoryIterator:
    def __init__(self, root: 'FileSystemItem'):
        self.stack = [root] if root.isDirectory() else []
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration
        curr = self.stack.pop()
        
        if curr.isDirectory():
            for child in curr.getChildren():
                self.stack.append(child)
                
        return curr
    
# File System: Responsible for adding filters and traversing file system
class FileSystem:
    def __init__(self):
        self.filters = []
        
    def addFilter(self, filter: Filter):
        if isinstance(filter, Filter):
            self.filters.append(filter)
            
    def traverse(self, root: 'FileSystemItem') -> List['FileSystemItem']:
        result = []
        for item in DirectoryIterator(root):
            if all(filter.apply(item) for filter in self.filters):
                result.append(item)
                
        return result
    
# Example Usage
f1 = File("StarTrek.txt", 5, "txt")
f2 = File("StarWars.xml", 10, "xml")
f3 = File("JusticeLeague.txt", 15, "txt")
f4 = File("IronMan.txt", 9, "txt")
f5 = File("Spock.jpg", 1, "jpg")
f6 = File("BigBangTheory.txt", 50, "txt")

root = Directory("root")
sub_dir = Directory("sub_dir")
root.addChild(sub_dir)
root.addChild(f1)
root.addChild(f2)

sub_dir.addChild(f3)
sub_dir.addChild(f4)
sub_dir.addChild(f5)
sub_dir.addChild(f6)

# Create Filters (Strategy Pattern)
size_filter = SizeFilter(5)  # Find files greater than 5MB
extension_filter = ExtensionFilter("txt")  # Find .txt files

# Initialize FileSystem and add filters
fs = FileSystem()
fs.addFilter(size_filter)
fs.addFilter(extension_filter)

# Traverse the directory and find matching files
matching_files = fs.traverse(root)
print("Matching Files:", matching_files)