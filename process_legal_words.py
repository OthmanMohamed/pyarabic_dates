from tqdm import tqdm

words = ["حافظة", "توكيل", "أصل", "قسم", "دعوى"]
words.extend(["الحافظة", "التوكيل", "القسم", "الدعوى"])

f = open("/home/o.mohamed/Downloads/sample_asr_words3_list.txt", "r")
lines = f.readlines()
f.close()

splitted_lines = []
for l in tqdm(lines):
    l = l.replace(',', '.')
    l = l.replace(';', '.')
    l = l.replace('-', '.')
    l = l.replace(',', '.')
    l = l.replace('–', '.')
    l = l.replace(',','،') 
    l = l.replace('؟ ', '.') 
    l = l.replace('?', '.')
    l = l.replace('%', '.')
    l = l.replace('٪', '.') 
    l = l.replace('^', '.') 
    l = l.replace('$', '.') 
    l = l.replace('|', '.') 
    l = l.replace('*', '.') 
    l = l.replace('+', '.')
    l = l.replace('-', '.')
    l = l.replace('؛', '.')
    l = l.replace('!', '.')
    l = l.replace('`', '.')
    l = l.replace(':', '.')
    l = l.replace(';', '.')
    l = l.replace('~', '.')
    l = l.replace('{', '.')
    l = l.replace('}', '.')
    l = l.replace('(', '.') 
    l = l.replace(')', '.') 
    l = l.replace('\\', '.') 
    l = l.replace('[', '.') 
    l = l.replace(']', '.')
    l = l.replace('،', '.')
    l = l.replace('؟', '.')
    l = l.replace('"', '.')
    l = l.replace("'", '.')
    splitted_lines.extend(l.split('.'))

splitted_sentences_filtered = []
for l in tqdm(splitted_lines):
    if any(word in l.split()  for word in words) and not "منشور في قسم" in l:
        splitted_sentences_filtered.append((l + '\n'))

print(len(splitted_sentences_filtered))
f = open("legal_words_C4.txt", "w")
f.writelines(splitted_sentences_filtered)
f.close()