class Solution:
    def alternatingSum(self, nums: List[int]) -> int:

        plus_sign = True
        sum = 0
        for num in nums:
            if plus_sign:
                sum += num
            else:
                sum -= num
            
            plus_sign = not plus_sign

        return sum

        