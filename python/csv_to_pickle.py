#!/usr/bin/python
import csv
import sys
import getopt
import os
from datetime import datetime, date, timedelta
import pickle
from osascript import osascript

#Lägger till ny data i pickles, ifall det inte finns någon ny data så hämta den och lägg till.
def main(argv):
    os.chdir("/Users/albinjonfelt/Documents/programmering/aktier/python/")

    inputfile = ""
    desired_file_name = date.isoformat(datetime.now()) + "clean_file.csv"

    bought_list = list(dict())
    sold_list = list(dict())
    all_list = list(dict())
    bin_path = os.path.join(os.path.dirname(os.getcwd()), 'bin')
    try:
        
        bought_path = os.path.join(bin_path, 'bought.pickle')
        with open(bought_path, 'rb') as f:
            bought_list = pickle.load(f)
        f.close()
        
        sold_path = os.path.join(bin_path, 'sold.pickle')
        with open(sold_path, 'rb') as f:
            sold_list = pickle.load(f)
        f.close()

        all_path = os.path.join(bin_path, 'all.pickle')
        with open(all_path, 'rb') as f:
            all_list = pickle.load(f)
        f.close()

    except FileNotFoundError:
        print("One or more pickle files missing, this will result in creating new pickle files")
        pass

    # First look in the bin folder after a cleaned file, if there is one, use that one and read from.
    # If these is none, download a new transaction export from nordnet.
    # The downloaded file defaults to using the same folder it was run from, which is the python folder.
    # Would be neat if it actually followed the instructions that are stored in chrome.
    # Anyhow, then the AppleScript for converting the CSV to utf-8 standard and outputs it to the bin folder.
    # The AppleScript also runs the "csv_cleaner_transactions.py" which cleans the file from unneccessary values.
    if desired_file_name not in os.listdir(bin_path):
        print("No clean file from today, downloading new file...")
        exec(open("/Users/albinjonfelt/Documents/programmering/aktier/python/login_and_download.py").read(), globals())
        print("Done downloading, running cleaning script...")
        return_val = osascript(
            '/Users/albinjonfelt/Documents/programmering/aktier/scripts/export_to_utf8.scpt')
        inputfile = return_val[1]
        print(f"Using file {inputfile} as input...")
    else:
        print(
            f"Using {desired_file_name} as input")
        inputfile += ('/Users/albinjonfelt/Documents/programmering/aktier/bin' +
                      "/" + desired_file_name)

    # Save all the values of one specific row into a dictionary, and append that to a list of dictionaries.
    # The values of the dictionary can then be accessed through bought/sold/all_list[X]['value_to_access']
    # Where X is to be iterable
    with open(inputfile, "r") as csv_file:
        my_reader = csv.reader(csv_file, delimiter=";", dialect='excel')
        for row in my_reader:
            csv_dict = {
                'id': row[0],
                'buisday': row[1],
                'liqday': row[2],
                'transtype': row[3],
                'name': row[4],
                'instrumenttype': row[5],
                'qty': row[6],
                'price': row[7],
                'fees': row[8],
                'totvalue': row[9],
                'forex': row[10],
                'buytotvalue': row[11],
                'result': row[12],
                'totqty': row[13],
                'balance': row[14],
                'forexrate': row[15]
            }

            exists = False
            for each in all_list:
                if csv_dict['id'] == each['id']:
                        exists = True
            if exists == False:
                all_list.append(csv_dict)
                
            if csv_dict['transtype'] == 'SÅLT':
                exists = False
                for each in sold_list:
                    if csv_dict['id'] == each['id']:
                        exists = True
                if exists == False:
                    sold_list.append(csv_dict)

            if csv_dict['transtype'] == 'KÖPT':
                exists = False
                for each in bought_list:
                    if csv_dict['id'] == each['id']:
                        exists = True
                if exists == False:
                    bought_list.append(csv_dict)

    folder_path = '/Users/albinjonfelt/Documents/programmering/aktier/bin/'

    with open(folder_path + 'sold.pickle', 'wb') as f:
        pickle.dump(sold_list, f, pickle.HIGHEST_PROTOCOL)
    f.close()
    with open(folder_path + 'bought.pickle', 'wb') as f:
        pickle.dump(bought_list, f, pickle.HIGHEST_PROTOCOL)
    f.close()
    with open(folder_path + 'all.pickle', 'wb') as f:
        pickle.dump(all_list, f, pickle.HIGHEST_PROTOCOL)
    f.close()
    print("All values pickled!")


if __name__ == "__main__":
    main(sys.argv[1:])
