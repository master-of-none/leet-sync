class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}

        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        for c in t:
            if c not in hashmap or hashmap[c] == 0:
                return c
            else:
                hashmap[c] -= 1
        
        return ""
        