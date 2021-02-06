import pickle
import csv
import os

def main():
    bin_path = '/Users/albinjonfelt/Documents/programmering/aktier/bin/'

    bought_list = list(dict())
    with open(os.path.join(bin_path, 'bought.pickle'), 'rb') as f:
        bought_list = pickle.load(f)
    names_list = list(str())
    [names_list.append(each['name']) for each in bought_list if each['name'] not in names_list]
    print(len(names_list))

    
    with open(os.path.join(bin_path, 'clean_names.csv'), 'wt') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(names_list)   

if __name__ == "__main__":
    main()
