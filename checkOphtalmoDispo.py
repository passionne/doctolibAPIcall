#!/usr/bin/env python3
# -*- coding: utf8 -*-

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import date

DOCTOR = {
	'all' : '9765-10984-2316-2317-2318-2319-2320-2322-2323-2324-2325-2328-2329-2330-2326-2566-2321-2379-2314',
	'Dr Rym Benosman' : '2314',
	'Dr Tristan Boret' : '2316',
	'Dr Imen Bouabane' : '10984',
	'Dr Guilhem Bruneau' : '2317',
	'Dr David Cailliau' : '2318',
	'Dr Vincent Dedes' : '2319',
	'Dr Caroline Florent-Bruandet' : '2320',
	'Dr Gilles Hochart' : '2321',
	'Dr Denis Jourdel' : '2322',
	'Dr François Malbrel' : '2323',
	'Dr Lisa Nouvel' : '2324',
	'Dr Rym Ouled Moussa' : '9765',
	'Dr Florent Racoussot' : '2325',
	'Dr Mathieu Sabatier' : '2566',
	'Dr Nicolas Santerre' : '2326',
	'Dr Anne-Sophie Sprimont' : '2328',
	'Dr Lucie Stalnikiewicz' : '2329'
}

DOCTOLIB_API_URL = "https://partners.doctolib.fr"
DOCTOLIB_API_PATH = "/availabilities/12498/"
DOCTOLIB_API_PARAMS = {
	"agenda_ids" : DOCTOR['all'],
    "insurance_type" : "",
    "limit" : "15"
}

params = urllib.parse.urlencode(DOCTOLIB_API_PARAMS).encode('ascii')
current_day = date.today().strftime('%Y-%m-%d')
url = DOCTOLIB_API_URL + DOCTOLIB_API_PATH + current_day + "?"

fullURL = "%s%s" % (url, params.decode('ascii'))
# print(fullURL)

html = urllib.request.urlopen(fullURL).read()

# req = urllib.request.Request(url = url, data=params)
# with urllib.request.urlopen(req) as response:
# 	print(response.status, response.reason)
# 	data = response.read().decode('utf-8')
# 	print(data)

# with urllib.request.urlopen(url, params) as response :
# 	print(response.status, response.reason)
# 	data = response.read().decode('utf-8')
# 	print(data)

soup = BeautifulSoup(html)
# print(soup.prettify())

slots = soup('div', {'class' : 'slots'})[0]
print(slots.prettify())

days=[]
times=[]

table = soup.find("table")
for th in table.thead.findAll("th"):
	days.append(' '.join(th.findAll(text=True)))

for tr in table.thead.findAll("tr"):
	line=[]
	for td in tr.findAll("td"):
		line.append(td.div.findAll('div', {'class' : 'slot'}))
	times.append(line)

print(str(days))
print(str(times))
