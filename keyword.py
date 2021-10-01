#!/usr/bin/env python

class KeyWord:
    """ generated source for class KeyWord """
    id = str()
    word = str()
    posTag = str()
    dependenceId = str()
    dependenceType = str()
    relationKeyWord = []

    #  ***************************************************************
    #  constructors
    # 
    # 	 *
    # 	 * @param _id, _word, _posTag, _dependenceId, _dependenceType, _relationKeyWord
    # 	 *        
    # 	 
    def __init__(self, **kwargs):
        """ generated source for method __init___0 """
        if kwargs:
            self.id = kwargs.get("id")
            self.word = kwargs.get("word")
            self.posTag = kwargs.get("posTag")
            self.dependenceId = kwargs.get("dependenceId")
            self.dependenceType = kwargs.get("dependenceType")
            self.relationKeyWord = []

    #  ***************************************************************
    def getId(self):
        """ generated source for method getId """
        return self.id

    #  ***************************************************************
    def getWord(self):
        """ generated source for method getWord """
        return self.word

    #  ***************************************************************
    def getPosTag(self):
        """ generated source for method getPosTag """
        return self.posTag

    #  ***************************************************************
    def getDependenceId(self):
        """ generated source for method getDependenceId """
        return self.dependenceId

    #  ***************************************************************
    def getDependenceType(self):
        """ generated source for method getDependenceType """
        return self.dependenceType

    #  ***************************************************************
    #  idRelation ***********************
    def getRelationKeyWord(self):
        """ generated source for method getRelationKeyWord """
        return self.relationKeyWord

    #  ***************************************************************
    def addRelationKeyWord(self, _keyWord):
        """ generated source for method addRelationKeyWord """
        self.relationKeyWord.append(_keyWord)

    #  ***************************************************************
    def printKeyWord(self):
        """ generated source for method printKeyWord """
        print("id:   " + self.id)
        print("word: " + self.word)
        print("posTag:  " + self.posTag)
        print("dependenceId:  " + self.dependenceId)
        print("dependenceType:  " + self.dependenceType)
        if self.relationKeyWord != None:
            i=0
            while i < len(self.relationKeyWord):
                print("\n" + self.word + " = <" + self.relationKeyWord[i].getWord() + ", " + self.relationKeyWord[i].getDependenceType() + ">")
                i += 1

    #  ***************************************************************

# WARNING runTransform: Generated source has invalid syntax. invalid syntax (<string>, line 94)