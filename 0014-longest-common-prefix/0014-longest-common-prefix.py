class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)

        while True:
            all_contain = True

            for st in strs:
                if not st.startswith(prefix):
                    prefix = prefix[:-1]
                    all_contain = False
                    break

            if all_contain:
                return prefix