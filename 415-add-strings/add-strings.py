class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ORD_ZERO = ord('0')
        out = []
        i, j = len(num1) - 1, len(num2) - 1
        total, carry = 0, 0

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += ord(num1[i]) - ORD_ZERO
                i -= 1
            if j >= 0:
                total += ord(num2[j]) - ORD_ZERO
                j -= 1
            
            carry = 0
            if total > 9:
                total -= 10
                carry = 1
            
            out.append(str(total))
        
        return "".join(reversed(out))
