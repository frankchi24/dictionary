import urllib2
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import re

word = raw_input("Input your word:\n> ")
url = 'http://cdict.info/query/'+ word
r = urllib2.urlopen(url).read()
soup = BeautifulSoup(r, 'lxml')
result = soup.find_all("", class_="resultbox")
a = result[0].div.extract()
b = result[0].div.extract()
# extract two times to get rid of the div xbox and another
prettify =  result[0].prettify()
no_divs = (re.sub(r'</div>','',prettify))
result = (re.sub(r'<div class="resultbox">','',no_divs))
result2 = (re.sub(r'\n','',result))
result3 = (re.sub(r'<br/>','\n',result2))
print result3



