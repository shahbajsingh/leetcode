class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.build(nums)
        
    def build(self, nums):
        '''Build segment tree.'''
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            
    def update(self, index, value):
        '''Update value at index.'''
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            
    def query(self, left, right):
        '''Sum in range [left, right).'''
        left += self.n
        right += self.n
        sum_ = 0
        while left < right:
            if left % 2:
                sum_ += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                sum_ += self.tree[right]
            left //= 2
            right //= 2
        return sum_
