import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # **Sort arr2 to enable binary search**
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find the insertion point for x in arr2
            idx = bisect.bisect_left(arr2, x)
            
            # Check the element at the insertion point (greater than or equal to x)
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                continue
                
            # Check the element just before the insertion point (less than x)
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                continue
                
            # If no element is within distance d, increment the count
            distance_value += 1
            
        return distance_value
