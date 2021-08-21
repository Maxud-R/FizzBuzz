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
               'BuzBuzz zzz': 1,
               'Bu zz B u z z B uzz': 0
               }
        for st in dic:
            result = self.ob.getOverlappings(st,'Buzz')
            assert  result == dic[st], 'testGetOverlappings in string:"'+st+'"\nFound '+str(result)+' concidences, instead of '+str(dic[st])
        print('TestFBDetector All passed') #otherwise error will throwed above
    def testGetLen(self):
        dic2 = {'abc': 3,
                'abcdt': 5,
                '12': 2,
                'IIS': 3,
                'AAA     D': 9,
                '': 0,
                'ok'*100: 200
                }
        for st in dic2:
            result = self.ob.getLen(st)
            assert result == dic2[st],  'testGetLen in string: "'+st+'"\nMeasured length is '+str(result)+', instead of '+str(dic2[st])
        print('TestGetLen All passed')
test = FBDTest()
test.testGetOverlappings()
test.testGetLen()