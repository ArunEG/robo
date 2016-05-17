#!/usr/bin/python
from pymongo import MongoClient
from utils.grammar import *
from utils.fragmenter import *

mongo = MongoClient()
db = mongo.Ai
vocabulary = db.vocabulary
while True:
    
    info = raw_input("Please enter your infos ")
    
    if info:
        sentances = get_sentance(info)
        for sentance in sentances:
            if sentance:
                words = get_words(sentance)
                if words:
                    for word in words:
                        if not db.vocabulary.find({'word':word}).count() > 0:
                            db.vocabulary.insert_one({'word':word.lower()})
                            print "WELL NEW vocabulary added \n "+word
                        else:
                            print "I know this word : "+word
        if any(indicator in info for indicator in past):
            print "it is in past tense"
            if is_question(info):
                print "I beleave you are trying to ask me something "
                oppnent = raw_input("May I know your name ?")
                print "Hi " + oppnent + ", Will talk to you soon"
        elif any(indicator in info for indicator in present):
            print "info in present tense"
            if is_question(info):
                print "I beleave you are trying to ask me something "
                oppnent = raw_input("May I know your name ?")
                print "Hi " + oppnent + ", Will talk to you soon"
        else:
            print "Sorry I couldn't understand, can you please teach me ?"
    else:
        print "Are you trying to make me fool !! aha ?,\n I couldnt understand what you are telling "


