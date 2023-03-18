'''
https://leetcode.com/problems/design-browser-history/description/
'''

class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cursor = 0
        self.bound = 0


    def visit(self, url: str) -> None:
        self.cursor += 1
        if self.cursor == len(self.history):
            self.history.append(url)
        else:
            self.history[self.cursor] = url
        self.bound = self.cursor

    def back(self, steps: int) -> str:
        self.cursor = max(self.cursor - steps, 0)

        return self.history[self.cursor]
        

    def forward(self, steps: int) -> str:
        self.cursor = min(self.cursor + steps, self.bound)

        return self.history[self.cursor]
        

if __name__ == "__main__":
    bh = BrowserHistory("leetcode.com")
    
    assert None == bh.visit("google.com")
    assert None == bh.visit("facebook.com")
    assert None == bh.visit("youtube.com")
    assert "facebook.com" == bh.back(1)
    assert "google.com" == bh.back(1)
    assert "facebook.com" == bh.forward(1)
    assert None == bh.visit("linkedin.com")
    assert "linkedin.com" == bh.forward(2)
    assert "google.com" == bh.back(2)
    assert "leetcode.com" == bh.back(7)


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)