#!/bin/python2
# coding:utf-8

import sys

def conll(freeling):
    words = []
    counter = 0
    for word in freeling:
	((token,lemma,tag,prob),real_prob) = word
	counter += 1
	tag = tag.replace('_question_','question')
	tag = tag.replace('_period_','period')
	tag = tag.replace('_colon_','colon')
        tag = tag.replace('_amp_','amp')
	tag = tag.replace('_exclamation_','exclamation')
	tag = tag.replace('PRP$','PRP_')
	tag = tag.replace('-','dash')
	tag = tag.replace('…','dots')
	tag = tag.replace(',','comma')
	tag = tag.replace('(','prnts1')
	tag = tag.replace(')','prnts2')
	tag = tag.replace('’','apostrophe')
	tag = tag.replace('“','quote')
	tag = tag.replace('”','quote')
	tag = tag.replace('"','quote')
	words.append((counter,token,lemma,tag,prob,real_prob))

    return words
