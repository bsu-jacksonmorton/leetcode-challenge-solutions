    def bestClosingTime(self, customers: str) -> int:
        res = 0
        profit = 0
        curr = 0
        for i in range(len(customers)):
            if customers[i] == "Y":
                curr += 1
            else:
                curr -= 1
            if curr > profit:
                res = i + 1
                profit = curr
        return res
