class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]

        for i in tokens:
            if i not in operators:
                stack.append(int(i))

            elif stack:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    result = a + b
                    stack.append(result)
                elif i == "-":
                    result = a - b
                    stack.append(result)
                elif i == "*":
                    result = a * b
                    stack.append(result)
                elif i == "/":
                    result = int(a / b)
                    stack.append(result)

        return stack[-1]