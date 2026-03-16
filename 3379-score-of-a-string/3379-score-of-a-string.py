class Solution:
    from itertools import pairwise
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for prev, next in pairwise(s):
            sum += abs(ord(prev) - ord(next))
        return sum
            
        