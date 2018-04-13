class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        digits = []
        for i in range(1, 7, 2):
            digits.append(int(color[i+1],16) - int(color[i],16))

        out = []
        for i in range(3):
            if digits[i] > 8:
                out.append(hex(int(color[1+2*i],16)+1).split('x')[-1])
            elif abs(digits[i]) <= 8:
                out.append(hex(int(color[1+2*i],16)).split('x')[-1])
            else:
                out.append(hex(int(color[1+2*i],16)-1).split('x')[-1])

        return '#' + out[0] + out[0] + out[1] + out[1] + out[2] + out[2]