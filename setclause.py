#!/usr/bin/env python
from .keyword import KeyWord
from .constituent import Constituent
from .clausetype import ClauseType

class SetClause:
    """ generated source for class SetClause """
    # ***************************************************************
    # 
    # 	 * 
    # 	 * 
    # 	 
    def setOfClause(self, sentence):
        """ generated source for method setOfClause """
        clauseTypeList = []
        clause = []
        kwRootVerb = KeyWord()
        kwVerb = KeyWord()
        kwVmodSinmilarVerb = KeyWord()
        constituent = Constituent()
        clauseType = ClauseType()
        rootSubject = str()
        subject = str()
        strId = str()
        countVerb = int()
        countClause = int()
        id1 = int()
        id2 = int()
        id1 = 0
        id2 = 0
        countVerb = 0
        countClause = 0
        kwVmodSinmilarVerb = None
        rootSubject = ""
        if constituent.isSentence(sentence):
            i=0
            while i < sentence.size():
                # main clause
                if constituent.isRootVerb(sentence.get(i).getId(), sentence):
                    kwRootVerb = sentence.get(i)
                    rootSubject = constituent.subject(kwRootVerb, sentence)
                    # keyword is a verb which support to verb1 and dependence type is vmod 
                    if (constituent.isVmodSimilarVerb(kwRootVerb, sentence)) and (not constituent.hasSubject(constituent.getKeyWordOfVmodSimilarVerb(kwRootVerb, sentence))):
                        # Main Clause
                        clause = clauseType.detectClauseType(sentence, rootSubject, kwRootVerb, constituent.getKeyWordOfVmodSimilarVerb(kwRootVerb, sentence))
                        clauseTypeList.extend(clause)
                        countClause = countClause + len(clause)
                        countVerb += 1
                    if not (constituent.isVmodSimilarVerb(kwRootVerb, sentence)):
                        # Main Clause 						
                        clause = clauseType.detectClauseType(sentence, rootSubject, kwRootVerb, kwVmodSinmilarVerb)
                        clauseTypeList.extend(clause)
                        countClause = countClause + len(clause)
                        countVerb += 1
                i += 1
            # for main clause
            #  SubbordinateClause  Or Coordinate
            while i < sentence.size():
                if "coord" in sentence.get(i).getDependenceType() and (sentence.getKeyWordConjByCoord(sentence.get(i).getId()).getId() != None):
                    strId = sentence.get(i).getDependenceId()
                    if constituent.isRootVerb(strId, sentence) or (constituent.isVerb(sentence.getKeyWordById(strId), sentence)) or ((constituent.isRootVerb(sentence.getKeyWordById(sentence.getKeyWordById(strId).getDependenceId()).getId(), sentence)) and sentence.getKeyWordById(sentence.getKeyWordById(strId).getId()).getDependenceType() == "vmod") or ((constituent.isVerb(sentence.getKeyWordById(sentence.getKeyWordById(sentence.getKeyWordById(strId).getDependenceId()).getId()), sentence)) and sentence.getKeyWordById(sentence.getKeyWordById(strId).getId()).getDependenceType() == "vmod"):
                        if constituent.isRootVerb(sentence.get(i).getDependenceId(), sentence) or (constituent.isVerb(sentence.getKeyWordById(sentence.get(i).getDependenceId()), sentence)):
                            kwVerb = sentence.getKeyWordById(strId)
                        else:
                            kwVerb = sentence.getKeyWordById(sentence.getKeyWordById(sentence.getKeyWordById(strId).getDependenceId()).getId())
                        subject = constituent.subject(kwVerb, sentence)
                        if (constituent.isVmodSimilarVerb(kwVerb, sentence)) and (not constituent.hasSubject(constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence))) and (len(subject)):
                            clause = self.coordinateClause(sentence, subject, kwVerb, constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence), sentence.get(i))
                            clauseTypeList.extend(clause)
                            countClause = countClause + len(clause)
                        if not (constituent.isVmodSimilarVerb(kwVerb, sentence)):
                            clause = self.coordinateClause(sentence, subject, kwVerb, kwVmodSinmilarVerb, sentence.get(i))
                            clauseTypeList.extend(clause)
                            countClause = countClause + len(clause)
                        strId = sentence.get(i).getId()
                        if (constituent.hasSubject(sentence.getKeyWordConjByCoord(strId))):
                            kwVerb = sentence.getKeyWordConjByCoord(strId)
                            subject = constituent.subject(kwVerb, sentence)
                        else:
                            if not (constituent.hasSubject(sentence.getKeyWordConjByCoord(strId))):
                                kwVerb = sentence.getKeyWordConjByCoord(strId)
                        if constituent.isVmodSimilarVerb(kwVerb, sentence) and  (len(subject)):
                            clause = clauseType.detectClauseType(sentence, subject, kwVerb, constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence))
                            clauseTypeList.extend(clause)
                            countClause = countClause + len(clause)
                            countVerb += 1
                        if not (constituent.isVmodSimilarVerb(kwVerb, sentence)) and (len(subject)):
                            clause = clauseType.detectClauseType(sentence, subject, kwVerb, kwVmodSinmilarVerb)
                            clauseTypeList.extend(clause)
                            countClause = countClause + len(clause)
                            countVerb += 1
                    strId = sentence.get(i).getDependenceId()
                    if not (constituent.isRootVerb(strId, sentence)):
                        if ("prd" not in sentence.getKeyWordById(strId).getDependenceType()) and ( "dep" not in sentence.getKeyWordById(strId).getDependenceType()) and ("dob" not in sentence.getKeyWordById(strId).getDependenceType()) and ("prp" not in sentence.getKeyWordById(strId).getDependenceType()) and ((constituent.isVerb(sentence.getKeyWordById(strId), sentence))):
                            strId = sentence.getKeyWordById(strId).getDependenceId()
                            kwVerb = sentence.getKeyWordById(strId)
                            subject = constituent.subject(kwVerb, sentence)
                            if (constituent.isVmodSimilarVerb(kwVerb, sentence)) and (not constituent.hasSubject(constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence))) and (len(subject)):
                                clause = self.coordinateClause(sentence, subject, kwVerb, constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence), sentence.get(i))
                                clauseTypeList.extend(clause)
                                countClause = countClause + len(clause)
                            if not (constituent.isVmodSimilarVerb(kwVerb, sentence)):
                                clause = self.coordinateClause(sentence, subject, kwVerb, kwVmodSinmilarVerb, sentence.get(i))
                                clauseTypeList.extend(clause)
                                countClause = countClause + len(clause)
                        if ("dep" in sentence.getKeyWordById(strId).getDependenceType()) and ((constituent.isRootVerb(sentence.getKeyWordById(strId).getDependenceId(), sentence)) or (constituent.isVerb(sentence.getKeyWordById(sentence.getKeyWordById(strId).getDependenceId()), sentence))):
                            strId = sentence.getKeyWordById(strId).getDependenceId()
                            kwVerb = sentence.getKeyWordById(strId)
                            subject = constituent.subject(kwVerb, sentence)
                            if (constituent.isVmodSimilarVerb(kwVerb, sentence)) and (not constituent.hasSubject(constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence))) and (len(subject)):
                                clause = self.coordinateClause(sentence, subject, kwVerb, constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence), sentence.get(i))
                                clauseTypeList.extend(clause)
                                countClause = countClause + len(clause)
                            if not (constituent.isVmodSimilarVerb(kwVerb, sentence)):
                                clause = self.coordinateClause(sentence, subject, kwVerb, kwVmodSinmilarVerb, sentence.get(i))
                                clauseTypeList.extend(clause)
                                countClause = countClause + len(clause)
                id1 = int(sentence.get(i).getDependenceId())
                id2 = int(sentence.get(i).getId())
                strId = sentence.get(i).getDependenceId()
                if (constituent.isVerb(sentence.get(i), sentence)) and (sentence.getKeyWordById(strId).getDependenceType()=="conj") and (not sentence.getKeyWordById(sentence.get(i).getDependenceId()).getDependenceType()=="prp") and ((not (id1 + 1 == id2))):
                    subject = ""
                    if constituent.hasSubject(sentence.getKeyWordById(strId)):
                        kwVerb = sentence.getKeyWordById(sentence.get(i).getDependenceId())
                        subject = constituent.subject(kwVerb, sentence)
                    if not (constituent.hasSubject(sentence.getKeyWordById(strId))):
                        kwVerb = sentence.getKeyWordById(sentence.get(i).getDependenceId())
                        if (sentence.getKeyWordById(kwVerb.getDependenceId()).getDependenceType()=="coord") and ((constituent.isRootVerb(sentence.getKeyWordById(kwVerb.getDependenceId()).getDependenceId(), sentence)) or (constituent.isVerb(sentence.getKeyWordById(sentence.getKeyWordById(kwVerb.getDependenceId()).getDependenceId()), sentence))):
                            subject = constituent.subject(sentence.getKeyWordById(sentence.getKeyWordById(kwVerb.getDependenceId()).getDependenceId()), sentence)
                    if (constituent.isVmodSimilarVerb(kwVerb, sentence)) and (not constituent.hasSubject(constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence))) and (len(subject)):
                        clause = self.subordinateClause(sentence, subject, kwVerb, constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence), sentence.get(i))
                        clauseTypeList.extend(clause)
                        countClause = countClause + len(clause)
                    if not (constituent.isVmodSimilarVerb(kwVerb, sentence)):
                        clause = self.subordinateClause(sentence, subject, kwVerb, kwVmodSinmilarVerb, sentence.get(i))
                        clauseTypeList.extend(clause)
                        countClause = countClause + len(clause)
                id1 = int(sentence.get(i).getDependenceId())
                id2 = int(sentence.get(i).getId())
                strId = sentence.get(i).getDependenceId()
                if (constituent.isVerb(sentence.get(i), sentence)) and not (sentence.get(i).getDependenceType()=="conj") and ((not (sentence.get(i).getDependenceType()=="dep")) or (constituent.hasSubject(sentence.get(i)))) and ((not ((id1 + 1) == id2))) and (constituent.isRootVerb(strId, sentence) or constituent.isVerb(sentence.getKeyWordById(strId), sentence) or constituent.isRootVerb(sentence.getKeyWordById(strId).getDependenceId(), sentence) or constituent.isVerb(sentence.getKeyWordById(sentence.getKeyWordById(strId).getDependenceId()), sentence)):
                    kwVerb = sentence.getKeyWordById(sentence.get(i).getDependenceId())
                    subject = constituent.subject(kwVerb, sentence)
                    if (constituent.isVmodSimilarVerb(kwVerb, sentence)) and (not constituent.hasSubject(constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence))):
                        kwVmodSinmilarVerb = constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence)
                    if not (constituent.isVmodSimilarVerb(kwVerb, sentence)):
                        kwVmodSinmilarVerb = None
                    if (len(subject)) and (not (sentence.get(i).getDependenceType()=="prd")) and (not sentence.getKeyWordById(sentence.get(i).getDependenceId()).getDependenceType()=="conj") and (not sentence.getKeyWordById(sentence.get(i).getDependenceId()).getDependenceType()=="prp"):
                        clause = self.subordinateClause(sentence, subject, kwVerb, kwVmodSinmilarVerb, sentence.get(i))
                        clauseTypeList.extend(clause)
                        countClause = countClause + len(clause)
                        kwVmodSinmilarVerb = None
                    if (not subject) and (constituent.hasSubject(sentence.getKeyWordById(sentence.getKeyWordById(sentence.get(i).getDependenceId()).getDependenceId()))) and (not sentence.getKeyWordById(sentence.get(i).getDependenceId()).getDependenceType()=="prp"):
                        kwVerb = sentence.getKeyWordById(sentence.getKeyWordById(sentence.get(i).getDependenceId()).getDependenceId())
                        subject = constituent.subject(kwVerb, sentence)
                        if (constituent.isVmodSimilarVerb(kwVerb, sentence)) and (not constituent.hasSubject(constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence))):
                            kwVmodSinmilarVerb = constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence)
                        if not (constituent.isVmodSimilarVerb(kwVerb, sentence)):
                            kwVmodSinmilarVerb = None
                        clause = self.subordinateClause(sentence, subject, kwVerb, kwVmodSinmilarVerb, sentence.get(i))
                        clauseTypeList.extend(clause)
                        countClause = countClause + len(clause)
                        kwVmodSinmilarVerb = None
                    if constituent.hasSubject(sentence.get(i)):
                        kwVerb = sentence.get(i)
                        subject = constituent.subject(kwVerb, sentence)
                    else:
                        if not (constituent.hasSubject(sentence.get(i))):
                            kwVerb = sentence.get(i)
                    if constituent.isVmodSimilarVerb(kwVerb, sentence) and (len(subject)):
                        clause = clauseType.detectClauseType(sentence, subject, kwVerb, constituent.getKeyWordOfVmodSimilarVerb(kwVerb, sentence))
                        clauseTypeList.extend(clause)
                        countClause = countClause + len(clause)
                        countVerb += 1
                    if not (constituent.isVmodSimilarVerb(kwVerb, sentence)) and (len(subject)):
                        kwVmodSinmilarVerb = None
                        clause = clauseType.detectClauseType(sentence, subject, kwVerb, kwVmodSinmilarVerb)
                        clauseTypeList.extend(clause)
                        countClause = countClause + len(clause)
                        countVerb += 1
                i += 1
        statNumberList=[]
        if countVerb > 0:
            VerbNumber = "Number of verb in sentence: " + "\t" + str(countVerb)
            statNumberList.append(VerbNumber)
        if countClause > 0:
            clauseNumber = "Number of clause in sentence: " + "\t" + str(countClause)
            statNumberList.append(clauseNumber)
        
        return clauseTypeList,statNumberList

    def subordinateClause(self, sentence, subject, kwVerb1, kwVerb2, kwSubVerb):
        """ generated source for method subordinateClause """
        clauseTypeList = []
        constituent = Constituent()
        kwVerb = KeyWord()
        verb = str()
        directObject = str()
        inDirectObject = str()
        verbToBe = str()
        complement = str()
        subClause = str()
        clause = str()
        verb = ""
        if kwVerb2 == None:
            kwVerb = kwVerb1
            verb = constituent.verb(kwVerb, sentence)
        if kwVerb2 != None:
            kwVerb = kwVerb2
            verb = constituent.verb2(kwVerb1, kwVerb2, sentence)
        directObject = constituent.directObject(kwVerb, sentence)
        inDirectObject = constituent.inDirectObject(kwVerb, sentence)
        verbToBe = constituent.verbToBe(kwVerb, sentence)
        complement = constituent.complement(kwVerb, sentence)
        subClause = constituent.subordinateClause(kwSubVerb, sentence)
        if (len(verb)) and (len(subject)) and (len(subClause)) and (not verbToBe):
            if (not directObject):
                clause = "SV + subClause:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + subClause + "\")"
                clauseTypeList.append(clause)
            if (len(directObject)) and (subClause not in directObject) and (not inDirectObject):
                clause = "SVO + subClause:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + subClause + "\")"
                clauseTypeList.append(clause)
            if (len(directObject)) and (subClause not in directObject) and ( len (inDirectObject)) and (subClause not in inDirectObject):
                clause = "SVOO + subClause:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + subClause + "\")"
                clauseTypeList.append(clause)
        if (len(verbToBe)) and ( len(complement)) and (len(subClause)) and (subClause not in complement):
            clause = "SVC + subClause:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + subClause + "\")"
            clauseTypeList.append(clause)
        return clauseTypeList

    def coordinateClause(self, sentence, subject, kwVerb1, kwVerb2, kwCoord):
        """ generated source for method coordinateClause """
        clauseTypeList = []
        constituent = Constituent()
        verb = str()
        directObject = str()
        inDirectObject = str()
        clause = str()
        coordClause = str()
        verbToBe = str()
        complement = str()
        kwVerb = KeyWord()
        verb = ""
        clause = ""
        coordClause = ""
        if kwVerb2 == None:
            kwVerb = kwVerb1
            verb = constituent.verb(kwVerb, sentence)
        if kwVerb2 != None:
            kwVerb = kwVerb2
            verb = constituent.verb2(kwVerb1, kwVerb2, sentence)
        directObject = constituent.directObject(kwVerb, sentence)
        inDirectObject = constituent.inDirectObject(kwVerb, sentence)
        coordClause = constituent.coordinateClause(kwCoord, sentence)
        verbToBe = constituent.verbToBe(kwVerb, sentence)
        complement = constituent.complement(kwVerb, sentence)
        if sentence.getKeyWordById(kwCoord.getDependenceId()).getDependenceType() == "dep":
            coordClause = sentence.getKeyWordById(kwCoord.getDependenceId()).getWord() + " " + coordClause
        if (len( verb)) and (len( subject)) and (len(coordClause)) and (not verbToBe):
            if (not directObject):
                clause = "SV + coordClause:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + coordClause + "\")"
                clauseTypeList.append(clause)
            if (len(directObject)) and (coordClause not in directObject):
                clause = "SVO + coordClause:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + coordClause + "\")"
                clauseTypeList.append(clause)
            if (len(directObject)) and (coordClause not in directObject) and (len(inDirectObject)) and (coordClause not in inDirectObject):
                clause = "SVOO + coordClause:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + coordClause + "\")"
                clauseTypeList.append(clause)
        if (len( verbToBe)) and ( len( complement)) and  (len(coordClause)):
            clause = "SVC + coordClause:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + coordClause + "\")"
            clauseTypeList.append(clause)
        return clauseTypeList
