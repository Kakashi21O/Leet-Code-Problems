class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            l = (start + end) // 2

            if nums[l] == target:
                return l
            elif nums[l] > target:
                end = l - 1
            else:
                start = l + 1

        return start