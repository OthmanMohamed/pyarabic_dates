from date_utils import prepare_txt, get_separate_numbers, extract_date, get_dates, extract_repeated_numbers, get_special_sessions_number, get_repeated_nums
from time_utils import get_time, extract_time
from herz_utils import get_herz, extract_herz
from number import detect_number_phrases_position, text2number
import araby 
from dates_const import DATE_FILL_WORDS, MONTH_WORDS, DAY_DEFINING_WORDS
import re
import sys

def add_pattern_brackets(original_txt, pattern, index):
    split_txt = original_txt.split()
    check_index = min(len(split_txt)-1, index)
    if split_txt[check_index] != '(' + pattern + ')':
        final_txt = " ".join(split_txt[:index]) + ' (' + pattern + ') ' + " ".join(split_txt[index:])
    else:
        final_txt = original_txt
    return final_txt


def process_dates(txt):
    txt, original_txt, wordlist, original_wordlist = prepare_txt(txt)
    # brack_txt = txt
    _, new_wordlist, new_original_wordlist, number_flag_list = get_separate_numbers(wordlist, original_wordlist)
    date_sentences, dates_flags_list, _ = get_dates(new_wordlist, number_flag_list, [0] * len(new_wordlist))
    sessions_sentences, special_session_flag_list, end_sessionds_indices = get_special_sessions_number(new_wordlist, number_flag_list, dates_flags_list)
    #TO BE REMOVED, BUT NEED FIRST TO HANDLE CASES LIKE 'تم فتح المحضر ثلاثة عشر (13) من يناير عام الفين اثنان وعشرين (2022)'
    # special_session_flag_list = [0] * len(number_flag_list)
    date_sentences, dates_flags_list, end_dates_indices = get_dates(new_wordlist, number_flag_list, special_session_flag_list)
    # repeated_nums, repeated_nums_flag = get_repeated_nums(new_wordlist, number_flag_list, dates_flags_list)
    # time_sentences = get_time(new_wordlist, number_flag_list, special_session_flag_list)
    # herz_sentences = get_herz(new_wordlist, number_flag_list, special_session_flag_list)
    # date_sentences, dates_flags_list = get_dates(new_wordlist, number_flag_list)
    time_sentences, times_flags_list, end_times_indices = get_time(new_wordlist, number_flag_list)
    herz_sentences = get_herz(new_wordlist, number_flag_list)
    repeated_nums, repeated_nums_flag, end_nums_indices = get_repeated_nums(new_wordlist, number_flag_list, dates_flags_list, times_flags_list)

    if date_sentences == ['']: date_sentences = []  
    if time_sentences == ['']: time_sentences = []
    if repeated_nums  == ['']: repeated_nums = []
    if herz_sentences == ['']: herz_sentences = []
    date_flag = 0
    time_flag = 0
    year_flag = 0

    for h in herz_sentences:
        if h == '': continue
        new_h, _, h_wordlist, _ = prepare_txt(h)
        herz_sent = extract_herz(new_h, h_wordlist)
        for i, w in enumerate(txt.split()):
                if w == h.split()[0]:
                    flag = 1
                    j = i
                    while j<len(txt.split()) and j-i < len(h.split()):
                        if txt.split()[j] != h.split()[j-i]: flag = 0
                        j += 1
                        if flag == 1: 
                            end_pattern_index = i + len(h.split())
                            break
        # brack_txt = add_pattern_brackets(brack_txt, herz_sent, end_pattern_index)
        txt = add_pattern_brackets(txt, herz_sent, end_pattern_index)
        original_txt = add_pattern_brackets(original_txt, herz_sent, end_pattern_index)
    
    for i, t in enumerate(time_sentences):
        if t == '': continue
        new_t, _, t_wordlist, _ = prepare_txt(t)
        hours, minutes = extract_time(new_t, t_wordlist)
        if hours == -1 or minutes == -1: continue
        else:
            time_flag = 1
            # for i, w in enumerate(txt.split()):
            #     if w == t.split()[0]:
            #         flag = 1
            #         j = i
            #         while j<len(txt.split()) and j-i < len(t.split()):
            #             if txt.split()[j] != t.split()[j-i]: flag = 0
            #             j += 1
            #         if flag == 1: end_pattern_index = i + len(t.split())
            # brack_txt = add_pattern_brackets(brack_txt, f'{int(hours):02d}' + ":" + f'{int(minutes):02d}' , end_pattern_index)
            brack_pattern = ' (' + f'{int(hours):02d}' + ":" + f'{int(minutes):02d})'
            if (end_times_indices[i]+1 < len(new_original_wordlist) and new_original_wordlist[end_times_indices[i]+1].strip() != brack_pattern.strip()) or end_times_indices[i]+1 == len(new_original_wordlist):
                new_original_wordlist[end_times_indices[i]] = new_original_wordlist[end_times_indices[i]] + brack_pattern
            # txt = add_pattern_brackets(txt, f'{int(hours):02d}' + ":" + f'{int(minutes):02d}' , end_pattern_index)
            # original_txt = add_pattern_brackets(original_txt, f'{int(hours):02d}' + ":" + f'{int(minutes):02d}', end_pattern_index)
            # txt = txt.replace(t, f'{int(hours):02d}' + ":" + f'{int(minutes):02d}')
    
    for j, d in enumerate(date_sentences):
        if d == '': continue
        new_d, _, d_wordlist, _ = prepare_txt(d)
        day, month, year = extract_date(new_d, d_wordlist)
        if day == -1 and month == -1 and year == -1: continue
        if year != -1:
            date_flag = 1
            year_flag = 1
            # for i, w in enumerate(txt.split()):
            #     if w == d.split()[0]:
            #         flag = 1
            #         j = i
            #         while j<len(txt.split()) and j-i < len(d.split()):
            #             if txt.split()[j] != d.split()[j-i]: flag = 0
            #             j += 1
            #         if flag == 1: end_pattern_index = i + len(d.split())
            if month != -1 and day != -1:
                # brack_txt = add_pattern_brackets(brack_txt, str(year) + "/" + str(month) + "/" + str(day), end_pattern_index)
                brack_pattern = ' (' + str(year) + "/" + str(month) + "/" + str(day) + ')'
                if (end_dates_indices[j]+1 < len(new_original_wordlist) and new_original_wordlist[end_dates_indices[j]+1].strip() != brack_pattern.strip()) or end_dates_indices[j]+1 == len(new_original_wordlist):
                    new_original_wordlist[end_dates_indices[j]] = new_original_wordlist[end_dates_indices[j]] + brack_pattern
                # txt = add_pattern_brackets(txt, str(year) + "/" + str(month) + "/" + str(day), end_pattern_index)
                # original_txt = add_pattern_brackets(original_txt, str(year) + "/" + str(month) + "/" + str(day), end_pattern_index)
                # txt = txt.replace(d, str(year) + "/" + str(month) + "/" + str(day))
            else:
                # brack_txt = add_pattern_brackets(brack_txt, str(year), end_pattern_index)
                brack_pattern = ' (' + str(year) + ')'
                if (end_dates_indices[j]+1 < len(new_original_wordlist) and new_original_wordlist[end_dates_indices[j]+1].strip() != brack_pattern.strip()) or end_dates_indices[j]+1 == len(new_original_wordlist):
                    new_original_wordlist[end_dates_indices[j]] = new_original_wordlist[end_dates_indices[j]] + brack_pattern
                # txt = add_pattern_brackets(txt, str(year), end_pattern_index)
                # original_txt = add_pattern_brackets(original_txt, str(year), end_pattern_index)
                # txt = txt.replace(d, str(year))
        elif day != -1 and month != -1:
            index = txt.find(d)
            for i, w in enumerate(txt.split()):
                if w == d.split()[0]:
                    flag = 1
                    j = i
                    while j<len(txt.split()) and j-i < len(d.split()):
                        if txt.split()[j] != d.split()[j-i]: flag = 0
                        j += 1
                    if flag == 1: end_pattern_index = i + len(d.split())
            if index == 0: continue
            tokenized = araby.tokenize(txt[:index])
            if tokenized[-1] in DAY_DEFINING_WORDS:
                # brack_txt = add_pattern_brackets(brack_txt, str(month) + "/" + str(day), end_pattern_index)
                txt = add_pattern_brackets(txt, str(month) + "/" + str(day), end_pattern_index)
                original_txt = add_pattern_brackets(original_txt, str(month) + "/" + str(day), end_pattern_index)
                # txt = txt.replace(d, str(month) + "/" + str(day))
                date_flag = 1
    
    for i, r in enumerate(repeated_nums):
        if r == '': continue
        if any(r in string for string in time_sentences): continue
        # end_pattern_index = -1
        # for i, w in enumerate(txt.split()):
        #         if w == r.split()[0]:      
        #             flag = 1
        #             j = i
        #             while j<len(txt.split()) and j-i < len(r.split()):
        #                 if txt.split()[j] != r.split()[j-i]: flag = 0
        #                 j += 1
        #             if flag == 1: 
        #                 end_pattern_index = i + len(r.split())
        #                 break
        new_r, _, r_wordlist, _ = prepare_txt(r)
        num = extract_repeated_numbers(new_r, r_wordlist)
        # if end_pattern_index >= 0: brack_txt = add_pattern_brackets(brack_txt, num, end_pattern_index)
        if end_nums_indices[i] >= 0: 
            brack_pattern = ' (' + num + ')'
            if (end_nums_indices[i]+1 < len(new_original_wordlist) and new_original_wordlist[end_nums_indices[i]+1].strip() != brack_pattern.split()) or end_nums_indices[i]+1 == len(new_original_wordlist):
                new_original_wordlist[end_nums_indices[i]] = new_original_wordlist[end_nums_indices[i]] + brack_pattern
            # txt = add_pattern_brackets(txt, num, end_pattern_index)
            # original_txt = add_pattern_brackets(original_txt, num, end_pattern_index)
            original_txt = ' '.join(new_original_wordlist)
        # txt = txt.replace(r, num)
    
    # txt = re.sub(r'(\d)\s+(\d)', r'\1\2', txt)
    return original_txt, date_flag, year_flag, time_flag, repeated_nums_flag

def main():
    txts = []
    file_path = "test/hyp_combined.txt"
    # file_path = sys.argv[1]
    f = open(file_path, encoding='utf-8')
    t = f.read()
    f.close()
    txts.extend(t.split('\n'))

    # txts.append("ما معلوماتك بشأن الواقعة محل التحقيق جيم حصل أنا شغال رئيس حفارين بالجبانة الفاطمية بمقام السيد البدوي من حوالي تمانية وعشرين سنة ودي مقابر عامة ومن حوالي تلات أيام بتاريخ تلاتاشر تمانية ألفين واحد وعشرين الساعة اتناشر الضهر")
    # txts.append("ما معلوماتك بشأن الواقعة محل التحقيق جيم حصل أنا شغال رئيس حفارين بالجبانة الفاطمية بمقام السيد البدوي من حوالي تمانية وعشرين سنة ودي مقابر عامة ومن حوالي تلات أيام بتاريخ تلاتاشر تمانية ألفين واحد وعشرين الساعة اتناشر الضهر جاتلي مكالمة من شخص يدعى محمد محمود وقالي انا معايا واحد قريبي متوفي ومحتاجين ندفنه وانا جاي على المقابر جهزلي المدفن لغاية لما اجي وفعلا حوالي الساعه خمسه ونص مساءا في نفس اليوم لقيت جنازة داخلة وكان معاها محمد محمود وكان في ناس من المرة كانو شايلين الجثمان وكانوا بيساعدو في الخير لغاية لما يوصلو لغاية لما جثمان للمدفن لحد ما قولتله على مكان المدفن وابتديت اشتغل زاستلمت الجثمان وكان متكفن ونزلتهم وقفلت وساعتها كان محمد واقف فقولتله فين التصريح قالي هصورهولك على طول وانا ساعتها اشتغل فضلت روحت جنازة تانية وفضلت مستني التصريح بتاع محمد لغاية بليل وكلمته اكتر من مرة ماردش عليا فاستنيت لتاني يوم الصبح روحتله عند مكان شغله سألت عليه وعرفت انه مش موجود فساعتها قلقت روحت على القسم بلغت وده كل اللي حصل")
    # txts.append("الجلسة الثالثه يوم تسعه وعشرين اتناشر الفين واحد وعشرين")
    # txts.append("بطاقة تحقيق شخصية رقم اتنين تمانية سبعة صفر واحد اتنين تسعة1 اتنين سبعة صفر صفر صفر تلاتة واحد")
    # txts.append("تم فتح الملف الثالث عشر من يناير عام الفين اثنان وعشرين")
    # txts.append("فتحت الجلسة الثالثة الخامس من اكتوبر الفين اتنين وعشرين بسرايا النيابة")
    # txts.append("في الساعه إحدى عشره صباحا وثلاثين دقيقه فتح المحضر")
    # txts.append("من يوم الثاني عشرة عشرين عشرين ")

    # txts.append( "  قبل اتنين وعشرين تسعة الفين وعشرة الساعة تمانية ونص مساء وحوالي تلات تيام تاريخ العاشر من يونيو عشرين واحد و عشرين الساعة العاشرة وخمس دقائق" )
    # txts.append("يوم الخميس الساعة خمسة وتلاتين دقيقة الساعة اتنين وعشرين دقيقة الحرز رقم ميتين وستاشر على اتناشر أأشياء قسم الاقصر")
    # txts.append( "يوم التلات تلاتاشر واحد" )
    # txts.append( "المبلغ المالي اتناشر الف جنيه محل الحرز مئتين وثلاثة على خمسمية اتنين وتلاتين" )
    # txts.append("المؤرخ في تلاتة وعشرين ستة الفين واحد وعشرين ورقم صادر عشرين واحد وعشرين اربعتاشر سبعة واحد صفر صفر صفر حداشر واحد وستين المكون من اتنين صفحات ")

    # for txt in txts:
    #     # new_txt, date_flag, year_flag, time_flag, repeated_nums_flag, brack_txt = process_dates(txt)
    #     new_txt, date_flag, year_flag, time_flag, repeated_nums_flag = process_dates(txt)
    #     # f = open("test/test_out.txt", 'w', encoding='utf-8')
    #     # f.write(new_txt)
    #     # f.close()   
    #     if 1 or date_flag or time_flag or repeated_nums_flag: print("TXT : " , txt, "\n", "NEW : ", new_txt, "\n\n\n")
    #     # if 1 or date_flag or time_flag or repeated_nums_flag: print("TXT : " , txt, "\n", "NEW : ", brack_txt, "\n\n\n")

    final_txts = []
    for txt in txts:
        new_txt, date_flag, year_flag, time_flag, repeated_nums_flag = process_dates(txt)
        # f = open("test/test_out.txt", 'w', encoding='utf-8')
        # f.write(brack_txt)
        # f.close()   
        # if 1 or date_flag or time_flag or repeated_nums_flag: print("TXT : " , txt, "\n", "NEW : ", new_txt, "\n\n\n")
        # if 1 or date_flag or time_flag or repeated_nums_flag: print("TXT : " , txt, "\n", "NEW : ", brack_txt, "\n\n\n")
        final_txts.append(new_txt)
    # f = open("../test_out.txt", 'w', encoding='utf-8')
    f = open("test/test_out.txt", 'w', encoding='utf-8')
    f.write('\n'.join(final_txts))
    f.close()


if __name__ == '__main__':
    main()