class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in strs:
                if len(j)<= i or j[i] != char:
                    return ans
            ans += char
        return ans