class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        
        for ch in s:
            letters[ch] = letters.get(ch, 0) +1
        
        for ch in t:
            if ch not in letters:
                return False
            
            letters[ch] -= 1
            if letters[ch] < 0:
                return False
        
        return True