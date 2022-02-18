import requests, fake_useragent
user = fake_useragent.UserAgent().random
headers = {'user_agent': user}
print(headers)
