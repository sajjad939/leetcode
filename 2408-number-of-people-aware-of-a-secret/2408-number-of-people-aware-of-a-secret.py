MOD = 10**9 + 7

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
      
        dp = [0] * (n + 1)
        dp[1] = 1
        
      
        pref = [0] * (n + 1)
        pref[1] = 1
        
        for i in range(2, n + 1):
           
            start = max(1, i - forget + 1)
            end = i - delay
            if end >= start:
            
                dp[i] = (pref[end] - pref[start - 1]) % MOD
            else:
                dp[i] = 0
            pref[i] = (pref[i - 1] + dp[i]) % MOD
        
      
        alive_start = max(1, n - forget + 1)
        ans = 0
        for i in range(alive_start, n + 1):
            ans = (ans + dp[i]) % MOD
        return ans
