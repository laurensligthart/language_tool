# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 08:28:13 2022

@author: laure
"""

import numpy as np
import os
import random as rd

"""
TO DO:
- check word encoding (utf-8?)
- double meanings
- verbs
"""






"""
Dictionaries of words with the format 
str((*article*) *word*) --> str((*article*) *word*)
"""
de_to_en = {}
en_to_de = {}
new_de_to_en = {}
new_en_to_de = {}


verb_list = [] #make into dict structure: sein -> [[present], [past], ...]


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_from_list():
    
    #reads the local word list file
    
    word_list = open(os.path.join(__location__, 'word_list.txt'), "r+")
    for line in word_list:
        [key, word] = line.split(";")
        key = key.strip()
        word = word.strip() #remove accidental whitespace
        
        try:
            de_to_en[key]
        except KeyError:
            de_to_en[key] = word
            en_to_de[word] = key
        
def write_to_list():
    
    #(re)creates the word list file in the same folder this python file is in
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    word_list = open(os.path.join(__location__, 'word_list.txt'), "w+")
    for key in de_to_en:
        word_list.write(key + ";" + de_to_en[key] + "\n")

def print_dict():
    
    for key in de_to_en:
        print(key + ", " + de_to_en[key])

def add(word_pair):
    
    try:
        de_word = (word_pair[0]).strip()
        en_word = (word_pair[1]).strip()
    
        de_to_en[de_word] = en_word
        en_to_de[en_word] = de_word
        new_de_to_en[de_word] = en_word
        new_en_to_de[en_word] = de_word
    except:
        print("probably wrong format. Try again")

def remove(word_pair):
    
    try:
        del de_to_en[word_pair[0]]
        del en_to_de[word_pair[1]]
    except KeyError:
        print("This word pair does not exist")
        return None
    
    try:
        del new_de_to_en[word_pair[0]]
        del new_en_to_de[word_pair[1]]
    except KeyError:
        return None

def practice(lang="", m=0, new=False):
    """
    lang: de/en, i.e. the language you want to translate to
    n: number of words you want to practice
    new: If you set new to "new", you'll practice only the words you entered at the start of this session
    """
    
    language = lang
    
    if lang == "":
        language = input("Which language do you want to translate to? de/en \n")
    
    if language == "de" and new:
        keys = [x for x in new_en_to_de]
    elif language == "en" and new:
        keys = [x for x in new_de_to_en]
    elif language == "de":
        keys = [x for x in en_to_de]
    elif language == "en":
        keys = [x for x in de_to_en]
    else:
        print("give language as 'de' or 'en'")
        return None
    
    if m == 0:
        try:
            print("there are now %s words available"%str(len(keys)))
            n = int(input("How many words do you want to practice? \n"))
        except TypeError:
            print("Make sure you input a number")
            return None
    else:
        n = m
    
    try: #sample n random keys, if possible
        key_nums = rd.sample(range(len(keys)), n)
                    
    except ValueError:
        print("You don't know that many words yet. Choose m <= " + str(len(keys)))
        return None
    
    count = 0
    while len(key_nums) > 0:
        key_num = key_nums[0]
        key = keys[key_num]
        answer = input(key + "\n")
        if answer == "stop":
            return None
        if language == "de" and new:
            sol = new_en_to_de[key]
        elif language == "en" and new:
            sol = new_de_to_en[key]
        elif language == "de":
            sol = en_to_de[key]
        elif language == "en":
            sol = de_to_en[key]
            
        if answer == sol:
            count += 1
        elif len(answer.split()) > 1:
            if answer.split()[1] == sol.split()[1]:
                retry = input("You got the article wrong. Try again: " + key + "\n")
                if retry == sol:
                    print("Correct!")
                    key_nums.append(key_num) #repeat at the end
                else:
                    print("Still wrong. The answer is " + sol)
                    key_nums.append(key_num) #repeat at the end
            else:
                print("Wrong. The answer is " + sol)
                key_nums.append(key_num) #repeat at the end
        else:
            print("Wrong. The answer is " + sol)
            key_nums.append(key_num) #repeat at the end
        
        key_nums.pop(0)
        print(str(count) + "/" + str(n))
        if count >= 2*n:
            print("That's enough for now.")
            break
    
    print("Good job, you're done!")

def verbs(tense):
    
    try:
        verb_file = open(os.path.join(__location__, 'verbs_%s.txt'%tense), "r+")
    except FileNotFoundError:
        verb_file = open(os.path.join(__location__, 'verbs_%s.txt'%tense), "w+")
    
    
    for line in verb_file:
        line = "".join(line.split()) #removes all whitespace
        verb_list.append(line.split(";"))

    new_words = input("Do you want to add new verbs? y/n \n")
    if new_words == "y" or new_words == "yes" or new_words == "Y":
        while True:
            new_word = input("give a verb conjugation in the format *sein;bin;bist;ist;sind;seid;sind* or type 'stop'. \n")
            if new_word == "stop":
                break
            else:
                verb = "".join(new_word.split())
                verb_conj = verb.split(";")
                if len(verb_conj) == 7:
                    verb_list.append()
                else:
                    print("Something went wrong with the formatting, try again:")
    
    print("there are now %s verbs available"%str(len(verb_list)))
    
    m = int(input("How many verbs do you want to practice? \n"))
    count = 0
    try: #samples n random keys, if possible
        key_nums = rd.sample(range(len(verb_list)), m)
                    
    except ValueError:
        print("You don't know that many words yet. Choose m <= " + str(len(verb_list)))
        return None
    
    person = ["ich ", "du ", "er/sie/es ", "wir ", "ihr ", "sie "]
    while len(key_nums) > 0:
        print(verb_list[key_nums[0]][0], "(%s)"%tense)
        conj = [input(x) for x in person]
        
        if conj == verb_list[key_nums[0]][1:]:
            print("Nice! \n")
            count += 1
        else:
            print("No") #make this better
            key_nums.append(key_nums[0]) #repeats at the end
        key_nums.pop(0)
    
        print(str(count) + "/" + str(m))
        if count >= 2*m:
            print("That's enough for now.")
            break
    #write to file
    

def start():
    """
    Run this at the start of your practice.
    It asks for new words you'd like to add
    """
    
    read_from_list()
    new_words = input("Do you want to add new words? y/n \n")
    if new_words == "y" or new_words == "yes" or new_words == "Y":
        while True:
            new_word = input("give a word pair in the format *German word*;*English word* or type 'stop'. \n")
            if new_word == "stop":
                break
            else:
                try:
                    add(new_word.split(";"))
                except:
                    print("wrong format.")
    
    print("there are now %s words available"%str(len(de_to_en)))
    print("You added %s words"%str(len(new_de_to_en)))

def update():
    write_to_list()
    read_from_list()

def finish():
    """
    Run this at the end of your practice
    """
    
    write_to_list()
    global new_en_to_de
    global new_de_to_en
    new_en_to_de = {}
    new_de_to_en = {}

def test():
    
    # a = ("der Zug", "the train")
    # add(a)
    
    read_from_list()
    practice("de", 2)
    practice("en", 2)
    remove(("der Zug", "the train"))

# start()
# practice()
# update()
# verbs("present")