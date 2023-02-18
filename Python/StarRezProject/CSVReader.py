import csv
import docx

file = open('Loft Kit Requests - Pending ORL.csv')
mydoc = docx.Document()
type(file)

csvreader = csv.reader(file)
rows = []

for row in csvreader:
    rows.append(row)
   
rows

file.close()

for x in rows:
    mydoc.add_paragraph(x)
    

mydoc.save("Loft_Kit_Stickers.docx")



print(rows)