import requests

# get content of http://127.0.0.1:5050/

# requests.request(method, url, **kwargs)[source]
response = requests.request('GET', 'http://127.0.0.1:5050/index.html')

if response.ok:
	print(response.text)

# def request(method, url):
# 	print(method)
	# return 'fhjfdsj'



# request( GET, 'http://127.0.0.1:5050')