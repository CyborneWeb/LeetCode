class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        vsota1 = 0
        vsota2 = 0

        for i in range(1, n+1):
            if i%m == 0:
                vsota2 += i
            else: 
                vsota1 += i

        return vsota1 - vsota2         
        