# textmod

Functions for modifying tokenized text (i.e. lists of words).

This can be used to pre- or post-process a text in an NLP task.

## Installation

`pip install git+ssh://git@github.com/ybracke/textmod.git`

## Requirements

* Python >= 3.7
* unidecode >= 1.3.4

```bash
pip install -r requirements.txt
```

To run tests: pytest >= 7.1

## Supported modifications

- Punctuation removal 
- lowercasing 
- unidecode 

## Usage

```python
config = {
    "remove_punct" : True,
    "translit" : "unidecode_GER",
    "lowercase" : True
}
text = [['Um', 'den', 'Vorrath', 'grüner', 'Olivenäſte', '.', 'Den', 'er', 
        'ſich', 'zur', 'Seite', 'hatte', 'hinlegen', 'laſſen', '.', 'Allmählig', 
        'in', 'die', 'Flamme', 'zu', 'ſchieben', '.']] 
tm = textmod.TextModifier(text, **config)
modified_text = tm.modify()

target_text = [['um', 'den', 'vorrath', 'grüner', 'olivenäste', 'den', 'er', 
                'sich', 'zur', 'seite', 'hatte', 'hinlegen', 'lassen', 'allmählig', 
                'in', 'die', 'flamme', 'zu', 'schieben']]

assert modified_text == target_text
```


## Possible future modifications

- truecasing 
- stemming 
- lemmatization 
  
- Order of manipulation matters, so watch out how you order stuff in the config
  - steps where order matters: 
    - remove punct <> lemmatization (lemmatizer may depend on tokenization)
    - unidecode <> lemmatization/stemming
    - lowercasing <> lemmatization/stemming


## License
Copyright © 2022 Berlin-Brandenburgische Akademie der Wissenschaften.

This project is licensed under the GNU General Public License v3.0.

