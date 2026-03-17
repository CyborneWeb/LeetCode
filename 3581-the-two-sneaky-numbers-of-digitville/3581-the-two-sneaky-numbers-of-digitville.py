class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky = []
        for num in nums:
            if nums.count(num) > 1 and num not in sneaky:
                sneaky.append(num)
        
        return sneaky
        