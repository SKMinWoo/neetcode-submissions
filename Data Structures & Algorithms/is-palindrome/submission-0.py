class Solution:
    def isPalindrome(self, s: str) -> bool:
        backwards = []
        forwards = []

        
        for i in range(len(s) -1, -1, -1):
            if s[i].isalnum():
                backwards.append(s[i].lower())
        
        for i in range(len(s)):
            if s[i].isalnum():
                forwards.append(s[i].lower())
        
        if backwards == forwards:
            return True
        
        return False