import pandas as pd
from pathlib import Path
import json, os

def excel_read_and_save(my_barcode):
    if my_barcode == '':
        return []
    try:
        xls = pd.read_excel('.\\.\\excel_file_2\\89-Turkey References & Prices 29.06.2018 (1).xlsx')
        df = pd.DataFrame(xls, columns=xls.columns)
        cols = ['Barcode', 'Product','Local Name']
        df = df[cols]
        #df = df.assign( **df.select_dtypes(['datetime']).astype(str).to_dict('list') ).to_json(orient="records")
        #parsed = json.loads(df)
        parsed = df.to_dict('records') #.tolist() #values.tolist() 

    except ValueError as e:
        print( e)
        parsed = []    
    
    return parsed