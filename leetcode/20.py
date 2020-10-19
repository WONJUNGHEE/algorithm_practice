class Solution:
    def isValid(self, s: str) -> bool:
        closer=[]
        for i in s:
            if i=="(" or i=="[" or i=="{" :
                closer.append(i)
            else:
                if(len(closer)==0):
                    return False
                if i==")":
                    if closer.pop()!="(":
                        return False
                if i=="]":
                    if closer.pop()!="[":
                        return False
                if i=="}":
                    if closer.pop()!="{":
                        return False
        if(len(closer)>0):
            return False
        return True