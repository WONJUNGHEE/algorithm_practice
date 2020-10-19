class Solution:
    def getNoZeroIntegers(n):
        x=0
        while(1):
            x+=1
            xx=list(str(x))
            if "0" in xx:
                continue
            print(x)
            k=n-x
            g=list(str(k))
            if "0" in g:
                continue
            else:
                break
        
        return [x,k]

    print(getNoZeroIntegers(10000))
