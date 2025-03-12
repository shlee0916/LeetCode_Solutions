'''
https://leetcode.com/problems/product-of-the-last-k-numbers/?envType=daily-question&envId=2025-02-14

Problem number: 1352
'''


class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.stream = [1]
        else:
            self.stream.append(self.stream[-1] * num)
        

    def getProduct(self, k: int) -> int:
        if len(self.stream) <= k:
            return 0
        else:
            return self.stream[-1] // self.stream[-k - 1]


if __name__ == "__main__":
    pn = ProductOfNumbers()

    for num in (3, 0, 2, 5, 4):
        pn.add(num)

    assert pn.getProduct(2) == 20
    assert pn.getProduct(3) == 40
    assert pn.getProduct(4) == 0

    pn.add(8)

    assert pn.getProduct(2) == 32


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)