class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        nums = {}

        for i, num in enumerate(n):
            temp = target - num

            if temp in nums:
                return [nums[temp] +1, i+1]
            
            nums[num] = i
        return []