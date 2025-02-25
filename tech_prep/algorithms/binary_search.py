import bisect

class BinarySearch:
    def binary_search_recursive(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            
            if arr[mid] == x: 
                return mid # element is in middle
            
            elif arr[mid] > x: # element is in left subarr
                return self.binary_search_recursive(arr, low, mid - 1, x)
            
            else: # element is in right subarr
                return self.binary_search_recursive(arr, mid + 1, high, x)
            
        else: # element not present
            return -1
        
    def binary_search_iterative(self, arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
        
        while low <= high:
            mid = (high + low) // 2
            
            if arr[mid] < x: # element is in right half
                low = mid + 1
                
            elif arr[mid] > x: # element is in left half
                high = mid - 1
                
            else: # element is the midpoint
                return mid 
            
        return -1 # element was not present
    
    def binary_search_bisect(self, arr, x):
        i = bisect.bisect_left(arr, x)
        if i != len(arr) and arr[i] == x:
            return i
        else: 
            return -1
        
        
if __name__ == '__main__':
    b = BinarySearch()
    arr = [2,3,4,10,40]
    x = 10
    
    # res = b.binary_search_recursive(arr, 0, len(arr) - 1, x)
    # res = b.binary_search_iterative(arr, x)
    res = b.binary_search_bisect(arr, x)
    
    msg = 'Element is at index {}'.format(res) if res != -1 else 'Element not found'
    print(msg)