class Solution(object):
    def removeElement(self, nums, val):
        cout = 0
        for i in nums:
            if i == val:
                cout+=1
        for i in range(0,cout):
            nums.remove(val)

        