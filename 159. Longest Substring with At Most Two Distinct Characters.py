from collections import Counter
class Solution:
    def longestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        result = 0
        window_state = Counter()
        for right in range(len(s)):
            window_state[s[right]] += 1
            while len(window_state) > 2:
                window_state[s[left]] -= 1
                if window_state[s[left]] == 0:
                    del window_state[s[left]]
                left += 1
            result = max(result, right - left + 1)
        return result



sol = Solution()
s = "f"
res = sol.longestSubstring(s)
print(res)
