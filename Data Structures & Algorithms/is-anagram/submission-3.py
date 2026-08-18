class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}

        for letter in range(len(s)):
            counts[s[letter]] = counts.get(s[letter], 0) + 1
            counts[t[letter]] = counts.get(t[letter], 0) - 1
        
        for i in counts.values():
            if i != 0:
                return False
        
        return True