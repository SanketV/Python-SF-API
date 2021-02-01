import zeep
from zeep import helpers
import pandas as pd
import pprint
import csv
pp = pprint.PrettyPrinter(indent=4)

wsdl = 'wsdl\wsdl_partner_jackson_prod.xml'
client = zeep.Client(wsdl=wsdl)

print("Call login()")
response = client.service.login(username='sanket.vaidya.fsc@jackson.com', password='Jackson2!tXsUSpJgHKvC8VHY2ON0QqGof')
print("Response : " + str(response.serverUrl))
print("Response : " + str(response.sessionId))

sid = response.sessionId
url = response.serverUrl

# Set new endpoint retrieved from login() call
client.service._binding_options["address"] = url

ids = ['0032E00002zzjJGQAY']

headerDict = {
    'DuplicateRuleHeader':
        {
            'allowSave': 'false',
            'includeRecordDetails': 'true',
            'runAsCurrentUser': 'true'
        },
        'SessionHeader':
        {
            'sessionId': sid
        }
}


class Contact:
    id = ''
    name = ''
    duplicateContactId = ''
    duplicateContactName = ''

result = client.service.findDuplicatesByIds(ids, _soapheaders=headerDict)

print("Duplicate Rule : " + result.body.result[0].duplicateResults[0].duplicateRule)

inputdata = pd.read_csv(".\\data\\Prod_Contacts_Created_Manually.csv", encoding='unicode_escape')
#pp.pprint(inputdata)

contactList = []

for row in inputdata.iterrows():

    rowId = row[1]['ID']
    rowName = row[1]['NAME']
    print(rowId + ', ' + rowName, end=" - ")

    c = Contact()
    c.id = rowId
    c.name = rowName

    result = client.service.findDuplicatesByIds([rowId], _soapheaders=headerDict)

    if result.body.result[0].duplicateResults[0].matchResults[0] is not None and \
            len(result.body.result[0].duplicateResults[0].matchResults[0].matchRecords) > 0:
        dupId = result.body.result[0].duplicateResults[0].matchResults[0].matchRecords[0].record.Id
        dupName = result.body.result[0].duplicateResults[0].matchResults[0].matchRecords[0].record._value_1[2].text
        print(dupId, end=" - ")
        print(dupName)
        c.duplicateContactId = dupId
        c.duplicateContactName = dupName
    else:
        print('No matching record.')
        c.duplicateContactId = ''
        c.duplicateContactName = 'No matching record'
    contactList.append(c)
#
# def make_csv(contactList):
#     with open('data\Out_Prod_ContactsWithDuplicates.csv','w', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter=",")
#         writer.writerow(
#                         ['Contact Id',
#                          'Name',
#                          'Duplicate Contact Id',
#                          'Duplicate Contact Name']
#         )
#
#         for c in contactList:
#             writer.writerow([c.id,
#                              c.name,
#                              c.duplicateContactId,
#                              c.duplicateContactName])
#
#
# make_csv(contactList)
