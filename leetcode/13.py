class Solution:
    def romanToInt(self, s: str) -> int:
        regDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        uniqueDict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        result = 0
        i = 0
        while i < len(s):
            
            if len(s)-i >= 2 and s[i:i+2] in uniqueDict:
                result += uniqueDict[s[i:i+2]]
                i += 2
            else:
                result += regDict[s[i]]
                i += 1
        return answer