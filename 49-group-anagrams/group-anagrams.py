class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for l in s:
                count[ord(l) - 97] += 1
            
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())