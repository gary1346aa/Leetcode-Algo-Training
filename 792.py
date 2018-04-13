class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        cnt = 0
        for word in words:
            ind = 0
            for char in word:
                find = S[ind:].find(char)
                if find == -1:
                    break
                else:
                    ind = (ind == 0) * (find + 1) + (ind != 0) * (find + ind + 1)

            if find != -1:
                cnt += 1

        return cnt
