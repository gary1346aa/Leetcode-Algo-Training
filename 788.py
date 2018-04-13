class Solution:
    def rotatedDigits(self, N):

        s = []
        for i in range (1,N+1):
            s.append(str(i))

        cnt = 0
        for num in s:
            tmp = ''
            for d in num:
                if d == '0':
                    tmp += '0'
                elif d == '1':
                    tmp += '1'
                elif d == '2':
                    tmp += ('5')
                elif d == '3':
                    tmp += ('X')
                elif d == '4':
                    tmp += ('X')
                elif d == '5':
                    tmp += ('2')
                elif d == '6':
                    tmp += ('9')
                elif d == '7':
                    tmp += ('X')
                elif d == '8':
                    tmp += ('8')
                elif d == '9':
                    tmp += ('6')
            cnt += tmp.find('X') == -1 and tmp != num


        return cnt