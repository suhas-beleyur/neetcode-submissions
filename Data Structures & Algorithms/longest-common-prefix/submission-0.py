class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        prefix=strs[0]
        for i in range(1, len(strs)):
            le = 0
            while le < min(len(strs[i]), len(prefix)):
                if prefix[le] != strs[i][le]:
                    break
                le+=1
            prefix = prefix[:le]
        return prefix