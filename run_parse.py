import json
import pandas
import os

if not os.path.exists("parsed_files"):
  os.mkdir("parsed_files")


dataset = pandas.DataFrame()

json_file_name = "json_files/dAAAb.json"

f = open(json_file_name, "r")
json_data = json.load(f)
f.close()

# print(json_data)

gh_id = json_data['login']
gh_number_id = json_data['id']
updated_at = json_data['updated_at']
followers = json_data['followers']


print(gh_id)
print(gh_number_id)
print(updated_at)
print(followers)

row = pandas.DataFrame.from_records(
  [
  {
    'gh_id': gh_id,
    'gh_number_id': gh_number_id,
    'updated_at': updated_at,
    'followers': followers
  }
  ]
  )

print(row)
dataset = pandas.concat([dataset, row])

dataset.to_csv("parsed_files/github_user_data.csv"
                , index=False)


