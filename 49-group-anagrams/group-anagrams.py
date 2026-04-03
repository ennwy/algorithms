class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        offset = ord('a')

        for s in strs:
            count = [0] * 26

            for l in s:
                count[ord(l) - offset] += 1
            
            key = tuple(count)
            an = anagrams.get(key, [])
            an.append(s)
            anagrams[key] = an
        
        return list(anagrams.values())