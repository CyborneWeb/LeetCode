class Solution:
    def minPartitions(self, n: str) -> int:
        largest = 0
        for char in n:
            if int(char) > largest:
                largest = int(char)
        
        return largest

        