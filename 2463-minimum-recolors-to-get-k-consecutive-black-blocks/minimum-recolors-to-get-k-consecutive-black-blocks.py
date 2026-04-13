class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        numr = blocks[:k].count("W")
        minr = numr
        for r in range(k, len(blocks)):
            l = r - k + 1

            if blocks[r] == "W":
                numr += 1
            if blocks[l - 1] == "W":
                numr -= 1
            
            minr = min(minr, numr)
        
        return minr
