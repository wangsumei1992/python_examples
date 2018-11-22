"""选择排序法"""
class Solution:
    def xuanzepaixu(self, nums):
        for i in range(len(nums)):
            #print(i)
            max_index = 0
            for j in range(len(nums) - i):
                #print(j)
                if nums[max_index] < nums[j]:
                    max_index = j
                    print(nums)
            nums[max_index], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[max_index]
        return nums
a = Solution()
print(a.xuanzepaixu([1, 5, 3, 2]))


