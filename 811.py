class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}

        for elements in cpdomains:
            a = int(elements.split(' ')[0])
            b = elements.split(' ')[1].split('.')
            for i in range(len(b)):
                tmp = b[i]
                for j in range(i + 1,len(b)):
                    tmp = tmp + '.' + b[j]
                if tmp in dict:
                    dict[tmp] += a
                else:
                    dict[tmp] = a

        out = []
        for key, val in dict.items():
            out.append(str(dict[key]) + " " + key)

        return out