from police_stations import police_stations
from number import text2number

tawkeel_wrong = ['تاكيد', 'توكيد', 'تأكيد']
asl_wrong = ["قصد", "قصر"]
da3wa_wrong = ["دعوة", "دعوا"]
hafza_wrong = ["محافظة"]
qesm_wrong = ["أسم", "اسم", "إسم"]

asl_suffix = ["الصحيفة", "المحضر", "المستند", "المستندات", "الاوراق", "الصحف", "المحاضر", "الدعوة", "الدعوى", "الدعوا"]
da3wa_suffix = ["اصلية", "فرعية", "عامة", "رقم"]
da3wa_prefix = ["اصل", "أصل", "طلب"]
hafza_prefix = ["قدم", "طلب الاطلاع على", "ضمن"]
hafza_suffix = ["مستندات"]

def process(txt):
    words = txt.split()
    processed_words = []
    for i in range(len(words)):
        if any (w in words[i] for w in tawkeel_wrong) and i+1<len(words) and (words[i+1]=="رقم" or text2number(words[i+1])>0):
            for w in tawkeel_wrong:
                if w in words[i]:
                    processed_words.append(words[i].replace(w, "توكيل"))
                    break
        elif any (w in words[i] for w in asl_wrong) and i+1<len(words) and any(w in words[i+1] for w in asl_suffix):
            for w in asl_wrong:
                if w in words[i]:
                    processed_words.append(words[i].replace(w, "أصل"))
                    break
        elif any (w in words[i] for w in da3wa_wrong) and i+1<len(words) and (any(w in words[i+1] for w in da3wa_suffix) or text2number(words[i+1])>0):
            for w in da3wa_wrong:
                if w in words[i]:
                    processed_words.append(words[i].replace(w, "دعوى"))
        elif any (w in words[i] for w in da3wa_wrong) and i-1>=0 and any(w in processed_words[i-1] for w in da3wa_prefix):
            for w in da3wa_wrong:
                if w in words[i]:
                    processed_words.append(words[i].replace(w, "دعوى"))
        elif any (w in words[i] for w in hafza_wrong)  and ((i+1<len(words)) and ( any(w in words[i+1] for w in hafza_suffix) or text2number(words[i+1])>0) or (i-1>=0 and any(w in processed_words[i-1] for w in hafza_prefix)) ):
            for w in hafza_wrong:
                if w in words[i]:
                    processed_words.append(words[i].replace(w, "حافظة"))
        elif any (w in words[i] for w in qesm_wrong) and (i+1<len(words) and (any(w in words[i+1] for w in police_stations))):
            for w in qesm_wrong:
                if w in words[i]:
                    processed_words.append(words[i].replace(w, "قسم"))
        else:
            processed_words.append(words[i])
    return ' '.join(processed_words)
        

def format_chunk(chunk):
    txts = []
    txts.extend(chunk.split('\n'))
    final_txts = []
    for txt in txts:
        new_txt = process(txt)
        final_txts.append(new_txt)
    return ('\n'.join(final_txts))