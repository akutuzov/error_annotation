#coding: utf-8
# Check spelling

import codecs, re, subprocess as sup, sys

def correction(string):
    return re.findall(': (.*?),', sup.Popen([u'aspell', '-a', '-l', 'en'], stdin=sup.PIPE,\
    stdout=sup.PIPE).communicate(string.encode('utf-8'))[0])