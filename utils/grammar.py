past = ['was','went','were','*ed']
present = ['is','*s','ing']
future = ['will','be']
question = ['what','why','who','which','where','when']

def is_question(statement):
    """ The function will receive the statement and it will check
        wether the the statemet is a question or not 
        @parm   : statement 
        @return : true or false
        @Author : Arun Gopi
        @Date   : 16/05/2016 """
    if any(indicator in statement.lower() for indicator in question):
        return True
    return False
