from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack = []
        for num in nums:
            while stack and gcd(stack[-1], num) > 1:
                prev = stack.pop()
                num = prev * num // gcd(prev, num)
            stack.append(num)
        return stack
