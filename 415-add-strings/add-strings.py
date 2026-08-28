class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = [0] * (max(len(num1), len(num2)) + 1) # [0 1 3 1]
        d = len(res) - 1 # 1
        
        d1 = len(num1) - 1 # -1
        d2 = len(num2) - 1 # -1
    ## sum 
        while d1 >= 0 or d2 >= 0:
            if d1 >= 0:
                res[d] += int(num1[d1])
                d1 -= 1

            if d2 >= 0:
                res[d] += int(num2[d2])
                d2 -= 1
        
            if res[d] > 9:
                res[d] -= 10
                res[d - 1] += 1
                # resStr[0] = str(sum)

            d -= 1

        resStr = ""
        for n in res:
            resStr += str(n)

        if resStr[0] == "0":
            return resStr[1:]
        
        return resStr
