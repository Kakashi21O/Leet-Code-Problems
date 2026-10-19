class Solution(object):
    def plusOne(self, digits):

        num = 0
        for i,v in enumerate(digits[::-1]):
            num += v * 10 ** i
        
        num += 1

        result_list = []

        for i in str(num):
            result_list.append(int(i))

        return result_list 


        