class Solution:
    def sumZero(self, n: int) -> list[int]:
        result = []
        
        # Make pairs: (1, -1), (2, -2), ..., until we reach n//2 pairs
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
        
        # If n is odd, add 0 to maintain the sum as zero
        if n % 2 == 1:
            result.append(0)
        
        return result
