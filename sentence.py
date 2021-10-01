#!/usr/bin/env python
from .keyword import KeyWord

class Sentence:
    """ generated source for class Sentence """
    sentence = []

    def __init__(self):
        """ generated source for method __init__ """
        self.sentence = []

    # ***************************************************************
    def addKeyWord(self, kWord):
        """ generated source for method addKeyWord """
        #kWord.printKeyWord()
        self.sentence.append(kWord)

    # ***************************************************************
    def get(self, pos):
        """ generated source for method get """
        return self.sentence[pos]

    # ***************************************************************
    def getIdAt(self, pos):
        """ generated source for method getIdAt """
        return self.sentence[pos].getId()

    # ***************************************************************
    def getWordAt(self, pos):
        """ generated source for method getWordAt """
        return self.sentence[pos].getWord()

    # ***************************************************************
    def getPosTagAt(self, pos):
        """ generated source for method getPosTagAt """
        return self.sentence[pos].getPosTag()

    # ***************************************************************
    def getDependenceIdAt(self, pos):
        """ generated source for method getDependenceIdAt """
        return self.sentence[pos].getDependenceId()

    # ***************************************************************
    def getDependenceTypeAt(self, pos):
        """ generated source for method getDependenceTypeAt """
        return self.sentence[pos].getDependenceType()

    # ***************************************************************
    # 
    # 	 *  get content of a KeyWord
    # 	 *  @param  id of a KeyWord  
    # 	 *  @return a KeyWord according to id, 
    # 	 *    
    # 	 
    def getKeyWordById(self, id):
        """ generated source for method getKeyWordById """
        kWord = KeyWord()
        i = 0
        while i < len(self.sentence):
            if self.sentence[i].getId() == id:
                kWord = self.sentence[i]
            i += 1
        return kWord

    def clear(self):
        """ generated source for method clear """
        self.sentence.clear()

    def size(self):
        """ generated source for method size """
        return len(self.sentence)

    def isQuestion(self):
        """ generated source for method isQuestion """
        i = 0
        while i < len(self.sentence):
            if "?" in self.sentence[i].getWord():
                return True
            i += 1
        return False

    def isCompareRemote2ID(self, kwVerb, kWord):
        """ generated source for method isCompareRemote2ID """
        id1 = int()
        id2 = int()
        id1 = int(kwVerb.getId())
        id2 = int(kWord.getId())
        if id1 < id2:
            if (id2 - id1) <= 2:
                return True
        else:
            if (id1 - id2) <= 2:
                return True
        return False

    def getKeyWordConjByCoord(self, idCoord):
        """ generated source for method getKeyWordConjByCoord """
        kWord = KeyWord()
        i = 0
        while i < len(self.sentence):
            if self.sentence[i].getDependenceId() == idCoord and self.sentence[i].getDependenceType() == "conj":
                kWord = self.sentence[i]
            i += 1
        return kWord

    def printSentenceContent(self):
        """ generated source for method printSentenceContent """
        i = 0
        while i < len(self.sentence):
            print(self.sentence[i].getWord() + " ")
            i += 1
        print("\n")

    def printSentenceKeyWord(self):
        """ generated source for method printSentenceKeyWord """
        i = 0
        while i < len(self.sentence):
            self.sentence[i].printKeyWord()
            print("\n")
            i += 1

# WARNING runTransform: Generated source has invalid syntax. invalid syntax (<string>, line 113)