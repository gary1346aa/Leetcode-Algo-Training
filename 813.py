class Solution:
    def largestSumOfAverages(self, A, K):

        DP = [[-1 for i in range(len(A))] for j in range(K)]

        P = [0]
        cum = 0
        for val in A:
            cum += val
            P.append(cum)

        for j in range(len(A)-1,K - 2,-1):
            DP[0][j] = (P[len(A)] - P[j])/ (len(A) - j)

        for i in range(1,K):
            for j in range(len(A) - i - 1,K - i - 2, -1):
                for k in range(j, len(A) - i):
                    DP[i][j] = max(DP[i][j], (P[k + 1] - P[j])/(k-j+1) + DP[i-1][k+1])
                    
        return DP[-1][0]