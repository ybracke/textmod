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

def escape(word):
    return ''.join([ESCAPE[s] if s in ESCAPE else s for s in word])
    
def unescape(word):
    return ''.join([UNESCAPE[s] if s in UNESCAPE else s for s in word])

def unidecode_classic(words):
    return [unidecode.unidecode(w,errors='preserve') for w in words]

def unidecode_ger(words):
    return [unescape(unidecode.unidecode(escape(w),errors='preserve')) 
            for w in words]

# (B) Punctuation removal

def remove_punctuation(words):
    ''' Remove punctuation from list of tokenized words '''
    return [w for w in words if re.sub(r'[^\w\s]', '', w) != '']

# (C) Case modification

def to_lowercase(words):
    ''' Convert a list of tokenized words to lowercase '''
    return [w.lower() for w in words]

def to_truecase(words):
    # TODO
    return words

# (D) Wordform modification (stem, lemma)
# TODO



class TextModifier:

    def __init__(self, doc=[], **kwargs):
        '''
        TextModifier object 

        Parameters
        ----------
        doc : list
            Strings to be modified. This can be either a list of strings or
            a list containing lists of strings (sentences). 
        config : dict
            Configurations for modification
        '''

        # Instance variables
        self.doc = doc
        self.config = kwargs
        self._config_ok()
        self.stemmer = None #TODO
        self.NLP = None #TODO

        # Is the data nested in sentences
        # Relevant for the application of methods
        self.is_nested_doc = False 
        if (len(doc) > 0) and (isinstance(doc[0], list)):
            self.is_nested_doc = True 


    def _config_ok(self):
        '''
        Check whether keys and values in self.config are acceptable
        '''

        accepted_keys = ['remove_punct','lowercase', 'truecase',
                         'convert_to', 'unidecode'] 
        boolean_keys = ['remove_punct','lowercase', 'truecase']
        for key,val in self.config.items():
            if key not in accepted_keys:
                raise ValueError(f"Unknown config entry: {key}={val}")
            else:
                if key in boolean_keys:
                    if not isinstance(val, bool):
                        raise ValueError(f"Unknown config entry: {key}={val}")
                elif key == 'convert_to':
                    if val not in ['lemma', 'stem']:
                        raise ValueError(f"Unknown config entry: {key}={val}")
                elif key == 'unidecode':
                    if val not in ['classic', 'GER']:
                        raise ValueError(f"Unknown config entry: {key}={val}")
                else: 
                    raise ValueError(f"Unknown config entry: {key}={val}")
        return True

    def apply_method(self, doc, method, doc_nested=False):
        '''
        Wrapper function for modification methods 
        Accounts for nested and unnested documents

        Can also be used to pass methods defined elsewhere to a TextModifier
        '''
        if doc_nested:
            return [method(sent) for sent in doc]
        return method(doc)

    def modify(self):
        '''
        Apply text modification functions in the order given in self.config

        '''
        doc = self.doc
        for method,val in self.config.items():
            # Boolean argument
            if val is True:
                if method == 'remove_punct':
                    doc = self.apply_method(doc, remove_punctuation, self.is_nested_doc)
                elif method == 'lowercase':
                    doc = self.apply_method(doc, to_lowercase, self.is_nested_doc)
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
                elif method == 'unidecode':
                    if val == 'classic':
                        doc = self.apply_method(doc, unidecode_classic, self.is_nested_doc)
                    elif val == 'GER':
                        doc = self.apply_method(doc, unidecode_ger, self.is_nested_doc)
                    elif val is None:
                        pass
        return doc

