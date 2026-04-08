from typing import *

class Solution:
    def maxPower(self, s: str) -> int:
        max_counter = counter = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                counter += 1
                if counter > max_counter:
                    max_counter = counter
            else:
                counter = 1
        return max_counter

solution = Solution()
s = "abbcccddddeeeeedcba"
result = solution.maxPower(s)
print(f"Результат для {s}: {result}")