class Solution(object):
    def longestCommonPrefix(self, strs):
        
        prefix = ""

        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            temp = True

            for j in strs[1:]:
                if i >= len(j) or strs[0][i] != j[i]:
                    temp = False
                    break

            if temp:
                prefix += strs[0][i]
            else:
                break

        return prefix