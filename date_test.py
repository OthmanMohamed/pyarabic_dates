from detect_date import process_dates

txt = "ليوم خمسة وعشرين اربعة هذا وقد ورد إلينا تقرير المعمل الجنائي الخاص بالحرز ألف خمسميه و تسعين تلاته إتنين و المثبت به الحرز ألف تسعميه"
new_txt, date_flag = process_dates(txt)
print(new_txt)
print(date_flag)

