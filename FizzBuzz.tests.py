import FizzBuzz

class FBTest:
    def __init__(self):
        self.ob = FizzBuzz.FizzBuzz()
        
    def TestFBDetector(self):
        dic = {'QFizze Buzz': 1}
        for st in dic:
            assert self.ob.FizzBuzzDetector(st) == dic[st], 'TestFBDetector not ok with string:'+dic[st]
        print('TestFBDetector All passed') #otherwise error will throwed above

test = FBTest()
test.TestFBDetector()
