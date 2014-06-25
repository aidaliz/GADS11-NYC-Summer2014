from urllib2 import urlopen
from json import load, dumps
import pandas as pd

url = 'http://api.npr.org/query?apiKey=' 
key = 'MDE1MDMzMTAxMDE0MDM1NzYxMjQ0NDIxOQ001'
url = url + key
url += '&numResults=1&format=json&id=1007&requiredAssets=image,text,audio' #1007 is science

response = urlopen(url)
json_obj = load(response)

#print json_obj['list']['teaser']

df = pd.Dataframe()
df['title'] = [story['title'] for story in json_obj
for i in df['title']:
    print i

#for story in json_obj['list']['story']:
#	print "TITLE: " + story['title']['$text'] + "\n"
#	print "DATE: " + story['storyDate']['$text'] + "\n"
#	print "TEASER: " + story['teaser']['$text'] + "\n"
	
#if 'byline' in story:
 #   print "BYLINE: " +story['byline'][0]['name']['$text'] + "\n"