import pymongo
import sys

#establish connection
connection = pymongo.Connection("mongodb://localhost", safe=True)

#students database
db=connection.students
scores=db.grades

#
def find():
    print "find, reporting for duty"

    #who has a score greater than 65
    query={'score':{'$gt':65, '$lt':100}}

    #_id field wont be shown only student_id an score will be shown
    selector={"_id":0, "student_id":1, "score":1}
    
    try:
        #sort by score
        #skips first 4 results
        #then saves 1 result
        
        #selector is optional parameter
        docs=scores.find(query, selector).sort('score',pymongo.ASCENDING).skip(4).limit(1)
    except:
        print "Unexpected error", sys.exc_info()[0]
    #iterate and prints doc
    for doc in docs:
        print doc

find()

def find_one():
    print "find one, reporting for duty"
    query ={'student_id': 10}
    try:
        doc = scores.find_one(query)

    except:
        print "Unexpected error", sys.exc_info()[0]

    print doc


