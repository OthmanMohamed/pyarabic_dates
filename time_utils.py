from dates_const import TIME_TRIGGERS

def extract_time(text, wordlist):
    separate_numbers, *_ = get_separate_numbers(wordlist)
    num_phrases = separate_numbers
    hours = -1
    minutes = -1
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
            if new_wordlist[i] in TIME_TRIGGERS:
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