from file import File
from filesystem import FileSystem
from search import Search

if __name__ == '__main__':
    f1 = File('abc', 'txt', 10)
    f2 = File('cde', 'txt', 20)
    f3 = File('def', 'pdf', 30)
    f4 = File('ghi', 'py', 5)
    f5 = File('uvw', 'java', 10)
    
    directory_files = [f1, f2, f3, f4, f5]
    fileSystem = FileSystem('/', True, [], directory_files)
    
    print(Search(directory_files, {"NameFilter": "abc"}, fileSystem).find_files())  # ["abc"]
    print(Search(directory_files, {"SizeFilter": (10, ">=")}, fileSystem).find_files())  # ["abc", "cde", "def", "uvw"]
    print(Search(directory_files, {"ExtensionFilter": "java", "SizeFilter": (10, ">=")}, fileSystem, "OR").find_files())  # ["uvw"]