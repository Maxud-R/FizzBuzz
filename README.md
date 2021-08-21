# FizzBuzz
This algorithm is replaces every third word in the string to Fizz, and every fifth letter in the word of string to Buzz.
On the task instructions algorithm takes only [a-z], else the method calls Exception.
### How to use
```Python
from FizzBuzz import FizzBuzz

ob = FizzBuzz()
string = 'the quick brown fox jumps over the lazy dog'
print(ob.replace(string))
```
## Detector
FizzBuzzDetector alows to find all concidences of substring in main string. It may used to check rightness of FizzBuzz algorithm
### How to use
```Python
from FizzBuzz import FizzBuzz
from FizzBuzzDetector import FizzBuzzDetector

ob = FizzBuzz()
tester = FizzBuzzDetector()
string = 'the quick brown fox jumps over the lazy dog'
result = ob.replace(string)
print(result)
print('Buzz in result: {0}'.format(tester.getOverlappings(result, 'Buzz')))
print('Fizz in result: {0}'.format(tester.getOverlappings(result, 'Fizz')))
```
