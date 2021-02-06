import os
from osascript import osascript
from datetime import date, datetime
os.chdir("/Users/albinjonfelt/Documents/programmering/aktier/python/")
bin_path = os.path.join(os.path.dirname(os.getcwd()), 'bin')
name_of_files = os.listdir(bin_path)
try:
    found_file = [filename for filename in name_of_files if 'clean_file.csv' in filename]
    os.remove(os.path.join(bin_path, 'all.pickle'))
    os.remove(os.path.join(bin_path, 'sold.pickle'))
    os.remove(os.path.join(bin_path, 'bought.pickle'))
    for filename in found_file:
        os.remove(os.path.join(bin_path, filename))
    print("Removed pickles and clean transaction data")
except (IndexError, FileNotFoundError):
    print("Some pickle file(s) was not found")
    pass

name_of_files = os.listdir()
found_file = next((filename for filename in name_of_files if 'transactions_export' in filename), False)
script_path = os.path.join(os.getcwd(), 'csv_to_pickle.py')
if found_file != False:
    print("There was a transactions-file")
    osascript('/Users/albinjonfelt/Documents/programmering/aktier/scripts/export_to_utf8.scpt')
    exec(open(script_path).read(), globals())
else:
    print("There was no transactions-file, will download a new one throught csv_cleaner_transactions.")   
    exec(open(script_path).read(), globals())
    
