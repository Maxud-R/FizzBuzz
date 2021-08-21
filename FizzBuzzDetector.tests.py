from FizzBuzzDetector import FizzBuzzDetector

class FBDTest:
    def __init__(self):
        self.ob = FizzBuzzDetector()
        
    def testGetOverlappings(self):
        dic = {'QFizze Buzz': 1,
               'aaaaBuzzbbbbBuzzccccBuzz ddddBuzzeeeeBuzz Fizz hhhhBuzz iiii': 6,
               '': 0,
               'jdske dfajeh fjskkk': 0,
               'BuzzBuzzBuzzBuzz': 4,
               'BuzBuzz zzz': 1, #the problem is here.
               'Bu zz B u z z B uzz': 0
               }
        for st in dic:
            assert self.ob.getOverlappings(st,'Buzz') == dic[st], 'TestFBDetector not ok with string:'+st
        print('TestFBDetector All passed') #otherwise error will throwed above
    def testGetLen(self):
        dic2 = {'abc': 3,
                'abcdt': 5,
                '12': 2,
                'IIS': 3,
                'AAA     D': 9
                }
        for st in dic2:
            assert self.ob.getLen(st) == dic2[st],  'TestGetLen not ok with string:'+st
        print('TestGetLen All passed')
test = FBDTest()
test.testGetOverlappings()
test.testGetLen()