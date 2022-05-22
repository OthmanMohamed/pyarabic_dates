from date_utils import prepare_txt, get_separate_numbers, extract_date, get_dates
from time_utils import get_time, extract_time
from number import detect_number_phrases_position, text2number
import araby
from dates_const import DATE_FILL_WORDS, MONTH_WORDS, DAY_DEFINING_WORDS
import os   

def process_dates(txt):
    txt, wordlist = prepare_txt(txt)
    print("txt : ", txt)
    print("wordlist : ", wordlist)
    separate_numbers, new_wordlist, number_flag_list = get_separate_numbers(wordlist)
    print("new_wordlist : ", new_wordlist)
    date_sentences = get_dates(new_wordlist, number_flag_list)
    time_sentences = get_time(new_wordlist, number_flag_list)
    print("time_sentences : ", time_sentences)
    if date_sentences == ['']: date_sentences = []
    if time_sentences == ['']: time_sentences = []
    date_flag = 0
    time_flag = 0
    year_flag = 0
    for d in date_sentences:
        if d == '': continue
        new_d, d_wordlist = prepare_txt(d)
        day, month, year = extract_date(new_d, d_wordlist)
        if day == -1 or month == -1: continue
        if year != -1:
            date_flag = 1
            year_flag = 1
            txt = txt.replace(d, str(year) + "/" + str(month) + "/" + str(day))
        else:
            index = txt.find(d)
            if index == 0: continue
            tokenized = araby.tokenize(txt[:index])
            if tokenized[-1] in DAY_DEFINING_WORDS:
            # if 1:
                txt = txt.replace(d, str(month) + "/" + str(day))
                date_flag = 1
    for t in time_sentences:
        if t == '': continue
        new_t, t_wordlist = prepare_txt(t)
        hours, minutes = extract_time(new_t, t_wordlist)
        if hours == -1 or minutes == -1: continue
        else:
            time_flag = 1
            txt = txt.replace(t, f'{hours:02d}' + ":" + f'{minutes:02d}')
    return txt, date_flag, year_flag, time_flag

def main():
    txt = "  قبل اتنين وعشرين تسعة الفين وعشرة وحوالي تلات تيام تاريخ العاشر من يونيو عشرين واحد و عشرين الساعة العاشرة وخمس دقائق"
    new_txt, date_flag, year_flag, time_flag = process_dates(txt)
    if date_flag: print("TXT : " , txt, "\n", "NEW : ", new_txt, "\n\n\n")
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