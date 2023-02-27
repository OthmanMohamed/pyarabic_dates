from __future__ import unicode_literals
# from datasets import tqdm
from tqdm import tqdm
import pyarabic.number
from pyarabic import araby
import re
import glob
import os

def preprocessing(text):
    lines = []
    for line in text:
        try:
            line = line.strip() 
            # remove old style retweet text "RT"
            line = re.sub(r'^RT[\s]+', '', line)
            # remove hyperlinks
            line = re.sub(r'https?:\/\/.*[\r\n]*', '', line)
            # remove hashtags
            # only removing the hash # sign from the word
            line = re.sub(r'#', '', line)
            #removing mentions
            line = re.sub(r':', '', line)
            line = re.sub(r'@[\w]+','',line)

            #replace punctuations with space
            line = re.sub(r"[,.;@?؟#!&$_]+\ *", " ", line)
            emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags=re.UNICODE)
            line  = emoji_pattern.sub(r'', line)
            line = line.replace('،',' ، ') 
            line = line.replace('؟ ', '') 
            line = line.replace('?', '')
            line = line.replace('%', '')
            line = line.replace('٪', '') 
            line = line.replace('^', '') 
            line = line.replace('$', '') 
            line = line.replace('|', '') 
            line = line.replace('*', '') 
            line = line.replace('+', '')
            line = line.replace('-', '')
            line = line.replace('؛', '')
            line = line.replace('!', '')
            line = line.replace('`', '')
            line = line.replace(':', '')
            line = line.replace(';', '')
            line = line.replace('~', '')
            line = line.replace('{', '')
            line = line.replace('}', '')
            line = line.replace('(', '') 
            line = line.replace(')', '') 
            line = line.replace('\\', '') 
            line = line.replace('[', '') 
            line = line.replace(']', '')

            #find arabic letters only
            line = ' '.join(re.findall(r'[*]|[\u0600-\u06FF]+|[\u0030-\u0039]+',line))
            #remove tashkeel
            line = araby.strip_tashkeel(line)

            #clean text
            line = re.sub(' +', ' ', line)
            if len(set(line.split())) > 2:
                # line = line + ' .'
                line = line + "\n"
                lines.append(line)
        except:
            continue
    # return set(lines)
    return lines

def process_file(f):
    out = ""
    in_f = open(f, 'r')
    in_d = in_f.readlines()
    in_f.close()
    in_d = preprocessing(in_d)
    new_in_d = []
    for d in in_d:
        new_in_d.extend(d.split('،'))
    in_d = new_in_d
    # in_d = [" من قيمة الأعمال المخالفة إذا كانت المخالفة لا تجاوز 200 ألف جنيه"]
    for line in in_d:
        processed = []
        words = line.split()

        for w in words:
            an = pyarabic.number.ArNumbers()
            try: ww = an.int2str(w)
            except: ww = " "
            if not "صفر" in ww: processed.append(ww)
            else: processed.append(w)
        if processed: out += " ".join(processed) + "\n"
    return out

def main():
    combined = ""
    # files = glob.glob("/home/o.mohamed/Downloads/legal_data/scrapped_books/*")
    files = glob.glob("/data/detect_dates/pyarabic_dates/*C4.txt")
    for f in files:
        try:
            out = process_file(f)
            combined += out
            # out_filename = os.path.join(os.path.dirname(f), "processed", os.path.basename(f)[:-4]+"_processed.txt")
            out_filename = os.path.join(os.path.dirname(f), os.path.basename(f)[:-4]+"_processed.txt")
            out_file = open(out_filename, 'w')
            out_file.write(out)
            out_file.close()
        except:
            print("ERROR ARISED IN FILE : ", f)
            # print(os.path.basename(f))
            # print(os.path.dirname(f))
    # out_filename = os.path.join(os.path.dirname(f), "processed", "combined.txt")
    # out_file = open(out_filename, 'w')
    # out_file.write(combined)
    # out_file.close()
    # process_file("/home/o.mohamed/Downloads/legal_data/scrapped_books/0.txt")

    words = ["حافظة", "توكيل", "أصل", "قسم", "دعوى"]
    words.extend(["الحافظة", "التوكيل", "القسم", "الدعوى"])
    global_counter = 0
    for w in words:
        counter = 0
        for l in tqdm(out.split('\n')):
            if w in l.split():
                counter += 1
                global_counter += 1
        print(f'{w}\t {counter}')
    print(global_counter)


if __name__ == '__main__':
    main()