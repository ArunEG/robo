def get_words(sentance):
    """ The function will return words in a sentance
    @Author : Arun Gopi
    @Date   : 16/05/2016 """
    words = []
    if sentance:
        words = sentance.split(" ")
    return words

def break_to_sentance(info):
    """ The function will return each sentance in a info 
    @Author : Arun Gopi
    @Date   : 16/05/2016 """
    sentance = []
    if info:
        sentance = info.split(".")
    return sentance
    