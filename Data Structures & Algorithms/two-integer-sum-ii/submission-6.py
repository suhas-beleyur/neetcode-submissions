class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        nums = {}

        for i, num in enumerate(n):
            temp = target - num

            if temp in nums:
                return [nums[temp], i + 1]

            nums[num] = i + 1
        return []
