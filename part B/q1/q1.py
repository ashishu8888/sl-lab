class reverseSentence:

    vowel = ["a","e","i","o","u"]
    countVowel = 0
    def __init__(self,sentence):
        self.sentence = sentence
        self.Reverse()

    def Reverse(self):
        self.reverse = " ".join(reversed(self.sentence.split()))
    
    def getVowelCount(self):
        for x in self.sentence:
            if (x.lower() == "a"):
                self.countVowel = self.countVowel + 1
                print(x)
            if (x.lower() == "e"):
                self.countVowel = self.countVowel + 1
                print(x)
            if (x.lower() == "i"):
                self.countVowel = self.countVowel + 1
                print(x)
            if (x.lower() == "o"):
                self.countVowel = self.countVowel + 1
                print(x)
            if (x.lower() == "u"):
                self.countVowel = self.countVowel + 1
                print(x)
        return self.countVowel


            

    

items = []

s = input("Enter a sentence: \n")
sen1 = reverseSentence(s)
items.append(sen1)

s = input("Enter a sentence: \n")
sen2 = reverseSentence(s)
items.append(sen2)

s = input("Enter a sentence: \n")
sen3 = reverseSentence(s)
items.append(sen3)

y = sorted(items, key=lambda x: x.getVowelCount(), reverse=True)

for x in y:
    print(
        f'reversed sentence = {x.reverse} vowel count = {round(x.getVowelCount()/2)} ')





