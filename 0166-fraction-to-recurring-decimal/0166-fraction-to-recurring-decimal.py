class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = ""
        
        # Handle negative sign
        if (numerator < 0) ^ (denominator < 0):
            result += "-"
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Get the whole number part
        whole_part = numerator // denominator
        result += str(whole_part)
        
        remainder = numerator % denominator
        if remainder == 0:
            return result
        
        result += "."
        remainder_positions = {}
        
        while remainder != 0:
            if remainder in remainder_positions:
                # Insert parentheses for repeating part
                pos = remainder_positions[remainder]
                result = result[:pos] + "(" + result[pos:] + ")"
                return result
            
            remainder_positions[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator
        
        return result
