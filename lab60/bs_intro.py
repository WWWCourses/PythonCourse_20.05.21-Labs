from bs4 import BeautifulSoup
import re

def get_html():
	filename = './front-end/index.html'
	with open(filename, 'r') as f:
		return f.read()

html = get_html()
soup = BeautifulSoup(html, 'html.parser')

# el = soup.body.table.children

# for i in el:
# 	print(f'>{i}<')

# for i in soup.body.table.stripped_strings:
# 	print(f'>{i}<')

# ------------------------------- find elements ------------------------------ #
# rows = soup.body.find_all(re.compile('^t'))
# print(rows)

# find first table
# table = soup.find_all('table', class_="table1class")
# print(table)

# get element by string HTML content:
# el = soup.find(string="Ivan")
# print(el.parent.next_sibling.nex)

# [
# 	{
# 	'name': 'Ivan',
# 	'Family': 'Ivanov'
# 	},
# 	{
# 	'name': 'Ivan',
# 	'Family': 'Ivanov'
# 	},
# ]

table = soup.find('table', id="table1")
# table = soup.select('#table1')


# rows = table.find_all('tr')[1:]

# data = []


# for row in rows:
# 	tds = row.find_all('td')

# 	data.append({
# 		'name': tds[0].text,
# 		'Family': tds[1].text
# 	})


# print(data)


# using css selector