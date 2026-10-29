class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x

        while r>=l:
            i = (l+r)//2
            if i*i == x:
                return i
            elif i*i <= x:
                l = i + 1
            elif i*i >= x:
                r = i - 1
        return r
            