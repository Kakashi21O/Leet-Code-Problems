class Solution(object):
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        r = ""

        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            total = x + y + carry
            r += str(total % 2)
            carry = total // 2

            i -= 1
            j -= 1

        return r[::-1]
        