class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = n & 1          # get the last bit of n
            res = (res << 1) | bit
            n = n >> 1           # remove the last bit from n

        return res