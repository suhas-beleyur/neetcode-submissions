class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def countSort():
            count = {}

            minVal, maxVal = min(nums), max(nums)

            for num in nums:
                count[num] = count.get(num, 0) + 1

            index = 0
            for val in range(minVal, maxVal+1):
                if val not in count:
                    continue
                while count[val] > 0:
                    nums[index] = val
                    index+=1
                    count[val]-=1

        countSort()
        return nums