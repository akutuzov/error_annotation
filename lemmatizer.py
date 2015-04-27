#!/bin/python
# coding: utf-8
# Extracting lemmas of words with Freeling
# author: Andrey Kutuzov
# GPL v 3.0
from __future__ import division
from itertools import izip_longest
import subprocess as sp

def lemmatizer(x):
	output = []
	tagged = sp.Popen([u'analyzer_client', u'30000'], stdin=sp.PIPE, stdout=sp.PIPE).communicate(x)[0]
	tagged = tagged.strip().split('\n')
	#print tagged
	for word in tagged:
		word = word.split()
		if word:
		    token = word[0]
    		    variants = word[1:]
		    variants2 = list(izip_longest(*[iter(variants)]*3))
		    lemmas = []
		    tags = []
		    probs = []
		    for i in variants2:
    			if len(i) == 3:
        		    (lemma,tag,prob) = i
        		    if tag.startswith('F'):
            			tag = lemma
        		    lemmas.append(lemma)
			    tags.append(tag)
        		    probs.append(prob)
		output.append((token,' '.join(lemmas),' '.join(tags),' '.join(probs)))
	return output

