from detect_date import process_dates

txt = "تسعتاشر عشرين ألفين وعشرين"
new_txt, _, _ = process_dates(txt)
print(new_txt)

