class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0          # начальный индекс самого длинного палиндрома
        max_len = 1        # длина самого длинного палиндрома (минимум 1)

        n = len(s)

        for i in range(n):
            # ----- Нечётный палиндром (центр в i) -----
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

            # ----- Чётный палиндром (центр между i и i+1) -----
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

        return s[start:start + max_len]

sol = Solution()
s = 'abc'
result = sol.longestPalindrome(s)
print(result)