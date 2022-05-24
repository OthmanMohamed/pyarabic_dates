from date_utils import prepare_txt, get_separate_numbers, extract_date, get_dates, extract_repeated_numbers
from time_utils import get_time, extract_time
from number import detect_number_phrases_position, text2number
import araby
from dates_const import DATE_FILL_WORDS, MONTH_WORDS, DAY_DEFINING_WORDS
import os  

def process_dates(txt):
    txt, wordlist = prepare_txt(txt)
    # print("wordlist : ", wordlist)
    separate_numbers, new_wordlist, number_flag_list = get_separate_numbers(wordlist)
    # print("new_wordlist : ", new_wordlist, "\n\n\n")
    date_sentences, repeated_nums_flag, repeated_nums = get_dates(new_wordlist, number_flag_list)
    print(repeated_nums)
    time_sentences = get_time(new_wordlist, number_flag_list)
    if date_sentences == ['']: date_sentences = []
    if time_sentences == ['']: time_sentences = []
    if repeated_nums == ['']: repeated_nums = []
    date_flag = 0
    time_flag = 0
    year_flag = 0
    for d in date_sentences:
        if d == '': continue
        new_d, d_wordlist = prepare_txt(d)
        day, month, year = extract_date(new_d, d_wordlist)
        if day == -1 and month == -1 and year == -1: continue
        if year != -1:
            date_flag = 1
            year_flag = 1
            if month != -1 and day != -1:
                txt = txt.replace(d, str(year) + "/" + str(month) + "/" + str(day))
            else:
                txt = txt.replace(d, str(year))
        elif day != -1 or month != -1:
            index = txt.find(d)
            if index == 0: continue
            tokenized = araby.tokenize(txt[:index])
            print(tokenized)
            if tokenized[-1] in DAY_DEFINING_WORDS:
                txt = txt.replace(d, str(month) + "/" + str(day))
                date_flag = 1
    for r in repeated_nums:
        if r == '': continue
        new_r, r_wordlist = prepare_txt(r)
        num = extract_repeated_numbers(new_r, r_wordlist)
        txt = txt.replace(r, num)
    for t in time_sentences:
        if t == '': continue
        new_t, t_wordlist = prepare_txt(t)
        hours, minutes = extract_time(new_t, t_wordlist)
        if hours == -1 or minutes == -1: continue
        else:
            time_flag = 1
            txt = txt.replace(t, f'{int(hours):02d}' + ":" + f'{int(minutes):02d}')
    return txt, date_flag, year_flag, time_flag, repeated_nums_flag

def main():
    # txt = "  قبل اتنين وعشرين تسعة الفين وعشرة الساعة تمانية ونص مساء وحوالي تلات تيام تاريخ العاشر من يونيو عشرين واحد و عشرين الساعة العاشرة وخمس دقائق"
    txt = "بطاقة تحقيق شخصية رقم اتنين تمانية سبعة صفر واحد اتنين تسعة اتنين سبعة صفر صفر صفر تلاتة واحد "
    new_txt, date_flag, year_flag, time_flag, repeated_nums_flag = process_dates(txt)
    if date_flag or time_flag or repeated_nums_flag: print("TXT : " , txt, "\n", "NEW : ", new_txt, "\n\n\n")
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