class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        res = ''
        
        for w in s:
            res += w[::-1] + " "
        
        return res[:-1]