from FizzBuzz import FizzBuzz

class FBTest:
    def __init__(self):
        self.ob = FizzBuzz()
        
    def testReplace(self):
        dic = {'aaaaabbbbbccccc dddddeeeee ffgg hhhhh iiii': 'aaaaBuzzbbbbBuzzccccBuzz ddddBuzzeeeeBuzz Fizz hhhhBuzz iiii',
               'djh djh kej kkfj w er q': 'djh djh Fizz kkfj w Fizz q',
               'q e r f': 'q e Fizz f',
               'ieudjerty': 'ieudBuzzerty'
               }
        for st in dic:
            assert self.ob.replace(st) == dic[st], 'TestReplace not ok with string:'+dic[st]
        #Testing error raising
        lis = ['ase', 'AAABBBC', '2387182Gs dasb', '2387182', 'a'*101]
        for a in lis:
            try:
                self.ob.replace(a)
                print('Not Ok, string was: '+a+', but error doesn`t throwed')
                return 1
            except Exception:
                pass
        print('OK: Exception was throwed on all incorrect strings')
        print('TestFBDetector All passed') #otherwise error will throwed above
        return 0
test = FBTest()
test.testReplace()
