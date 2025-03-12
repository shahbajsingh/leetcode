from filter import NameFilter, SizeFilter, ExtensionFilter

class Search:
    def __init__(self, dir, filters, fileSystem, condition=None):
        self.dir = dir
        self.filters = filters
        self.fileSystem = fileSystem
        self.condition = condition
        
    def check_conditions(self, file, instances, condition):
        if condition is None:
            return instances[0].match(file)
        elif condition == 'AND':
            return all(filter.match(file) for filter in instances)
        else: # condition == 'OR'
            return any(filter.match(file) for filter in instances)
        
    def find_files(self):
        queue = [self.fileSystem]
        res = []
        
        # create filter instances
        filter_classes = [globals()[filter_name](value) for filter_name, value in self.filters.items()]
        
        # BFS to traverse directories
        while queue:
            node = queue.pop(0)
            for file in node.files:
                if self.check_conditions(file, filter_classes, self.condition):
                    res.append(file.get_name())
            queue.extend(node.subDirs)
            
        return res