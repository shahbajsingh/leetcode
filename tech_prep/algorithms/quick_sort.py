class QuickSort:
    def partition(self, array, low, high):
        # choose rightmost element as pivot
        pivot = array[high]
        
        # ptr for greater element
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
    
    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)
            
if __name__ == '__main__':
    q = QuickSort()
    data = [1,7,4,1,10,9,-2]
    print('Array before quick sort: ')
    print(data)
    
    size = len(data)
    q.quickSort(data, 0, size - 1)
    
    print('Array after quick sort: ')
    print(data)
    