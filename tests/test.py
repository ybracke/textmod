import sys
sys.path.append('/home/bracke/code/normpreproc')
# sys.path.append('..') # Why doesn't this work here, while it does in eval-de-normal?
from src.preprocessing import TextModifier


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
    "unidecode" : "GER",
    "lowercase" : True
}

wordlist_mod = TextModifier(wordlist, **config).modify()
print(wordlist_mod)