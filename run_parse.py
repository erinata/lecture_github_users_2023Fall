import json
import pandas
import os

if not os.path.exists("parsed_files"):
  os.mkdir("parsed_files")


dataset = pandas.DataFrame()

json_file_name = "json_files/erinata.json"

f = open(json_file_name, "r")
json_data = json.load(f)
f.close()

# print(json_data)

gh_id = json_data['login']
gh_number_id = json_data['id']
plan_name = json_data['plan']['name']
updated_at = json_data['updated_at']
followers = json_data['followers']


print(gh_id)
print(gh_number_id)
print(plan_name)
print(updated_at)
print(followers)


