import sys
sys.path.append('/home/bracke/code/normpreproc')
# sys.path.append('..') # Why doesn't this work here, while it does in eval-de-normal?
import src.preprocessing


# Example list for testing
wordlist = ['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', '.', 'Den', 'er', 
    'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', '.', 'Allmählig', 
    'in', 'die', 'Flamme', 'zu', 'ſchieben', '.']
wordlist_sents = [
    ['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', '.'], 
    ['Den', 'er', 'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', '.'], 
    ['Allmählig', 'in', 'die', 'Flamme', 'zu', 'ſchieben', '.']
]



