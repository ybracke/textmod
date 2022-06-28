#!/usr/bin/env python3
import re
import unidecode

# (A) Transliteration

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

def escape(token):
    return ''.join([ESCAPE[s] if s in ESCAPE else s for s in token])
    
def unescape(token):
    return ''.join([UNESCAPE[s] if s in UNESCAPE else s for s in token])

def unidecode_classic(tokens):
    ''' Transliteration with unidecode '''
<<<<<<< HEAD
    return [unidecode.unidecode(t,errors='preserve') for t in tokens]
=======
    return [unidecode.unidecode(w,errors='preserve') for t in tokens]
>>>>>>> 1512b6224b8e691a9780db4b70fd9dec63c73cdb

def unidecode_ger(tokens):
    ''' Transliteration with unidecode but keep ÄÖÜäöüß'''
    return [unescape(unidecode.unidecode(escape(t),errors='preserve')) 
            for t in tokens]

# (B) Punctuation removal

def remove_punctuation(tokens):
    ''' Remove punctuation from list of tokenized tokens '''
    return [t for t in tokens if re.sub(r'[^\w\s]', '', t) != '']

def punct_idxs(tokens):
    return [i for i,t in enumerate(tokens) 
            if re.sub(r'[^\w\s]', '', t) == ''
            ]

# (C) Case modification

def to_lowercase(tokens):
    ''' Convert a list of tokenized tokens to lowercase '''
    return [t.lower() for t in tokens]

def to_truecase(tokens):
    # TODO
    return tokens

# (D) Wordform modification (stem, lemma)
# TODO



class TextModifier:

    def __init__(self, doc=[], **kwargs):
        '''
        TextModifier object 

        Parameters
        ----------
        doc : list of lists of strings
            Document to be modified, consisting of sentences (list) and tokens
            (str). Hint: If your doc consists of a single tokenlist (no
            sentences), just wrap it inside another list before passing it.  
        config : dict
            Configurations for modification
        '''

        # Instance variables
        self.doc = doc
        self.config = kwargs
        self._config_ok()
        self.stemmer = None #TODO
        self.NLP = None #TODO

    def _config_ok(self):
        '''
        Check whether keys and values in self.config are acceptable
        '''

        accepted_keys = ['remove_punct','lowercase', 'truecase',
                         'convert_to', 'translit', 'comment'] 
        boolean_keys = ['remove_punct','lowercase', 'truecase']
        for key,val in self.config.items():
            if key not in accepted_keys:
                raise ValueError(f"Unknown config entry: {key}={val}")
            else:
                if key in boolean_keys:
                    if not isinstance(val, bool):
                        raise ValueError(f"Unknown config entry: {key}={val}")
                elif key == 'comment':
                    pass
                elif key == 'convert_to':
                    if val not in ['lemma', 'stem']:
                        raise ValueError(f"Unknown config entry: {key}={val}")
                elif key == 'translit':
                    if val not in ['unidecode', 'unidecode_GER']:
                        raise ValueError(f"Unknown config entry: {key}={val}")
                else: 
                    raise ValueError(f"Unknown config entry: {key}={val}")
        return True

    def modify(self):
        '''
        Apply text modification functions in the order given in self.config
        '''

        doc = self.doc
        for method,val in self.config.items():
            # Boolean argument
            if val is True:
                if method == 'remove_punct':
                    doc = [remove_punctuation(s) for s in doc]
                elif method == 'lowercase':
                    doc = [to_lowercase(s) for s in doc]
                elif method == 'truecase':
                    # TODO
                    pass
            # Other
            else:
                if method == 'convert_to':
                    if val == 'lemma':
                        # TODO
                        pass
                    elif val == 'stem':
                        # TODO 
                        pass
                elif method == 'translit':
                    if val == 'unidecode':
                        doc = [unidecode_classic(s) for s in doc]
                    elif val == 'unidecode_GER':
                        doc = [unidecode_ger(s) for s in doc]
                    elif val is None:
                        pass
        return doc

