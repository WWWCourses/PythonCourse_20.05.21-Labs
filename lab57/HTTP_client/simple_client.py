import requests

def save_to_file(content):
	with open('./data/test.html','w') as f:
		f.write(content)

base_url = 'http://127.0.0.1:8080/'

headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

# response = requests.get(base_url, headers=headers)
response = requests.post(base_url, headers=headers)

if response.ok:
	# print(response.text)
	save_to_file(response.text)
	print(response.headers)
