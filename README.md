# `textmod`

Functions for modifying lists of text

To be used for pre- or post-precessing in my tool comparison.

Directory `code2recycle` contains symlinks to previously written programs
that already contain much of the desired functionality.

# Functionalities (present and future)

- Punctuation removal   
  - different definitions / lists of punctuation? (typically pre-process)
- lowercasing (both)
- unidecode (typically pre-process)
- option to apply additional external functions
- truecasing (typically post-process) **TODO**
- stemming (typically post-process) **TODO**
- lemmatization (typically post-process) **TODO**
  
- Order of manipulation matters, so watch out how you order stuff in the config
  - steps where order matters: 
    - remove punct <> lemmatization (lemmatizer may depend on tokenization)
    - unidecode <> lemmatization/stemming
    - lowercasing <> lemmatization/stemming

# TODOs

- [ ] Take care of lemmatization/stemming:
  - Look at the discussion here: https://dmm.bbaw.de/dstar-teambbaw/pl/q3b4kq7m4jd8deaxn4oij7ybuc
  - Look at: /home/bracke/code/normpreproc/code2recycle/preproc.py

# Requirements

```bash
pip install -r requirements.txt
```

