MOD = 10**9 + 7

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)  # dp[i] = number of people who learn secret on day i
        dp[1] = 1

        shareable = 0  # how many people can share today

        for day in range(2, n + 1):
            # add those who become able to share today
            if day - delay >= 1:
                shareable = (shareable + dp[day - delay]) % MOD
            # remove those who forget today
            if day - forget >= 1:
                shareable = (shareable - dp[day - forget]) % MOD
            dp[day] = shareable  # new people learning today

        # Count people who still remember on day n
        ans = sum(dp[max(1, n - forget + 1): n + 1]) % MOD
        return ans
