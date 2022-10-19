from dates_const import TIME_TRIGGERS, TIME_TERMINATING
from number_const import TIME_FRACTIONS
from number import text2number
from date_utils import get_separate_numbers

def extract_time(text, wordlist):
    hours = -1
    minutes = -1
    fraction_in_txt = 0
    if any(word in text for word in TIME_FRACTIONS):
        fraction_in_txt = 1
    if fraction_in_txt:
        for i, w in enumerate(wordlist):
            if w in TIME_FRACTIONS.keys():
                minutes = text2number(TIME_FRACTIONS[w])
            elif (w.startswith('و') and w[1:] in TIME_FRACTIONS.keys()):
                minutes = text2number(TIME_FRACTIONS[w[1:]])
    separate_numbers, *_ = get_separate_numbers(wordlist, wordlist)
    num_phrases = separate_numbers
    for n in num_phrases:
        nn = text2number(n)
        if nn==0: nn = n
        if hours == -1:
            hours = nn
        elif minutes == -1:
            minutes = nn
        else:
            minutes = int(minutes) + int(nn)
    else:
        if minutes == -1: 
            if hours >= 20:
                combined = hours
                hours = combined%10
                minutes = combined - hours
            else:
                minutes = 0
    return hours, minutes


def get_time(new_wordlist, number_flag_list):
    state = "START"
    time_sentences = []
    time_sent = ""
    times_flags_list = [0] * len(new_wordlist)
    for i in range(len(new_wordlist)):
        # if special_session_flag_list[i] == 1: continue
        # print(i)
        # print(state)
        # print(text2number(new_wordlist[i]))
        # print(text2number(new_wordlist[i]) <= 24 and text2number(new_wordlist[i]) > 0)
        # print(new_wordlist[i], '\n\n\n\n')
        if new_wordlist[i] in TIME_TRIGGERS:
            state = "TIME TRIGGERED"
        elif state == "TIME TRIGGERED":
            times_indices = []
            time_sent = ""
            # if text2number(new_wordlist[i]) <= 24 and text2number(new_wordlist[i]) > 0:
            if text2number(new_wordlist[i]) <= 60 and text2number(new_wordlist[i]) > 0:
                time_sent += new_wordlist[i]
                times_indices.append(i)
                state = "HOUR"
            else:
                state = "START"
        elif state == "HOUR":
            if new_wordlist[i] in TIME_TERMINATING:
                time_sent += " " + new_wordlist[i]
                times_indices.append(i)
                if i+1 < len(number_flag_list) and number_flag_list[i+1] == 0:
                    time_sentences.append(time_sent)
                    for t_i in times_indices:
                        times_flags_list[t_i] = 1
                    state = "START"
                elif i+1 < len(number_flag_list) and number_flag_list[i+1] == 1 and new_wordlist[i+1].startswith('و') and text2number(new_wordlist[i+1]) > 0 and text2number(new_wordlist[i+1]) < 60:
                    time_sent += " " + new_wordlist[i]
                    times_indices.append(i)
                    state = "MINUTE"
                elif i+1 < len(number_flag_list) and new_wordlist[i+1].startswith('و') and new_wordlist[i+1][1:] in TIME_FRACTIONS.keys():
                    time_sent += " " + new_wordlist[i]
                    times_indices.append(i)
                    state = "MINUTE"
            elif (number_flag_list[i] == 1 and text2number(new_wordlist[i]) > 0 and text2number(new_wordlist[i]) < 60) or new_wordlist[i][1:] in TIME_FRACTIONS.keys():
                time_sent += " " + new_wordlist[i]
                times_indices.append(i)
                state = "MINUTE"
            elif i+1 < len(number_flag_list) and number_flag_list[i+1] == 0:
                time_sentences.append(time_sent)
                for t_i in times_indices:
                    times_flags_list[t_i] = 1
                state = "START"
        elif state == "MINUTE":
            if new_wordlist[i] in TIME_TERMINATING:
                time_sent += " " + new_wordlist[i]
                times_indices.append(i)
                time_sentences.append(time_sent)
                for t_i in times_indices:
                    times_flags_list[t_i] = 1
                state = "START"
            elif number_flag_list[i] == 0 and not new_wordlist[i][1:] in TIME_FRACTIONS.keys():
                time_sentences.append(time_sent)
                for t_i in times_indices:
                    times_flags_list[t_i] = 1
                state = "START"
    else:
        if state == "HOUR" or state == "MINUTE":
            time_sentences.append(time_sent)
            for t_i in times_indices:
                times_flags_list[t_i] = 1
            
    return time_sentences, times_flags_list