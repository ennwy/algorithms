class BrowserHistory:
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        while len(self.stack) > self.curr + 1:
            self.stack.pop()
        
        self.stack.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        back = self.curr - steps
        if back < 0:
            self.curr = 0
        else:
            self.curr = back

        return self.stack[self.curr]

    def forward(self, steps: int) -> str:
        nxt = self.curr + steps
        if nxt >= len(self.stack):
            self.curr = len(self.stack) - 1
        else:
            self.curr = nxt
        
        return self.stack[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)