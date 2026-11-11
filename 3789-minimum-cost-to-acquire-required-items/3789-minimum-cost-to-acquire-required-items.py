class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Option 1: Buy only type 1 and type 2 items separately
        opt1 = need1 * cost1 + need2 * cost2
        
        # Option 2: Buy only type 3 items to cover the larger requirement
        opt2 = max(need1, need2) * costBoth
        
        # Option 3: Cover the overlapping needs with type 3, and the remainder with single items
        common = min(need1, need2)
        opt3 = common * costBoth + (need1 - common) * cost1 + (need2 - common) * cost2
        
        return min(opt1, opt2, opt3)
