class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] # [5,10,-5]

        for a in asteroids:
            if stack and stack[-1] > 0 and a < 0:
                while stack and abs(a) > abs(stack[-1]) and stack[-1] > 0:
                    stack.pop()

                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif abs(a) == abs(stack[-1]):
                    stack.pop()

            else:
                stack.append(a)

        return stack

def signDiff(n1: int, n2: int) -> bool:
    if n1 >= 0:
        return n2 < 0
    return n2 >= 0


            


    
