class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        result = []  
        
        for a in range(1, n):
            b = n - a
            if "0" not in str(a) and "0" not in str(b):
                result.append(a)  
                result.append(b)   
                break              
        
        return result