# lexicon and corporas
# corpora - body of text. lexicon - dictionary, words and their meanings 

# Objective: Help buidling up Vocab list with any articles or tv show script
# 1. tokenize text files texts in to strings in a list
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader #read your own corpus
import urllib2
import json

corpus_root = '/home/frank/Dropbox/ScriptSearch/How I Met Your Mother/Season 1/ONE'
#PlaintextCorpusReader can't read srt, have to convert them into txt files
own_corpus = PlaintextCorpusReader(corpus_root, '.*')
#set the subtitles file as corpus using nltk plaintextcorpusreader
results_list = []
def check_meaning(word):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=showmeeng&key=1890848919&type=data&doctype=json&version=1.1&q='+ word.lower()
    #store results of the word and meaning and to write them on file
    try:
        wordinfo= urllib2.urlopen(url).read().decode('utf-8')
        #get the youdou api and read it with urllib module, decode utf-8(not sure why yet)
        data = json.loads(wordinfo)
        #load the api json data with json module
        phonetic = data['basic']['us-phonetic']
        #get the key of the basic and us-phonetic data
        phonetic_txt = "[%s]" % phonetic.encode('utf8')
        explains = data['basic']['explains']
        # print phonetic_txt         
        results_list.append(word+"\n")
        results_list.append(phonetic_txt+"\n")
        for explain in explains:
            # print explain
            results_list.append(explain.encode('utf8')+"\n")        
        #append the phonetic and explainations to a list for later file write
    except KeyError:
        no_meaning.append(word)
        #pass will ignore the keyError and do nothing 


# 2. filter words that are not needed, filter stop words, stems the words back, porterStemmers
filtered_words = set(list(own_corpus.words()))
# use words function of the corpus reader 
stop_words = set(stopwords.words("english"))


# 3. store remaining words and build then as words list
no_meaning = []
#store the word with no meaning using api
results_word = []
#store the word with meaning

for word in filtered_words:
    if len(word) >= 5 and bool(re.search(r'\D+',word)) and not bool(re.search(r'(he*)',word)):
        # 4. Look up those words by scriping or url referencing online English-Chinese dictionary
        # print word
        check_meaning(word.lower())
    else:
        pass

print "====================================================="
print "Found meaning for %d words" % (len(results_word)-len(no_meaning))
print "There are %d words meaning we can't find:" % len(no_meaning)
print no_meaning

try:
    write_in_file = int(raw_input("Do you wanna print the results?\n> "))
except ValueError:
    write_in_file = 0
if write_in_file == 1:
    filename =  raw_input("Name the file.\n>")+".txt"
    results_file = open(filename,"a")
    for result in results_list:
        results_file.write(result)
    results_file.close()
else:
    pass




# for w in filtered_sentence:
# 	if w not in stop_words :
# 		print w


# sents = sent_tokenize(raw)
#tokenize the raw data in to sentences
# for i in sents:
    # print i
#loop through all senteces and print them out

 
# stop words
# stop_words = set(stopwords.words("english"))
# words = word_tokenize(example)
# filtered_sentence = []
# for w in words:
# 	if w not in stop_words:
# 		filtered_sentence.append(w)
# print filtered_sentence
# filtered_sentence = []
# sents = wordlists.sents()

#=-========================================================================================================================================

#=-========================================================================================================================================
#http://fanyi.youdao.com/openapi?path=data-mode

         

# api url: 'http://fanyi.youdao.com/openapi.do?keyfrom=showmeeng&key=1890848919&type=data&doctype=json&version=1.1&q='+word
#=-========================================================================================================================================
# 5. Get the meaning and kk sonics and lay them out in your own text files
#=-========================================================================================================================================
# 6. Now you got the best English teacher time saver




