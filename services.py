def get_answer(db,statement):
    db.myset.find_one(prepare_data)
    
def prepare_data(statement):
    statement= statement.lower()
    return statement
 
def get_sentence(db,statement):
    final = prepare_data(statement)
    print "SENTANCE  : ",str(final)
    return db.myset.find_one({'sentence':str(final)})
    
def ask_answer():
    answer = raw_input("I did not head this question before. can you tell me how to answer ?")
    return answer