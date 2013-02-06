import pymongo
import sys

db=connection.students
scores=db.grades

print "insert, reporting duty"

a={ "student_id" : 0, "type" : "exam", "score" : 54.6535436362647 }

b={ "student_id" : 1, "type" : "exam", "score" : 74.6535436362647 }

scores.insert(a)
scores.insert(b)


try:
    score=scores.find_one({'student_id':1})

    #save -> insert/update
    score['review_date']=datetime.datetime.utcnow()
    score.save(score)

    #update
    #adding a upsert=True flag in the update will add that if something new come it will create an entity otherwise it will upate
    
    score.update({'student_id':1}, score)

    #$set
    #more efficient way to store
    score.update({'stuent_id',:1}, {'$set':{'review_date':datetime.datetime.utcnow()}})

    

    
    
    score=scores.find_one({'student_id':1})
    print score


    
except:
    print "Unexpected"
    raise


#update -> wholesale
