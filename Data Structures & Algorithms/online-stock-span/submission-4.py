class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
    #    self.prices.append(price)
    #    count = 0
    #    for e in self.prices[::-1]:
    #        if e <= price:
    #            count += 1
    #        else:
    #            break
    #    return count
        span = 1

        while self.prices and self.prices[-1][0] <= price:
            span += self.prices[-1][1]
            self.prices.pop()
        self.prices.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)