class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #selection sort

        for i in range(len(nums)):
            minn = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minn]:
                    minn = j
            nums[i], nums[minn] = nums[minn], nums[i]

        return nums