import csv

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, delimiter=';', **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

filename = 'fylgi-flokka-allir.csv'

ifile  = open(filename, "rb")
reader = unicode_csv_reader(open(filename))
rownum = 0
batch = []

def parse_date(datestring):
    #datestring = datestring.replace('-','.')
    splits = datestring.split('-')
    return splits


for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        #print row
        colnum = 3
        columns = range(3,len(row))
        for column in columns:
            datelist = parse_date(header[column])
            batch.append([datelist[2]+"."+datelist[1]+"."+datelist[0], row[1],row[0], row[column]])
    rownum += 1

ifile.close()


import unicodecsv
filename = open("capacent_transposed_for_kannanir_master.csv", 'wb')
w = unicodecsv.writer(filename, encoding='utf-8')
w.writerow(['Dags','Konnun','Flokkur','Fylgi'])
w.writerows(batch)
