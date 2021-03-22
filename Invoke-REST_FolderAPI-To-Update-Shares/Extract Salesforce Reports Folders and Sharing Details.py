import csv
import requests
from SF_API import SalesforceAPIBangBang

class Folder:
    id = ''
    label = ''
    name = ''
    type = ''
    url = ''
    folderSharesUrl = ''
    shares = []

class Shares:
    accessType = ''
    shareId = ''
    shareType = ''
    sharedWithId = ''
    sharedWithLabel = ''
    

salesforceAPI = SalesforceAPIBangBang()
foldersJSON = salesforceAPI.sf_api_call(action='/services/data/v46.0/folders?page=1&pageSize=300')

folders = foldersJSON["folders"]

foldersList = []

counter = 1

for f in folders:
    
    counter = counter + 1
    
    fld = Folder()
    fld.id = f['id']
    fld.label = f['label']
    fld.name = f['name']
    fld.type = f['type']
    fld.url = f['url']
    
    folderSharesUrl = salesforceAPI.sf_api_call(f['url'])['sharesUrl']
    fld.folderSharesUrl = folderSharesUrl
    
    folderShares = salesforceAPI.sf_api_call(folderSharesUrl)["shares"]

    fldSharesList = []    
        
    for fs in folderShares:
        fldShare = Shares()
        fldShare.accessType = fs['accessType']
        fldShare.shareType = fs['shareType']
        fldShare.shareId = fs['shareId']
        fldShare.sharedWithId = fs['sharedWithId']
        fldShare.sharedWithLabel = fs['sharedWithLabel']
        fldSharesList.append(fldShare)
    
    fld.shares = fldSharesList
    foldersList.append(fld)

    #print("• Share : " + fldShare.accessType + ' , ' + fldShare.shareType + ' - ' + fldShare.sharedWithLabel)
    
   
def make_csv(foldersList):
    with open('data\SF Folder Lists and Shares.csv', 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(['FolderName',
                         'FolderType',
                         'Url',
                         'FolderSharesUrl',
                         'SharedWith',
                         'ShareType',
                         'AccessType'])
        
        for fld in foldersList:
            for fldShare in fld.shares:
                writer.writerow([fld.label, 
                                 fld.type,
                                 fld.url,
                                 fld.folderSharesUrl,
                                 fldShare.sharedWithLabel,
                                 fldShare.shareType,
                                 fldShare.accessType])
                print('• ' + fld.label + ' - ' + fldShare.sharedWithLabel)
                
make_csv(foldersList)
 
