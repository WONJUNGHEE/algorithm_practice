class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0 
        start=""
        end=""
        count=1
        maxcount=0
        for i in s:
            for j in range(len(s)
            if start=="":
                start=i
            else:
                start+=i
                count+=1
                end=i
                if i in start:
                    start=end
                    end=""
                    count=1
                    
                if count >maxcount:
                    maxcount=count
        return maxcount
        


s="asb"

if "a" in s:
    print(s)