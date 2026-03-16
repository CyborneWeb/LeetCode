class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k #returns the remainder when dividing the sum of nums 

        