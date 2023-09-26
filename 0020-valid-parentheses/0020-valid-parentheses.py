class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{", ")":"(", "]":"["}
        stack = []

        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                
                else:
                    return False
                
            else:
                stack.append(c)
        
        return True if not stack else False
        