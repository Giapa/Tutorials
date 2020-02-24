'''
Task: Find all the info from the seventh semester
'''

#Imports
import requests
from bs4 import BeautifulSoup

#User agent header
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

#Send the request
page = requests.get('https://www.iee.ihu.gr/en/udg_courses/',headers=header)
#Parse the html
soup = BeautifulSoup(page.content,'html.parser')

#Find all tables
tables = soup.find_all('table')
#Get the seventh table
table = tables[6]
#Find all tr 
trs = table.find_all('tr')

#Create empty list
infos = list()
#List including all the column names
categories = ['code','title','category','h-t','h-l','ects']

#Looping through trs
for tr in trs:
	#Find all tds 
	tds = tr.find_all('td')
	#Create empty dict
	data = dict()

	# data['code'] = tds[0].text
	# data['title'] = tds[1].text
	# data['category'] = tds[2].text
	#This is the same as the code below

	#Loop through tds
	for num,td in enumerate(tds):
		#Not including the strong tags
		if not td.find('strong'):
			#Get the string of categories list
			tag = categories[num]
			#Add key-value pair to dictionary
			data[tag] = td.text
	#Append dictionary to list
	infos.append(data)

#Remove empty dictionaries inside of list.
infos = [item for item in infos if item]

#The following code is the same as above
# for item in infos:
# 	if item is not None:
# 		infos.append(item)

#Open file in append mode
with open('./info.txt','a') as file:
	#Loop through the info list
	for data in infos:
		#Loop through the dictionary
		for key,val in data.items():
			#Write values to file
			file.write(f"{key}:{val} ")
		file.write('\n\n')
