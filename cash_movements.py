import os
import json
import pandas as pd

config = json.load(open("config.json"))

path1 = os.path.abspath(config.get("file1"))
path2 = os.path.abspath(config.get("file2"))

def convert_json(path1,path2):

    df1 = pd.read_csv(path1,index_col=False)
    
    df1=df1.fillna("")
    df1.columns = [i.strip() for i in df1.columns]

    df1 = df1.map(lambda x: x.strip() if isinstance(x, str) else x)
    data1 = df1.to_dict(orient='records')
    
    df2 = pd.read_csv(path2,index_col=False)
    df2=df2.fillna("")
    df2.columns = [i.strip() for i in df2.columns]

    df2 = df2.map(lambda x: x.strip() if isinstance(x, str) else x)
    data2 = df2.to_dict(orient='records')

    d = dict()
    # Converting dict values from json string to list
    d["Elequin Securities"] = data1       
    d["Elequin Investments"] = data2
    
    # Send dictionary to Json file
    # New Json file(confg) will be created 
    with open("output.json","w") as file:
        json.dump(d,file)

    
convert_json(path1,path2)

