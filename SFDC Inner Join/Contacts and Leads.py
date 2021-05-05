import pandas as pd

csvCounter: int = 1

df_Classic_Contacts = pd.read_csv(
    'C:\\•Jackson\\05 02 21 SFCOM-1438 Non Advisor Leads\\Classic Contacts RecType IMG JNLD RBD.csv', encoding='latin1')
df_Lightning_Leads = pd.read_csv('C:\\•Jackson\\05 02 21 SFCOM-1438 Non Advisor Leads\\Lightning Leads.csv',
                                 encoding='latin1')

matchingLeads = pd.merge(df_Classic_Contacts, df_Lightning_Leads, left_on='ID', right_on='MIGRATION_KEY__C')

# print("• Total matching Leads found : " + str(matchingLeads.count()))

matchingLeads.to_csv("C:\\•Jackson\\05 02 21 SFCOM-1438 Non Advisor Leads\\00 Matching_Leads_Contacts.csv")

groupOnTerritoryChannel = matchingLeads.groupby('TERRITORY_CHANNEL__R.NAME')

# print(groupOnTerritoryChannel.count())

for channelName, channelGroup in groupOnTerritoryChannel:
    print("•" + channelName)
    channelName = str(channelName).replace("/", "_")
    channelGroup.to_csv(
        'C:\\•Jackson\\05 02 21 SFCOM-1438 Non Advisor Leads\\0{} Matching_Leads_Contacts_{}.csv'.format(csvCounter,
                                                                                                        channelName))
    csvCounter = csvCounter + 1
    # channelGroup[['ID_y', 'ACCOUNT.NAME']]
#
# matchingLeads.to_csv("C:\\•Jackson\\05 02 21 SFCOM-1438 Non Advisor Leads\\01 Matching_Leads_Contacts.csv")
#
# for i in range(1, 100):
#     print("")
#     for data in matchingLeads:
#         print(matchingLeads[data], end=",")
