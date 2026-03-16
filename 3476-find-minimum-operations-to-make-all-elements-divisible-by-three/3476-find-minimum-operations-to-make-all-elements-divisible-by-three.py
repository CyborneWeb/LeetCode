class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        for num in nums:
            operations += min(1, num%3)
        
        return operations