class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        temp = 0
        
        for i in s:
            result += roman[i]

            if temp and roman[temp] < roman[i]:
                result -= 2 * roman[temp]

            temp = i

        return result
            