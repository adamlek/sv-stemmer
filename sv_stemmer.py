# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:55:45 2016

@author: Adam

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
#Byta ut

#< resuts with 3x consonants as ending is wrong, what rule?

class sv_stemmer():
    def __init__(self):
        self.word = None      
        
        self.vowels = vowels
        self.valid_s = valid_s
        self.suff_1 = suff_1
        self.suff_2 = suff_2
        self.suff_3 = suff_3
        self.suff_4 = suff_4

    #< !!! r1 preceeded by atleast 3 characters
    def step0(self, seq):
        for i, l in enumerate(seq):
            if i >= 3:
                if l not in self.vowels and (i+1) != len(seq):
                    if seq[i+1] in self.vowels:
                        print(seq[:i], '||',seq[i:])
                        return seq[:i], seq[i:]

    def step1a(self, seq):
        for i in [7,6,5,4,3,2,1]:
            suffs = [x for x in suff_1 if len(x) == i]
            for suff in suffs:
                if suff in seq[-i:]:
                    print(suff, 'suff')
                    if suff == seq:
                        return '' #< suff is whole of seq, remove all
                       
                    else:
                        if len(seq) > 1:
                            return seq[:len(seq)-len(suff)] #return r1 minus suff
                        else:
                            return '' #< ending == 1, remove
                else:
                    continue
        return seq #return seq if no suffix present

    def step1b(self, seq):
        if len(seq) <= 1:
            if seq[-1] == 's':
                if self.word[-1] in self.valid_s:
                    return '' #suff 's' followed by valid_s
                else:
                    return seq #suff followed by != valid_s
            else:
                return seq #return seq
        else:
            if seq[-1] == 's':
                if seq[-2] in self.valid_s:
                    return seq[:-1] #suff 's' followed by valid_s in r1
                else:
                    return seq #suff != followed by valid_s in r1
            else:
                return seq #return seq

    def step2(self, seq):
        if seq[-2:] in suff_2: #if seq ends with consonant pair
            return seq[:-1] #remove last letter
        else:
            return seq #return seq

    def step3(self, seq):
        if seq in suff_4: #ending of seq is "fullt" or "löst"
            return seq[:-1] #return "full" "lös"
        else:
            if seq[-3:] in suff_3: #ends in lig or els
                return seq[:-3]
            elif seq[-2:] in suff_3: #ends in ig
                return seq[:-2]
            else:
                return seq
            

    def stem(self, word):
        if len(word) >= 4:
            word_ending = self.step0(word)
            if word_ending:
                print(word_ending)
                self.word = word_ending[0]            
            
                ending = self.step1a(word_ending[1])
                if ending:
                    ending = self.step1b(ending)
                else:
                    if ending == None:
                        ending = ''
                    print('ret 1a')
                    return''.join([word_ending[0], ending])

            else:
                print('ret 1ab')
                return word
            
            if ending:
                ending = self.step2(ending)
            else:
                if ending == '':
                    print('ret 2')
                    return''.join([word_ending[0], ending])
            
            if ending:
                ending = self.step3(ending)
                if ending == '':
                    print('ret 3')
                    return''.join([word_ending[0], ending])
       
#            if ending:
#                ending = self.step4(ending)
#                if ending == '':
#                    print('ret 4')
#                    return''.join([word_ending[0], ending])
            if ending:
                return ''.join([word_ending[0], ending])
       
        print('ret START')
        return word


def main():
    sv_stem = sv_stemmer()
    w = []
#    svord = ["böjning"]
    svord = []
    with open('/home/usr1/git/stemmer_data/sv_test2.txt') as f:
        for line in f:
            w.append(line.split())
        
    for line in w:
        for word in line:
            word = word.lower()
            word = re.sub('[^a-zåäö]', '', word)
            svord.append(word)         
#        
    res = []
    for word in svord:
        s = sv_stem.stem(word)
        res.append((word, s))
    
    for t in res:
        print(t)

if __name__ == '__main__':
    main()