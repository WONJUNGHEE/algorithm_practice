class Solution:
    def isPalindrome(self, x: int) ->bool :
        y=list(str(x))
        z=y[::-1]
        if(z==y):
            return True
        else:
            return False

print(Solution().isPalindrome(1))

