class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def swap(s, i, j):
            lst = list(s);
            lst[i], lst[j] = lst[j], lst[i]
            return ''.join(lst)

        index = 0
        for s in S:
            for i in range(len(T)):
                if T[i] == s:
                    T = swap(T,i,index)
                    index += 1

        return T