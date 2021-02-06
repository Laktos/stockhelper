#!/usr/bin/python
import csv
import sys, getopt
import re
import string

def main(argv):
   inputfile = argv[0]
   outputfile = argv[1]
   print(inputfile)
   print(outputfile)
    
   with open(inputfile, "rt") as csv_file:
    my_reader = csv.reader(csv_file, delimiter=";")

    with open(outputfile, 'wt') as f:
        writer = csv.writer(f, delimiter=";")

        for row in my_reader:
            if (row[6] == "Aktier" or "Mini" in row[6] or "Certifikat" in row[6]) and (row[4] in ['KÖPT', 'SÅLT', 'INLÖSEN UTTAG VP']):
                row = row[0:19]
                row.pop(10)
                row.pop(7)
                row.pop(1)
                for i in range (0, len(row)):
                    if ' ' in row[i] or ',' in row[i]:
                        if i == 4:
                            row[i] = re.sub(r"\s+", "_", row[i], flags=re.UNICODE)
                            #Abnormalities which have changed name over the course of owning the stocks.
                            row[i] = row[i].replace('ABB_U', 'ABB')
                            row[i] = row[i].replace('SPOR_TIA', 'SPOR')
                        elif i == 3:
                            row[i] = row[i].replace('INLÖSEN UTTAG VP', 'SÅLT')
                        else: 
                            row[i] = re.sub(r"\s+", "", row[i], flags=re.UNICODE)
                            row[i] = row[i].replace(',', '.')    


                    if '−' in row[i] and i > 5:
                        new_string = row[i]
                        row[i] = re.sub('−', '-', new_string)    
                    row[i] = re.sub(r"\s+", "", row[i], flags=re.UNICODE)
                writer.writerow(row)
    

if __name__ == "__main__":
   main(sys.argv[1:])





    