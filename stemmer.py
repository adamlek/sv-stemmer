"""
http://snowball.tartarus.org/algorithms/swedish/stemmer.html
SNOWBALL IMPLEMENTATION:

step 0:
mark r1 area (first consonant followed by a vowel)

step 1a:
find longest suff_1 in r1
    DELETE

step 1b:
if r1 ends with 's'
    DELETE iff preceded by valid_s

step 2:
search for one among suff_2 in r1
    DELETE last token

step 3:
search for longest in suff_3 and suff_4
    if suff_3 DELETE
    if suff_4 DELETE last token


"""
import re
from itertools import *

vowels = ['å', 'ä', 'ö', 'a', 'e', 'i', 'o', 'u', 'y']
valid_s = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'l', 'm', 'n', 'o', 'p', 'r',
           't', 'v', 'y']
#ORIGINAL FROM WEBSITE
#suff_1 = ['a', 'arna', 'erna', 'heterna', 'orna', 'ad', 'e', 'ade', 'ande', 'arne',
#          'are', 'aste', 'en', 'anden', 'aren', 'heten', 'ern', 'ar', 'er', 'eter',
#          'or', 'as', 'arnas', 'ernas', 'ornas', 'es', 'ades', 'andes', 'ens', 'arens',
#          'etens', 'erns', 'at', 'andet', 'het', 'ast']
suff_1 = ['a', 'arna', 'erna', 'heterna', 'orna', 'ad', 'e', 'ade', 'ande', 'arne',
          'are', 'aste', 'en', 'anden', 'aren', 'heten', 'ern', 'ar', 'er', 'eter',
          'or', 'as', 'arnas', 'ernas', 'ornas', 'es', 'ades', 'andes', 'ens', 'arens',
          'etens', 'erns', 'at', 'andet', 'het', 'ast', 'bart', 'ning', 'ellt']
suff_2 = ['dd', 'gd', 'nn', 'dt', 'gt', 'kt', 'tt']
suff_3 = ['lig', 'ig', 'els']
suff_4 = ['löst', 'fullt']

def step0(word):
    pass

def step1a(word):
    pass

def step1b(word):
    pass

def step2(word):
    pass

def step3(word):
    pass

def main():
    pass

if __name__ == '__main__':
    main()
