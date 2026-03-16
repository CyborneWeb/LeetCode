class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        vsota = 0
        for operation in operations:
            if operation[1] == "-":
                vsota -= 1
            else:
                vsota += 1
        return vsota
        