# error_annotation
This is a framework for pre-annotating learner corpora with typical errors.
The system itself is described in detail in the paper 'Semi-automated typical error annotation for learner English essays: integrating frameworks' (included in this repository).
It can be used to ease the work of human annotator who spot errors in learner texts. It employs Aspell spellchecker and Freeling suite of linguistic analyzers (http://nlp.lsi.upc.edu/freeling/) to find positions where there is a possible error.

The system is used together with Brat web annotation framework (http://brat.nlplab.org/) and works automatically whenever a new document is uploaded via web interface. It is processed and annotations with possible errors are generated. 
Aferwards, human annotators can use them as hints to make error spotting easier.

The system was developed for Russian Error-Annotated Learner English Corpus (REALEC, http://realec.org).

Instructions
============

You should have Brat, Freeling and Aspell installed on your Unix server. Supposedly, Aspell is already there, if not, check http://aspell.net/.
Freeling must run as a service with English model. Actually, as two services:
    - it should listen on port 40005 with default settings (returning the most probable morphosyntactic tags for input text);
    - another Freeling instance should listen on port 3000 with parameter '--outf morfo' (returning the full set of possible tags).

The port values can of course be changed in the files lemmatizer.py and lemmatizer2.py. Instructions on running Freeling as a service can be found at http://nlp.lsi.upc.edu/freeling/doc/userman/html/node89.html.

The following files should be placed in the server/src/ directory of your Brat installation:
    - aspell2.py
    - conll2standoff.py
    - docimport.py (overwriting previous one)
    - freeling2conll.py
    - lemmatizer2.py
    - lemmatizer.py

That's pretty much all. Now when a document is uploaded via Brat interface it will be automatically tagged with possible mistakes.

Contacts
========
Andrey Kutuzov	akutuzov@hse.ru
Elizaveta Kuzmenko	eakuzmenko_2@edu.hse.ru