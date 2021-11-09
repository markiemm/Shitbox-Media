# import requests
# import json
# import config

# with open("config.json") as file:
#     config = json.load(file)


# status_api_get_services = requests.get("http://status.shitbox.media/api/services?api=" + config["status_api_key"])


# print(status_api_get_services.json()[1]["online"])

import json
config = json.load(open("config.json", "r", encoding="utf-8"))
print(config)
print(type(config))

if 101 % 2 == 1:
    print("bruh")
else:
    print("test")
