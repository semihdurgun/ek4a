import pandas as pd
import json

xls = pd.read_excel('.\\.\\excel_file_2\\89-Turkey References & Prices 29.06.2018 (1).xlsx')
df_sanofi = pd.DataFrame(xls, columns=xls.columns)
cols = ['Barcode', 'Product','Local Name']
df_sanofi = df_sanofi[cols]

xls = pd.read_excel('.\\.\\excel_file_2\\Pinakas Tropopoimeno Deltio Anatheorimenon Timon farmakon December 2020 (3).xlsx')
df_yunanistan = pd.DataFrame(xls, columns=xls.columns)
xls = pd.read_excel('.\\.\\excel_file_2\\17.05.2021TARHLDETAYLILAFYATLSTESGNCELLEME_8f4366e0-68b8-4ec1-b253-81a149b4b78e.xlsx')
df_turkey = pd.DataFrame(xls, columns=xls.columns)

dfFull = df_sanofi.merge(df_turkey, left_on='Barcode', right_on='BARKOD')[["BARKOD","ATC KODU ","ILAC ADI","KAYNAK ULKE","GERCEK KAYNAK FIYAT (GKF) (€)" ]]

# for Yunanistan
dfFull["yunanistan_benzer_urun"] = ""

for i in range(len(dfFull)):
    for j in range(len(df_yunanistan)):
        if dfFull.iloc[i,1] == df_yunanistan.iloc[j,3]:
            dfFull.loc[i, "yunanistan_benzer_urun"] += "\"" + str(df_yunanistan.iloc[j, 1]) + "\":[\"" + df_yunanistan.iloc[j, 2].replace("\"", "") + "\",\"" + str(df_yunanistan.iloc[j, 5]) + "\"],"

yunanistan_json = dfFull.to_dict("records")

for i in range(len(yunanistan_json)):
    try:
        if yunanistan_json[i]["yunanistan_benzer_urun"] != "":
            yunanistan_json[i]["yunanistan_benzer_urun"] = "{" + yunanistan_json[i]["benzer_urun"][:-1] + "}"
            yunanistan_json[i]["yunanistan_benzer_urun"] = json.loads(yunanistan_json[i]["benzer_urun"])
    except:
        print(yunanistan_json[i])

with open('yunanistan_json.json', 'w') as f:
    json.dump(yunanistan_json, f)