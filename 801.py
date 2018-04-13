class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n0 = 0
        s0 = 1
        for i in range(len(A) - 1):
            n1 = 1001
            s1 = 1001
            if A[i] < A[i+1] and B[i] < B[i+1]:
                n1 = min(n1,n0)
                s1 = min(s1,s0+1)
            if A[i] < B[i+1] and B[i] < A[i+1]:
                n1 = min(n1,s0)
                s1 = min(s1,n0+1)
            n0 = n1
            s0 = s1
            
        return min(n1,s1)