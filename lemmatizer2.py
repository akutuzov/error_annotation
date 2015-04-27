#!/bin/python
# coding: utf-8
# Extracting lemmas of words with Freeling
# author: Andrey Kutuzov
# GPL v 3.0
from __future__ import division
import subprocess as sp

def lemmatizer2(x):
	lemmas = []
	tagged = sp.Popen([u'analyzer_client', u'40005'], stdin=sp.PIPE, stdout=sp.PIPE).communicate(x)[0]
	tagged = tagged.strip().split('\n')
	for word in tagged:
		word = word.split()
		if word:
			lemmas.append(word[3])
	return lemmas

