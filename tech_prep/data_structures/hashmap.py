class HashMap:
    def __init__(self):
        self.map = {}
        
    def put(self, key, value):
        '''Insert or update a key-value pair.'''
        self.map[key] = value
        
    def get(self, key):
        '''Retrieve a value by key.'''
        return self.map.get(key, None)  # return None if key not found
    
    def remove(self, key):
        '''Remove a key from the map.'''
        if key in self.map:
            del self.map[key]