class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        p1 = inf
        p2 = inf
        for price in prices:
            if price <= p1:
                p2 = p1
                p1 = price
            else:
                p2 = min(p2, price)
        return money if money - (p1+p2) < 0 else money - (p1+p2)
