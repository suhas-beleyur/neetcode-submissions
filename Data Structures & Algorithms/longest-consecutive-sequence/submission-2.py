class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, maxx = set(nums), 0

        for num in nums:
            if not num - 1 in nums:
                length = 1
                while num + length in nums:
                    length += 1
                maxx = max(length, maxx)
        return maxx
