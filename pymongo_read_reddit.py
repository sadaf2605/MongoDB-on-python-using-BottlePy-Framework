import json
import urllib2
import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)

db= connection.reddit

stories=db.stories

raddit_page= urllib2.urlopen("http://www.reddit.com/r/technology/.json")

parsed=json.loads(raddit_page.read())

for item in parsed['data']['children']:
    stories.insert(item['data'])

print 'printing stories that matches microsoft'
print stories.find({'title':{'$reg':'microsoft'}})
