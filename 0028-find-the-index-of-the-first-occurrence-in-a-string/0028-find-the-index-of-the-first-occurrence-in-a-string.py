class Solution(object):
    def strStr(self, haystack, needle):
        l_hay = len(haystack)
        l_need = len(needle)

        for j in range(l_hay - l_need + 1):
            k = j
            i = 0

            while i < l_need and haystack[k] == needle[i]:
                k += 1
                i += 1

            if i == l_need:
                return j

        return -1