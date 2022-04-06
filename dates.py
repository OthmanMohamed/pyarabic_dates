from pyarabic.number import extract_number_phrases
from pyarabic.number import detect_number_phrases_position
from pyarabic.number import text2number
from pyarabic.number_const import UNITS_ORDINAL_WORDS
from pyarabic import araby

MONTH_WORDS = {
    u'يناير': 1,
    u'فبراير': 2,
    u'مارس': 3,
    u'ابريل': 4,
    u'مايو': 5,
    u'يونيو': 6,
    u'يونيه': 6,
    u'يونية': 6,
    u'يوليو': 7,
    u'يولية': 7,
    u'يوليه': 7,
    u'اغسطس': 8,
    u'أغسطس': 8,
    u'سبتمبر': 9,
    u'اكتوبر': 10,
    u'نوفمبر': 11,
    u'ديسمبر': 12
}

def extract_date(text, wordlist):
    month_word_in_txt = 0
    if any(word in text for word in MONTH_WORDS):
        month_word_in_txt = 1
    num_phrases_pos = detect_number_phrases_position(wordlist)
    num_phrases = extract_number_phrases(text)
    month = -1
    day = -1
    year = -1
    for word in wordlist:
        if word in MONTH_WORDS:
            num_phrases.append(word)
    print(num_phrases)
    for n in num_phrases:
        print(n)
        nn = text2number(n)
        print(nn)
        if nn == 0:
            nn = MONTH_WORDS[n]
            month = nn 
        else:
            if day == -1: 
                day = nn
            else:
                year = nn
    return day, month, year

if __name__ == '__main__':
    txt = "رفعت الجلسة يوم سبعتاشر فبراير الفين وعشرين"
    wordlist = araby.tokenize(txt)
    inv_UNITS_ORDINAL_WORDS = {v: k for k, v in UNITS_ORDINAL_WORDS.items()}
    for i, word in enumerate(wordlist):
        if word in inv_UNITS_ORDINAL_WORDS:
            wordlist[i] = inv_UNITS_ORDINAL_WORDS[word]
            txt = txt.replace(word, wordlist[i])
        elif word.startswith(u'ال') and word[2:] in inv_UNITS_ORDINAL_WORDS:
            wordlist[i] = inv_UNITS_ORDINAL_WORDS[word[2:]]
            txt = txt.replace(word, wordlist[i])
    # print("WORDLIST : ", wordlist)
    day, month, year = extract_date(txt, wordlist)
    print(day, month, year)
    