import zeep
from zeep import helpers
from lxml import etree
import requests
import xml.etree.ElementTree as ET
from zeep import xsd
from zeep.plugins import HistoryPlugin
import urllib, os

# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
# client = zeep.Client(wsdl=wsdl)
# print(client.service.Method1('Zeep', 'is cool'))

wsdl = 'wsdl\soapresponder.wsdl.xml'
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('LOCAL Zeep WSDL', 'is super cool.'))
history = HistoryPlugin()

wsdl = 'wsdl\wsdl_partner_jackson_qa.xml'
client2 = zeep.Client(wsdl=wsdl, plugins=[history])

print("Call login()")

response = client2.service.login(username='sanket.vaidya.fsc@jackson.com.qa',password='Jackson3!NhCgdAONzaxx0IiknUHKAQbx')

print("Response : " + str(response.serverUrl))
print("Response : " + str(response.sessionId))

sid = response.sessionId
url = response.serverUrl

print("url : " + url)

client2.service._binding_options["address"] = url

print("Session id : " + sid)

ids = ['0032E00002zzjJGQAY']
print('Invoking Find Duplicates 3')

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


result = client2.service.findDuplicatesByIds(ids, _soapheaders=headerDict)

sObjectWSDL = client2.get_type('ns0:sObject')
print(sObjectWSDL)
retObj = helpers.serialize_object(result.body.result[0].duplicateResults[0].matchResults[0].matchRecords[0].record._value_1, client2.get_type('ns0:sObject'))
#print(retObj)
print(retObj)

