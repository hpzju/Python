import requests

url = 'https://icanhazdadjoke.com/search'
h = {"Accept": "application/json"}
p = {"page": 1, "limit": 10, "term": "cat"}

response = requests.get(url, headers=h, params=p)

data = response.json()

print(data)

# url = 'http://kb.knoconida.com'

# dir(requests)

# response = requests.get(url, verify=False)

# info = f"""{{
# url:   {url},
# code: {response.status_code},
# headers: {response.headers},
# encoding: {response.encoding},~
# cookies: {response.cookies},
# elapsed: {response.elapsed}
# history: {response.history},
# json: {response.json},
# text: {response.text},
# content: {response.content}
# }}"""

# print(info)
