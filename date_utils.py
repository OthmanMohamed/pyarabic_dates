from number import extract_number_phrases
from number import detect_number_phrases_position
from number import text2number
import araby
from number_const import UNITS_ORDINAL_WORDS, UNITS_ORDINAL_WORDS_FEMININ, COMPLICATIONS
from dates_const import ACCEPT_NUMBER_PREFIX, MONTH_WORDS, YEARS_REPLACE
from dates_const import DATE_FILL_WORDS, DAY_DEFINING_WORDS
import re


def prepare_txt(txt):
    # REPLACE MULTI SPACES
    repeared_spaces = re.compile(r' +')
    txt = repeared_spaces.sub(' ', txt)
    # REPLACE و WITH SPACES
    txt = txt.replace(u' و ', u' و')
    # REPLACE COMMON YEAR NAMES "مثال: عشرين عشرين ---> الفين وعشرين"
    for word in YEARS_REPLACE:
        if txt.find(word) != -1:
            txt = txt.replace(word, YEARS_REPLACE[word])
    # TOKENIZE
    wordlist = araby.tokenize(txt)
    # REPLACE ORDINALS WITH NUMBER WORDS
    inv_UNITS_ORDINAL_WORDS = {v: k for k, v in UNITS_ORDINAL_WORDS.items()}
    inv_UNITS_ORDINAL_WORDS_FEMININ = {v: k for k, v in UNITS_ORDINAL_WORDS_FEMININ.items()}
    txt = ""
    for i, word in enumerate(wordlist):
        if word in inv_UNITS_ORDINAL_WORDS:
            # REPLACE ORDINALS EVEN WITHOUT ال ; MAY NEED TO BE REMOVED 
            wordlist[i] = inv_UNITS_ORDINAL_WORDS[word]
        elif word.startswith(u'ال') and word[2:] in inv_UNITS_ORDINAL_WORDS:
            # REPLACE ORDINALS CONTAINING ال
            wordlist[i] = inv_UNITS_ORDINAL_WORDS[word[2:]]
        elif word in inv_UNITS_ORDINAL_WORDS_FEMININ:
            # REPLACE ORDINALS EVEN WITHOUT ال ; MAY NEED TO BE REMOVED 
            wordlist[i] = inv_UNITS_ORDINAL_WORDS_FEMININ[word]
        elif word.startswith(u'ال') and word[2:] in inv_UNITS_ORDINAL_WORDS_FEMININ:
            # REPLACE ORDINALS CONTAINING ال
            wordlist[i] = inv_UNITS_ORDINAL_WORDS_FEMININ[word[2:]]
        txt = txt + " " + wordlist[i]
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
    # print(wordlist, num_phrases_pos)
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
            # print("wordlist : ", wordlist)
            # print("wordlist[i] : ", wordlist[i])
            # print("temp_word : ", temp_word)
            # print("new_wordlist : ", new_wordlist, "\n\n\n")
            if len(temp_word) == 0: temp_word += wordlist[i]
            else:
                if wordlist[i].startswith(u'و') and not wordlist[i].startswith(u'واحد') and text2number(wordlist[i]) >= 20:
                    if i > slice[0]:
                        if wordlist[i-1] != u'واحدة': temp_word += " " + wordlist[i]
                        else:
                            separate_numbers.append(temp_word)
                            new_wordlist.append(temp_word)
                            temp_word = wordlist[i]
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
    flags_list = []
    for w in new_wordlist:
        if " " in w or detect_number_phrases_position([w]):
            flags_list.append(1)
        else:
            flags_list.append(0)
    return separate_numbers, new_wordlist, flags_list


def get_dates(new_wordlist, number_flag_list):
    state = "START"
    date_sentences = []
    date_sent = ""
    for i in range(len(new_wordlist)):
        # print(i)
        # print(state)
        # print(new_wordlist[i], '\n\n\n\n')
        if state == "START":
            date_sent = ""
            if number_flag_list[i]==1:
                if text2number(new_wordlist[i]) <= 31 and text2number(new_wordlist[i]) > 0:
                    date_sent += new_wordlist[i]
                    state = "DAY"
                else:
                    state = "REPEATED NUMS"
        elif state == "DAY":
            if number_flag_list[i]==0 and not (new_wordlist[i] in DATE_FILL_WORDS or new_wordlist[i] in MONTH_WORDS):
                state = "START"
            elif number_flag_list[i]==1 and (text2number(new_wordlist[i]) < 0 or text2number(new_wordlist[i]) > 12):
                state = "REPEATED NUMS"
            else:
                date_sent += " " + new_wordlist[i]
                if number_flag_list[i]==1 or new_wordlist[i] in MONTH_WORDS:
                    state = "MONTH"
        elif state == "MONTH":
            if number_flag_list[i]==0 and not new_wordlist[i] in DATE_FILL_WORDS:
                date_sentences.append(date_sent)
                state = "START"
            else:
                date_sent += " " + new_wordlist[i]
                if number_flag_list[i]==1:
                    if text2number(new_wordlist[i]) > 1900:
                        date_sentences.append(date_sent)
                        state = "START"
                    else:
                        state = "REPEATED NUMS"
        elif state == "REPEATED NUMS":
            date_sent = ""
            if number_flag_list[i]==0: state = "START"

    else:
        if state == "MONTH" or state == "YEAR":
            date_sentences.append(date_sent)
    return date_sentences

    
def extract_date(text, wordlist):
    # print("TXT : ", text)
    # print("WORDLIST : ", wordlist)
    month_word_in_txt = 0
    if any(word in text for word in MONTH_WORDS):
        month_word_in_txt = 1
    separate_numbers, *_ = get_separate_numbers(wordlist)
    num_phrases = separate_numbers
    # print("NUM PHRASES : ", num_phrases)
    month = -1
    day = -1
    year = -1
    if month_word_in_txt:
        for word in wordlist:
            if word in MONTH_WORDS:
                num_phrases.append(word)
    # print("NUM PHRASES AFTER : ", num_phrases)
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