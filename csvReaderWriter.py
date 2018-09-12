import csv
import phpserialize
import collections

inputFileName = 'testCsvFile.csv'
outputFileName = 'testCsvFileOut.csv'

with open(inputFileName) as csvFileInput, open(outputFileName, 'w') as csvFileOutput:
     csvDataInput   = csv.reader(csvFileInput, delimiter = ';', quotechar="'")
     csvWriter = csv.writer(csvFileOutput, delimiter=';', quotechar="'", lineterminator = '\n')
     
     #iteration = 1
     for row in csvDataInput:
          print(row)
          unserializedData = phpserialize.loads(bytes(row[3], 'utf-8'), array_hook=collections.OrderedDict)

          csvWriter.writerow(
                    [
                         unserializedData[b'intKey'], 
                         unserializedData[b'arrayKey'], 
                         unserializedData[b'boolKey']
                    ]
          )
          
'''
          if(iteration == 4):
               break
          iteration = iteration + 1
'''
print('Done')