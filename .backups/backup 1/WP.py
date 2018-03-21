
# Word Processor (WP)
#   For learning word frequency and usage

from PyDictionary import PyDictionary

def parse_words(log):
    #Given a single log, returns a dictionary of words and frequency
    words = log.split()
    word_dict = {}
    for i in range(0, len(words)):
        if words[i] in word_dict:
            word_dict[words[i]] += 1
        else:
            word_dict[words[i]] = 1
    return word_dict

dictionary = PyDictionary()
print(dictionary.meaning('go'))
