class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def isPalindrome(s,l,r):
            nonlocal res, resLen
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l)+1 > resLen:
                    res = s[l:r+1]
                    resLen = (r-l) + 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # For odd length
            l, r = i, i
            isPalindrome(s,l,r)

            # For Even length
            l, r = i, i+1
            isPalindrome(s,l,r)
        
        return res