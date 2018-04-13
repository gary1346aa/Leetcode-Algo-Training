class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def count(A):
            cnt = []
            i = 0
            while i < len(A):
                cnt.append([A[i],1])
                while i < len(A) - 1:
                    if A[i+1] == A[i]:
                        cnt[-1][1] += 1
                        i += 1  
                    else:
                        break
                i += 1
            return cnt

        s = count(S)
        out = 0
        for word in words:
            w = count(word)
            if (len(w) == len(s)):
                test = True
                for i in range(len(s)):
                    if w[i][0] != s[i][0]:
                        test = False
                        break
                    else:
                        if w[i][1] > s[i][1]:
                            test = False
                            break
                        elif w[i][1] < s[i][1]:
                            if s[i][1] == 2:
                                test = False
                                break

                if test == True:
                    out += 1

        return out