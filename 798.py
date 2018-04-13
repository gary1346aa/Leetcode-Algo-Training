class Solution:
    
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        R = [0]*(len(A)+1)

        for index, value in enumerate(A):
            if value > index:
                R[index + 1] += 1
                R[len(A) - (value-index) + 1] -= 1
            else :
                R[0] += 1
                R[index - value + 1] -= 1
                R[index + 1] += 1
                

        Kmax = -1
        Kind = 0
        cur = 0
        for ind, val in enumerate(R):
            cur += val
            if cur > Kmax:
                Kmax = cur
                Kind = ind

                
        return Kind