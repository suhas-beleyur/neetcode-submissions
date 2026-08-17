class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        maxEle = nums[0]

        for i, num in enumerate(nums):
            if counter == 0:
                maxEle = num
                
            if maxEle != num:
                counter-=1
                continue
            counter+=1

        return maxEle

