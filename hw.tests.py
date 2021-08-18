import hw

class TestInput:
    def TestInpFormats(self, func):
        lis = [
            123, "aB", "123", "[]", "d"*90
        ]
        for l in lis:
            func(l)
        return 'All passed' #otherwise error will throwed above
    
test = TestInput()
ob = hw.Hw('letter is ')
print(test.TestInpFormats(ob.print)) #tested function