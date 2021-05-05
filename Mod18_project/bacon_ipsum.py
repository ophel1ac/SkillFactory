import requests
import json

param = {"type": "meat-and-filler"}


r = requests.get("https://baconipsum.com/api/", params=param)
j = json.loads(r.content)
print(j)
