class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        total = 0

        for l, r in queries:
            steps = 0
            # skip zero since it requires no operations
            start = max(l, 1)

            while start <= r:
                # find the largest power of 4 (power = 4^k) such that power <= start
                power = 1
                k = 0
                while power * 4 <= start:
                    power *= 4
                    k += 1

                # current block is [power, power*4 - 1]
                block_end = power * 4 - 1
                # restrict to within [start, r]
                end = block_end if block_end <= r else r
                count = end - start + 1

                # each number in this block needs (k + 1) steps (divisions by 4 to reach zero)
                steps += count * (k + 1)

                # move to the next number after end
                start = end + 1

            # each operation applies to two single-number steps, so we compute ceil(steps/2)
            total += (steps + 1) // 2

        return total
