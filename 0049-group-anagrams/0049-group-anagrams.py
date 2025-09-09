class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            freq = [0] * 26 
            for ch in word:
                freq[ ord(ch) - ord('a') ] += 1
            
            key = tuple(freq)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())                