class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in range(0,n+1):
            a,b = b,a+b
        return a

        