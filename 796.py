class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        ind = 0
        while(ind != len(A)):

            d = ind
            ind = B[ind+1:].find(A[0])
            if (ind == -1):
                break
            else:
                ind += d + 1

            if (B[ind:]+B[0:ind] == A) == True:
                break

        return B[ind:]+B[0:ind] == A