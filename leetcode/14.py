class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=""
        if (len(strs)==0):
            return answer
        
        if (len(strs)==1):
            return strs[0]
        for i in range(len(min(strs))):
            s=strs[0][i]
            fleg=False
            for j in strs:
                if j[i]==s:
                    fleg=True
                else:
                    fleg=False
                    break
            if (fleg):
                answer+=s
            else:
                break
        return answer