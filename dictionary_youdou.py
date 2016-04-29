import urllib2
import json

def check_meaning(word):
	url = 'http://fanyi.youdao.com/openapi.do?keyfrom=showmeeng&key=1890848919&type=data&doctype=json&version=1.1&q='+ word
	try:
		results = open("meaning.csv","a")
		results.write("\n"+word +"\n")
		wordinfo= urllib2.urlopen(url).read().decode('utf-8')
		data = json.loads(wordinfo)
		phonetic = data['basic']['us-phonetic']
		print "[%s]" % phonetic.encode('utf8')
		results.write("[%s]\n" % phonetic.encode('utf8'))
		explains = data['basic']['explains']
		for meaning in explains:
			print meaning
		# print to a file, decode utf to unicode
		for meaning_text in explains:
			results.write("%s\n" % meaning_text.encode('utf8'))
		results.close()
	except KeyError:
		pass
		#pass will ignore the keyError and do nothing 

words = []
quit = 1
word = raw_input("Input your word:\n> ")
words.append(word)
while quit == 1:
	input_word = raw_input("Input anther?\nPress enter if not\n> ")	
	if input_word == "":
		break
	else:
		words.append(input_word) 
print "These are your words: "
print words
raw_input("Press enter to look up their meanings.\n> ")
for word in words:
	print word
	check_meaning(word)

	     




# api url: 'http://fanyi.youdao.com/openapi.do?keyfrom=showmeeng&key=1890848919&type=data&doctype=json&version=1.1&q='+word