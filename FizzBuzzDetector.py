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
        overlapCount = 0
        substrCharCount = self.getLen(substr)
        stringCharCount = self.getLen(string)
        if not stringCharCount or not substrCharCount:
            return 0 #if length input is 0
        stringCur = 0
        while True:
            if string[stringCur] == substr[0]:
                if string[stringCur:stringCur+substrCharCount] == substr:
                    stringCur += substrCharCount
                    overlapCount += 1
            if stringCur >= stringCharCount-1: #variable used once, but reads every iteration
                break
            stringCur += 1
        return overlapCount
        