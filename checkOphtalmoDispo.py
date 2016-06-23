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

def call_doctolib_api(from_date, params):
	url_parameters = urllib.parse.urlencode(params)
	from_date_str = from_date.strftime('%Y-%m-%d')
	url = DOCTOLIB_API_URL + DOCTOLIB_API_PATH + from_date_str + "?" + url_parameters
	html = urllib.request.urlopen(url).read()
	return html

html = call_doctolib_api(date.today(), DOCTOLIB_API_PARAMS)

soup = BeautifulSoup(html)

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
