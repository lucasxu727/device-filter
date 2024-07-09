#imports
import pandas as pd
import json
import sys
import fileinput

file_name = ''.join(fileinput.input())
usernameDatabase = set()
clean_data = []
rows_as_dicts = []

try:
    df = pd.read_json(file_name, lines=True)
except ValueError as e:
    sys.exit(f'Error reading JSON: {e}')

client_data = df[(df['deviceType'] == 'CLIENT') & (df['manufacturer'].notna())]
#2nd 

userDupeCount = 0
userCount = 0
for index, row in client_data.iterrows():
    if row['userName'] is not None and row['userName'] in usernameDatabase:
        userDupeCount += 1
        continue
    else:
        usernameDatabase.add(row['userName'])
        row_dict = row.to_dict()
        clean_data.append(row_dict)
        userCount += 1

output = json.dumps(clean_data)


print(output)