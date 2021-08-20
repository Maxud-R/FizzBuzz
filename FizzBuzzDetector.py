class FizzBuzzDetector:
    def getLen(self, astring): #length of substr, alternative for len()
        CurChar = 0
        while True: 
            try:
                CurChar += 1
                astring[CurChar]
            except IndexError:
                return CurChar
    #In: string and substring. Out: number of concidences substring in the string
    def getOverlappings(self, qstr, substr):
        OverlapCount = 0
        SubstrCharCount = self.getLen(substr)
        qstrCharCount = self.getLen(qstr)
        qstrCur = 0
        while True:
            substrCur = 0
            for char in substr: #This two cycles checks finds substring in string moving char by char. Optimization needed
                if qstr[qstrCur] != char: #если текущий символ строки не соотв. текущему символу подстроки
                    qstrCur += 1
                    break
                if substrCur == SubstrCharCount-1: #if the current char is the last in substring
                    OverlapCount += 1
                    print(qstrCur)
                    qstrCur += 1
                    break
                substrCur += 1
                qstrCur += 1
            if qstrCur >= qstrCharCount-1:
                break
        return OverlapCount
print(FizzBuzzDetector().getOverlappings('ABCABCABC ABCABC ABCABC ABC', 'ABC'))