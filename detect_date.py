from date_utils import prepare_txt, get_separate_numbers, extract_date, get_dates, extract_repeated_numbers
from time_utils import get_time, extract_time
from herz_utils import get_herz, extract_herz
from number import detect_number_phrases_position, text2number
import araby
from dates_const import DATE_FILL_WORDS, MONTH_WORDS, DAY_DEFINING_WORDS
import os  
import re

def add_pattern_brackets(original_txt, pattern, index):
    split_txt = original_txt.split()
    check_index = min(len(split_txt)-1, index)
    if split_txt[check_index] != '(' + pattern + ')':
        final_txt = " ".join(split_txt[:index]) + ' (' + pattern + ') ' + " ".join(split_txt[index:])
    else:
        final_txt = original_txt
    return final_txt


def process_dates(txt):
    # REPLACE و WITH SPACES
    txt = txt.replace(u' و ', u' و')
    brack_txt = txt
    txt, wordlist = prepare_txt(txt)
    # print("wordlist : ", wordlist)
    _, new_wordlist, number_flag_list = get_separate_numbers(wordlist)
    # print(separate_numbers)
    # print("new_wordlist : ", new_wordlist, "\n\n\n")
    date_sentences, repeated_nums_flag, repeated_nums = get_dates(new_wordlist, number_flag_list)
    time_sentences = get_time(new_wordlist, number_flag_list)
    herz_sentences = get_herz(new_wordlist, number_flag_list)
    if date_sentences == ['']: date_sentences = []
    if time_sentences == ['']: time_sentences = []
    if repeated_nums == ['']: repeated_nums = []
    if herz_sentences == ['']: herz_sentences = []
    date_flag = 0
    time_flag = 0
    year_flag = 0
    for h in herz_sentences:
        if h == '': continue
        new_h, h_wordlist = prepare_txt(h)
        herz_sent = extract_herz(new_h, h_wordlist)
        for i, w in enumerate(txt.split()):
                if w == h.split()[0]:
                    flag = 1
                    j = i
                    while j<len(txt.split()) and j-i < len(h.split()):
                        if txt.split()[j] != h.split()[j-i]: flag = 0
                        j += 1
                    if flag == 1: end_pattern_index = i + len(h.split())
                    break
        brack_txt = add_pattern_brackets(brack_txt, herz_sent, end_pattern_index)
        txt = add_pattern_brackets(txt, herz_sent, end_pattern_index)
    for t in time_sentences:
        if t == '': continue
        new_t, t_wordlist = prepare_txt(t)
        hours, minutes = extract_time(new_t, t_wordlist)
        if hours == -1 or minutes == -1: continue
        else:
            time_flag = 1
            for i, w in enumerate(txt.split()):
                if w == t.split()[0]:
                    flag = 1
                    j = i
                    while j<len(txt.split()) and j-i < len(t.split()):
                        if txt.split()[j] != t.split()[j-i]: flag = 0
                        j += 1
                    if flag == 1: end_pattern_index = i + len(t.split())
            brack_txt = add_pattern_brackets(brack_txt, f'{int(hours):02d}' + ":" + f'{int(minutes):02d}' , end_pattern_index)
            txt = add_pattern_brackets(txt, f'{int(hours):02d}' + ":" + f'{int(minutes):02d}' , end_pattern_index)
            # txt = txt.replace(t, f'{int(hours):02d}' + ":" + f'{int(minutes):02d}')
    for d in date_sentences:
        if d == '': continue
        new_d, d_wordlist = prepare_txt(d)
        day, month, year = extract_date(new_d, d_wordlist)
        if day == -1 and month == -1 and year == -1: continue
        if year != -1:
            date_flag = 1
            year_flag = 1
            for i, w in enumerate(txt.split()):
                if w == d.split()[0]:
                    flag = 1
                    j = i
                    while j<len(txt.split()) and j-i < len(d.split()):
                        if txt.split()[j] != d.split()[j-i]: flag = 0
                        j += 1
                    if flag == 1: end_pattern_index = i + len(d.split())
            if month != -1 and day != -1:
                brack_txt = add_pattern_brackets(brack_txt, str(year) + "/" + str(month) + "/" + str(day), end_pattern_index)
                txt = add_pattern_brackets(txt, str(year) + "/" + str(month) + "/" + str(day), end_pattern_index)
                # txt = txt.replace(d, str(year) + "/" + str(month) + "/" + str(day))
            else:
                brack_txt = add_pattern_brackets(brack_txt, str(year), end_pattern_index)
                txt = add_pattern_brackets(txt, str(year), end_pattern_index)
                # txt = txt.replace(d, str(year))
        elif day != -1 and month != -1:
            index = txt.find(d)
            for i, w in enumerate(txt.split()):
                if w == d.split()[0]:
                    flag = 1
                    j = i
                    while j<len(txt.split()) and j-i < len(d.split()):
                        if txt.split()[j] != d.split()[j-i]: flag = 0
                        j += 1
                    if flag == 1: end_pattern_index = i + len(d.split())
            if index == 0: continue
            tokenized = araby.tokenize(txt[:index])
            if tokenized[-1] in DAY_DEFINING_WORDS:
                brack_txt = add_pattern_brackets(brack_txt, str(month) + "/" + str(day), end_pattern_index)
                txt = add_pattern_brackets(txt, str(month) + "/" + str(day), end_pattern_index)
                # txt = txt.replace(d, str(month) + "/" + str(day))
                date_flag = 1
    for r in repeated_nums:
        if r == '': continue
        if any(r in string for string in time_sentences): continue
        end_pattern_index = -1
        for i, w in enumerate(txt.split()):
                if w == r.split()[0]:
                    flag = 1
                    j = i
                    while j<len(txt.split()) and j-i < len(r.split()):
                        if txt.split()[j] != r.split()[j-i]: flag = 0
                        j += 1
                    if flag == 1: end_pattern_index = i + len(r.split())
                    break
        new_r, r_wordlist = prepare_txt(r)
        num = extract_repeated_numbers(new_r, r_wordlist)
        if end_pattern_index >= 0: brack_txt = add_pattern_brackets(brack_txt, num, end_pattern_index)
        txt = add_pattern_brackets(txt, num, end_pattern_index)
        # txt = txt.replace(r, num)
    txt = re.sub(r'(\d)\s+(\d)', r'\1\2', txt)
    return brack_txt, date_flag, year_flag, time_flag, repeated_nums_flag, txt

def main():
    txts = []
    txts.append( "  قبل اتنين وعشرين تسعة الفين وعشرة الساعة تمانية ونص مساء وحوالي تلات تيام تاريخ العاشر من يونيو عشرين واحد و عشرين الساعة العاشرة وخمس دقائق" )
    txts.append( "رقم القيد خمسمية سبعة وسبعين الف ستمية اتنين وخمسين " )
    txts.append( "قرار الاخضاع رقم تسعة واربعين (49) لسنة الفين وستاشر (2016)" )
    txts.append("المؤرخ في تلاتة وعشرين ستة الفين واحد وعشرين ورقم صادر عشرين واحد وعشرين اربعتاشر سبعة واحد صفر صفر صفر حداشر واحد وستين المكون من اتنين صفحات ")

    for txt in txts:
        new_txt, date_flag, year_flag, time_flag, repeated_nums_flag, brack_txt = process_dates(txt)
        if date_flag or time_flag or repeated_nums_flag: print("TXT : " , txt, "\n", "NEW : ", new_txt, "\n\n\n")
        if date_flag or time_flag or repeated_nums_flag: print("TXT : " , txt, "\n", "NEW : ", brack_txt, "\n\n\n")
    # directory = "/data/mahkama"
    # for filename in os.listdir(directory):
    #     f = os.path.join(directory, filename)
    #     if f.endswith(".txt"):
    #         f_o = open(f, 'r')
    #         txt = f_o.read()
    #         new_txt, date_flag, year_flag = process_dates(txt)
    #         if date_flag : print("TXT : " , txt, "\n", "NEW : ", new_txt, "\n\n\n")


if __name__ == '__main__':
    main()