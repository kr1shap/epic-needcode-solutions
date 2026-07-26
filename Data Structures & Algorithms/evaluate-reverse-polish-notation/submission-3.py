class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                else:  # division
                    stack.append(int(x / y))  # truncates toward zero
        return stack[0]
