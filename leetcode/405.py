class Solution:
    def toHex(self, num: int) -> str:
        x=hex(num & (2**32-1))
        x=x[2:]
        return x 