from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                right = int(stack.pop())
                left = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(left + right)
                if tokens[i] == "-":
                    stack.append(left - right)
                if tokens[i] == "*":
                    stack.append(left * right)
                if tokens[i] == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
sol = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result = sol.evalRPN(tokens)
print(result)