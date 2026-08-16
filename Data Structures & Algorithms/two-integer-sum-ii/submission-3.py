class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l, r = 0, len(n) - 1

        while l < r:
            cur_sum = n[l] + n[r]

            if cur_sum < target:
                l += 1

            elif cur_sum > target:
                r -= 1

            else:
                return [l + 1, r + 1]

        return []
