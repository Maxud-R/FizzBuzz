#Algorithm that replaces every third word in the letter to Fizz, and every fifth letter in the word to Buzz.
#Алгоритм, который заменяет каждое третее слово в письме на Fizz и каждую пятую букву в слове на Buzz
#Принимает строку от 7 до 100 символов включительно и буквы нижнего регистра
class FizzBuzz:
    def replace(self, rawstr):
        if len(rawstr) < 7 or len(rawstr) > 100 or not (rawstr in rawstr.lower()):
            raise Exception("Wrong input string, str length must be 7 <= s <= 100 and string must consist of lowercase letters a-z")
        
        #this part splits string into words and words into parts, 5 char length
        wordList = rawstr.split(" ")
        for word in range(0, len(wordList)):
            tempWord = wordList[word]
            wordList[word] = []
            for a in range(round(len(tempWord)/5)):
                if len(tempWord[5:]):
                    wordList[word].append(tempWord[:5])
                    tempWord = tempWord[5:]
            wordList[word].append(tempWord)
            
        #next part replace each last letter of part to Buzz
        for word in range(len(wordList)):
            for part in range(len(wordList[word])):
                if len(wordList[word][part]) >= 5:
                    wordList[word][part] = wordList[word][part][:-1]+"Buzz"
            wordList[word] = "".join(wordList[word]) #join parts into words back
            
        #now wordList[word] is a list of words. Next code replace every third word to Fizz
        for word in range(2, len(wordList), 3):
            wordList[word] = "Fizz"
            
        return " ".join(wordList)
print("Result: "+FizzBuzz().replace(input("Input a string:")))
