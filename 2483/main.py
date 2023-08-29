class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pre = 0
        post = 0
        # build the initial postfix
        for c in customers:
            if c == "Y":
                post += 1
        res = 0
        penalty = post
        for i in range(len(customers)):
            c = customers[i]
            if c == "N":
                pre += 1
            if c == "Y":
                post -= 1
            curr_pen = pre + post
            if curr_pen < penalty:
                res = i + 1
                penalty = curr_pen
        return res
