from datetime import datetime
import pickle
import os
import json

def calculate_stats_from_sold_stock(temp_sold_list, bought_stock):

    last_date = datetime.strptime(bought_stock['buisday'], "%Y-%m-%d")
    first_day = datetime.strptime(bought_stock['buisday'], "%Y-%m-%d")
    qty_sold = 0
    value = 0.0
    total = 0.0
    for each in temp_sold_list:
        value = float(each['totvalue'])
        total += value
        if datetime.strptime(each['buisday'], "%Y-%m-%d") > last_date:
            last_date = datetime.strptime(each['buisday'], "%Y-%m-%d")
        qty_sold += int(each['qty'])

    diff_days = last_date - first_day
    avg_selling_price = total / int(bought_stock['qty'])


    temp_dict = {
        'name': bought_stock['name'],
        'avg_sell_price': avg_selling_price,
        'held_days': diff_days,
    }
    return temp_dict


def main():
    os.chdir("/Users/albinjonfelt/Documents/programmering/aktier/python/")
    print("Started program...")
    bought_list = list(dict())
    sold_list = list(dict())
    all_list = list(dict())

    bin_path = os.path.join(os.path.dirname(os.getcwd()), 'bin')
    #Ladda in all picklad data, som kommer från transaktionsexporter
    with open(os.path.join(bin_path, 'bought.pickle'), 'rb') as f:
        bought_list = pickle.load(f)
    with open(os.path.join(bin_path, 'sold.pickle'), 'rb') as f:
        sold_list = pickle.load(f)
    with open(os.path.join(bin_path, 'all.pickle'), 'rb') as f:
        all_list = pickle.load(f)
    print("Loaded data...")

    all_list.sort(key=lambda extract : extract['name'])

    for x in range(len(all_list)):
        if all_list[x]['name'] == "ABB_U":
            all_list[x]['name'] == "ABB"

    closed_trades = list(list(dict()))
    active_trades = list(list(dict()))
    same_stock_names = list()
    for transaction in all_list:
        #This is only for the first transaction
        if len(same_stock_names) == 0:
            same_stock_names.append(transaction)
        elif transaction['name'] == same_stock_names[0]['name']:
            same_stock_names.append(transaction)
        else:
            
            same_stock_names.sort(key=lambda extract : extract['id'])
            print(len(same_stock_names))
            print(same_stock_names[0]['name'])

            bought = 0
            sold = 0
            one_trade = list()
                
            for each in same_stock_names:
                
                if(each['transtype'] == 'KÖPT'):
                    bought += int(each['qty'])
                    one_trade.append(each)
                
                elif(each['transtype'] == 'SÅLT'):
                    sold += int(each['qty'])
                    one_trade.append(each)

                else:
                    raise Exception('Wrong type of transaction-type')

                if(bought == sold and bought != 0):
                    print("Adding a new stock to closed trades: " + one_trade[0]['name'])
                    closed_trades.append(one_trade[:])
                    one_trade.clear()
                    bought = 0
                    sold = 0
            
            if(bought > sold):
                active_trades.append(one_trade)
                
            same_stock_names.clear()
            same_stock_names = [transaction]
    def clean_name(name):
        clean_name = name
        if("BEAR" in name or "BULL" in name):
            first_pos = clean_name.find("_", clean_name.find("_"))
            clean_name = clean_name[first_pos + 1:]
            last_pos = clean_name.find("_")
            clean_name = clean_name[:last_pos]
        elif ("MINI" in name):
            first_pos = clean_name.find("_", clean_name.find("_") + 1)
            clean_name = clean_name[first_pos + 1:]
            last_pos = clean_name.find("_")
            clean_name = clean_name[:last_pos]

        return clean_name

    list_of_trades = list()
    for trade in closed_trades:
        indexed_trade = {
            "name" : clean_name(trade[0]['name']),
            "id" : int(trade[len(trade) - 1]['id']),
            "category" : "closed",
            "transactions" : trade
        }
        list_of_trades.append(indexed_trade)

    for trade in active_trades:
        indexed_trade = {
            "name" : clean_name(trade[0]['name']),
            "id" : int(trade[len(trade) - 1]['id']),
            "category" : "open",
            "transactions" : trade
        }
        list_of_trades.append(indexed_trade)

    with open(os.path.join(bin_path, 'all_trades.json'), 'w') as active_trades_json:
       json.dump(list_of_trades, active_trades_json,indent = 4)
    
if __name__ == "__main__":
    main()
