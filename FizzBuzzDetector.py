class FizzBuzzDetector:
    def getLen(self, astring): #length of substr, alternative for len()
        CurChar = 0
        if not astring:
            return 0
        while True: 
            try:
                CurChar += 1
                astring[CurChar]
            except IndexError:
                return CurChar
    #In: string and substring. Out: number of concidences substring in the string
    def getOverlappings(self, string, substr):
        OverlapCount = 0
        SubstrCharCount = self.getLen(substr)
        stringCharCount = self.getLen(string)
        if not stringCharCount or not SubstrCharCount:
            return 0
        stringCur = 0
        while True:
            substrCur = 0
            for char in substr: #This two cycles checks finds substring in string moving char by char. Optimization needed
                if string[stringCur] != char: #если текущий символ строки не соотв. текущему символу подстроки
                    stringCur += 1
                    break
                if substrCur == SubstrCharCount-1: #if the current char is the last in substring
                    OverlapCount += 1
                    stringCur += 1
                    break
                substrCur += 1
                stringCur += 1
            if stringCur >= stringCharCount-1:
                break
        return OverlapCount