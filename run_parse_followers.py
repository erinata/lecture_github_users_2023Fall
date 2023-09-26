import json
import pandas
import os
import glob

dataset = pandas.DataFrame()

for json_file_name in glob.glob("followers_json_files/*.json"):
  f = open(json_file_name, "r")
  json_data = json.load(f)
  f.close()
  
  for user_info in json_data:
    gh_id = user_info['login']
    
    row = pandas.DataFrame.from_records([{
        'gh_id': gh_id
      }])
    dataset = pandas.concat([dataset, row])


dataset.to_csv("input_files/seed2.csv"
                , index=False)
