import re

class PersonalVocabulary:
    #vocabulary set
    vet = set()
    def __init__(self):
        #print("onLoading...")
        vines = []
        try:
            file = open("pv.txt","rt")
            #vocabulary lines
            vines = file.readlines()
        except FileNotFoundError:
            file = open("pv.txt","x")
            print("pv.txt dont exist, but i creat it")
        file.close()

        for line in vines:
            if line == "\n":
                continue
            self.vet.add(line[0:len(line)-1])
    
    def add(self, word):
        self.vet.add(word)
        self.load(self.vet)

    def load(self, vet):
        text = ""
        for word in vet:
            text += word + "\n"
        
        with open("pv.txt","wt") as outfile:
            outfile.write(text)
    
    def delete(self,dltWord):
        self.vet.discard(dltWord)
        self.load(self.vet)
        


class PeelWord:
    text = ""
    def __init__(self):
        try:
            file = open("rowMeat.txt","rt")
            #vocabulary lines
            self.text = file.read()
        except FileNotFoundError:
            file = open("rowMeat.txt","x")
            print("rowMeat.txt dont exist, but i creat it")
        file.close()

    #将文本内容中的生词剥离出来
    def peel(self):
        pv = PersonalVocabulary()
        firstDiff = self.sieve() - pv.vet
        secondDiff = set()
        for word in firstDiff:
            secondDiff.add(word.lower())

        return secondDiff - pv.vet

    #把文本中的单词筛出来
    #大小写
    def sieve(self):
        list = re.findall(r'[a-z]+',self.text,re.I)
        return set(list)