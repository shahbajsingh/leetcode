class MergeSort:
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
        
        # copy data to temp arrays
        for i in range(0, n1):
            L[i] = arr[l + i]
            
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
            
        # merge temp arrays back into arr[l..r]
        i = 0       # initial index of first subarray
        j = 0       # initial index of second subarray
        k = l       # initial index of merged subarray
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        # copy remaining elements (if exist) of L[]
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            
        # copy remaining elements (if exist) of R[]
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            
    def mergeSort(self, arr, l, r):
        if l < r:
            # same as (l+r) // 2 but avoids overflow
            m = l + (r - l) // 2
            
            # sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)
            
if __name__ == '__main__':
    m = MergeSort()
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    
    print('Before merge sort: ')
    for i in range(n):
        print(arr[i], end=' ')
    print()
    
    m.mergeSort(arr, 0, n-1)
    
    print('After merge sort: ')
    for i in range(n):
        print(arr[i], end=' ')
    
    print()