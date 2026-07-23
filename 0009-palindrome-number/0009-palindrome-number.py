class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        temp = 0
        p = 0
        while num>0:
            temp = (temp*10) + (num%10)
            num = num//10

        if temp == x:
            return True
        else:
            return False            
