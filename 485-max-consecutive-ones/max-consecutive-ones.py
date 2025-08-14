from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        window = 0
        ans = 0
        
        for right in range(len(nums)):
            window += nums[right]  # Add current number to window sum
            
            # Shrink window if it contains a zero (for problems with flips)
            # For basic problem, you can skip this while loop
            
            while (right - left + 1) != window:  # Means there's at least one zero
                window -= nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)  # Update max length
        
        return ans
