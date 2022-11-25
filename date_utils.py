# from sympy import N
from os import stat
from number import extract_number_phrases
from number import detect_number_phrases_position
from number import text2number
from number_const import UNITS_ORDINAL_WORDS, UNITS_ORDINAL_WORDS_FEMININ, inv_UNITS_ORDINAL_WORDS_FEMININ, inv_UNITS_ORDINAL_WORDS
from dates_const import ACCEPT_NUMBER_PREFIX, MONTH_WORDS, YEARS_REPLACE, SPECIAL_SESSIONS_WORDS
from dates_const import DATE_FILL_WORDS, DAY_DEFINING_WORDS, TEN_PREFIX, DATE_TRIGGERS, NUMBER_TRIGGERS
import re

def prepare_txt(txt):
    # REPLACE و WITH SPACES
    txt = txt.replace(u' و ', u' و')
    original_txt = txt
    # Normalize Letters
    txt = txt.replace(u'أ', u'ا')
    txt = txt.replace(u'إ', u'ا')
    txt = txt.replace(u'ه ', u'ة ')
    txt = txt.replace('ه\n', 'ة\n')
    # REPLACE MULTI SPACES
    # repeared_spaces = re.compile(r' +')
    # txt = repeared_spaces.sub(' ', txt)
    # REPLACE COMMON YEAR NAMES "مثال: عشرين عشرين ---> الفين وعشرين"
    for word in YEARS_REPLACE:
        if txt.find(word) != -1:
            if txt[txt.find(word)-1] != u'و': # To avoid wrongly detecting repeated numbers
                txt = txt.replace(word, YEARS_REPLACE[word])
    # TOKENIZE
    # wordlist = araby.tokenize(txt)
    wordlist = txt.split()
    original_wordlist = original_txt.split()
    # REPLACE ORDINALS WITH NUMBER WORDS
    # inv_UNITS_ORDINAL_WORDS = {v: k for k, v in UNITS_ORDINAL_WORDS.items()}
    # inv_UNITS_ORDINAL_WORDS_FEMININ = {v: k for k, v in UNITS_ORDINAL_WORDS_FEMININ.items()}
    # print(inv_UNITS_ORDINAL_WORDS_FEMININ)
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
        txt = txt + " " + wordlist[i] if i!=0 else txt + wordlist[i]
    # txt = txt.replace(u' )', u')')
    # txt = txt.replace(u'( ', u'(')
    return txt, original_txt, wordlist, original_wordlist


def is_complication(word):
    is_comp = 0
    if u'مية' in word or u'مائة' in word or u'مئة' in word or u'ميه' in word or u'مائه' in word or u'مئه' in word or u'ميتين' in word or u'مئتين' in word or u'مائتين' in word or u'متين' in word:
        is_comp = 1
    if word.endswith(u'الاف') or word.endswith(u'آلاف') or word.endswith(u'ألاف') or word.endswith(u'تلاف') or word.endswith(u'الف') or word.endswith(u'ألف') or word.endswith(u'ألفين') or word.endswith(u'الفين'):
        is_comp = 1
    if u'مليون' in word or u'ملايين' in word:
        is_comp = 1
    return is_comp


def get_separate_numbers(wordlist, original_wordlist):
    num_phrases_pos = detect_number_phrases_position(wordlist)
    # print(wordlist, num_phrases_pos)
    separate_numbers = []
    new_wordlist = []
    new_original_wordlist = []
    j=0
    for slice in num_phrases_pos:
        while j<slice[0]:
            new_wordlist.append(wordlist[j])
            new_original_wordlist.append(original_wordlist[j])
            j+=1
        j = slice[1] + 1
        temp_word = ""
        temp_original_word = ""
        for i in range(slice[0], slice[1]+1):
            # print("wordlist : ", wordlist)
            # print("wordlist[i] : ", wordlist[i])
            # print("temp_word : ", temp_word)
            # print("new_wordlist : ", new_wordlist, "\n\n\n")
            if len(temp_word) == 0: 
                temp_word += wordlist[i]
                temp_original_word += original_wordlist[i]
            else:
                if wordlist[i].startswith(u'و') and not wordlist[i].startswith(u'واحد') and (text2number(wordlist[i]) >= 20 and text2number(wordlist[i]) <= 90 and text2number(wordlist[i-1]) < text2number(wordlist[i])):
                    if wordlist[i-1] != u'واحدة': 
                        temp_word += " " + wordlist[i]
                        temp_original_word += " " + original_wordlist[i]
                    else:
                        separate_numbers.append(temp_word)
                        new_wordlist.append(temp_word)
                        new_original_wordlist.append(temp_original_word)
                        temp_word = wordlist[i]
                        temp_original_word = original_wordlist[i]
                # elif is_complication(wordlist[i-1]) or is_complication(wordlist[i]):
                elif is_complication(wordlist[i-1]) and text2number(wordlist[i]) < text2number(wordlist[i-1]):
                    temp_word += (" " + wordlist[i])
                    temp_original_word += (" " + original_wordlist[i])
                elif (wordlist[i] in ACCEPT_NUMBER_PREFIX) and (text2number(wordlist[i]) > text2number(wordlist[i-1])) and (text2number(wordlist[i-1])!=0):
                    if (wordlist[i] == u'عشر' or wordlist[i] == u'عشرة' or wordlist[i] == u'عشره' or wordlist[i] == u'مية' or wordlist[i] == u'مئة' or wordlist[i] == u'مائة' or wordlist[i] == u'الف' or wordlist[i] == u'ألف')\
                        and\
                        (((wordlist[i-1] not in TEN_PREFIX) and (wordlist[i-1][2:] not in TEN_PREFIX)  and  (wordlist[i-1][1:] not in TEN_PREFIX))\
                        or (i>1 and wordlist[i-2] in DAY_DEFINING_WORDS)) :
                        separate_numbers.append(temp_word)
                        new_wordlist.append(temp_word)
                        new_original_wordlist.append(temp_original_word)
                        temp_word = wordlist[i]
                        temp_original_word = original_wordlist[i]
                    else:
                        temp_word += (" " + wordlist[i])
                        temp_original_word += (" " + original_wordlist[i])
                else:
                    separate_numbers.append(temp_word)
                    new_wordlist.append(temp_word)
                    new_original_wordlist.append(temp_original_word)
                    temp_word = wordlist[i]
                    temp_original_word = original_wordlist[i]
        separate_numbers.append(temp_word)
        new_wordlist.append(temp_word)
        new_original_wordlist.append(temp_original_word)
    while j<len(wordlist):
        new_wordlist.append(wordlist[j])
        new_original_wordlist.append(original_wordlist[j])
        j+=1
    flags_list = []
    for w in new_wordlist:
        if " " in w or detect_number_phrases_position([w]):
            flags_list.append(1)
        else:
            flags_list.append(0)
    return separate_numbers, new_wordlist, new_original_wordlist, flags_list

def get_special_sessions_number(new_wordlist, number_flag_list, dates_flags_list):
    sessions_sentences = []
    flags_list = []
    end_indices = []
    i = 0
    while i < len(new_wordlist):
        if any(word in new_wordlist[i] for word in SPECIAL_SESSIONS_WORDS):
            session_sent = new_wordlist[i]
            flags_list.append(1)
            special_session_flag = 0
            while i+1 < len(new_wordlist) and number_flag_list[i+1] == 1 and dates_flags_list[i+1]==0:
                flags_list.append(1)
                special_session_flag = 1
                session_sent += " " + new_wordlist[i+1]
                i += 1
                break
            if special_session_flag: 
                sessions_sentences.append(session_sent)
                end_indices.append(i)
        else:
            flags_list.append(0)
        i += 1
    return sessions_sentences, flags_list, end_indices

def get_repeated_nums(new_wordlist, number_flag_list, dates_flags_list, times_flags_list):
    repeated_num_sent = ""
    repeated_nums_flag = 0
    repeated_nums = []
    end_indices = []
    for i in range(len(new_wordlist)):
        if dates_flags_list[i] == 1 or times_flags_list[i] == 1: 
            if repeated_num_sent != "" and not all(s.isnumeric() for s in repeated_num_sent.split()):
                repeated_nums.append(repeated_num_sent)
                end_indices.append(i-1)
                repeated_nums_flag = 1
                repeated_num_sent = ""
            continue
        if number_flag_list[i] == 1:
            repeated_num_sent += " " + new_wordlist[i]
        if number_flag_list[i] == 0 and repeated_num_sent != "": 
                if not all(s.isnumeric() for s in repeated_num_sent.split()):
                    repeated_nums.append(repeated_num_sent)
                    end_indices.append(i-1)
                    repeated_nums_flag = 1
                    repeated_num_sent = ""
    else:
        if repeated_num_sent != "":
            repeated_nums.append(repeated_num_sent)
            end_indices.append(i-1)
            repeated_nums_flag = 1
    return repeated_nums, repeated_nums_flag, end_indices

def get_separate_repeated_numbers(new_wordlist, number_flag_list):
    state = "START"
    repeated_num_sentences = []
    end_indices = []
    repeated_num_flags_list = [0] * len(new_wordlist)
    repeated_num_sent = ""
    for i in range(len(new_wordlist)):
        if state == "START":
            repeated_num_sent = ""
            if any(word in new_wordlist[i] for word in NUMBER_TRIGGERS) and i+1<len(new_wordlist) and number_flag_list[i+1] == 1:
            # if (u'رقم' in new_wordlist[i] or u'قومي' in new_wordlist[i] or u'بطاقة' in new_wordlist[i]) and i+1<len(new_wordlist) and number_flag_list[i+1] == 1:
                state = "TRIGGERED"
        elif state == "TRIGGERED":
            if number_flag_list[i] == 1:
                repeated_num_flags_list[i] = 1
                repeated_num_sent += " " + new_wordlist[i]
            elif repeated_num_sent:
                repeated_num_sentences.append(repeated_num_sent)
                repeated_num_sent = ""
                end_indices.append(i-1)
                repeated_num_sent = ""
                if any(word in new_wordlist[i] for word in NUMBER_TRIGGERS) and i+1<len(new_wordlist) and number_flag_list[i+1] == 1:
                # if (u'رقم' in new_wordlist[i] or u'قومي' in new_wordlist[i] or u'بطاقة' in new_wordlist[i]) and i+1<len(new_wordlist) and number_flag_list[i+1] == 1:
                    state = "TRIGGERED"
                else: state = "START"
    else:
        if repeated_num_sent:
            repeated_num_sentences.append(repeated_num_sent)
            end_indices.append(i)
    return repeated_num_sentences, repeated_num_flags_list, end_indices



def get_dates(new_wordlist, number_flag_list, special_session_flag_list):
    state = "START"
    date_sentences = []
    end_indices = []
    dates_flags_list = [0] * len(new_wordlist)
    for i in range(len(new_wordlist)):
        if special_session_flag_list[i] == 1: continue
        if state == "START":
            if new_wordlist[i] in DATE_TRIGGERS or (new_wordlist[i][0] == u'و' and new_wordlist[i][1:] in DATE_TRIGGERS) or (new_wordlist[i] in DAY_DEFINING_WORDS and new_wordlist[i].startswith(u'ال')):
                state = "TRIGGERED"
        elif state == "TRIGGERED":
            # if repeated_nums_flag and not repeated_num_sent == "":
            #     repeated_nums.append(repeated_num_sent)
            # if special_session_flag_list[i] == 1:
            #     if number_flag_list[i] == 1:
            #         repeated_num_sent += new_wordlist[i]
            #         repeated_nums_flag = 1
            #     continue
            dates_indices = []
            date_sent = ""
            # repeated_num_sent = ""
            if number_flag_list[i]==1:
                # if text2number(new_wordlist[i]) <= 2030 and text2number(new_wordlist[i]) >1900:
                #     date_sent += new_wordlist[i]
                #     dates_indices.append(i)
                #     state = "YEAR"
                # elif text2number(new_wordlist[i]) <= 31 and text2number(new_wordlist[i]) > 0:
                if (not new_wordlist[i].startswith(u'ال')) or new_wordlist[i].startswith(u'الف'):
                    if text2number(new_wordlist[i]) <= 31 and text2number(new_wordlist[i]) > 0:
                        date_sent += new_wordlist[i]
                        dates_indices.append(i)
                        state = "DAY"
            if state != "DAY": 
                if new_wordlist[i] in DATE_TRIGGERS or (new_wordlist[i][0] == u'و' and new_wordlist[i][1:] in DATE_TRIGGERS) or (new_wordlist[i] in DAY_DEFINING_WORDS and new_wordlist[i].startswith(u'ال')):
                    state = "TRIGGERED"
                else: state = "START"
                # else:
                #     repeated_num_sent += new_wordlist[i]
                #     state = "REPEATED NUMS"
        elif state == "DAY":
            if number_flag_list[i]==0 and not (new_wordlist[i] in DATE_FILL_WORDS or new_wordlist[i] in MONTH_WORDS):
                # repeated_num_sent = date_sent
                # if not all(s.isnumeric() for s in repeated_num_sent.split()):
                #     repeated_nums.append(repeated_num_sent)
                #     repeated_nums_flag = 1
                if new_wordlist[i] in DATE_TRIGGERS or (new_wordlist[i][0] == u'و' and new_wordlist[i][1:] in DATE_TRIGGERS) or (new_wordlist[i] in DAY_DEFINING_WORDS and new_wordlist[i].startswith(u'ال')):
                    state = "TRIGGERED"
                else: state = "START"
            # elif number_flag_list[i]==1 and (text2number(new_wordlist[i]) < 0 or text2number(new_wordlist[i]) > 12):
            #     date_sent += " " + new_wordlist[i]
            #     state = "REPEATED NUMS"
            elif (number_flag_list[i]==1 and (text2number(new_wordlist[i]) > 0 and text2number(new_wordlist[i]) <= 12)) or new_wordlist[i] in MONTH_WORDS or new_wordlist[i] in DATE_FILL_WORDS:
                date_sent += " " + new_wordlist[i]
                dates_indices.append(i)
                if number_flag_list[i]==1 or new_wordlist[i] in MONTH_WORDS:
                    state = "MONTH"
            else:
                if new_wordlist[i] in DATE_TRIGGERS or (new_wordlist[i][0] == u'و' and new_wordlist[i][1:] in DATE_TRIGGERS) or (new_wordlist[i] in DAY_DEFINING_WORDS and new_wordlist[i].startswith(u'ال')):
                    state = "TRIGGERED"
                else: state = "START"
        elif state == "MONTH":
            if number_flag_list[i]==0 and not new_wordlist[i] in DATE_FILL_WORDS:
                date_sentences.append(date_sent)
                for d_i in dates_indices:
                    dates_flags_list[d_i] = 1
                end_indices.append(i-1)
                if new_wordlist[i] in DATE_TRIGGERS or (new_wordlist[i][0] == u'و' and new_wordlist[i][1:] in DATE_TRIGGERS) or (new_wordlist[i] in DAY_DEFINING_WORDS and new_wordlist[i].startswith(u'ال')):
                    state = "TRIGGERED"
                else: state = "START"
            else:
                date_sent += " " + new_wordlist[i]
                dates_indices.append(i)
                if number_flag_list[i]==1:
                    if text2number(new_wordlist[i]) >= 1900 and text2number(new_wordlist[i]) <= 2030:
                        date_sentences.append(date_sent)
                        end_indices.append(i)
                        for d_i in dates_indices:
                            dates_flags_list[d_i] = 1
                    if new_wordlist[i] in DATE_TRIGGERS or (new_wordlist[i][0] == u'و' and new_wordlist[i][1:] in DATE_TRIGGERS) or (new_wordlist[i] in DAY_DEFINING_WORDS and new_wordlist[i].startswith(u'ال')):
                        state = "TRIGGERED"
                    else: state = "START"
                    # else:
                    #     state = "REPEATED NUMS"
        elif state == "YEAR":
            if number_flag_list[i]==0: 
                for d_i in dates_indices:
                    dates_flags_list[d_i] = 1
                date_sentences.append(date_sent)
                end_indices.append(i-1)
            if new_wordlist[i] in DATE_TRIGGERS or (new_wordlist[i][0] == u'و' and new_wordlist[i][1:] in DATE_TRIGGERS) or (new_wordlist[i] in DAY_DEFINING_WORDS and new_wordlist[i].startswith(u'ال')):
                    state = "TRIGGERED"
            else: state = "START"
            # else:
            #     repeated_num_sent = date_sent + " " + new_wordlist[i]
            #     state = "REPEATED NUMS"
        # elif state == "REPEATED NUMS":
        #     if repeated_num_sent == "": repeated_num_sent = date_sent
        #     date_sent = ""
        #     if number_flag_list[i]==0: 
        #         if not all(s.isnumeric() for s in repeated_num_sent.split()):
        #             repeated_nums.append(repeated_num_sent)
        #             repeated_nums_flag = 1
        #         state = "START"
        #     else:
        #         repeated_num_sent += " " + new_wordlist[i]
    else:
        if state == "MONTH" or state == "YEAR":
            date_sentences.append(date_sent)
            end_indices.append(i)
            for d_i in dates_indices:
                dates_flags_list[d_i] = 1
        # if state == "DAY":
        #     pass
            # repeated_nums.append(date_sent)
            # repeated_nums_flag = 1
        # if state == "REPEATED NUMS":
        #     if repeated_num_sent == "": repeated_num_sent = date_sent
        #     repeated_nums.append(repeated_num_sent)
        #     repeated_nums_flag = 1
    return date_sentences, dates_flags_list, end_indices

    
def extract_date(text, wordlist):
    # print("TXT : ", text)
    # print("WORDLIST : ", wordlist)
    month_word_in_txt = 0
    if any(word in text for word in MONTH_WORDS):
        month_word_in_txt = 1
    separate_numbers, *_ = get_separate_numbers(wordlist, wordlist)
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
                    elif int(nn)>1900 and int(nn)<2030:
                        year = nn
            else:
                if day == -1: 
                    day = nn
                elif int(nn)>1900 and int(nn)<2030:
                    year = nn
    else:
        for n in num_phrases:
            nn = text2number(n)
            if nn==0: nn = n
            if day == -1 and nn>0 and nn<=31:
                day = nn
            elif year == -1 and nn>1990 and nn<=2030:
                year = nn
            elif month == -1 and nn<=12 and nn>0:
                month = nn
            elif int(nn)>1900 and int(nn)<2030:
                year = nn
    return day, month, year

def extract_repeated_numbers(text, wordlist):
    num = ""
    num_phrases, *_ = get_separate_numbers(wordlist, wordlist)
    for i, n in enumerate(num_phrases):
        nn = text2number(n)
        if nn == 0 and (n != 'صفر' and n != 'زيرو'): nn = n
        if n.startswith(u'و') and not num_phrases[i].startswith(u'واحد') and i>0: num += " و " + str(nn)
        else: num += str(nn)
    return num

if __name__ == '__main__':
    txt = "رفعت الجلسة يوم سبعتاشر من فبراير عشرين اتنين وعشرين بعد"
    # txt = "17"
    txt, _, wordlist, _ = prepare_txt(txt)
    day, month, year = extract_date(txt, wordlist)
    print(day, month, year)
