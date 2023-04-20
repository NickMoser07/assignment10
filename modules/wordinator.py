class Wordinator:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word < other.word

    def __add__(self, other):
        return self.word + other.word

    def __mul__(self, factor):
        return self.word * factor

    def __truediv__(self, other):
        mixed_word = ""
        for i in range(max(len(self.word), len(other.word))):
            if i < len(self.word):
                mixed_word += self.word[i]
            if i < len(other.word):
                mixed_word += other.word[i]
        return mixed_word

    def __mod__(self, other):
        len1 = len(self.word)
        len2 = len(other.word)
        midlen1 = len1//2
        midlen2 = len2//2
        extra1 = (len1 - midlen1)
        extra2 = (len2 - midlen2)
        if extra1 % 2 != 0:
            extra1 -= 1
        if extra1 + midlen1 < len1:
            midlen1 += 1
        elif extra1 + midlen1 > len1:
            midlen1 -= 1
        if extra2 % 2 != 0:
            extra2 -= 1
        if extra2 + midlen2 < len2:
            midlen2 += 1
        elif extra2 + midlen2 > len2:
            midlen2 -= 1

        return self.word[extra1 // 2:(extra1//2)+midlen1], other.word[extra2 // 2:(extra2//2)+midlen2]
    def __switchCase(self, word):
        charList = [i for i in word]
        for i in range(len(charList)):
            if charList[i].isupper():
                charList[i] = charList[i].lower()
            elif charList[i].islower():
                charList[i] = charList[i].upper()
        finalString = ""
        for i in charList:
            finalString += i
        return finalString

    def __sub__(self, other):
        return self.__switchCase(self.word), self.__switchCase(other.word)

    def backWordSlice(self):
        return self.word[::-1]

    def backWordManual(self):
        reversed_word = ""
        for i in range((len(self.word))-1, -1, -1):
            reversed_word += self.word[i]
        return reversed_word

    def __str__(self):
        return self.word