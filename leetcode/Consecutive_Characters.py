class Solution:
    def maxPower(self, s: str) -> int:
        conti=' '
        max =1
        count =1
        for i in s:
            if i==conti:
                count+=1
                if max < count:
                    max= count
            else:
                count=1
                conti=i
        return max
