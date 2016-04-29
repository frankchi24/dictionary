import numpy as np
import csv
import urllib2
import json

		
a= np.loadtxt('Workbook1.csv',
							delimiter = ',',
							unpack = True,
							#to specify different variables
							dtype = 'str')
z = 0

for eachWord in a:
	y = 0
	url = 'http://fanyi.youdao.com/openapi.do?keyfrom=showmeeng&key=1890848919&type=data&doctype=json&version=1.1&q='+ eachWord
	wordinfo= urllib2.urlopen(url).read().decode('utf-8')
	data = json.loads(wordinfo)
	phonetic = data['basic']['us-phonetic']		
	explains = data['basic']['explains']
	results = "["+str(phonetic.encode('utf8'))+"]"
	for meaning_text in explains:
		results = results + ","+ meaning_text.encode('utf8')
		y = y + 1
	saveLine = eachWord + ',' + results 
	z = 5-y
	saveLine = saveLine + "," + z*"," + "\n"
	saveFile = open('newCSV.csv','a')
	saveFile.write(saveLine)
	saveFile.close()




