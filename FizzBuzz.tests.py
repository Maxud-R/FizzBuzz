from FizzBuzz import FizzBuzz

class FBTest:
    def __init__(self):
        self.ob = FizzBuzz()
        
    def TestReplace(self):
        dic = {'aaaaabbbbbccccc dddddeeeee ffgg hhhhh iiii': 'aaaaBuzzbbbbBuzzccccBuzz ddddBuzzeeeeBuzz Fizz hhhhBuzz iiii',
               'djh djh kej kkfj w er q': 'djh djh Fizz kkfj w Fizz q',
               'q e r f': 'q e Fizz f',
               'ieudjerty': 'ieudBuzzerty'
               }
        for st in dic:
            assert self.ob.replace(st) == dic[st], 'TestReplace not ok with string:'+dic[st]
        #Testing error raising
        try:
            self.ob.replace('ase') #method doesn`t use string < 7 length
            self.ob.replace('AAABBBC') #method doesn`t use upper case chars
            self.ob.replace('2387182Gs dasb') #method doesn`t use digits
            self.ob.replace('2387182') #стоит всё таки поместить в цикл, потому что если один не подходит то уже вызывает ошибку, даже если остальные норм
            self.ob.replace('a'*101) ##method doesn`t use string > 100 length
            print('Not Ok: input string not correct, but error does`nt throwed')
        except Exception:
            print('OK: Exception was throwed on not correct string')
        print('TestFBDetector All passed') #otherwise error will throwed above

test = FBTest()
test.TestReplace()
