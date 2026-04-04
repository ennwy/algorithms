class Solution:
    def isHappy(self, n: int) -> bool:

        def get_squared_sum(n: int) -> int:
            s = 0
            last_digit = 0

            while n != 0:
                last_digit = n % 10
                s += last_digit * last_digit
                n = n // 10
            
            return s

        seen = set()
        s = get_squared_sum(n)

        seen.add(s)

        while s != 1:
            s = get_squared_sum(s)

            if s in seen:
                return False

            seen.add(s)

        return s == 1