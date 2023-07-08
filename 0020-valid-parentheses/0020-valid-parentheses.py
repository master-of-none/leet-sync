class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
        