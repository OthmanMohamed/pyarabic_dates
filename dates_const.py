ACCEPT_NUMBER_PREFIX = [
    u'الاف',
    u'الف',
    u'ألاف',
    u'آلاف',
    u'تلاف',
    u'مليون',
    u'ملايين',
    u'مية',
    u'مائة',
    u'مئة',
    u'ميه',
    u'مائه',
    u'مئه',
    u'مليار',
    u'مليارات',
    u'عشر',
    u'عشرة'
]

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
    u'ديسمبر': 12,
    u'ديسيمبر': 12
}

YEARS_REPLACE = {
    u'عشرين حداشر' : u'الفين وحداشر',
    u'عشرين اتناشر' : u'الفين واتناشر',
    u'عشرين تلاتاشر' : u'الفين وتلاتاشر',
    u'عشرين اربعتاشر' : u'الفين واربعتاشر',
    u'عشرين أربعتاشر' : u'الفين واربعتاشر',
    u'عشرين خمستاشر' : u'الفين وخمستاشر',
    u'عشرين ستاشر' : u'الفين وستاشر',
    u'عشرين سبعتاشر' : u'الفين وسبعتاشر',
    u'عشرين تمانتاشر' : u'الفين وتمانتاشر',
    u'عشرين تسعتاشر' : u'الفين وتسعتاشر',
    u'عشرين عشرين' : u'الفين وعشرين',
    u'عشرين واحد وعشرين' : u'الفين واحد وعشرين',
    u'عشرين اتنين وعشرين' : u'الفين اتنين وعشرين',
    u'عشرين أتنين وعشرين' : u'الفين اتنين وعشرين',
    u'عشرين تلاتة وعشرين' : u'الفين تلاتة وعشرين',
    u'عشرين اربعة وعشرين' : u'الفين اربعة وعشرين',
    u'عشرين أربعة وعشرين' : u'الفين اربعة وعشرين',
    u'عشرين خمسة وعشرين' : u'الفين خمسة وعشرين',
    u'عشرين ستة وعشرين' : u'الفين ستة وعشرين',
    u'عشرين سبعة وعشرين' : u'الفين سبعة وعشرين',
    u'عشرين تمانية وعشرين' : u'الفين تمانية وعشرين',
    u'عشرين تسعة وعشرين' : u'الفين تسعة وعشرين',
    u'عشرين تلاتين' : u'الفين وتلاتين',
}

DATE_FILL_WORDS = [
    "من",
    "في",
    "يوم",
    "شهر",
    "سنة",
    "عام",
    "ليوم",
    "لشهر",
    "لسنة",
    "لعام",
    "للعام",
    "بيوم",
    "بشهر",
    "بسنة",
    "بعام"
]

DAY_DEFINING_WORDS = [
    "اليوم",
    "يوم",
    "بيوم",
    "ليوم",
    "الموافق",
    "فجر",
    "مساء",
    "صباح",
    "بتاريخ",
    "تاريخ",
    "السبت",
    "سبت",
    "الحد",
    "الاحد",
    "الأحد",
    "حد",
    "احد",
    "أحد",
    "الاتنين",
    "الأتنين",
    "الإتنين",
    "اتنين",
    "أتنين",
    "إتنين",
    "التلات",
    "تلات",
    "الثلاثاء",
    "ثلاثاء",
    "الاربع",
    "الأربع",
    "اربع",
    "أربع",
    "الخميس",
    "خميس",
    "الجمعه",
    "الجمعة",
    "جمعه",
    "جمعة",
    "في"
]

TIME_TRIGGERS = [
    "الساعة",
    "تمام",
    "حوالي"
]

TIME_TERMINATING = [
    "دقايق",
    "دقائق",
    "دقيقة",
    "مساء",
    "مساءا",
    "صباح",
    "صباح",
    "ظهرا",
    "ظهر",
    "ضهرا",
    "ضهر"
]

TEN_PREFIX = [ #words that can come before عشر or عشرة
    'أحد',
    'احد',
    'إحدى',
    'احدى',
    'اثنا',
    'اثنتا',
    'إثنا',
    'إثنتا',
    'ثلاث',
    'ثلاثة',
    'اربع',
    'اربعة',
    'أربع',
    'أربعة',
    'خمس',
    'خمسة',
    'ستة',
    'ست',
    'سبعة',
    'سبع',
    'ثمان',
    'ثمانية',
    'ثماني',
    'تسع',
    'تسعة',
]