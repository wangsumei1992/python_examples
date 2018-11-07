class Paixu:
    def maopao(self, nums):
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    print(nums)
        return nums
a = Paixu()
print(a.maopao([5, 8, 2, 4]))