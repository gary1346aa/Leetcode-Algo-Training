class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        tmpl = 0
        tmpr = 0
        cntl = 0
        cntr = 0
        for i in range(len(A)):
            if A[i] > R:
                cntr += (i-tmpr)*(i-tmpr+1)/2
                tmpr = i + 1
            if A[i] > L - 1:
                cntl += (i-tmpl)*(i-tmpl+1)/2
                tmpl = i + 1
            if i == len(A) - 1:
                cntr += (i-tmpr+1)*(i-tmpr+2)/2
                cntl += (i-tmpl+1)*(i-tmpl+2)/2
                
        return int(cntr - cntl)