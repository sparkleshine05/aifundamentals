import json

data = {"name": "Ashutosh", "score" : 92, "passed" : "True"}

with open("data.json", "w") as f:
    json.dump(data, f)
    