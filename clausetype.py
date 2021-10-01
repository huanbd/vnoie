#!/usr/bin/env python
from .constituent import Constituent
from .keyword import KeyWord

class ClauseType:
    """ generated source for class ClauseType """
    # ***************************************************************
    # 
    # 	 * Clause types SV, SVC, SVO  
    # 	 * SV: Intransitive verb 			==> extended patterns: SV, SVA, SVAA,
    # 	 * SVC: Linking verb + complement	==> extended patterns: SVC, SVCA, SVCAA,
    # 	 * SVO: transitive verb				
    # 	 * @param sentence
    # 	 
    def detectClauseType(self, sentence, subject, kwVerb1, kwVerb2):
        """ generated source for method detectClauseType """
        clauseType = []
        constituent = Constituent()
        kwVerb = KeyWord()
        verb = str()
        verbToBe = str()
        directObject = str()
        inDirectObject = str()
        complement = str()
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
        # clause-type detection
        # *********************************************************************
        if (len(directObject)) and (not verbToBe):
            if (len(inDirectObject)):
                clauseType = self.SVOO(sentence, subject, kwVerb1, kwVerb2)
            if (not inDirectObject):
                clauseType = self.SVO(sentence, subject, kwVerb1, kwVerb2)
        else:
            if (len(verbToBe)) and (len(complement)):
                clauseType = self.SVC(sentence, subject, kwVerb1, kwVerb2)
            if (len(verbToBe)) and (not complement):
                clauseType = self.SVA(sentence, subject, kwVerb1, kwVerb2)
            if (len(verb)) and (not verbToBe) and (not complement):
                clauseType = self.SV(sentence, subject, kwVerb1, kwVerb2)
        return clauseType

    # end detectClauseType
    # *******************************************************************
    # 
    # 	 * Clause Type: SVOO
    # 	 * 
    # 	 
    def SVOO(self, sentence, subject, kwVerb1, kwVerb2):
        """ generated source for method SVOO """
        clauseTypeList = []
        constituent = Constituent()
        kwVerb = KeyWord()
        clause = str()
        verb = str()
        directObject = str()
        inDirectObject = str()
        dir = str()
        loc = str()
        mnr = str()
        prp = str()
        tmp = str()
        prd = str()
        verb = ""
        if kwVerb2 == None:
            kwVerb = kwVerb1
            verb = constituent.verb(kwVerb, sentence)
        if kwVerb2 != None:
            kwVerb = kwVerb2
            verb = constituent.verb2(kwVerb1, kwVerb2, sentence)
        directObject = constituent.directObject(kwVerb, sentence)
        inDirectObject = constituent.inDirectObject(kwVerb, sentence)
        dir = constituent.adverbOfDir(kwVerb, sentence)
        loc = constituent.adverbOfLoc(kwVerb, sentence)
        mnr = constituent.adverbOfMnr(kwVerb, sentence)
        prp = constituent.adverbOfPrp(kwVerb, sentence)
        tmp = constituent.adverbOfTmp(kwVerb, sentence)
        prd = constituent.predicate(kwVerb, sentence)
        if (len(subject)) and (len(verb)) and (len(directObject)) and (len(inDirectObject)):
            clause = "SVOO:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\")"
            clauseTypeList.append(clause)
            # SVOOA:write into List<String> about clause type SVOA with Adverb: location
            if (len(loc)):
                clause = "SVOO:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + loc.strip() + "\")"
                clauseTypeList.append(clause)
            # SVOOA:write into List<String> about clause type SVOA with Adverb: temporal
            if (len(tmp)):
                clause = "SVOOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOA (A:purpose)
            if (len(prp)) and (len(tmp)):
                clause = "SVOOAA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + prp.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOA (A:purpose)
            if (len(prp)):
                clause = "SVOOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + prp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOA (A:manner)
            if (len(mnr)):
                clause = "SVOOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + mnr.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOA (A:direction)
            if (len(dir)):
                clause = "SVOOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + dir.strip() + "\")"
                clauseTypeList.append(clause)
            # SVOOAA: write into List<String> about clause type SVOA with Adverb: location and temporal
            if (len(loc)) and (len(tmp)):
                clause = "SVOOAA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + loc.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # SVOO Prd: write into List<String> about clause type SVOO predicate 
            if (len(prd)):
                clause = "SVOO Prd:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + inDirectObject.strip() + "\", \"" + prd.strip() + "\")"
                clauseTypeList.append(clause)
        return clauseTypeList

    # end SVOO
    # *******************************************************************
    # 
    # 	 * Clause Type: SVO
    # 	 * 
    # 	 
    def SVO(self, sentence, subject, kwVerb1, kwVerb2):
        """ generated source for method SVO """
        clauseTypeList = []
        constituent = Constituent()
        kwVerb = KeyWord()
        clause = str()
        verb = str()
        directObject = str()
        inDirectObject = str()
        dir = str()
        loc = str()
        mnr = str()
        prp = str()
        tmp = str()
        prd = str()
        verb = ""
        if kwVerb2 == None:
            kwVerb = kwVerb1
            verb = constituent.verb(kwVerb, sentence)
        if kwVerb2 != None:
            kwVerb = kwVerb2
            verb = constituent.verb2(kwVerb1, kwVerb2, sentence)
        directObject = constituent.directObject(kwVerb, sentence)
        inDirectObject = constituent.inDirectObject(kwVerb, sentence)
        dir = constituent.adverbOfDir(kwVerb, sentence)
        loc = constituent.adverbOfLoc(kwVerb, sentence)
        mnr = constituent.adverbOfMnr(kwVerb, sentence)
        prp = constituent.adverbOfPrp(kwVerb, sentence)
        tmp = constituent.adverbOfTmp(kwVerb, sentence)
        prd = constituent.predicate(kwVerb, sentence)
        if (len(subject)) and (len(verb)) and (len(directObject)) and (not inDirectObject):
            # SVO: write into List<String> about clause type SVO	
            clause = "SVO:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\")"
            clauseTypeList.append(clause)
            # SVOA:write into List<String> about clause type SVOA with Adverb: location
            if (len(loc)):
                clause = "SVOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + loc.strip() + "\")"
                clauseTypeList.append(clause)
            # SVOA: write into List<String> about clause type SVOA with Adverb: temporal
            if (len( tmp)):
                clause = "SVOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOA (A:purpose) 
            if (len( prp)):
                clause = "SVOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + prp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOA (A:purpose) 
            if (len( prp)) and (len(tmp)):
                clause = "SVOAA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + prp.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOA (A:manner)
            if (len(mnr)):
                clause = "SVOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + mnr.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOA (A:direction)
            if (len(dir)):
                clause = "SVOA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + dir.strip() + "\")"
                clauseTypeList.append(clause)
            # SVOAA: write into List<String> about clause type SVOA with Adverb: temporal
            if (len(loc)) and (len(tmp)):
                clause = "SVOAA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + loc.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVOPrd (Predicate)
            if (len(prd)):
                clause = "SVO Predicate:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + directObject.strip() + "\", \"" + prd.strip() + "\")"
                clauseTypeList.append(clause)
        return clauseTypeList

    # end SVO
    # *******************************************************************
    # 
    # 	 * Clause Type: SVC
    # 	 * 
    # 	 
    def SVC(self, sentence, subject, kwVerb1, kwVerb2):
        """ generated source for method SVC """
        clauseTypeList = []
        constituent = Constituent()
        kwVerb = KeyWord()
        clause = str()
        verbToBe = str()
        complement = str()
        dir = str()
        loc = str()
        mnr = str()
        prp = str()
        tmp = str()
        prd = str()
        # verb = "";
        if kwVerb2 == None:
            kwVerb = kwVerb1
            # verb   = constituent.verb(kwVerb, sentence);
        if kwVerb2 != None:
            kwVerb = kwVerb2
            # verb   = constituent.verb2(kwVerb1, kwVerb2, sentence);
        verbToBe = constituent.verbToBe(kwVerb, sentence)
        complement = constituent.complement(kwVerb, sentence)
        dir = constituent.adverbOfDir(kwVerb, sentence)
        loc = constituent.adverbOfLoc(kwVerb, sentence)
        mnr = constituent.adverbOfMnr(kwVerb, sentence)
        prp = constituent.adverbOfPrp(kwVerb, sentence)
        tmp = constituent.adverbOfTmp(kwVerb, sentence)
        prd = constituent.predicate(kwVerb, sentence)
        # *********************************************************************
        # SVC: write into List<String> about clause type SVC (S+"la"+Complement)
        if (len(verbToBe)):
            if (len(complement)):
                clause = "SVC:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\")"
                clauseTypeList.append(clause)
                # write into List<String> about clause type SVCA according to location
                if (len(loc)):
                    clause = "SVCA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + loc.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVCA according to temporal
                if (len(tmp)):
                    clause = "SVCA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + tmp.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVCA according to location and temporal
                if (len(loc)) and (len(tmp)):
                    clause = "SVCAA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + tmp.strip() + "\", \"" + loc.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVCA according to purpose
                if (len(prp)):
                    clause = "SVCA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + prp.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVCA according to purpose
                if (len(prp)) and (len(tmp)):
                    clause = "SVCA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + prp.strip() + "\", \"" + tmp.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVCA according to direction
                if (len(dir)):
                    clause = "SVCA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + dir.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVCA according to manner
                if (len(mnr)):
                    clause = "SVCA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + mnr.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVC predicate
                if (len(prd)):
                    clause = "SVC predicate:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + complement.strip() + "\", \"" + prd.strip() + "\")"
                    clauseTypeList.append(clause)
        # ///
        return clauseTypeList

    # end SVC
    # *******************************************************************
    # 
    # 	 * Clause Type: SVA (V: verb to be)
    # 	 * 
    # 	 
    def SVA(self, sentence, subject, kwVerb1, kwVerb2):
        """ generated source for method SVA """
        clauseTypeList = []
        constituent = Constituent()
        kwVerb = KeyWord()
        clause = str()
        verbToBe = str()
        complement = str()
        dir = str()
        loc = str()
        mnr = str()
        prp = str()
        tmp = str()
        prd = str()
        # verb = "";
        if kwVerb2 == None:
            kwVerb = kwVerb1
            # verb   = constituent.verb(kwVerb, sentence);
        if kwVerb2 != None:
            kwVerb = kwVerb2
            # verb   = constituent.verb2(kwVerb1, kwVerb2, sentence);
        verbToBe = constituent.verbToBe(kwVerb, sentence)
        complement = constituent.complement(kwVerb, sentence)
        dir = constituent.adverbOfDir(kwVerb, sentence)
        loc = constituent.adverbOfLoc(kwVerb, sentence)
        mnr = constituent.adverbOfMnr(kwVerb, sentence)
        prp = constituent.adverbOfPrp(kwVerb, sentence)
        tmp = constituent.adverbOfTmp(kwVerb, sentence)
        prd = constituent.predicate(kwVerb, sentence)
        # *********************************************************************
        # SVC: write into List<String> about clause type SVC (S+"la"+Complement)
        if ( len(verbToBe)):
            # have not Complement   (S + V="la" + A)  
            if (not complement):
                # write into List<String> about clause type SVA according to location
                if (len(loc)):
                    clause = "SVA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + loc.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVA according to temporal
                if (len(tmp)):
                    clause = "SVA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + tmp.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVAA according to temporal	
                if (len(loc)) and (len(tmp)):
                    clause = "SVAA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + tmp.strip() + "\", \"" + loc.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVA according to purpose
                if (len(prp)):
                    clause = "SVA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + prp.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVA according to purpose
                if (len(prp)) and (len(tmp)):
                    clause = "SVA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + prp.strip() + "\", \"" + tmp.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVA according to direction
                if (len(dir)):
                    clause = "SVA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + dir.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SVA according to manner
                if (len(mnr)):
                    clause = "SVA:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + mnr.strip() + "\")"
                    clauseTypeList.append(clause)
                # write into List<String> about clause type SV predicate
                if (len(prd)):
                    clause = "SV predicate:(\"" + subject.strip() + "\", \"" + verbToBe.strip() + "\", \"" + prd.strip() + "\")"
                    clauseTypeList.append(clause)
        return clauseTypeList

    # end SVA (A: verb to be)
    # *******************************************************************
    # 
    # 	 * Clause Type: SV 
    # 	 * 
    # 	 
    def SV(self, sentence, subject, kwVerb1, kwVerb2):
        """ generated source for method SV """
        clauseTypeList = []
        constituent = Constituent()
        kwVerb = KeyWord()
        clause = str()
        verb = str()
        directObject = str()
        verbToBe = str()
        complement = str()
        dir = str()
        loc = str()
        mnr = str()
        prp = str()
        tmp = str()
        prd = str()
        verb = ""
        if kwVerb2 == None:
            kwVerb = kwVerb1
            verb = constituent.verb(kwVerb, sentence)
        if kwVerb2 != None:
            kwVerb = kwVerb2
            verb = constituent.verb2(kwVerb1, kwVerb2, sentence)
        directObject = constituent.directObject(kwVerb, sentence)
        verbToBe = constituent.verbToBe(kwVerb, sentence)
        complement = constituent.complement(kwVerb, sentence)
        dir = constituent.adverbOfDir(kwVerb, sentence)
        loc = constituent.adverbOfLoc(kwVerb, sentence)
        mnr = constituent.adverbOfMnr(kwVerb, sentence)
        prp = constituent.adverbOfPrp(kwVerb, sentence)
        tmp = constituent.adverbOfTmp(kwVerb, sentence)
        prd = constituent.predicate(kwVerb, sentence)
        # *********************************************************************
        # SV: write into List<String> about clause type SVi
        if (len(verb)) and (not directObject) and (not verbToBe) and (not complement):
            clause = "SV:(\"" + subject.strip() + "\", \"" + verb.strip() + "\")"
            clauseTypeList.append(clause)
            # write into List<String> about clause type SViA (A:location) 
            if (len(loc)):
                clause = "SVA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + loc.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SViA (A:temporal) 
            if (len(tmp)):
                clause = "SVA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SViAA (A:temporal)
            if (len(loc)) and (len(tmp)):
                clause = "SVAA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + loc.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SViA (A:purpose) 
            if (len(prp)):
                clause = "SVA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + prp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SViA (A:purpose) 
            if (len(prp)) and (len(tmp)):
                clause = "SVAA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + prp.strip() + "\", \"" + tmp.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SViA (A:Manner)
            if (len(mnr)):
                clause = "SVA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + mnr.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SViA (A:Direction) 
            if (len(dir)):
                clause = "SVA:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + dir.strip() + "\")"
                clauseTypeList.append(clause)
            # write into List<String> about clause type SVi predicate (A:Direction) 
            if (len(prd)):
                clause = "SV Predicate:(\"" + subject.strip() + "\", \"" + verb.strip() + "\", \"" + prd.strip() + "\")"
                clauseTypeList.append(clause)
        return clauseTypeList

    #  end SV

# end class
