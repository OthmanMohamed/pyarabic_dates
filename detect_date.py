from dates import prepare_txt, get_separate_numbers
from pyarabic.number import detect_number_phrases_position, text2number
from dates_const import DATE_FILL_WORDS

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
    for i in range(len(new_wordlist)):
        if state == "START":
            date_sent = ""
            if number_flag_list[i]==1 and text2number(new_wordlist[i]) <= 31:
                date_sent += new_wordlist[i]
                state = "DAY"
        elif state == "DAY":
            if number_flag_list[i]==0 and not new_wordlist[i] in DATE_FILL_WORDS:
                state = "START"
            else:
                date_sent += " " + new_wordlist[i]
                print(date_sent)
                if number_flag_list[i]==1 and text2number(new_wordlist[i]) > 0 and text2number(new_wordlist[i]) <= 12:
                    state = "MONTH"
        elif state == "MONTH":
            if number_flag_list[i]==0 and not new_wordlist[i] in DATE_FILL_WORDS:
                date_sentences.append(date_sent)
                state = "START"
            else:
                date_sent += " " + new_wordlist[i]
                if number_flag_list[i]==1:
                    date_sentences.append(date_sent)
                    state = "START"
    else:
        date_sentences.append(date_sent)
    return date_sentences
        

def main():
    txt = "روحت امبارح انا وخمسة اصحابي جيبنا اربعين حاجة وده كان يوم خمسة وعشرين من شهر اتناشر الفين وواحد بعدين مشينا عدينا على اتنين صحابنا ورجعنا ذكريات تمانتاشر سبعة"
    txt, wordlist = prepare_txt(txt)
    separate_numbers, new_wordlist = get_separate_numbers(wordlist)
    number_flag_list = number_flags(new_wordlist)
    date_sentences = get_dates(new_wordlist, number_flag_list)
    print(date_sentences)


if __name__ == '__main__':
    main()