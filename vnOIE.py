from .datawriter import DataWriter

class vnOIE:
    """ generated source for class vnOIE """

    def extract(dataList):
        Writer = DataWriter()

        sentenceList = []
        
        sentenceList = Writer.extract_Sentence(dataList)

        result = Writer.extract_SetClause(sentenceList)

        return result

    def main():
        Writer = DataWriter()

        fileName = "/home/huanbd/vnoie/resources/data_in.txt"
        
        sentenceList = []
        
        sentenceList = Writer.writeSentenceList(fileName)

        outputFileName = "/home/huanbd/vnoie/resources/data_out.txt"

        Writer.writeFile_SetClause(outputFileName, sentenceList)
