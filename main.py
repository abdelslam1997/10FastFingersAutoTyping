'''
So did i can do it ?
let us find out :)
'''
import re
import keyboard
import time

def read_page_source():
    string = input('Paste Page Source: ')
    return str(string)

def extract_words(source):
    words = []
    for word in re.findall('>(.*?)</span>', source):
        words.append(word)

    words[0] = words[0][words[0].find('>')+1:]
    return words

def type_words(words):
    for word in words:
        keyboard.write(word)
        time.sleep(0.1)
        keyboard.press_and_release('space')


str = read_page_source()
words_list = extract_words(str)
time.sleep(5)
type_words(words_list)