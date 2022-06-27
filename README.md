# README

Text manipulation functionalities

Actually, this can be either pre- or post-precessing so I might rename this
module to `normedit`/`normmanip`/`normprocess` or something like that.

For now (2022-06-24) this is project is a stub with a template file and a test
file. Directory `code2recycle` contains symlinks to previously written programs
that already contain much of the desired functionality.

Important: This module is not supposed to do any reading and writing of data.
This will be done by `~/code/compare-tools/python/prepoc.py`, which is already
quite complete.

# TODOs

- [ ] Take care of lemmatization/stemming:
  - Look at the discussion here: https://dmm.bbaw.de/dstar-teambbaw/pl/q3b4kq7m4jd8deaxn4oij7ybuc
  - Look at: /home/bracke/code/normpreproc/code2recycle/preproc.py

## Done

- [x] What is the input/output format of this module
- [x] Get an overview over the code in `code2recycle`

# What the program should be able to do

- Punctuation removal   
  - different definitions / lists of punctuation? (typically pre-process)
- lowercasing (both)
- truecasing (typically post-process)
- unidecode (typically pre-process)
  - "keep Umlauts+ß"-option (see unicode_ger.py)
- option to apply hand-written rules (in dict or so) (both)
- stemming (typically post-process)
- lemmatization (typically post-process)
  
- Order of manipulation matters, so watch out how you order stuff in the config
  - steps where order matters: 
    - remove punct <> lemmatization (lemmatizer may depend on tokenization)
    - unidecode <> lemmatization/stemming
    - lowercasing <> lemmatization/stemming


# Requirements

```bash
pip install -r requirements.txt
```

