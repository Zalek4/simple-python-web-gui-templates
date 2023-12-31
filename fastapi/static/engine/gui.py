import datetime
import time
import inspect
import ah_logging
log = ah_logging.Logging.log
date = datetime.date

class LT_Gui():
    # ===================================================
    # Function Name: ext_get_date
    # Description: Gets the current date in "Month date, year" format.
    # Input values: N/A
    # ===================================================
    def ext_get_date():
        st = time.time()
        func_name = inspect.stack()[0][3]
        log(1, f'{func_name:=^80}')
    
        try:
            today = date.today()
            formatted_date = today.strftime('%B %d, %Y')
    
        except:
            log(4, 'CRITICAL ERROR')
    
        et = time.time()
        tt = et - st
        log(1, f'Function executed in - {tt}')
        return(formatted_date)