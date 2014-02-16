import csv

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, delimiter=';', **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

filename = 'MMR-kannanir.csv'

ifile  = open(filename, "rb")
reader = unicode_csv_reader(open(filename))
rownum = 0
batch = []
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        #print row
        colnum = 3
        columns = range(3,len(row))
        for column in columns:
            batch.append([header[column], row[1],row[0], row[column]])
    rownum += 1

ifile.close()
import unicodecsv
filename = open("transposed_for_kannanir_master.csv", 'wb')
w = unicodecsv.writer(filename, encoding='utf-8')
w.writerows(batch)
