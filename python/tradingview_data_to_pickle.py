from datetime import datetime
import pickle
import os
import csv
import json
import uuid

def main():
    os.chdir("/Users/albinjonfelt/Documents/programmering/aktier/python/")

    names_of_files = os.listdir('/Users/albinjonfelt/Documents/programmering/aktier/data')
    #Remove that pesky ds_store, which saves the structure of the files in the folder. 
    names_of_files.remove(".DS_Store")

    path = '/Users/albinjonfelt/Documents/programmering/aktier/data/'

    #Kommer åt individuella värden genom big_dict[stock_name][index 0 -> antal rader][info]
    
    #Convert timestamp in tradingview files to readable date
    from_timestamp_to_date_string = lambda timestamp : datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d')
    list_of_stock_data = list()
    #big_dict = dict(list(dict()))
    for file_name in names_of_files:
        with open(path + file_name, "r") as f:
            my_reader = csv.DictReader(f, delimiter=";", dialect='excel')
            stock_name = file_name[file_name.find('_') + 1: file_name.find(',')]
            #Row list has all the data of one stock.
            row_list = list()
            for row in my_reader:
                #Change names of some rows that can't be read as JSON in swift otherwise.
                row['kStoch'] = row.pop('%K')
                row['dStoch'] = row.pop('%D')
                row['moneyflow'] = row.pop('MF')
                row['signalMacd'] = row.pop('Signal')
                row['baseLine'] = row.pop('Base Line')
                row['conversionLine'] = row.pop('Conversion Line') 
                row['volumeMa'] = row.pop('Volume MA')
                row['laggingSpan'] = row.pop('Lagging Span')
                row['leadOne'] = row.pop('Lead 1')
                row['leadTwo'] = row.pop('Lead 2')
                row['bollingerbandspercentage'] = row.pop('Bollinger Bands %B') 
                row['date'] = from_timestamp_to_date_string(row['time'])
                row_list.append(row)
        #Insert the entire row list (all rows from one csv file) into the dictionary, using the edited file name (the stock name) as key
        one_stock = {
            "name" : stock_name,
            "data" : row_list,
            "id" : str(uuid.uuid4())
        }
        list_of_stock_data.append(one_stock)

    #Example on how to use the dictionary for getting all dates available
    #for x in range(0, len(big_dict['TOBII'])): print(big_dict['TOBII'][x]['date'])
    bin_path = os.path.join(os.path.dirname(os.getcwd()), 'bin')
    with open(os.path.join(bin_path, 'big_dict.pickle'), 'wb') as f:
        pickle.dump(list_of_stock_data, f, pickle.HIGHEST_PROTOCOL)
    with open(os.path.join(bin_path, 'downloaded_tradingview_data.json'), 'w') as data:
        json.dump(list_of_stock_data, data, indent = 4, sort_keys=True)
   

if __name__ == "__main__":
    main()