import xml.sax
import xmltodict
import pprint
import glob
import csv

pp = pprint.PrettyPrinter(indent=4)


reportList = []

def make_csv():
    print("• • make csv • •")
    with open(".\\data\\01 Reports and Criteria.csv", 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(['ReportName', 'Criteria'])
        for l in reportList:
            rPath = l[0].replace('Reports-2\\reports\\','')
            writer.writerow([rPath, l[1]])
            

def insertReportEntry(reportName, criteria):   
    tupleEntry = reportName, criteria    
    reportList.append(tupleEntry)
    print('♠ ♠ ♠ ' + reportName + ' --- ' + criteria )
              
   
if ( __name__ == "__main__"):
      
   for file in glob.glob("**/*.report", recursive=True):
       #pp.pprint("• • File name : " + file)
       
       with open(file) as fd:
           doc = xmltodict.parse(fd.read())
    
       filtersDict = doc["Report"].get("filter")
       
       if filtersDict is not None:
           
           criteriaDict = filtersDict.get("criteriaItems")
           
           if criteriaDict is not None:
               if isinstance(criteriaDict, list):
                   for criteriaDictElement in criteriaDict:                   
                       if criteriaDictElement["column"] == "Account$Owner.UserRole":
                           #pp.pprint(" • " + criteriaDictElement["value"])
                           insertReportEntry(file, criteriaDictElement["value"])
               elif isinstance(criteriaDict, dict):
                   donothin = None
                   #if criteriaDict["column"] == "Account$Owner.UserRole":
                   #pp.pprint(criteriaDict)
                           
   make_csv()    
   
   
   