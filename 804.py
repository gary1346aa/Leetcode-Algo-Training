class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = []
        for word in words:
            tmp = ""
            for char in word:
                tmp  = tmp + trans[ord(char) - 97]
            code.append(tmp)


        def split(words,i):
            if len(words) == 0:
                return 0
            else:
                tmp = 0
                A = []
                B = []
                C = []
                D = []
                for word in words:
                    if i == len(word) - 1:
                        if word[i] == '.':
                            C.append(word)
                        else:
                            D.append(word)
                    else:
                        if word[i] == '.':
                            A.append(word)
                        else:
                            B.append(word)
                return (len(C)!= 0) + (len(D)!= 0) + split(A,i+1) + split(B,i+1)

        return split(code,0)