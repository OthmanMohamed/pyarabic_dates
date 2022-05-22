from dates_const import TIME_TRIGGERS, TIME_TERMINATING
from number_const import TIME_FRACTIONS
from number import text2number
from date_utils import get_separate_numbers

def extract_time(text, wordlist):
    for i, w in enumerate(wordlist):
        if w in TIME_FRACTIONS.keys():
            wordlist[i] = TIME_FRACTIONS[w]
        elif (w.startswith('و') and w[1:] in TIME_FRACTIONS.keys()):
            wordlist[i] = 'و' + TIME_FRACTIONS[w[1:]]
    print(wordlist)
    separate_numbers, *_ = get_separate_numbers(wordlist)
    print(separate_numbers)
    num_phrases = separate_numbers
    hours = -1
    minutes = -1
    for n in num_phrases:
        nn = text2number(n)
        if nn==0: nn = n
        if hours == -1:
            hours = nn
        elif minutes == -1:
            minutes = nn
    else:
        if minutes == -1: minutes = 0
    return hours, minutes


def get_time(new_wordlist, number_flag_list):
    state = "START"
    time_sentences = []
    time_sent = ""
    for i in range(len(new_wordlist)):
        # print(i)
        # print(state)
        # print(new_wordlist[i], '\n\n\n\n')
        if state == "START":
            if new_wordlist[i] in TIME_TRIGGERS:
                state = "TIME TRIGGERED"
        elif state == "TIME TRIGGERED":
            time_sent = ""
            if text2number(new_wordlist[i]) <= 24 and text2number(new_wordlist[i]) > 0:
                time_sent += new_wordlist[i]
                state = "HOUR"
            else:
                state = "START"
        elif state == "HOUR":
            if new_wordlist[i] in TIME_TERMINATING:
                time_sent += " " + new_wordlist[i]
                if i+1 < len(number_flag_list) and number_flag_list[i+1] == 0:
                    time_sentences.append(time_sent)
                    state = "START"
                elif i+1 < len(number_flag_list) and number_flag_list[i+1] == 1 and new_wordlist[i+1].startswith('و') and text2number(new_wordlist[i+1]) > 0 and text2number(new_wordlist[i+1]) < 60:
                    time_sent += " " + new_wordlist[i]
                    state = "MINUTE"
                elif i+1 < len(number_flag_list) and new_wordlist[i+1].startswith('و') and new_wordlist[i+1][1:] in TIME_FRACTIONS.keys():
                    time_sent += " " + new_wordlist[i]
                    state = "MINUTE"
            elif (number_flag_list[i] == 1 and text2number(new_wordlist[i]) > 0 and text2number(new_wordlist[i]) < 60) or new_wordlist[i][1:] in TIME_FRACTIONS.keys():
                time_sent += " " + new_wordlist[i]
                state = "MINUTE"
            elif i+1 < len(number_flag_list) and number_flag_list[i+1] == 0:
                time_sentences.append(time_sent)
                state = "START"
        elif state == "MINUTE":
            if new_wordlist[i] in TIME_TERMINATING:
                time_sent += " " + new_wordlist[i]
                time_sentences.append(time_sent)
                state = "START"
            elif number_flag_list[i] == 0 and not number_flag_list[i][1:] in TIME_FRACTIONS.keys():
                time_sentences.append(time_sent)
                state = "START"
    else:
        if state == "HOUR" or state == "MINUTE":
            time_sentences.append(time_sent)
    return time_sentences