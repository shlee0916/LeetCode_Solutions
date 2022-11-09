'''
https://leetcode.com/problems/online-stock-span/description/
'''

class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        res = 1

        while self.prices and self.prices[-1][0] <= price:
            res += self.prices.pop()[1]

        self.prices.append((price, res))

        return self.prices[-1][1]


if __name__ == "__main__":
    stock_spanner = StockSpanner()

    assert stock_spanner.next(100) == 1
    assert stock_spanner.next(80) == 1
    assert stock_spanner.next(60) == 1
    assert stock_spanner.next(70) == 2
    assert stock_spanner.next(60) == 1
    assert stock_spanner.next(75) == 4
    assert stock_spanner.next(85) == 6