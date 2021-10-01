#!/usr/bin/env python
from .datareader import DataReader
from .keyword import KeyWord
from .sentence import Sentence
from .constituent import Constituent
from .setclause import SetClause

class DataWriter:
    """ generated source for class DataWriter """

    def extract_Sentence(self, dataList):
        sentenceList = []
        sentenceList = self.writeSentenceList_FromList(dataList)
        sentenceList = self.addRelationKeyWord(sentenceList)
        return sentenceList

    def writeSentenceList_FromList(self,dataList):
        readFile = DataReader()
        # ** Write data from List into  SentenceList
        sentenceList = []
        count = 0
        # count the number of lines in a sentence
        j = 0
        # starting position in a sentence
        i = 0
        while i < len(dataList):
            row = dataList[i].strip()
           
            if (not row) and (count > 1):
               
                sentence = Sentence()
                k=0
                while k < count:
                    line = dataList[j].strip()
                    wordLine = readFile.ReadWordLine(line)
                    
                    idWord = wordLine[0]
                    token = wordLine[1]
                    tag = wordLine[4]
                    dependenceId = wordLine[6]
                    dependenceType = wordLine[7]
                    kWord = KeyWord(id=idWord, word=token,posTag= tag,dependenceId= dependenceId,dependenceType= dependenceType)
                    
                    sentence.addKeyWord(kWord)
                    j += 1
                    k += 1
                
                sentenceList.append(sentence)
                j = 0
                count = 0
            else:
                if count == 0:
                    j = i
                count += 1
            i += 1
        return sentenceList

    def extract_SetClause(self, sentenceList):
        """ generated source for method writeFile_SetClause """
        result=[]
        constituent = Constituent()
        setClause = SetClause()
        ClauseTypeList = []
        sentenceLine = str()
        strVerbNumber = []
        
        countWord = 0
        countTrueSentence = 0
        countFalseSentence = 0
        sentenceNumber = 0
        lineNumber = 0
        i = 0
        while i < len(sentenceList):
            sentenceLine = ""
            ClauseTypeList,StatNumberList = setClause.setOfClause(sentenceList[i])

            if (constituent.isSentence(sentenceList[i]) and (len(ClauseTypeList) > 0)):
                countTrueSentence += 1
                countWord = 0
                j=0
                while j < sentenceList[i].size():
                    sentenceLine = sentenceLine + sentenceList[i].getWordAt(j) + " "
                    if not (sentenceList[i].getDependenceTypeAt(j) == "punct"):
                        countWord += 1
                    j += 1
                
            else:
                countFalseSentence += 1
            
            if (len(ClauseTypeList)) and constituent.isSentence(sentenceList[i]):
                strVerbNumber = StatNumberList[0].split("\t")
                verbNumber = int(strVerbNumber[1])
                temp=[]
                if verbNumber >= 1:
                    print(sentenceLine)
                    print("Number of word in sentence: \t" + str(countWord))
                    print("Number of sentences are true: \t" + str(countTrueSentence))

                    k=0
                    while k < len(ClauseTypeList):
                        lineNumber += 1
                        sentenceLine = ClauseTypeList[k]
                        subs = sentenceLine.split(":(")
                        clauseType = subs[0]
                        clause = [x.replace("\"","").strip() for x in subs[1].replace(")","").split("\",")]
                        
                        temp.append({"type":clauseType,"sentence":clause})
                        k += 1
                    result.append(temp)
            
            print(StatNumberList[0])
            print(StatNumberList[1])
            print("\n")
            i += 1
        
        
        print("Write successfull about input data. Giving clause types")
        print("The total number of sentences has in: \t" + str(len(sentenceList)))
        print("The total number of sentences are true: \t" + str(countTrueSentence))
        print("The total number of sentences are false: \t" + str(countFalseSentence))
        return result

    # 
    # 	 *  function main use to read data file and write into a List
    # 	 *  @param  data file  
    # 	 *  @return write data into List that every line is content of a sentence and every word is a KeyWord, 
    # 	 *    
    # 	 
    def writeSentenceList(self, fileName):
        """ generated source for method writeSentenceList """
        sentenceList = []
        sentenceList = self.writeSentenceList_FromFile(fileName)
        sentenceList = self.addRelationKeyWord(sentenceList)
        return sentenceList

    # 
    # 	 *  read data from file and write into a list. However, it don't have add RelationKeyWord  
    # 	 *  @return  Sentence list  
    # 	 
    def writeSentenceList_FromFile(self, fileName):
        """ generated source for method writeSentenceList_FromFile """
        dataList = []
        readFile = DataReader()
        # ******** read from data file into the List  **************
        dataList = readFile.readFile(fileName)
        # ** Write data from List into  SentenceList
        sentenceList = []
        count = 0
        # count the number of lines in a sentence
        j = 0
        # starting position in a sentence
        i = 0
        while i < len(dataList):
            row = dataList[i].strip()
            print("row:",row)
            if (not row) and (count > 1):
                print("null and count > 1")
                sentence = Sentence()
                k=0
                while k < count:
                    line = dataList[j].strip()
                    wordLine = readFile.ReadWordLine(line)
                    print(wordLine)
                    idWord = wordLine[0]
                    token = wordLine[1]
                    tag = wordLine[4]
                    dependenceId = wordLine[6]
                    dependenceType = wordLine[7]
                    kWord = KeyWord(id=idWord, word=token,posTag= tag,dependenceId= dependenceId,dependenceType= dependenceType)
                    
                    sentence.addKeyWord(kWord)
                    j += 1
                    k += 1
                
                #sentence.printSentenceContent()
                sentenceList.append(sentence)
                j = 0
                count = 0
            else:
                if count == 0:
                    j = i
                count += 1
            i += 1
        return sentenceList

    def addRelationKeyWord(self, _sentenceList):
        """ generated source for method addRelationKeyWord """
        sentenceList = []
        sentenceList = _sentenceList
        sentence = Sentence()
        kWord = KeyWord()
        kWordFind = KeyWord()
        i = 0
        while i < len(sentenceList):
            sentence = sentenceList[i]
            j=0
            while j < sentence.size():
                kWord = sentence.get(j)
                k=0
                while k < sentence.size():
                    kWordFind = sentence.get(k)
                    if kWord.getId() == kWordFind.getDependenceId():
                        kWord.addRelationKeyWord(kWordFind)
                    k += 1
                j += 1
            i += 1
        return sentenceList

    def writeFile(self, fileName, sentenceList):
        """ generated source for method writeFile """
        try:
            writer = open(fileName,"w",encoding="utf-8")
            i=0
            while i < len(sentenceList):
                sentenceLine = ""
                j=0
                while j < sentenceList[i].size():
                    sentenceLine = sentenceLine + sentenceList[i].getWordAt(j) + " "
                    j += 1
                sentenceLine = (i + 1) + ": " + sentenceLine + "\t" + sentenceList[i].size()
                writer.write(sentenceLine)
                writer.write("\n")
                i += 1
            writer.close()
            print("write successfull about write data from sentenceList into file")
        except Exception as e:
            print(e.getMessage())
            e.printStackTrace()

    def writeFile_SetClause(self, fileName, sentenceList):
        """ generated source for method writeFile_SetClause """
        writer = open(fileName,"w",encoding="utf-8")
        constituent = Constituent()
        setClause = SetClause()
        ClauseTypeList = []
        sentenceLine = str()
        strVerbNumber = []
        
        countWord = 0
        countTrueSentence = 0
        countFalseSentence = 0
        sentenceNumber = 0
        lineNumber = 0
        i = 0
        while i < len(sentenceList):
            sentenceLine = ""
            ClauseTypeList = setClause.setOfClause(sentenceList[i])
            if (constituent.isSentence(sentenceList[i]) and (len(ClauseTypeList) > 2)):
                countTrueSentence += 1
                countWord = 0
                j=0
                while j < sentenceList[i].size():
                    sentenceLine = sentenceLine + sentenceList[i].getWordAt(j) + " "
                    if not (sentenceList[i].getDependenceTypeAt(j) == "punct"):
                        countWord += 1
                    j += 1
                sentenceLine = str(countTrueSentence) + ": " + sentenceLine + "\t" + str(countWord)
            else:
                countFalseSentence += 1
            if (len(ClauseTypeList)) and constituent.isSentence(sentenceList[i]) and (len(ClauseTypeList) > 2):
                strVerbNumber = ClauseTypeList[len(ClauseTypeList) - 2].split("\t\t")
                verbNumber = int(strVerbNumber[1])
                if verbNumber >= 1:
                    lineNumber += 1
                    sentenceNumber += 1
                    sentenceLine = str(lineNumber) + "\t" + str(sentenceNumber) + "\t" + sentenceLine
                    writer.write(sentenceLine)
                    writer.write("\n")
                    k=0
                    while k < len(ClauseTypeList):
                        lineNumber += 1
                        sentenceLine = str(lineNumber) + "\t" + str(sentenceNumber) + "\t" + ClauseTypeList[k]
                        writer.write(sentenceLine)
                        writer.write("\n")
                        k += 1
                    writer.write("\n")
            i += 1
        totalSentenceNumber = str()
        totalSentenceNumber = "Total sentence number in file: " + "\t" + str(sentenceNumber)
        writer.write(totalSentenceNumber)
        writer.write("\n")
        writer.close()
        print("write successfull about input data into file. Giving clause types")
        print("The total number of sentences has in file: \t" + str(len(sentenceList)))
        print("The total number of sentences are true: \t" + str(countTrueSentence))
        print("The total number of sentences are false: \t" + str(countFalseSentence))

    def printSentenceList(self, sentenceList):
        """ generated source for method printSentenceList """
        i = 0
        while i < len(sentenceList):
            print("\n\n************* Sentence: " + i + "*********************")
            sentenceList[i].printSentenceContent()
            i += 1
