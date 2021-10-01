#!/usr/bin/env python

class DataReader:
    """ generated source for class DataReader """
    # 
    # 	 * read data from file
    # 	 *
    # 	 * @param data file name 
    # 	 * @return list of file data 
    # 	 
    def readFile(self, fileName):
        """ generated source for method readFile """
        try:
            reader = open(fileName,"r",encoding="utf-8")
            data=[]
            print("readFile")
            for line in reader.readlines():
                if line !=None:
                     data.append(line)    
            reader.close()
            print("cound data: ",len(data))
            return data
        except Exception as e:
            print(e.getMessage())
            e.printStackTrace()
            return None

    # end readFile
    # 
    # 	 * Read a data Line and return String [] words 
    # 	 *
    # 	 * @param  a data Line in List
    # 	 * @return String[] words in a line 
    # 	 
    def ReadWordLine(self, dataLine):
        """ generated source for method ReadWordLine """
        words = dataLine.split("\t")
        return words

    # 
    # 	 * print all data by line which a line is a string 
    # 	 *
    # 	 * @param  a data Line in List
    # 	 * @return all lines in data file 
    # 	 
    def printDataFile(self, dataFileList):
        """ generated source for method printDataFile """
        i = 0
        while i < len(dataFileList):
            print(dataFileList[i])
            i += 1

# WARNING runTransform: Generated source has invalid syntax. invalid syntax (<string>, line 29)