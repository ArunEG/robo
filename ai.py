#!/usr/bin/python
from pymongo import MongoClient
from utils.grammar import *
from utils.fragmenter import *
from services import ask_answer,get_sentance

mongo = MongoClient()
db = mongo.Ai
vocabulary = db.vocabulary
while True:
    
    info = raw_input("Please enter your statement ")
    data_set = {}
    
    if info:
        sentances = break_to_sentance(info)
        for sentance in sentances:
            if sentance:
                existing_sentance = get_sentance(db,sentance)
                
                if not existing_sentance:
                    data_set['sentance'] = sentance
                    words = get_words(sentance)
                    if words:
                        data_set['words'] = words
                        for word in words:
                            if not db.vocabulary.find({'word':word}).count() > 0:
                                db.vocabulary.insert_one({'word':word.lower()})
                                print "WELL NEW vocabulary added \n "+word
                            else:
                                print "I know this word : "+word
                    data_set['type'] = 'statement'
                    if is_question(sentance):
                        data_set['type'] = 'question'
                        new_ans = ask_answer()
                        data_set['answers'] = new_ans
                        reco = db.myset.insert_one(data_set)
                else:
                    import ipdb; ipdb.set_trace()
                    print "I : ",existing_sentance.answers[0]
                    new_ans = ask_answer()
                    if new_ans:
                        import ipdb; ipdb.set_trace()
                        new_answers = existing_sentance['answers']
                        new_answers.append(new_ans)
                        db.myset.update({'_id':existing_sentance.insert_id}, {"answers": new_answers}, upsert=False)          
                    
    else:
        print "Are you trying to make me fool !! aha ?,\n I couldnt understand what you are telling "


