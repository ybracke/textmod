#!/usr/bin/env python3
import re
import unidecode

# Map Umlauts and 'ß' to private use codepoints
# see: https://unicode-table.com/en/blocks/private-use-area/
ESCAPE = {
    'Ä' : '\ue000',
    'Ö' : '\ue001',
    'Ü' : '\ue002',
    'ä' : '\ue003',
    'ö' : '\ue004',
    'ü' : '\ue005',
    'ß' : '\ue006',
}

UNESCAPE = {
    '\ue000' : 'Ä',
    '\ue001' : 'Ö',
    '\ue002' : 'Ü',
    '\ue003' : 'ä',
    '\ue004' : 'ö',
    '\ue005' : 'ü',
    '\ue006' : 'ß',
}


def escape(word):
    return ''.join([ESCAPE[s] if s in ESCAPE else s for s in word])
    
def unescape(word):
    return ''.join([UNESCAPE[s] if s in UNESCAPE else s for s in word])

def unidecode_classic(words):
    return [unidecode.unidecode(w,errors='preserve') for w in words]

def unidecode_ger(words):
    return [unescape(unidecode.unidecode(escape(w),errors='preserve')) 
            for w in words]


def remove_punctuation(words):
    """ Remove punctuation from list of tokenized words """
    return [w for w in words if re.sub(r'[^\w\s]', '', w) != '']

def to_lowercase(words):
    """ Convert a list of tokenized words to lowercase """
    return [w.lower() for w in words]

def to_truecase(words):
    return words


class TextModifier:

    def __init__(self, words=[], **kwargs
                #  lowercase=False, 
                #  truecase=False, 
                #  remove_punct=False, 
                #  special_form=None, 
                #  unidecode=None, # or {'classic', 'unicode_ger'}
                ):
        
        # Instance variables
        self.words = words
        self.config = kwargs
        self.stemmer = None #TODO
        self.NLP = None #TODO



    def modify(self):
        '''
        Parameters
        ----------
        words : list of strings OR list of lists of strings
            data to modify
        config : dict
            dict with configurations for modification
        '''
        words = self.words
        for method,val in self.config.items():
            # Boolean argument
            if val is True:
                if method == 'remove_punct':
                    words = remove_punctuation(words)
                elif method == 'lowercase':
                    words = to_lowercase(words)
                elif method == 'truecase':
                    # words = to_truecase(words) # TODO
                    pass
                # else:
                #     print(f"Ignoring unknown config: {method}={val}")
            # Other
            else:
                if method == 'convert_to':
                    if val == 'lemma':
                        # TODO
                        pass
                    elif val == 'stem':
                        # TODO 
                        pass
                    # else:
                    #     print(f"Ignoring unknown config: {method}={val}")
                elif method == 'unidecode':
                    if val == 'classic':
                        words = unidecode_classic(words)
                    elif val == 'GER':
                        words = unidecode_ger(words)
                    elif val is None:
                        pass
                #     else:
                #         print(f"Ignoring unknown config: {method}={val}")
                # else:
                #     print(f"Ignoring unknown config: {method}={val}")
        return words

