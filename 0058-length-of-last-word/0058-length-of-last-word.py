class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for letter in s[::-1]:
            if letter == " " and count == 0:
                continue
            elif letter == " " and count != 0:
                return count
            else:
                count += 1
        return count

