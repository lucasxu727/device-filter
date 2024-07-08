#imports
import pandas as pd
import json
import sys
import fileinput

file_name = ''.join(fileinput.input())
phoneManufacturerDatabase = {"Apple, Inc.", "Samsung Electronics Co.,Ltd", "Google Inc."}
usernameDatabase = set()
clean_data = []
rows_as_dicts = []

try:
    df = pd.read_json(file_name, lines=True)
except ValueError as e:
    sys.exit(f'Error reading JSON: {e}')

client_data = df[(df['deviceType'] == 'CLIENT') & (df['manufacturer'].notna())]
#2nd 

#if manufacturer is in the databse, transfer row into clean database as well as recording the username, if the username is already detected, do not transfer
userDupeCount = 0
for index, row in client_data.iterrows():
    if row['manufacturer'] in phoneManufacturerDatabase:
        if row['userName'] is not None and row['userName'] in usernameDatabase:
            userDupeCount += 1
            continue
        else: 
            usernameDatabase.add(row['userName'])
            row_dict = row.to_dict()
            clean_data.append(row_dict)

output = json.dumps(clean_data)

print(output)