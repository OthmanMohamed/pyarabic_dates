from number import text2number
from date_utils import get_separate_numbers

separators = ["على", "علي", "فصلة"]
separators_dict = {"على" : "/", "علي" : "/" , "فصلة" : ","}

def get_herz(new_wordlist, number_flag_list):
    state = "START"
    herz_sentences = []
    herz_sent = ""
    separator_flag = 0
    for i in range(len(new_wordlist)):
        if state == "START":
            herz_sent = ""
            if number_flag_list[i] == 1:
                herz_sent += " " + new_wordlist[i]
                state = "NUM"
            else:
                state = "START"
        elif state == "NUM":
            if new_wordlist[i] in separators:
                herz_sent += " " + new_wordlist[i]
                separator_flag = 1
                state = "SEPEARATOR"
            elif number_flag_list[i] == 1:
                herz_sent += " " + new_wordlist[i]
                state = "NUM"
            else:
                if separator_flag: herz_sentences.append(herz_sent)
                herz_sent = 0
                state = "START"
        elif state == "SEPEARATOR":
            if new_wordlist[i] in separators and new_wordlist[i] == new_wordlist[i-1]:
                herz_sent += " " + new_wordlist[i]
                state = "SEPARATOR"
            elif number_flag_list[i] == 1:
                herz_sent += " " + new_wordlist[i]
                state = "NUM"
            else:
                state = "START"
    else:
        if state == "NUM" and separator_flag: herz_sentences.append(herz_sent)
    return herz_sentences

def extract_herz(text, wordlist):
    txt = ""
    if any(s in text for s in separators):
        txt = text
        separate_numbers, *_ = get_separate_numbers(wordlist)
        for num in separate_numbers:
            txt = txt.replace(num, str(text2number(num)))
        for s in separators:
            txt = txt.replace(s, separators_dict[s])
    return txt.replace(" ", "")