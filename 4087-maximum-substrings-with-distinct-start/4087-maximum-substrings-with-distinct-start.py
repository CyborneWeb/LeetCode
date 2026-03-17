class Solution:
    def maxDistinct(self, s: str) -> int:
        used = ""
        count = 0
        for char in s:
            if char not in used:
                count += 1

            used += char
        
        return count

        