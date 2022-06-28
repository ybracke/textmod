import sys
sys.path.append('/home/bracke/code/textmod')
# sys.path.append('..') # Why doesn't this work here, while it does in eval-de-normal?
from textmod import TextModifier


# Example list for testing
wordlist = ['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', '.', 'Den', 'er', 
    'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', '.', 'Allmählig', 
    'in', 'die', 'Flamme', 'zu', 'ſchieben', '.']
wordlist_sents = [
    ['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', '.'], 
    ['Den', 'er', 'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', '.'], 
    ['Allmählig', 'in', 'die', 'Flamme', 'zu', 'ſchieben', '.']
]


config = {
    # "comment" : "This is a stub of the preproc config file; still under development",
    "remove_punct" : True,
    "translit" : "unidecode_GER",
    "lowercase" : True
}

def to_uppercase(words):
    ''' Convert a list of tokenized words to lowercase '''
    return [w.upper() for w in words]

tf = TextModifier([wordlist], **config)
wordlist_mod = tf.modify()
# print(tf.doc)
# wordlist_mod = tf.apply_method(wordlist_sents, to_uppercase, doc_nested=True)
print(wordlist_mod)