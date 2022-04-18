from number import extract_number_phrases
from number import detect_number_phrases_position
from number import text2number
from number_const import UNITS_ORDINAL_WORDS, COMPLICATIONS
import araby
from dates_const import ACCEPT_NUMBER_PREFIX, MONTH_WORDS, YEARS_REPLACE
import re

def prepare_txt(txt):
    rex = re.compile(r' +')
    txt = rex.sub(' ', txt)
    for word in YEARS_REPLACE:
        if txt.find(word) != -1:
            txt = txt.replace(word, YEARS_REPLACE[word])
    txt = txt.replace(u' و ', u' و')
    wordlist = araby.tokenize(txt)
    inv_UNITS_ORDINAL_WORDS = {v: k for k, v in UNITS_ORDINAL_WORDS.items()}
    for i, word in enumerate(wordlist):
        if word in inv_UNITS_ORDINAL_WORDS:
            wordlist[i] = inv_UNITS_ORDINAL_WORDS[word]
            txt = txt.replace(word, wordlist[i])
        elif word.startswith(u'ال') and word[2:] in inv_UNITS_ORDINAL_WORDS:
            wordlist[i] = inv_UNITS_ORDINAL_WORDS[word[2:]]
            txt = txt.replace(word, wordlist[i])
    return txt, wordlist

def is_complication(word):
    is_comp = 0
    if u'مية' in word or u'مائة' in word or u'مئة' in word or u'ميه' in word or u'مائه' in word or u'مئه' in word or u'ميتين' in word or u'مئتين' in word or u'مائتين' in word:
        is_comp = 1
    if word.endswith(u'الاف') or word.endswith(u'آلاف') or word.endswith(u'ألاف') or word.endswith(u'تلاف') or word.endswith(u'الف') or word.endswith(u'ألف') or word.endswith(u'ألفين') or word.endswith(u'الفين'):
        is_comp = 1
    if u'مليون' in word or u'ملايين' in word:
        is_comp = 1
    return is_comp

def get_separate_numbers(wordlist):
    num_phrases_pos = detect_number_phrases_position(wordlist)
    separate_numbers = []
    new_wordlist = []
    j=0
    for slice in num_phrases_pos:
        while j<slice[0]:
            new_wordlist.append(wordlist[j])
            j+=1
        j = slice[1] + 1
        temp_word = ""
        for i in range(slice[0], slice[1]+1):
            if len(temp_word) == 0: temp_word += wordlist[i]
            else:
                if wordlist[i].startswith(u'و') and wordlist[i]!= u'واحد':
                    temp_word += " " + wordlist[i]
                elif is_complication(wordlist[i-1]):
                    temp_word += (" " + wordlist[i])
                elif wordlist[i] in ACCEPT_NUMBER_PREFIX and text2number(wordlist[i]) > text2number(wordlist[i-1]):
                    temp_word += (" " + wordlist[i])
                else:
                    separate_numbers.append(temp_word)
                    new_wordlist.append(temp_word)
                    temp_word = wordlist[i]
        separate_numbers.append(temp_word)
        new_wordlist.append(temp_word)
    while j<len(wordlist):
        new_wordlist.append(wordlist[j])
        j+=1
    return separate_numbers, new_wordlist
    
def extract_date(text, wordlist):
    month_word_in_txt = 0
    if any(word in text for word in MONTH_WORDS):
        month_word_in_txt = 1
    separate_numbers, _ = get_separate_numbers(wordlist)
    num_phrases = separate_numbers
    month = -1
    day = -1
    year = -1
    if month_word_in_txt:
        for word in wordlist:
            if word in MONTH_WORDS:
                num_phrases.append(word)

    if month_word_in_txt:
        for n in num_phrases:
            nn = text2number(n)
            if nn == 0:
                if n in MONTH_WORDS:
                    nn = MONTH_WORDS[n]
                    month = nn 
                else:
                    nn = n
                    if day == -1:
                        day = nn
                    elif month == -1:
                        month = nn
                    else:
                        year = nn
            else:
                if day == -1: 
                    day = nn
                else:
                    year = nn
    else:
        for n in num_phrases:
            nn = text2number(n)
            if nn==0: nn = n
            if day == -1:
                day = nn
            elif month == -1:
                month = nn
            else:
                year = nn

    return day, month, year

if __name__ == '__main__':
    txt = "رفعت الجلسة يوم سبعتاشر من فبراير عشرين اتنين وعشرين بعد"
    # txt = "17"
    txt, wordlist = prepare_txt(txt)
    day, month, year = extract_date(txt, wordlist)
    print(day, month, year)