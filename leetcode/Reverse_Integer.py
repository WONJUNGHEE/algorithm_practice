class Solution:
    def reverse(x):
        number= list(str(x))
        
        if(x<0):
            miuns=number[1::]
            miuns=miuns[::-1]
            x=int(''.join(miuns))
            if (x>=2**31-1):
                return 0
            return '-'+str(x) 
        number=number[::-1]
        if (int(''.join(number))>=2**31-1):
            return 0
        return int(''.join(number))


print(Solution.reverse(2**31+2))


print(2**31)