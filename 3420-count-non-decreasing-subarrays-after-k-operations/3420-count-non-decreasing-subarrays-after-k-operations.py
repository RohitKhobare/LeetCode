from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        # Monotonic deque storing [val, count] from right to left
        dq = deque()
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            curr = nums[l]
            cnt = 1
            
            # Merge elements to the right that are smaller than nums[l]
            # since they must all be raised to at least nums[l]
            while dq and dq[0][0] < curr:
                val, c = dq.popleft()
                cost += (curr - val) * c
                cnt += c
                
            dq.appendleft([curr, cnt])
            
            # Shrink the window from the right if operations exceed k
            while cost > k:
                # The rightmost element in the window corresponds to the back of the deque
                cost -= (dq[-1][0] - nums[r])
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
                
            # All subarrays starting at l and ending between l and r are valid
            ans += (r - l + 1)
            
        return ans
