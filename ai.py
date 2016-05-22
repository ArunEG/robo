#!/usr/bin/python
from pymongo import MongoClient
from utils.grammar import *
from utils.fragmenter import *
from services import ask_answer,get_sentence

mongo = MongoClient()
db = mongo.Ai
vocabulary = db.vocabulary
while True:
    
    info = raw_input("Please enter your statement ")
    data_set = {}
    
    if info:
        sentences = break_to_sentance(info)
        for sentence in sentences:
            if sentence:
                existing_sentence = get_sentence(db,sentence)
                
                if not existing_sentence:
                    print "I am hearing this sentence at first time"
                    data_set['sentence'] = sentence.lower()
                    words = get_words(sentence)
                    if words:
                        data_set['words'] = words
                        for word in words:
                            if not db.vocabulary.find({'word':word}).count() > 0:
                                db.vocabulary.insert_one({'word':word.lower()})
                                print "WELL NEW vocabulary added \n "+word
                            else:
                                print "I know this word : "+word
                    data_set['type'] = 'statement'
                    if is_question(sentence):
                        data_set['type'] = 'question'
                        new_ans = ask_answer()
                        data_set['answers'] = [new_ans]
                    reco = db.myset.insert_one(data_set)
                else:
                    print "I : ",existing_sentence['answers'][0]
                    new_ans = ask_answer()
                    if new_ans:
                        
                        new_answers = existing_sentence['answers']
                        new_answers.append(new_ans)
                        db.myset.update({'_id':existing_sentence.insert_id}, {"answers": new_answers}, upsert=False)          
                    
    else:
        print "Are you trying to make me fool !! aha ?,\n I couldnt understand what you are telling "


