#!/usr/bin/env python

from .keyword import KeyWord
from sortedcontainers import SortedDict

class Constituent:
    """ generated source for class Constituent """
    # ***************************************************************
    # 
    # 	 * all constituents of a sentence
    # 	 * SUBJECT, VERB, DIRECT OBJECT, IN DIRECT OBJECT, VERB TO BE, COMPLEMENT, ADVERB 
    # 	 * 
    # 	 
    # ***************************************************************
    # 
    # 	 * SUBJECT
    # 	 * @param Verb, sentence 
    # 	 * @return String Subject according to Verb 
    # 	 * 
    # 	 
    def subject(self, kwVerb, sentence):
        """ generated source for method subject """
        strSubject = str()
        hmSubject = dict()
        hmSubject = self.getSubject(kwVerb, sentence)
        strSubject = self.convertedHashMapToString(hmSubject)
        return strSubject

    # end subject
    # ***************************************************************
    # 
    # 	 * VERB
    # 	 * @param kwVerb, sentence 
    # 	 * @return String verb according to kwVerb 
    # 	 * 
    # 	 
    def verb(self, kwVerb, sentence):
        """ generated source for method verb """
        strVerb = str()
        hmVerb = dict()
        hmVerb = self.getVerb(kwVerb, sentence)
        strVerb = self.convertedHashMapToString(hmVerb)
        return strVerb

    # end verb
    # ***************************************************************
    # 
    # 	 * VERB 2
    # 	 * @param kwVerb, sentence 
    # 	 * @return String verb according to kwVerb 
    # 	 * 
    # 	 
    def verb2(self, kwVerb1, kwVerb2, sentence):
        """ generated source for method verb2 """
        strVerb2 = str()
        hmVerb = dict()
        hmVerb = self.getVerb2(kwVerb1, kwVerb2, sentence)
        strVerb2 = self.convertedHashMapToString(hmVerb)
        return strVerb2

    # end verb
    # ***************************************************************
    # 
    # 	 * VERB TO BE
    # 	 * @param kwVerb, sentence 
    # 	 * @return String Subject according to Verb 
    # 	 * 
    # 	 
    def verbToBe(self, kwVerb, sentence):
        """ generated source for method verbToBe """
        strVerbToBe = str()
        hmVerbToBe = dict()
        hmVerbToBe = self.getVerbToBe(kwVerb, sentence)
        strVerbToBe = self.convertedHashMapToString(hmVerbToBe)
        return strVerbToBe

    # end verbToBe
    # ***************************************************************
    # 
    # 	 * COMPLEMENT
    # 	 * @param Verb, sentence 
    # 	 * @return String Subject according to Verb 
    # 	 * 
    # 	 
    def complement(self, kwVerb, sentence):
        """ generated source for method complement """
        strComplement = str()
        hmComplement = dict()
        hmComplement = self.getComplement(kwVerb, sentence)
        strComplement = self.convertedHashMapToString(hmComplement)
        return strComplement

    # end complement
    # ***************************************************************
    # 
    # 	 * DIRECT OBJECT
    # 	 * @param Verb, sentence 
    # 	 * @return String direct objetc according to Verb 
    # 	 * 
    # 	 
    def directObject(self, kwVerb, sentence):
        """ generated source for method directObject """
        strDirectObject = str()
        hmDirectObject = dict()
        hmDirectObject = self.getDirectObject(kwVerb, sentence)
        strDirectObject = self.convertedHashMapToString(hmDirectObject)
        return strDirectObject

    # end DirectObject	
    # ***************************************************************
    # 
    # 	 * IN DIRECT OBJECT
    # 	 * @param Verb, sentence 
    # 	 * @return String in direct object according to Verb 
    # 	 * 
    # 	 
    def inDirectObject(self, kwVerb, sentence):
        """ generated source for method inDirectObject """
        strInDirectObject = str()
        hmInDirectObject = dict()
        hmInDirectObject = self.getInDirectObject(kwVerb, sentence)
        strInDirectObject = self.convertedHashMapToString(hmInDirectObject)
        return strInDirectObject

    # end DirectObject	
    # ***************************************************************
    # 
    # 	 * adverb of loc 
    # 	 * @param kwVerb, sentence 
    # 	 * @return String adverb of loc according to Verb 
    # 	 * 
    # 	 
    def adverbOfLoc(self, kwVerb, sentence):
        """ generated source for method adverbOfLoc """
        strLoc = str()
        hmLoc = dict()
        hmLoc = self.getAdverbOfLoc(kwVerb, sentence)
        strLoc = self.convertedHashMapToString(hmLoc)
        return strLoc

    # end loc
    # ***************************************************************
    # 
    # 	 * adverb of tmp 
    # 	 * @param kwVerb, sentence 
    # 	 * @return String adverb tmp according to Verb 
    # 	 * 
    # 	 
    def adverbOfTmp(self, kwVerb, sentence):
        """ generated source for method adverbOfTmp """
        strTmp = str()
        hmTmp = dict()
        hmTmp = self.getAdverbOfTmp(kwVerb, sentence)
        strTmp = self.convertedHashMapToString(hmTmp)
        return strTmp

    # end tmp	
    # ***************************************************************
    # 
    # 	 * adverb of direction 
    # 	 * @param kwVerb, sentence 
    # 	 * @return String adverb of dir according to Verb 
    # 	 * 
    # 	 
    def adverbOfDir(self, kwVerb, sentence):
        """ generated source for method adverbOfDir """
        strDir = str()
        hmDir = dict()
        hmDir = self.getAdverbOfDir(kwVerb, sentence)
        strDir = self.convertedHashMapToString(hmDir)
        return strDir

    # end Dir	
    # ***************************************************************
    # 
    # 	 * adverb of manner 
    # 	 * @param kwVerb, sentence 
    # 	 * @return String adverb of mnr according to Verb 
    # 	 * 
    # 	 
    def adverbOfMnr(self, kwVerb, sentence):
        """ generated source for method adverbOfMnr """
        strMnr = str()
        hmMnr = dict()
        hmMnr = self.getAdverbOfMnr(kwVerb, sentence)
        strMnr = self.convertedHashMapToString(hmMnr)
        return strMnr

    # end Mnr	
    # ***************************************************************
    # 
    # 	 * adverb of purpose 
    # 	 * @param kwVerb, sentence 
    # 	 * @return String adverb of prp according to Verb 
    # 	 * 
    # 	 
    def adverbOfPrp(self, kwVerb, sentence):
        """ generated source for method adverbOfPrp """
        strPrp = str()
        hmPrp = dict()
        hmPrp = self.getAdverbOfPrp(kwVerb, sentence)
        strPrp = self.convertedHashMapToString(hmPrp)
        return strPrp

    # end Prp	
    # ***************************************************************
    # 
    # 	 * predicate
    # 	 * @param kwVerb, sentence 
    # 	 * @return String predicate according to Verb 
    # 	 * 
    # 	 
    def predicate(self, kwVerb, sentence):
        """ generated source for method predicate """
        strPrd = str()
        hmPrd = dict()
        hmPrd = self.getPrd(kwVerb, sentence)
        strPrd = self.convertedHashMapToString(hmPrd)
        return strPrd

    # end prd
    # ***************************************************************
    # 
    # 	 *  subordinate Clause
    # 	 * @param kwVerb, sentence 
    # 	 * @return subordinateClause 
    # 	 * 
    # 	 
    def subordinateClause(self, kwVerb, sentence):
        """ generated source for method subordinateClause """
        strSubClause = str()
        hmSubClause = dict()
        hmSubClause = self.getSubordinateClause(kwVerb, sentence)
        strSubClause = self.convertedHashMapToString(hmSubClause)
        return strSubClause

    # end SubClause	
    # ***************************************************************
    # 
    # 	 * CoordinateClause 
    # 	 * @param kwVerb, sentence 
    # 	 * @return String CoordinateClause 
    # 	 * 
    # 	 
    def coordinateClause(self, kwVerb, sentence):
        """ generated source for method coordinateClause """
        strCoorClause = str()
        hmCoorClause = dict()
        hmCoorClause = self.getCoordinateClause(kwVerb, sentence)
        strCoorClause = self.convertedHashMapToString(hmCoorClause)
        return strCoorClause

    # end SubClause	
    # ***************************************************************
    # ***************************************************************
    # 
    # 	 * getSubject  according to Verb
    # 	 * 
    # 	 * @return HashMap<id, KeyWord> express Subject according to Verb 
    # 	 * 
    # 	 
    def getSubject(self, kwVerb, sentence):
        """ generated source for method getSubject """
        subject = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if ("sub" in sentence.get(i).getDependenceType()) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if 2 == len((sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId().charAt(1) - '0')
                else:
                    id = int(sentence.get(i).getId())
                subject[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        subject[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        subject = self.getAllRelationKeyWord(relationId, subject, sentence)
                        j += 1
            i += 1
        return subject

    def getVerb(self, kwVerb, sentence):
        """ generated source for method getVerb """
        verb = dict()
        setRemovedWord = ["sub", "dob", "iob", "punct", "loc", "tmp", "pmod", "coord", "dep", "prp", "mnr", "dir", "prd"]
        setLinkingVerb = []
        id = int()
        relationId = int()
        if kwVerb.getWord() not in setLinkingVerb:
            if 2 == len(kwVerb.getId()) and (kwVerb.getId()[0] == 65279) and (kwVerb.getId()[1] == '1'):
                id = (kwVerb.getId()[1] - '0')
            else:
                id = int(kwVerb.getId())
            verb[id] = kwVerb
            if kwVerb.getRelationKeyWord() != None:
                j=0
                while j < len(kwVerb.getRelationKeyWord()):
                    if (kwVerb.getRelationKeyWord()[j].getDependenceType() not in setRemovedWord) and (not (self.isVerb(kwVerb.getRelationKeyWord()[j], sentence))) and ((sentence.isCompareRemote2ID(kwVerb, kwVerb.getRelationKeyWord()[j]))) and (not (self.hasSubject(kwVerb.getRelationKeyWord()[j]))) and not (self.isObjectOfPreposition(kwVerb, kwVerb.getRelationKeyWord()[j], sentence)):
                        relationId = int(kwVerb.getRelationKeyWord()[j].getId())
                        verb[relationId] = kwVerb.getRelationKeyWord()[j]
                        verb = self.getAllRelationKeyWordByVerb(relationId, verb, sentence)
                    if (kwVerb.getRelationKeyWord()[j].getDependenceType() == "dob"):
                        break
                    j += 1
        return verb

    def getVerb2(self, kwVerb1, kwVerb2, sentence):
        """ generated source for method getVerb2 """
        verb = dict()
        setRemovedWord = ["sub", "dob", "iob", "punct", "loc", "tmp", "pmod", "coord", "dep", "prp", "mnr", "dir"]
        id = int()
        relationId = int()
        if 2 == len(kwVerb1.getId()) and (kwVerb1.getId()[0] == 65279) and (kwVerb1.getId()[1] == '1'):
            id = (kwVerb1.getId().charAt(1) - '0')
        else:
            id = int(kwVerb1.getId())
        verb[id] = kwVerb1
        if kwVerb1.getRelationKeyWord() != None:
            j=0
            while j < len(kwVerb1.getRelationKeyWord()):
                if (kwVerb1.getRelationKeyWord()[j].getDependenceType() not in setRemovedWord) and ((sentence.isCompareRemote2ID(kwVerb1, kwVerb1.getRelationKeyWord()[j]))) and (not (self.hasSubject(kwVerb1.getRelationKeyWord()[j]))):
                    relationId = int(kwVerb1.getRelationKeyWord()[j].getId())
                    verb[relationId] = kwVerb1.getRelationKeyWord()[j]
                    if not (kwVerb1.getRelationKeyWord()[j].getId() == (kwVerb2.getId())):
                        verb = self.getAllRelationKeyWordByVerb(relationId, verb, sentence)
                j += 1
        return verb

    def getVerbToBe(self, kwVerb, sentence):
        """ generated source for method getVerbToBe """
        verb = dict()
        setRemovedWord = ["sub", "dob", "iob", "punct", "loc", "tmp", "pmod", "coord", "dep", "vmod", "prp"]
        id = int()
        relationId = int()
        if kwVerb.getWord() == "là":
            if 2 == len(kwVerb.getId()) and (kwVerb.getId()[0] == 65279) and (kwVerb.getId()[1] == '1'):
                id = (kwVerb.getId()[1] - '0')
            else:
                id = int(kwVerb.getId())
            verb[id]= kwVerb
            if kwVerb.getRelationKeyWord() != None:
                j=0
                while j < len(kwVerb.getRelationKeyWord()):
                    if (kwVerb.getRelationKeyWord()[j].getDependenceType() not in setRemovedWord) and (not (self.isVmodSimilarVerb(kwVerb.getRelationKeyWord()[j], sentence))):
                        relationId = int(kwVerb.getRelationKeyWord()[j].getId())
                        verb[relationId] = kwVerb.getRelationKeyWord()[j]
                        verb = self.getAllRelationKeyWord(relationId, verb, sentence)
                    j += 1
        return verb

    def getComplement(self, kwToBeVerb, sentence):
        """ generated source for method getComplement """
        complement = dict()
        setComplement = ["dob", "vmod"]
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if sentence.get(i).getDependenceId() == kwToBeVerb.getId() and (sentence.get(i).getDependenceType() in setComplement) and (kwToBeVerb.getWord() == ("là")):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                complement[id]= sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        complement[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        complement = self.getAllRelationKeyWord(relationId, complement, sentence)
                        j += 1
            i += 1
        return complement

    def getDirectObject(self, kwVerb, sentence):
        """ generated source for method getDirectObject """
        directObject = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if (("dob" in sentence.get(i).getDependenceType()) or ("voc" in sentence.get(i).getDependenceType()) or (self.isObjectOfPreposition(kwVerb, sentence.get(i), sentence))) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                directObject[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        directObject[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        directObject = self.getAllRelationKeyWord(relationId, directObject, sentence)
                        j += 1
            i += 1
        return directObject

    def getInDirectObject(self, kwVerb, sentence):
        """ generated source for method getInDirectObject """
        inDirectObject = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if ("iob" in sentence.get(i).getDependenceType()) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                inDirectObject[id]= sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        inDirectObject[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        inDirectObject = self.getAllRelationKeyWord(relationId, inDirectObject, sentence)
                        j += 1
            i += 1
        return inDirectObject

    def isObjectOfPreposition(self, kwVerb, kwPreposition, sentence):
        """ generated source for method isObjectOfPreposition """
        if (kwPreposition.getDependenceId() == kwVerb.getId()) and (kwPreposition.getPosTag() == "E") and (kwPreposition.getDependenceType() == "vmod"):
            if kwPreposition.getRelationKeyWord() != None:
                k=0
                while k < len(kwPreposition.getRelationKeyWord()):
                    if kwPreposition.getRelationKeyWord()[k].getDependenceType() == "pob":
                        return True
                    k += 1
        return False

    def getAdverbOfLoc(self, kwVerb, sentence):
        """ generated source for method getAdverbOfLoc """
        loc = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if ("loc" in sentence.get(i).getDependenceType()) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                loc[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        loc[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        loc = self.getAllRelationKeyWord(relationId, loc, sentence)
                        j += 1
            i += 1
        return loc

    def getAdverbOfTmp(self, kwVerb, sentence):
        """ generated source for method getAdverbOfTmp """
        tmp = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if ("tmp" in sentence.get(i).getDependenceType()) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                tmp[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        tmp[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        tmp = self.getAllRelationKeyWord(relationId, tmp, sentence)
                        j += 1
            i += 1
        return tmp

    def getAdverbOfPrp(self, kwVerb, sentence):
        """ generated source for method getAdverbOfPrp """
        prp = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if ("prp" in sentence.get(i).getDependenceType()) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                prp[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        prp[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        prp = self.getAllRelationKeyWord(relationId, prp, sentence)
                        j += 1
            i += 1
        return prp

    def getAdverbOfDir(self, kwVerb, sentence):
        """ generated source for method getAdverbOfDir """
        dir = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if ("dir" in sentence.get(i).getDependenceType()) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                dir[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        dir[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        dir = self.getAllRelationKeyWord(relationId, dir, sentence)
                        j += 1
            i += 1
        return dir

    def getAdverbOfMnr(self, kwVerb, sentence):
        """ generated source for method getAdverbOfMnr """
        mnr = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if ( "mnr" in sentence.get(i).getDependenceType()) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                mnr[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        mnr[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        mnr = self.getAllRelationKeyWord(relationId, mnr, sentence)
                        j += 1
            i += 1
        return mnr

    def getPrd(self, kwVerb, sentence):
        """ generated source for method getPrd """
        prd = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if (("prd" in sentence.get(i).getDependenceType())) and (sentence.get(i).getDependenceId() == kwVerb.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                prd[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        prd[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        prd = self.getAllRelationKeyWord(relationId, prd, sentence)
                        j += 1
            i += 1
        return prd

    def getKeyWordOfVmodSimilarVerb(self, kwVerb, sentence):
        """ generated source for method getKeyWordOfVmodSimilarVerb """
        kwVerb2 = KeyWord()
        setWord = ["dob", "iob", "punct", "loc", "tmp", "pmod", "dep", "prp", "mnr", "dir"]
        if kwVerb.getRelationKeyWord() != None:
            i=0
            while i < len(kwVerb.getRelationKeyWord()):
                if "vmod" in kwVerb.getRelationKeyWord()[i].getDependenceType():
                    k=0
                    while k < sentence.size():
                        if (sentence.get(k).getDependenceId() == (kwVerb.getRelationKeyWord()[i].getId())) and (sentence.get(k).getDependenceType() in setWord):
                            kwVerb2 = kwVerb.getRelationKeyWord()[i]
                        k += 1
                i += 1
        return kwVerb2

    def getSubordinateClause(self, kwVerb, sentence):
        """ generated source for method getSubordinateClause """
        subordinate = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if sentence.get(i).getId() == (kwVerb.getId()) and (self.isRootVerb(sentence.get(i).getDependenceId(), sentence) or self.isVerb(sentence.get(i), sentence)):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                subordinate[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        subordinate[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        subordinate = self.getAllRelationKeyWord(relationId, subordinate, sentence)
                        j += 1
            i += 1
        return subordinate

    def getCoordinateClause(self, kwCoord, sentence):
        """ generated source for method getCoordinateClause """
        coord = dict()
        id = int()
        relationId = int()
        i = 0
        while i < sentence.size():
            if sentence.get(i).getId()==(kwCoord.getId()):
                if (2 == len(sentence.get(i).getId())) and (sentence.get(i).getId()[0] == 65279) and (sentence.get(i).getId()[1] == '1'):
                    id = (sentence.get(i).getId()[1] - '0')
                else:
                    id = int(sentence.get(i).getId())
                coord[id] = sentence.get(i)
                if sentence.get(i).getRelationKeyWord() != None:
                    j=0
                    while j < len(sentence.get(i).getRelationKeyWord()):
                        relationId = int(sentence.get(i).getRelationKeyWord()[j].getId())
                        coord[relationId] = sentence.get(i).getRelationKeyWord()[j]
                        coord = self.getAllRelationKeyWord(relationId, coord, sentence)
                        j += 1
            i += 1
        return coord

    def isSentence(self, sentence):
        """ generated source for method isSentence """
        i = 0
        while i < sentence.size():
            if ("sub" in sentence.get(i).getDependenceType()) and (self.isRootVerb(sentence.get(i).getDependenceId(), sentence)) and (not sentence.isQuestion()):
                return True
            i += 1
        return False

    def hasSubject(self, kwVerb):
        """ generated source for method hasSubject """
        if kwVerb.getRelationKeyWord() != None:
            i=0
            while i < len(kwVerb.getRelationKeyWord()):
                if "sub" in kwVerb.getRelationKeyWord()[i].getDependenceType():
                    return True
                i += 1
        return False

    def isRootVerb(self, id, sentence):
        """ generated source for method isRootVerb """
        setVerbType = ["V", "A", "N"]
        i = 0
        while i < sentence.size():
            if (sentence.get(i).getId() == id) and (sentence.get(i).getPosTag() in setVerbType) and ("root" in sentence.get(i).getDependenceType()):
                return True
            i += 1
        return False

    def isVerb(self, kwVerb, sentence):
        """ generated source for method isVerb """
        setPosTag = ["V", "A"]
        setAdverbType = ["tmp", "loc", "prp", "dir", "mnr"]
        setRemovedWord = ["sub", "dob", "iob", "punct", "loc", "tmp", "pmod", "coord", "dep", "prp", "mnr", "dir", "prd"]
        id1 = int()
        id2 = int()
        i = 0
        while i < sentence.size():
            if (sentence.get(i).getId() == (kwVerb.getId())) and ("root" not in sentence.get(i).getDependenceType()) and (sentence.get(i).getPosTag() in setPosTag) and (sentence.get(i).getDependenceType() not in setAdverbType) and ((not (sentence.getKeyWordById(kwVerb.getDependenceId()).getPosTag() == "N")) or (self.hasSubject(kwVerb))):
                id1 = int(sentence.get(i).getDependenceId())
                id2 = int(kwVerb.getId())
                if self.isRootVerb(sentence.get(i).getDependenceId(), sentence):
                    if (self.hasSubject(kwVerb) or (not (sentence.isCompareRemote2ID(sentence.getKeyWordById(sentence.get(i).getDependenceId()), sentence.get(i)))) or (not ((id1 + 1) == id2))) and (id1 < id2) and (not (sentence.getKeyWordById(kwVerb.getDependenceId()).getDependenceType() == "sub")):
                        return True
                else:
                    if ((self.hasSubject(kwVerb)) or (kwVerb.getDependenceType() == "conj") or (not (sentence.isCompareRemote2ID(sentence.getKeyWordById(sentence.get(i).getDependenceId()), sentence.get(i)))) or ((not ((id1 + 1) == id2)))) and (id1 < id2) and (not (sentence.getKeyWordById(kwVerb.getDependenceId()).getDependenceType() == "sub")):
                        return True
                    k=0
                    while k < sentence.size():
                        if (sentence.get(k).getDependenceId() == kwVerb.getId()) and (sentence.get(k).getDependenceType() in setRemovedWord) and (not (sentence.getKeyWordById(kwVerb.getDependenceId()).getDependenceType()=="sub")):
                            return True
                        k += 1
            i += 1
        return False

    def isVmodSimilarVerb(self, kwVerb, sentence):
        """ generated source for method isVmodSimilarVerb """
        setPosTag = ["V", "A", "E", "N"]
        setWord = ["dob", "iob", "punct", "loc", "tmp", "pmod", "dep", "prp", "mnr", "dir"]
        id1 = int()
        id2 = int()
        if kwVerb.getRelationKeyWord() != None:
            i=0
            while i < len(kwVerb.getRelationKeyWord()):
                if "vmod" in  kwVerb.getRelationKeyWord()[i].getDependenceType() and (kwVerb.getRelationKeyWord()[i].getPosTag() in setPosTag):
                    k=0
                    while k < sentence.size():
                        if sentence.get(k).getDependenceId() == (kwVerb.getRelationKeyWord()[i].getId()) and (sentence.get(k).getDependenceType() in setWord):
                            id1 = int(kwVerb.getId())
                            id2 = int(kwVerb.getRelationKeyWord()[i].getId())
                            if (id1 + 1) == id2:
                                return True
                        k += 1
                i += 1
        return False

    def getAllRelationKeyWord(self, idParent, relationKeyWord, sentence):
        """ generated source for method getAllRelationKeyWord """
        allRelationKeyWord = dict()
        allRelationKeyWord = relationKeyWord
        depenedenceId = int()
        id = int()
        k = 0
        while k < sentence.size():
            depenedenceId = int(sentence.get(k).getDependenceId())
            if depenedenceId == idParent:
                id = int(sentence.get(k).getId())
                allRelationKeyWord[id] = sentence.get(k)
                self.getAllRelationKeyWord(id, allRelationKeyWord, sentence)
            k += 1
        return allRelationKeyWord

    def getAllRelationKeyWordByVerb(self, idParent, relationKeyWord, sentence):
        """ generated source for method getAllRelationKeyWordByVerb """
        allRelationKeyWord = dict()
        allRelationKeyWord = relationKeyWord
        depenedenceId = int()
        id = int()
        k = 0
        while k < sentence.size():
            depenedenceId = int(sentence.get(k).getDependenceId())
            if (depenedenceId == idParent) and not (sentence.get(k).getDependenceType() == "coord") and not (self.isVerb(sentence.get(k), sentence)):
                id = int(sentence.get(k).getId())
                allRelationKeyWord[id] = sentence.get(k)
                self.getAllRelationKeyWord(id, allRelationKeyWord, sentence)
            k += 1
        return allRelationKeyWord

    def convertedHashMapToString(self, hMap):
        """ generated source for method convertedHashMapToString """
        strValue = str()
        strValue = ""
        sorted = SortedDict(hMap)
        for k in sorted.keys():
            strValue = strValue + sorted[k].getWord() + " "
        return strValue
