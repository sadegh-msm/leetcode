class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        wrd = strs[0]
        length = len(wrd)

        for a in strs[1:]:
            while wrd != a[0:length]:
                length -= 1
                if length == 0:
                    return ""
                wrd = wrd[0:length]

        return wrd
