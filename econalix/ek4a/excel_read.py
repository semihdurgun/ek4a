import pandas as pd
from pathlib import Path
import json, os
from econalix.settings import BASE_DIR

def excel_read_and_save(pageName,year,week):
    try:
        sheet_name = BASE_DIR / ('excel_file' + "\\"+ str(year) + '-' + str(week) + '.xlsx')
        xls = pd.read_excel(sheet_name,sheet_name=pageName)
        df = pd.DataFrame(xls, columns=xls.columns)
        df = df.assign( **df.select_dtypes(['datetime']).astype(str).to_dict('list') ).to_json(orient="records")
        parsed = json.loads(df)
    except ValueError as e:
        print( e)
        parsed = []    
    except FileNotFoundError as e:
        print( e)
        return -1 

    return parsed
        