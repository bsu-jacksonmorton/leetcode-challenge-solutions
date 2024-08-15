class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0}
        cost = 5
        for bill in bills:
            if bill - cost > 0:
                owed_monies = bill - cost
                while owed_monies and owed_monies >= 10 and change[10]:
                    change[10] -= 1
                    owed_monies -= 10
                while owed_monies and owed_monies >= 5 and change[5]:
                    change[5] -= 1
                    owed_monies -= 5
                if owed_monies: return False # all outta change :(
            if bill == 5 or bill == 10:
                change[bill] += 1
        return True
            
