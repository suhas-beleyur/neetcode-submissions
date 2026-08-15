class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zerocount = nums.count(0)
        res = []

        for num in nums:
            if num == 0:
                continue
            product *= num
        
        for num in nums:
            if zerocount > 1:
                res.append(0)
            elif zerocount == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                # if product/num = 0
                res.append(product//num)
        
        return res