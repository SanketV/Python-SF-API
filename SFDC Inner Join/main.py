import pandas as pd

df_PlatformRep_from_classic = pd.read_csv('.\\data\\00 CLASSIC 1 - Contact Platform Rep.csv', encoding='latin1')
df_NonRep_from_classic = pd.read_csv('.\\data\\00 CLASSIC 2 - Contact Non-Rep.csv', encoding='latin1')
df_from_QA = pd.read_csv('.\\data\\05 Lightning QA - Contacts.csv', encoding='latin1')
df_from_QA_LEADS = pd.read_csv('.\\data\\06 Lightning QA - Leads.csv', encoding='latin1')

resultPlatformRep = pd.merge(df_PlatformRep_from_classic, df_from_QA, on='Migration_Key__c')
resultNonRep = pd.merge(df_NonRep_from_classic, df_from_QA, on='Migration_Key__c')

print('• Total matching records for Platform Rep : ' + str(resultPlatformRep['Migration_Key__c'].count()))
print("• Total matching Record for Non-Rep: " + str(resultNonRep["Migration_Key__c"].count()))

resultPlatformRep.to_csv(".\\data\\out_01_Platform_Rep_Contacts_in_Lightning.csv")
resultNonRep.to_csv(".\\data\\out_02_Non_Rep_Contacts_in_Lightning.csv")

resultPlatformRep_CheckWithLeads = pd.merge(df_PlatformRep_from_classic, df_from_QA_LEADS, on='Migration_Key__c')
resultNonRep_CheckWithLeads = pd.merge(df_NonRep_from_classic, df_from_QA_LEADS, on='Migration_Key__c')
print('• Matching records for Platform Rep with LEADS : ' + str(resultPlatformRep_CheckWithLeads['Migration_Key__c'].count()))
print('• Matching records for Non Rep with LEADS : ' + str(resultNonRep_CheckWithLeads['Migration_Key__c'].count()))


