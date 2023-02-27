from date_utils import get_separate_repeated_numbers, prepare_txt, get_separate_numbers, extract_date, get_dates, extract_repeated_numbers, get_special_sessions_number, get_repeated_nums
from time_utils import get_time, extract_time
from herz_utils import get_herz, extract_herz
from number import detect_number_phrases_position, text2number
from process_special_words import process as process_special_words
import araby
from dates_const import DATE_FILL_WORDS, MONTH_WORDS, DAY_DEFINING_WORDS
import re
import sys

def add_pattern_brackets(original_txt, pattern, index):
    split_txt = original_txt.split()
    check_index = min(len(split_txt)-1, index)
    if split_txt[check_index] != '(' + pattern + ')':
        final_txt = " ".join(split_txt[:index]) + ' (' + pattern + ') ' + " ".join(split_txt[index:])
    else:
        final_txt = original_txt
    return final_txt


def process_dates(txt):
    txt, original_txt, wordlist, original_wordlist = prepare_txt(txt)
    _, new_wordlist, new_original_wordlist, number_flag_list = get_separate_numbers(wordlist, original_wordlist)
    date_sentences, dates_flags_list, _ = get_dates(new_wordlist, number_flag_list, [0] * len(new_wordlist))
    sessions_sentences, special_session_flag_list, end_sessionds_indices = get_special_sessions_number(new_wordlist, number_flag_list, dates_flags_list)
    date_sentences, dates_flags_list, end_dates_indices = get_dates(new_wordlist, number_flag_list, special_session_flag_list)
    time_sentences, times_flags_list, end_times_indices = get_time(new_wordlist, number_flag_list)
    # herz_sentences = get_herz(new_wordlist, number_flag_list)
    # repeated_nums, repeated_nums_flag, end_nums_indices = get_repeated_nums(new_wordlist, number_flag_list, dates_flags_list, times_flags_list)
    repeated_nums, repeated_nums_flag, end_nums_indices = get_separate_repeated_numbers(new_wordlist, number_flag_list)

    #TO BE REMOVED
    time_sentences = ['']

    if date_sentences == ['']: date_sentences = []  
    if time_sentences == ['']: time_sentences = []
    if repeated_nums  == ['']: repeated_nums = []
    # if herz_sentences == ['']: herz_sentences = []
    date_flag = 0
    time_flag = 0
    year_flag = 0
    
    for i, t in enumerate(time_sentences):
        if t == '': continue
        new_t, _, t_wordlist, _ = prepare_txt(t)
        hours, minutes = extract_time(new_t, t_wordlist)
        if hours == -1 or minutes == -1: continue
        else:
            time_flag = 1
            brack_pattern = ' (' + f'{int(hours):02d}' + ":" + f'{int(minutes):02d})'
            if (end_times_indices[i]+1 < len(new_original_wordlist) and new_original_wordlist[end_times_indices[i]+1].strip() != brack_pattern.strip()) or end_times_indices[i]+1 == len(new_original_wordlist):
                new_original_wordlist[end_times_indices[i]] = new_original_wordlist[end_times_indices[i]] + brack_pattern
    
    for j, d in enumerate(date_sentences):
        if d == '': continue
        new_d, _, d_wordlist, _ = prepare_txt(d)
        day, month, year = extract_date(new_d, d_wordlist)
        if day == -1 and month == -1 and year == -1: continue
        if year != -1:
            date_flag = 1
            year_flag = 1
            if month != -1 and day != -1:
                brack_pattern = ' (' + str(year) + "/" + str(month) + "/" + str(day) + ')'
                if (end_dates_indices[j]+1 < len(new_original_wordlist) and new_original_wordlist[end_dates_indices[j]+1].strip() != brack_pattern.strip()) or end_dates_indices[j]+1 == len(new_original_wordlist):
                    new_original_wordlist[end_dates_indices[j]] = new_original_wordlist[end_dates_indices[j]] + brack_pattern
            else:
                brack_pattern = ' (' + str(year) + ')'
                if (end_dates_indices[j]+1 < len(new_original_wordlist) and new_original_wordlist[end_dates_indices[j]+1].strip() != brack_pattern.strip()) or end_dates_indices[j]+1 == len(new_original_wordlist):
                    new_original_wordlist[end_dates_indices[j]] = new_original_wordlist[end_dates_indices[j]] + brack_pattern
        elif day != -1 and month != -1:
            date_flag = 1
            brack_pattern = ' (' + str(month) + "/" + str(day) + ')'
            if (end_dates_indices[j]+1 < len(new_original_wordlist) and new_original_wordlist[end_dates_indices[j]+1].strip() != brack_pattern.strip()) or end_dates_indices[j]+1 == len(new_original_wordlist):
                new_original_wordlist[end_dates_indices[j]] = new_original_wordlist[end_dates_indices[j]] + brack_pattern
        #     index = txt.find(d)
        #     for i, w in enumerate(txt.split()):
        #         if w == d.split()[0]:
        #             flag = 1
        #             j = i
        #             while j<len(txt.split()) and j-i < len(d.split()):
        #                 if txt.split()[j] != d.split()[j-i]: flag = 0
        #                 j += 1
        #             if flag == 1: end_pattern_index = i + len(d.split())
        #     if index == 0: continue
        #     tokenized = araby.tokenize(txt[:index])
        #     if tokenized[-1] in DAY_DEFINING_WORDS:
        #         txt = add_pattern_brackets(txt, str(month) + "/" + str(day), end_pattern_index)
        #         original_txt = add_pattern_brackets(original_txt, str(month) + "/" + str(day), end_pattern_index)
        #         date_flag = 1

    for i, r in enumerate(repeated_nums):
        if r == '': continue
        if any(r in string for string in time_sentences): continue
        new_r, _, r_wordlist, _ = prepare_txt(r)
        num = extract_repeated_numbers(new_r, r_wordlist)
        if end_nums_indices[i] >= 0: 
            brack_pattern = ' (' + num + ')'
            if (end_nums_indices[i]+1 < len(new_original_wordlist) and new_original_wordlist[end_nums_indices[i]+1].strip() != brack_pattern.split()) or end_nums_indices[i]+1 == len(new_original_wordlist):
                new_original_wordlist[end_nums_indices[i]] = new_original_wordlist[end_nums_indices[i]] + brack_pattern
            # original_txt = ' '.join(new_original_wordlist)
    
    original_txt = ' '.join(new_original_wordlist)
    return original_txt, date_flag, year_flag, time_flag

def prepare_input(txt):
    return_txts = []
    temp_t = ""
    for i, t in enumerate(txt):
        if not t.strip():
            if i+1<len(txt) and (not txt[i+1].strip()):
                continue
            else: 
                if temp_t:
                    return_txts.append(temp_t)
                    temp_t = ""
                return_txts.append(t)
        else:
            temp_t += " " + t
    else: 
        if temp_t:
            return_txts.append(temp_t)
            temp_t = ""
    return return_txts

def format_chunk(chunk, process_nums = 1, process_boost_words = 1):
    txts = []
    txts.extend(chunk.split('\n'))
    txts = prepare_input(txts)
    final_txts = []
    for txt in txts:
        if process_boost_words == '1':
            new_txt = process_special_words(txt)
        else: new_txt = txt
        if process_nums == '1':
            new_txt, date_flag, year_flag, time_flag = process_dates(new_txt) 
        final_txts.append(new_txt)
    return ('\n'.join(final_txts))

def main():
    txts = []
    # file_path = "/data/detect_dates/pyarabic_dates/test/nyaba_sample.txt"
    # file_path = "/data/detect_dates/pyarabic_dates/test/dummy_test.txt"
    # file_path = "/data/Zenhom_demo_files/demo_files/combined.txt"
    file_path = sys.argv[1]
    process_nums, process_boost_words = [sys.argv[2], sys.argv[3]]
    f = open(file_path, encoding='utf-8')
    t = f.read()
    f.close()
    txts.extend(t.split('\n'))
    # txts = ['حضر الاستاذ بتوكيد رقم خمسة اتنين سبعة عشرة وطلب قصر الدعوة']
    # txts = ["بتاريخ خمسة تمانية الف تسعمية اتنين وستين"]
    # txts = ['ورقم اتنين تسعة سبعة خمسة حداشر مية وعشرين سبعة']
    # txts = ['حضر الاستاذ محمد عيد عن المدعي بتوكيل رقم الف مية تمانية وتسعين الف عشرين اتنين وعشرين ورقم مليون وميتين الف وخمسة ثم رقم الف ميتين ستة وسبعين ورقم اتنين تسعة سبعة خمسة حداشر مية وعشرين سبعة']
    # txts = ['حضر الاستاذ محمد عيد عن المدعي بتوكيل رقم الف تلتمية تمانية وتسعين الف عشرين اتنين وعشرين ']
    # txts = ['الساعه تلاته ونص']
    # txts = prepare_input(txts)

    final_txts = []
    for txt in txts:
        # new_txt, date_flag, year_flag, time_flag = process_dates(txt)
        new_txt = format_chunk(txt, process_nums, process_boost_words)
        print(new_txt)
        final_txts.append(new_txt)
    f = open("test/test_out.txt", 'w', encoding='utf-8')
    f.write('\n'.join(final_txts))
    f.close()


if __name__ == '__main__':
    main()