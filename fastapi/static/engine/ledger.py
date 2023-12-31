import time
import datetime
import json
import string
import inspect
import ah_logging
from engine import globals
log = ah_logging.Logging.log
today = datetime.date.today()

class LT_Accounting():
    # ===================================================
    # Function Name: N/A
    # Description: N/A
    # Input values: N/A
    # ===================================================
    def ext_update_global():
        st = time.time()
        func_name = inspect.stack()[0][3]
        log(1, f'{func_name:=^80}')
    
        try:
            globals.test = "I'm an updated global!"
            log(1, globals.test)
    
        except:
            log(4, 'CRITICAL ERROR')
    
        et = time.time()
        tt = et - st
        log(1, f'Function executed in - {tt}')

    # ===================================================
    # Function Name: N/A
    # Description: N/A
    # Input values: N/A
    # ===================================================
    def ext_send_global():
        st = time.time()
        func_name = inspect.stack()[0][3]
        log(1, f'{func_name:=^80}')
    
        try:
            test = globals.test
    
        except:
            log(4, 'CRITICAL ERROR')
    
        return(test)

        et = time.time()
        tt = et - st
        log(1, f'Function executed in - {tt}')

    # ===================================================
    # Function Name: lt_create_ledger
    # Description: Creates a ledger at the specified directory
    # Input values: N/A
    # ===================================================
    def lt_create_ledger():
        st = time.time()
        func_name = inspect.stack()[0][3]
        log(1, f"{func_name:=^80}")

        try: 
            log(1, f"Creating ledger at : [INSERT LEDGER PATH HERE]")

            new_ledger_data = {
                "assets": {},
                "holdings": {},
                "liabilities": {},
                "buckets": {},
                "transactions": {}
            }

            ledger_json = json.dumps(new_ledger_data, indent=4)

            with open("ledger.json", "w") as outfile:
                outfile.write(ledger_json)
        
        except:
            log(4, "CRITICAL ERROR")

        et = time.time()
        tt = et - st
        log(1, f"Function executed in - {tt}")

# ===================================================
    # Function Name: lt_read_ledger
    # Description: Reads a ledger at the specified directory
    # Input values: file(string - file path)
    # ===================================================
    def lt_read_ledger(file):
        log(1, f"{'Reading ledger':=^80}")
        log(1, f"Attempting to read ledger from : {file}")

        ledger = open(file)

        ledger_data = json.load(ledger)

        log(1, f"Ledger contains :")
        data_types = list()
        for data_type in ledger_data:
            data_types.append(data_type)

        for item in data_types:
            log(1, f"{item} : {len(ledger_data[item])}")

        return(ledger_data)

    # ===================================================
    # Function Name: lt_create_asset
    # Description: Creates an asset in the loaded ledger
    # Input values: account_name (string), account_balance(float)
    # ===================================================
    def lt_create_asset(account_name, account_balance):
        log(1, f"{'Creating Asset':=^80}")

        try:
            alphabet = list(string.ascii_lowercase)
            for letter in alphabet:
                creation_date = today.strftime("%Y/%m/%d")
                account_info = {
                    "name": f"{account_name}_{letter}",
                    "status": "Open",
                    "balance": account_balance,
                    "date": creation_date
                }

                ledger_data = globals.ledger_data
                ledger_data['assets'][account_info['name']] = account_info
                log(1, f">\tAsset created : {account_name}")

                json_object = json.dumps(ledger_data, indent=4)

                with open("ledger.json", "w") as outfile:
                    outfile.write(json_object)

        except:
            log(4, f"CRITICAL ERROR")

    # ===================================================
    # Function Name: lt_create_holding
    # Description: Creates a holding in the loaded ledger
    # Input values: N/A
    # ===================================================
    def lt_create_holding():
        st = time.time()
        func_name = inspect.stack()[0][3]
        log(1, f'{func_name:=^80}')
    
        try:
            alphabet = list(string.ascii_lowercase)
            for letter in alphabet:
                holding_name = "Invesco S&P 500 Equal Weight ETF"
                holding_ticker = "RSP"
                creation_date = today.strftime("%Y/%m/%d")
                holding_info = {
                    "name": f"{holding_name}_{letter}",
                    "ticker": holding_ticker,
                    "date": creation_date
                }

                # I think this can use the original globals approach instead of this.
                ledger_data = LT_Accounting.lt_read_ledger()
                ledger_data['holdings'][holding_info['name']] = holding_info
                log(1, f"Holding created : {holding_name}")

                json_object = json.dumps(ledger_data, indent=4)

                with open("ledger.json", "w") as outfile:
                    outfile.write(json_object)
    
        except:
            log(4, 'CRITICAL ERROR')
    
        et = time.time()
        tt = et - st
        log(1, f'Function executed in - {tt}')

if __name__ == "__main__":
    LT_Accounting.lt_read_ledger("C:/ah/github/lute/ledger.json")
    LT_Accounting.lt_create_holding()