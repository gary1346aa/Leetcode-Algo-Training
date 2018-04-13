class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        unit = 0
        line = 1
        for s in S:
            if unit + widths[ord(s) - 97] > 100:
                line += 1
                unit = widths[ord(s) - 97]
            else:
                unit += widths[ord(s) - 97]
                
        return [line,unit]