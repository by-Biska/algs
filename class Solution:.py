from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        my_list = []

        for i in range(len(s)):
            if s[i] in ('[', '(', '{'):
                my_list += s[i]
            else:
                if len(my_list) == 0:
                    return False
                if s[i] == ']' and my_list[-1] == '[':
                    my_list.pop()
                elif s[i] == ')' and my_list[-1] == '(':
                    my_list.pop()
                elif s[i] == '}' and my_list[-1] == '{':
                    my_list.pop()
                else:
                    return False
        if len(my_list) == 0:
            return True
        else:
            return False

solution = Solution()
s = "(])"
result = solution.isValid(s)
print(f"Результат для {s}: {result}")