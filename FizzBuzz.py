class FizzBuzzDetector:
    def getLen(self, astring): #length of substr, alternative for len()
        CurChar = 0
        while True: 
            try:
                CurChar += 1
                astring[CurChar]
            except IndexError:
                return CurChar
    #Принимает строку и выдаёт кол-во совпадений строки в подстроке, без встроенных функций.
    def getOverlappings(self, qstr, substr):
        OverlapCount = 0
        SubstrCharCount = self.getLen(substr)
        qstrCharCount = self.getLen(qstr)
        qstrCur = 0
        while True:
            substrCur = 0
            for char in substr:
                if qstr[qstrCur] != char: #если символ не соотв. текущему в подстроке
                    qstrCur += 1
                    break
                if char == substr[-1] and substrCur == SubstrCharCount-1: #если текущий символ - это последний симв. подстроки.
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