class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for i in range(len(nums)):
            left = target - nums[i]
            if left in num_dict:
                return [num_dict[left], i]
            else:
                num_dict[nums[i]] = i
        return None
s = Solution()
print(s.twoSum([1, 2 , -1, -3, 0], 0))
