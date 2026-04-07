class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def perform(num1, num2, operator) -> int:
            if operator == "+":
                return num1 + num2
            if operator == "-":
                return num1 - num2
            if operator == "*":
                return num1 * num2
            if operator == "/":
                return int(num1 / num2)


        operators = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
                continue

            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(perform(num1, num2, t))

        
        return stack[-1]
            
            
            


        

