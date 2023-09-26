import requests
import json
import os
import pandas
import time

if not os.path.exists("followers_json_files"):
  os.mkdir("followers_json_files")
    
access_point = "https://api.github.com"

f = open("token", "r")
token = f.read()
f.close()

followers_url_list = pandas.read_csv("parsed_files/github_user_data.csv")
followers_url_list = followers_url_list['followers_url']

github_session = requests.Session()
github_session.auth = ("erinata", token)

response_text = github_session.get(access_point + "/rate_limit").text
print(json.loads(response_text))

for followers_url in followers_url_list:
  user_id = followers_url.split("/")[-2]
  file_name = "followers_json_files/" + user_id + ".json"
  
  if os.path.exists(file_name):
    # pass
    print("File exists: ", user_id)

  else:
    try:
      print(user_id)
      response_text = github_session.get(followers_url).text

      json_text = json.loads(response_text)

      f = open(file_name + ".tmp", "w")
      f.write(json.dumps(json_text))
      f.close()
      
      os.rename(file_name + ".tmp", file_name)
    except Exception as e:
      print(e)
      
    time.sleep(5)
    
    










