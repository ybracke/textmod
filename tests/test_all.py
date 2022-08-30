import textmod
import pytest


def test_escape_ä() -> None:
    w = textmod.escape('Olivenäste')
    assert w == 'Oliven\ue003ste'

def test_unescape_ue003() -> None:
    w = textmod.unescape('Oliven\ue003ste')
    assert w == 'Olivenäste'

def test_unescape_other() -> None:
    w = textmod.unescape('\ue100')
    assert w == '\ue100'

def test_unidecode_classic() -> None:
    w = textmod.unidecode_classic('Olivenäſte')
    assert w == ['O','l','i','v','e','n','a','s','t','e']

def test_unidecode_classic_empty() -> None:
    w = textmod.unidecode_classic('')
    assert w == []

def test_unidecode_ger() -> None:
    w = textmod.unidecode_ger('Olivenäſte')
    assert w == ['O','l','i','v','e','n','ä','s','t','e']

def test_remove_punctuation() -> None:
    tokens = ['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', '.', 'Den', 'er', 
              'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', '.', 'Allmählig', 
              'in', 'die', 'Flamme', 'zu', 'ſchieben', '.']
    l = textmod.remove_punctuation(tokens)
    assert l == ['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', 'Den', 'er', 
              'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', 'Allmählig', 
              'in', 'die', 'Flamme', 'zu', 'ſchieben']

def test_remove_punctuation_allpunct() -> None:
    tokens = ['...', '?',  '.']
    l = textmod.remove_punctuation(tokens)
    assert l == []

def test_remove_punctuation_nopunct() -> None:
    tokens = ['alpha', 'beta',  'gamma']
    l = textmod.remove_punctuation(tokens)
    assert l == tokens

def test_punct_idxs() -> None:
    tokens = ['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', '.', 'Den', 'er', 
              'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', '.',]   
    idxs = textmod.punct_idxs(tokens)
    assert idxs == [5,14] 

def test_to_lowercase_empty() -> None:
    tokens = ['', '', '']
    t = textmod.to_lowercase(tokens)
    assert t == ['', '', '']

def test_config_ok_good() -> None:
    config = {
        "remove_punct" : True,
        "translit" : "unidecode_GER",
        "lowercase" : True
    }
    tm = textmod.TextModifier(**config)
    assert tm._config_ok 

def test_config_ok_bad_value1() -> None:
    config = {
        "remove_punct" : 5,
        "translit" : "unidecode_GER",
        "lowercase" : True
    }
    with pytest.raises(ValueError, match=r"Unknown config entry.*"):
        tm = textmod.TextModifier(**config)


def test_config_ok_bad_value2() -> None:
    config = {
        "aaaaa" : "bbbb",
        "translit" : "unidecode_GER",
        "lowercase" : True
    }
    with pytest.raises(ValueError, match=r"Unknown config entry.*"):
        tm = textmod.TextModifier(**config)

def test_modify_ok() -> None:
    config = {
        "remove_punct" : True,
        "translit" : "unidecode_GER",
        "lowercase" : True
    }
    text = [['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', '.', 'Den', 'er', 
            'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', '.', 'Allmählig', 
            'in', 'die', 'Flamme', 'zu', 'ſchieben', '.']]   
    target_text = [['um', 'den', 'vorrath', 'grüner', 'olivenäste', 'den', 'er', 
                'sich', 'zur', 'seite', 'hatte', 'hinlegen', 'lassen', 'allmählig', 
                'in', 'die', 'flamme', 'zu', 'schieben']]
    tm = textmod.TextModifier(text, **config)
    assert tm.modify() == target_text


def test_bad() -> None:
    assert True == False