from FizzBuzzDetector import FizzBuzzDetector

class FBDTest:
    def __init__(self):
        self.ob = FizzBuzzDetector()
        
    def TestFBDetector(self):
        dic = {'QFizze Buzz': 1}
        for st in dic:
            assert self.ob(st) == dic[st], 'TestFBDetector not ok with string:'+dic[st]
        print('TestFBDetector All passed') #otherwise error will throwed above

test = FBDTest()
test.TestFBDetector()