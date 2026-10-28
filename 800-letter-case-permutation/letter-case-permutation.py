class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []

        def backtrack(index, path):
            while index < len(s) and s[index].isdigit():
                path += s[index]
                index += 1
            
            if index == len(s):
                result.append(path)
                return 

            backtrack(index+1, path+s[index].lower())
            backtrack(index+1, path+s[index].upper())
        
        backtrack(0, "")

        return result