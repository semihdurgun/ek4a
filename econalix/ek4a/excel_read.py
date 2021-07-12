import pandas as pd
from pathlib import Path
import json

def excel_read_and_save(pageName):
    try:
        xls = pd.read_excel(r'.\excel_file\ek_4A_08.07.2021.xlsx',sheet_name=pageName)
        df = pd.DataFrame(xls, columns=xls.columns) 
        df = df.assign( **df.select_dtypes(['datetime']).astype(str).to_dict('list') ).to_json(orient="records")
        parsed = json.loads(df)  
    except ValueError as e:
        print( e)
        parsed = []    
    
    return parsed

    #sheet_to_df = {}
    #for sheet_name in xls.sheet_names:
    #    sheet_to_df[sheet_name] = xls.parse(sheet_name)  
    #return sheet_to_df     
        