from dates import prepare_txt, get_separate_numbers, extract_date
from pyarabic.number import detect_number_phrases_position, text2number
from dates_const import DATE_FILL_WORDS, MONTH_WORDS
import os


def number_flags(new_wordlist):
    flags_list = []
    for w in new_wordlist:
        if " " in w or detect_number_phrases_position([w]):
            flags_list.append(1)
        else:
            flags_list.append(0)
    return flags_list

def get_dates(new_wordlist, number_flag_list):
    state = "START"
    date_sentences = []
    date_sent = ""
    for i in range(len(new_wordlist)):
        # print(state)
        # print(new_wordlist[i])
        if state == "START":
            date_sent = ""
            if number_flag_list[i]==1 and text2number(new_wordlist[i]) <= 31:
                date_sent += new_wordlist[i]
                state = "DAY"
        elif state == "DAY":
            if number_flag_list[i]==0 and not (new_wordlist[i] in DATE_FILL_WORDS or new_wordlist[i] in MONTH_WORDS):
                state = "START"
            else:
                date_sent += " " + new_wordlist[i]
                if (number_flag_list[i]==1 and text2number(new_wordlist[i]) > 0 and text2number(new_wordlist[i]) <= 12) or new_wordlist[i] in MONTH_WORDS:
                    state = "MONTH"
        elif state == "MONTH":
            if number_flag_list[i]==0 and not new_wordlist[i] in DATE_FILL_WORDS:
                date_sentences.append(date_sent)
                state = "START"
            else:
                date_sent += " " + new_wordlist[i]
                if number_flag_list[i]==1:
                    if text2number(new_wordlist[i]) > 1000:
                        date_sentences.append(date_sent)
                        state = "START"
                    else:
                        state = "REPEATED NUMS"
        elif state == "REPEATED NUMS":
            date_sent = ""
            if number_flag_list[i]==0: state = "START"

    else:
        date_sentences.append(date_sent)
    return date_sentences
        

def process_dates(txt):
    txt, wordlist = prepare_txt(txt)
    separate_numbers, new_wordlist = get_separate_numbers(wordlist)
    # print(separate_numbers)
    number_flag_list = number_flags(new_wordlist)
    date_sentences = get_dates(new_wordlist, number_flag_list)
    if date_sentences == ['']: date_sentences = []
    date_flag = 0
    if date_sentences: date_flag = 1
    for d in date_sentences:
        if d == '': continue
        d, d_wordlist = prepare_txt(d)
        day, month, year = extract_date(d, d_wordlist)
        if year != -1:
            txt = txt.replace(d, str(day) + "/" + str(month) + "/" + str(year))
        else:
            txt = txt.replace(d, str(day) + "/" + str(month))
    return txt, date_flag

def main():
    # txt = "خمستاشر خمسه ألفين وخمستاشر محضر تحقيق إنه في يوم الأربعاء الموافق الثامن عشر من شهر نوفمبر لعام ألفين وعشرين من الميلاد"
    # new_txt, date_flag = process_dates(txt)
    # if date_flag: print("TXT : " , txt, "\n", "NEW : ", new_txt, "\n\n\n")
    directory = "/data/mahkama"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f.endswith(".txt"):
            f_o = open(f, 'r')
            txt = f_o.read()
            new_txt, date_flag = process_dates(txt)
            if date_flag: print("TXT : " , txt, "\n", "NEW : ", new_txt, "\n\n\n")


if __name__ == '__main__':
    main()