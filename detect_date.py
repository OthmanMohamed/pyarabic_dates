from date_utils import prepare_txt, get_separate_numbers, extract_date, get_dates
from number import detect_number_phrases_position, text2number
import araby
from dates_const import DATE_FILL_WORDS, MONTH_WORDS, DAY_DEFINING_WORDS
import os   

def process_dates(txt):
    txt, wordlist = prepare_txt(txt)
    separate_numbers, new_wordlist, number_flag_list = get_separate_numbers(wordlist)
    date_sentences = get_dates(new_wordlist, number_flag_list)
    if date_sentences == ['']: date_sentences = []
    date_flag = 0
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
    return txt, date_flag, year_flag

def main():
    txt = "  قبل اتنين تسعة الفين وعشرة وحوالي تلات تيام تاريخ العاشر من يونيو عشرين واحد وعشرين الساعة العاشرة وخمس دقائق"
    new_txt, date_flag, year_flag = process_dates(txt)
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