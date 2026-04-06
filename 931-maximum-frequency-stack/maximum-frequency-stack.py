class FreqStack:
    def __init__(self):
        self.nums = defaultdict(int)
        self.freq = [[], []]

    def push(self, val: int) -> None:
        self.nums[val] += 1

        f = self.nums[val]

        while len(self.freq) <= f:
            self.freq.append([])
        
        self.freq[f].append(val)

    def pop(self) -> int:
        val = self.freq[-1].pop()
        self.nums[val] -= 1

        while self.freq and not self.freq[-1]:
            self.freq.pop()
        
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()