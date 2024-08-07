class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ()
        for i in word1:
            result = word1.append(i)
        for j in word2:
            result = word2.append(j)

        return result 


