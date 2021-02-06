import os
import csv
from datetime import datetime
from datetime import date

os.chdir("/Users/albinjonfelt/Documents/programmering/aktier/python/")
download_folder = "/Users/albinjonfelt/Downloads"
name_list = os.listdir(download_folder)
downloaded_stocks = list()

desired_stocks = list()

bin_path = os.path.join(os.path.dirname(os.getcwd()), 'bin')

with open(os.path.join(bin_path, "clean_names.csv"), "r") as csv_file:
    my_reader = csv.reader(csv_file, delimiter=";")
    transform = list(list()) 
    for row in my_reader:
        transform.append(row)
    for each in transform[0]:
        desired_stocks.append(each)

for each in name_list:
    first_pos = each.find('_')
    last_pos = each.find(',')
    
    if(".csv" in each):
        if each[first_pos + 1: last_pos] not in desired_stocks:
            os.remove(os.path.join(download_folder, each))
            continue
        elif each[first_pos + 1: last_pos] in downloaded_stocks:
            os.remove(os.path.join(download_folder, each))
            continue
            
        downloaded_stocks.append(each[first_pos + 1:last_pos])

missing = list()

for each in desired_stocks:
    if each not in downloaded_stocks:
        print(each)
        missing.append(each)

clean_missing = list()

for each in missing:
    #print (each)
    if 'MINI' in each:
        first_pos = each.find('_')
        last_pos = each.index('_', first_pos + 3)    
        clean_missing.append(each[first_pos + 3:last_pos])
    elif 'BEAR' in each or 'BULL' in each:
        first_pos = each.find('_')
        last_pos = each.index('_', first_pos + 4)    
        clean_missing.append(each[first_pos + 1:last_pos])
    else:
        clean_missing.append(each)

no_dupes = list()
[no_dupes.append(each) for each in clean_missing if each not in no_dupes]

with open(os.path.join(bin_path, 'missing_stocks.csv'), 'wt') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(no_dupes)  

            


