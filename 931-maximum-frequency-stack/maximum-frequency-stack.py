class FreqStack:
    def __init__(self):
        self.nums = defaultdict(int)
        self.freq = []

    def push(self, val: int) -> None:
        self.nums[val] += 1

        if self.nums[val] > len(self.freq):
            self.freq.append([])
        
        self.freq[self.nums[val]-1].append(val)

    def pop(self) -> int:
        val = self.freq[-1].pop()
        self.nums[val] -= 1

        if not self.freq[-1]:
            self.freq.pop()
        
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()