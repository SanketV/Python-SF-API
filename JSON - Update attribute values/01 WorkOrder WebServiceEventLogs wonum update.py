import csv
import pandas as pd
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)


data = pd.read_csv(".\\data\\ReplaceWONUMCorrectionScriptCSV.csv")
workOrderTable = list(zip(data['NG_Request__c'],
                          data['NewJSONwonum'],
                          data['NewJOSNwokorderid'],
                          data['Id'],
                          data['Name']))

updatedJSONDict = {} 

pp.pprint('Req wonum • New wonum • New workorderid ')

for row in workOrderTable:
    
    jsonReq = json.loads(row[0])
    pp.pprint(jsonReq["member"][0]["wonum"] + ' • ' + str(row[1]) + ' • ' + str(row[2]))
    jsonReq["member"][0]["wonum"] = str(row[1])
    jsonReq["member"][0]["workorderid"] = str(row[2])

    updatedJSONDict[row[3]] = jsonReq

    
with open('data\\dataOut.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['Id',
                     'NG_Request__c'
                     ])
    
    for rowJson in updatedJSONDict:
        writer.writerow([rowJson, 
                         json.dumps(updatedJSONDict[rowJson])
                         ])
        
   