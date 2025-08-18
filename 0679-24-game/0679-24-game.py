

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6
        
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON
            
            # Pick any two numbers and try all operations
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    
                    next_nums = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            next_nums.append(nums[k])
                    
                    # Try all operations
                    for val in self.compute(nums[i], nums[j]):
                        next_nums.append(val)
                        if solve(next_nums):
                            return True
                        next_nums.pop()
            
            return False
        
        return solve(cards)
    
    def compute(self, a, b):
        results = [a + b, a - b, b - a, a * b]
        if abs(b) > 1e-6:  # avoid divide by zero
            results.append(a / b)
        if abs(a) > 1e-6:
            results.append(b / a)
        return results


# Example usage:
sol = Solution()
print(sol.judgePoint24([4, 1, 8, 7]))  # True, because (8-4)*(7-1)=24
print(sol.judgePoint24([1, 2, 1, 2]))  # False
