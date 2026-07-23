class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            new = target - num

            if (target - num) in seen:
                return [seen[new], i]

            seen[num] = i
        