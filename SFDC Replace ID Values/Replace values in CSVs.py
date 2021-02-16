import pprint
import glob
import csv

pp = pprint.PrettyPrinter(indent=4)

text = open("DataLoaderCSVFiles\\ProdDataContacts - bpdSanket.csv", "r")
for file in glob.glob("FindReplaceValues/*.csv", recursive=True):
   pp.pprint("• • File name : " + file)
   with open(file) as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
           print(row['IdToFind'] + ' • ' + row['IdToReplace'])
           text = ''.join([i for i in text]).replace(row['IdToFind'], row['IdToReplace'])

pp.pprint(text)
x = open("output.csv","w")
x.writelines(text)
x.close()

