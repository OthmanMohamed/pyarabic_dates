#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
Constants used for number module
"""
# at top of module
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
)

try:
    import araby
    import normalize
except:
    from . import araby
    from . import normalize
   

THAOUSAND_MULTIPLE = ()
NUMBER_TEN_MASCULIN_UNITS = (
    u'اثني',
    u'اثنا',
    u'إثني',
    u'إثنا',
    u'أحد',
    u'ثلاثة',
    u'أربعة',
    u'خمسة',
    u'ستة',
    u'سبعة',
    u'ثمانية',
    u'تسعة',
)
NUMBER_TEN_FEMININ_UNITS = (
    u'إحدى',
    u'اثنتا',
    u'اثنتي',
    u'ثلاث',
    u'أربع',
    u'خمس',
    u'ست',
    u'سبع',
    u'ثمان',
    u'ثماني',
    u'تسع',
)

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

NUMBER_WORDS = {
    u'صفر': 0,
    u'زيرو': 0,
    u'واحد': 1,
    u'واحدة': 1,
    u'واحده': 1,
    u'اثنان': 2,
    u'أثنان': 2,
    u'إثنان': 2,
    u'اتنين': 2,
    u'إتنين': 2,
    u'أتنين': 2,
    u'اتنان': 2,
    u'ثلاثة': 3,
    u'تلاتة': 3,
    u'ثلاثه': 3,
    u'تلاته': 3,
    u'أربعة': 4,
    u'اربعة': 4,
    u'أربعه': 4,
    u'اربعه': 4,
    u'خمسة': 5,
    u'خمسه': 5,
    u'ستة': 6,
    u'سته': 6,
    u'سبعة': 7,
    u'سبعه': 7,
    u'ثمانية': 8,
    u'تمانية': 8,
    u'ثمانيه': 8,
    u'تمانيه': 8,
    u'تسعة': 9,
    u'تسعه': 9,
    u'عشرة': 10,
    u'عشره': 10,
    u'حداشر': 11,
    u'اتناشر': 12,
    u'تناشر': 12,
    u'أتناشر': 12,
    u'إتناشر': 12,
    u'تلاتاشر': 13,
    u'تلتاشر': 13,
    u'اربعتاشر': 14,
    u'ربعتاشر': 14,
    u'أربعتاشر': 14,
    u'خمستاشر': 15,
    u'ستاشر': 16,
    u'سبعتاشر': 17,
    u'تمانتاشر': 18,
    u'تمنتاشر': 18,
    u'تسعتاشر': 19,
    u'عشرون': 20,
    u'ثلاثون': 30,
    u'تلاتون': 30,
    u'أربعون': 40,
    u'اربعون': 40,
    u'خمسون': 50,
    u'ستون': 60,
    u'سبعون': 70,
    u'ثمانون': 80,
    u'تمانون': 80,
    u'تسعون': 90,
    u'مئة': 100,
    u'مية': 100,
    u'مئتان': 200,
    u'ثلاثمئة': 300,
    u'تلتمية': 300,
    u'أربعمئة': 400,
    u'أربعمئة': 400,
    u'اربعمئة': 400,
    u'اربعمئة': 400,
    u'ربعمية': 400,
    u'خمسمئة': 500,
    u'خمسمية': 500,
    u'ستمئة': 600,
    u'ستمية': 600,
    u'سبعمئة': 700,
    u'سبعمية': 700,
    u'ثمانمئة': 800,
    u'تمنمية': 800,
    u'تسعمئة': 900,
    u'تسعمية': 900,
    u'مئه': 100,
    u'ميه': 100,
    u'مئتان': 200,
    u'ثلاثمئه': 300,
    u'تلتميه': 300,
    u'أربعمئه': 400,
    u'أربعمئه': 400,
    u'ربعميه': 400,
    u'خمسمئه': 500,
    u'خمسميه': 500,
    u'ستمئه': 600,
    u'ستميه': 600,
    u'سبعمئه': 700,
    u'سبعميه': 700,
    u'ثمانمئه': 800,
    u'تمنميه': 800,
    u'تسعمئه': 900,
    u'تسعميه': 900,

    u'ثلاثمائة': 300,
    u'أربعمائة': 400,
    u'اربعمائة': 400,
    u'خمسمائة': 500,
    u'ستمائة': 600,
    u'سبعمائة': 700,
    u'ثمانمائة': 800,
    u'تسعمائة': 900,
    u'ثلاثمائه': 300,
    u'أربعمائه': 400,
    u'اربعمائه': 400,
    u'خمسمائه': 500,
    u'ستمائه': 600,
    u'سبعمائه': 700,
    u'ثمانمائه': 800,
    u'تسعمائه': 900,

    u'ألف': 1000,
    u'ألفا': 1000,
    u'الف': 1000,
    u'الفا': 1000,

    u'مليون': 1000000,
    u'مليار': 1000000000,

    u'ألفان': 2000,
    u'ألفين': 2000,
    u'الفان': 2000,
    u'الفين': 2000,
    u'الفي': 2000,
    u'الفا': 2000,

    u'مليونان': 2000000,
    u'مليونا': 2000000,
    u'مليونين': 2000000,
    u'مليوني': 2000000,

    u'ملياران': 2000000000,
    u'مليارا': 2000000000,
    u'مليارين': 2000000000,
    u'ملياري': 2000000000,

    u'أحد': 1,
    u'احد': 1,
    u'إحدى': 1,
    u'احدى': 1,

    u'اثنين': 2,
    u'إثنين': 2,
    u'إثنان': 2,

    u'اثني': 2,
    u'اثنا': 2,
    u'إثني': 2,
    u'إثنا': 2,
    u'ثلاث': 3,
    u'تلات': 3,
    u'تلت': 3,
    u'أربع': 4,
    u'اربع': 4,
    u'خمس': 5,
    u'ست': 6,
    u'سبع': 7,
    u'ثمان': 8,
    u'تمان': 8,
    u'تمن': 8,
    u'ثماني': 8,
    u'تماني': 8,
    u'تسع': 9,
    u'عشر': 10,
    u'ثلاثا': 3,
    u'تلاتا': 3,
    u'أربعا': 4,
    u'اربعا': 4,
    u'خمسا': 5,
    u'ستا': 6,
    u'سبعا': 7,
    u'تمانيا': 8,
    u'تسعا': 9,
    u'عشرا': 10,

    u'عشرين': 20,
    u'ثلاثين': 30,
    u'تلاتين': 30,
    u'أربعين': 40,
    u'اربعين': 40,
    u'خمسين': 50,
    u'ستين': 60,
    u'سبعين': 70,
    u'ثمانين': 80,
    u'تمانين': 80,
    u'تسعين': 90,
    u'مائة': 100,
    u'مية': 100,
    u'مائه': 100,
    u'ميه': 100,
    u'مئتين': 200,
    u'ميتين': 200,
    u'متين': 200,
    u'الاف': 1000,
    u'تلاف': 1000,
    u'تلاتلاف': 3000,
    u'اربعتلاف': 4000,
    u'خمستلاف': 5000,
    u'ستلاف': 6000,
    u'سبعتلاف': 7000,
    u'تمانتلاف': 8000,
    u'تسعتلاف': 9000,
    u'عشرتلاف': 10000,
    u'آلاف': 1000,
    u'ملايين': 1000000,
    u'مليارات': 1000000000,
}

VOCALIZED_NUMBER_WORDS = {
    # i: unvocalized
    # r ; marafou3 رفع
    # r2 : marfou3 + tanwin
    # n : mansoub
    # n2: mansoub + tanwin
    # j : majrour
    # j2 : majrour + tanwin
    u'صفر': {u'i': u'صِفْر', u'r': u'صِفْرُ', u'r2': u'صِفْرٌ', u'n': u'صِفْرَ',
             u'n2': u'صِفْرً', u'j': u'صِفْرِ', u'j2': u'صِفْرٍ', u's': u''},
    u'واحد': {u'i': u'وَاحِد', u'r': u'وَاحِدُ', u'r2': u'وَاحِدٌ', u'n': u'وَاحِدَ',
              u'n2': u'وَاحِدً', u'j': u'وَاحِدِ', u'j2': u'وَاحِدٍ', u's': u''},
    u'واحدة': {u'i': u'وَاحِدَة', u'r': u'وَاحِدَةُ', u'r2': u'وَاحِدَةٌ',
               u'n': u'وَاحِدَةَ', u'n2': u'وَاحِدَةً', u'j': u'وَاحِدَةِ', u'j2': u'وَاحِدَةٍ',
               u's': u''},
    u'اثنان': {u'i': u'اثنان', u'r': u'اثنان', u'r2': u'اثنانٌ',
               u'n': u'اثنانَ', u'n2': u'اثنانً', u'j': u'اثنانِ', u'j2': u'اثنانٍ',
               u's': u'*'},
    u'ثلاثة': {u'i': u'ثَلاثَة', u'r': u'ثَلاثَةُ', u'r2': u'ثَلاثَةٌ', u'n': u'ثَلاثَةَ',
               u'n2': u'ثَلاثَةً', u'j': u'ثَلاثَةِ', u'j2': u'ثَلاثَةٍ', u's': u''},
    u'أربعة': {u'i': u'أَرْبَعَة', u'r': u'أَرْبَعَةُ', u'r2': u'أَرْبَعَةٌ',
               u'n': u'أَرْبَعَةَ', u'n2': u'أَرْبَعَةً', u'j': u'أَرْبَعَةِ', u'j2': u'أَرْبَعَةٍ',
               u's': u''},
    u'خمسة': {u'i': u'خَمْسَة', u'r': u'خَمْسَةُ', u'r2': u'خَمْسَةٌ', u'n': u'خَمْسَةَ',
              u'n2': u'خَمْسَةً', u'j': u'خَمْسَةِ', u'j2': u'خَمْسَةٍ', u's': u''},
    u'ستة': {u'i': u'سِتَّة', u'r': u'سِتَّةُ', u'r2': u'سِتَّةٌ', u'n': u'سِتَّةَ',
             u'n2': u'سِتَّةً', u'j': u'سِتَّةِ', u'j2': u'سِتَّةٍ', u's': u''},
    u'سبعة': {u'i': u'سَبْعَة', u'r': u'سَبْعَةُ', u'r2': u'سَبْعَةٌ', u'n': u'سَبْعَةَ',
              u'n2': u'سَبْعَةً', u'j': u'سَبْعَةِ', u'j2': u'سَبْعَةٍ', u's': u''},
    u'ثمانية': {u'i': u'ثَمانِيَة', u'r': u'ثَمانِيَةُ', u'r2': u'ثَمانِيَةٌ',
                u'n': u'ثَمانِيَةَ', u'n2': u'ثَمانِيَةً', u'j': u'ثَمانِيَةِ',
                u'j2': u'ثَمانِيَةٍ', u's': u''},
    u'تسعة': {u'i': u'تِسْعَة', u'r': u'تِسْعَةُ', u'r2': u'تِسْعَةٌ', u'n': u'تِسْعَةَ',
              u'n2': u'تِسْعَةً', u'j': u'تِسْعَةِ', u'j2': u'تِسْعَةٍ', u's': u''},
    u'عشرة': {u'i': u'عَشْرَة', u'r': u'عَشْرَةُ', u'r2': u'عَشْرَةٌ', u'n': u'عَشْرَةَ',
              u'n2': u'عَشْرَةً', u'j': u'عَشْرَةِ', u'j2': u'عَشْرَةٍ', u's': u''},
    u'عشرون': {u'i': u'عِشْرُونَ', u'r': u'عِشْرُونَ', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'ثلاثون': {u'i': u'ثَلاثُونَ', u'r': u'ثَلاثُونَ', u'r2': u'', u'n': u'',
                u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'أربعون': {u'i': u'أَرْبَعُونَ', u'r': u'أَرْبَعُونَ', u'r2': u'', u'n': u'',
                u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'خمسون': {u'i': u'خَمْسُونَ', u'r': u'خَمْسُونَ', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'ستون': {u'i': u'سِتُّونَ', u'r': u'سِتُّونَ', u'r2': u'', u'n': u'',
              u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'سبعون': {u'i': u'سَبْعُونَ', u'r': u'سَبْعُونَ', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'ثمانون': {u'i': u'ثمانون', u'r': u'ثمانون', u'r2': u'', u'n': u'',
                u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'تسعون': {u'i': u'تِسْعُونَ', u'r': u'تِسْعُونَ', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'مئة': {u'i': u'مِئَة', u'r': u'مِئِةُ', u'r2': u'مِئَةٌ', u'n': u'مِئَةَ',
             u'n2': u'مِئَةً', u'j': u'مِئَةِ', u'j2': u'مِئَةٍ', u's': u''},
    u'مئتان': {u'i': u'مِئَتَانِ', u'r': u'مِئَتَانِ', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'ثلاثمئة': {u'i': u'ثَلَاثمِئَة', u'r': u'ثَلَاثُمِئَةِ', u'r2': u'ثَلَاثُمِئَةٍ',
                 u'n': u'ثَلَاثَمِئَةِ', u'n2': u'ثَلَاثَمِئَةٍ', u'j': u'ثَلَاثِمِئَةِ',
                 u'j2': u'ثَلَاثِمِئَةٍ', u's': u''},
    u'أربعمئة': {u'i': u'أَرْبَعمِئَة', u'r': u'أَرْبَعُمِئَةِ', u'r2': u'أَرْبَعُمِئَةٍ',
                 u'n': u'أَرْبَعَمِئَةِ', u'n2': u'أَرْبَعَمِئَةٍ', u'j': u'أَرْبَعِمِئَةِ',
                 u'j2': u'أَرْبَعِمِئَةٍ', u's': u''},
    u'خمسمئة': {u'i': u'خَمْسمِئَة', u'r': u'خَمْسُمِئَةِ', u'r2': u'خَمْسُمِئَةٍ',
                u'n': u'خَمْسَمِئَةِ', u'n2': u'خَمْسَمِئَةٍ', u'j': u'خَمْسِمِئَةِ',
                u'j2': u'خَمْسِمِئَةٍ', u's': u''},
    u'ستمئة': {u'i': u'سِتّمِئَة', u'r': u'سِتُّمِئَةِ', u'r2': u'سِتُّمِئَةٍ',
               u'n': u'سِتَّمِئَةِ', u'n2': u'سِتَّمِئَةٍ', u'j': u'سِتِّمِئَةِ',
               u'j2': u'سِتِّمِئَةٍ', u's': u''},
    u'سبعمئة': {u'i': u'سَبْعمِئَة', u'r': u'سَبْعُمِئَةِ', u'r2': u'سَبْعُمِئَةٍ',
                u'n': u'سَبْعَمِئَةِ', u'n2': u'سَبْعَمِئَةٍ', u'j': u'سَبْعِمِئَةِ',
                u'j2': u'سَبْعِمِئَةٍ', u's': u''},
    u'ثمانمئة': {u'i': u'ثَمَانمِئَة', u'r': u'ثَمَانُمِئَةِ', u'r2': u'ثَمَانُمِئَةٍ',
                 u'n': u'ثَمَانَمِئَةِ', u'n2': u'ثَمَانَمِئَةٍ', u'j': u'ثَمَانِمِئَةِ',
                 u'j2': u'ثَمَانِمِئَةٍ', u's': u''},
    u'تسعمئة': {u'i': u'تِسْعمِئَة', u'r': u'تِسْعُمِئَةِ', u'r2': u'تِسْعُمِئَةٍ',
                u'n': u'تِسْعَمِئَةِ', u'n2': u'تِسْعَمِئَةٍ', u'j': u'تِسْعِمِئَةِ',
                u'j2': u'تِسْعِمِئَةٍ', u's': u''},
    u'ثلاثمائة': {u'i': u'ثَلَاثمِائَة', u'r': u'ثَلَاثُمِائَةِ', u'r2': u'ثَلَاثُمِائَةٍ',
                  u'n': u'ثَلَاثَمِائَةِ', u'n2': u'ثَلَاثَمِائَةٍ', u'j': u'ثَلَاثِمِائَةِ',
                  u'j2': u'ثَلَاثِمِائَةٍ', u's': u''},
    u'أربعمائة': {u'i': u'أَرْبَعمِائَة', u'r': u'أَرْبَعُمِائَةِ', u'r2': u'أَرْبَعُمِائَةٍ',
                  u'n': u'أَرْبَعَمِائَةِ', u'n2': u'أَرْبَعَمِائَةٍ', u'j': u'أَرْبَعِمِائَةِ',
                  u'j2': u'أَرْبَعِمِائَةٍ', u's': u''},
    u'خمسمائة': {u'i': u'خَمْسمِائَة', u'r': u'خَمْسُمِائَةِ', u'r2': u'خَمْسُمِائَةٍ',
                 u'n': u'خَمْسَمِائَةِ', u'n2': u'خَمْسَمِائَةٍ', u'j': u'خَمْسِمِائَةِ',
                 u'j2': u'خَمْسِمِائَةٍ', u's': u''},
    u'ستمائة': {u'i': u'سِتّمِائَة', u'r': u'سِتُّمِائَةِ', u'r2': u'سِتُّمِائَةٍ',
                u'n': u'سِتَّمِائَةِ', u'n2': u'سِتَّمِائَةٍ', u'j': u'سِتِّمِائَةِ',
                u'j2': u'سِتِّمِائَةٍ', u's': u''},
    u'سبعمائة': {u'i': u'سَبْعمِائَة', u'r': u'سَبْعُمِائَةِ', u'r2': u'سَبْعُمِائَةٍ',
                 u'n': u'سَبْعَمِائَةِ', u'n2': u'سَبْعَمِائَةٍ', u'j': u'سَبْعِمِائَةِ',
                 u'j2': u'سَبْعِمِائَةٍ', u's': u''},
    u'ثمانمائة': {u'i': u'ثَمَانمِائَة', u'r': u'ثَمَانُمِائَةِ', u'r2': u'ثَمَانُمِائَةٍ',
                  u'n': u'ثَمَانَمِائَةِ', u'n2': u'ثَمَانَمِائَةٍ', u'j': u'ثَمَانِمِائَةِ',
                  u'j2': u'ثَمَانِمِائَةٍ', u's': u''},
    u'تسعمائة': {u'i': u'تِسْعمِائَة', u'r': u'تِسْعُمِائَةِ', u'r2': u'تِسْعُمِائَةٍ',
                 u'n': u'تِسْعَمِائَةِ', u'n2': u'تِسْعَمِائَةٍ', u'j': u'تِسْعِمِائَةِ',
                 u'j2': u'تِسْعِمِائَةٍ', u's': u''},
    u'ألف': {u'i': u'أَلْف', u'r': u'أَلْف', u'r2': u'أَلْفٌ', u'n': u'أَلْفَ',
             u'n2': u'أَلْفً', u'j': u'أَلْفِ', u'j2': u'أَلْفٍ', u's': u''},
    u'ألفا': {u'i': u'أَلْفًا', u'r': u'أَلْفًا', u'r2': u'أَلْفًا', u'n': u'أَلْفًا',
              u'n2': u'أَلْفًا', u'j': u'أَلْفًا', u'j2': u'أَلْفًا', u's': u'أَلْفًا'},
    u'مليون': {u'i': u'مِلْيُون', u'r': u'مِلْيُونُ', u'r2': u'مِلْيُونٌ',
               u'n': u'مِلْيُونَ', u'n2': u'مِلْيُونً', u'j': u'مِلْيُونِ',
               u'j2': u'مِلْيُونٍ', u's': u''},
    u'مليار': {u'i': u'مِلْيَار', u'r': u'مِلْيَارُ', u'r2': u'مِلْيَارٌ',
               u'n': u'مِلْيَارَ', u'n2': u'مِلْيَارً', u'j': u'مِلْيَارِ',
               u'j2': u'مِلْيَارٍ', u's': u''},
    u'ألفان': {u'i': u'ألْفَانِ', u'r': u'ألْفَانِ', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'ألفين': {u'i': u'ألْفَيْنِ', u'r': u'ألْفَيْنِ', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'مليونان': {u'i': u'مِلْيُونَانِ', u'r': u'مِلْيُونَانِ', u'r2': u'', u'n': u'',
                 u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'مليونين': {u'i': u'مِلْيُونَيْنِ', u'r': u'مِلْيُونَيْنِ', u'r2': u'', u'n': u'',
                 u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'ملياران': {u'i': u'مِلْيَارَانِ', u'r': u'مِلْيَارَانِ', u'r2': u'', u'n': u'',
                 u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'مليارين': {u'i': u'مِلْيَارَيْنِ', u'r': u'مِلْيَارَيْنِ', u'r2': u'', u'n': u'',
                 u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'أحد': {u'i': u'أَحَد', u'r': u'أَحُدُّ', u'r2': u'أَحَدٌ', u'n': u'أَحَدَ',
             u'n2': u'أَحَدً', u'j': u'أَحَدِ', u'j2': u'أَحَدٍ', u's': u''},
    u'إحدى': {u'i': u'إحْدَى', u'r': u'إحْدَى', u'r2': u'إحْدَىٌ', u'n': u'إحْدَى',
              u'n2': u'إحْدًى', u'j': u'إحْدَىِ', u'j2': u'إحْدَىٍ', u's': u'*'},
    u'اثنين': {u'i': u'اِثْنَينِ', u'r': u'اِثْنَينِ', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'إثنين': {u'i': u'إثنين', u'r': u'إثنين', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'إثنان': {u'i': u'إثنان', u'r': u'إثنان', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'اثني': {u'i': u'اِثْنَيْ', u'r': u'اِثْنَيْ', u'r2': u'', u'n': u'', u'n2': u'',
              u'j': u'', u'j2': u'', u's': u'*'},
    u'اثنا': {u'i': u'اِثْنَا', u'r': u'اثنا', u'r2': u'', u'n': u'', u'n2': u'',
              u'j': u'', u'j2': u'', u's': u'*'},
    u'إثني': {u'i': u'إثني', u'r': u'إثني', u'r2': u'', u'n': u'', u'n2': u'',
              u'j': u'', u'j2': u'', u's': u'*'},
    u'إثنا': {u'i': u'إثنا', u'r': u'إثنا', u'r2': u'', u'n': u'', u'n2': u'',
              u'j': u'', u'j2': u'', u's': u'*'},
    u'ثلاث': {u'i': u'ثَلاث', u'r': u'ثَلاثُ', u'r2': u'ثَلاثٌ', u'n': u'ثَلاثَ',
              u'n2': u'', u'j': u'ثَلاثِ', u'j2': u'ثَلاثٍ', u's': u''},
    u'أربع': {u'i': u'أَرْبَع', u'r': u'أَرْبَعُ', u'r2': u'أَرْبَعٌ', u'n': u'أَرْبَعَ',
              u'n2': u'', u'j': u'أَرْبَعِ', u'j2': u'أَرْبَعٍ', u's': u''},
    u'خمس': {u'i': u'خَمْس', u'r': u'خَمْسُ', u'r2': u'خَمْسٌ', u'n': u'خَمْسَ',
             u'n2': u'', u'j': u'خَمْسِ', u'j2': u'خَمْسٍ', u's': u''},
    u'ست': {u'i': u'سِتّ', u'r': u'سِتُّ', u'r2': u'سِتٌّ', u'n': u'سِتَّ', u'n2': u'',
            u'j': u'سِتِّ', u'j2': u'سِتٍّ', u's': u''},
    u'سبع': {u'i': u'سَبْع', u'r': u'سَبْعُ', u'r2': u'سَبْعٌ', u'n': u'سَبْعَ',
             u'n2': u'', u'j': u'سَبْعِ', u'j2': u'سَبْعٍ', u's': u''},
    u'ثمان': {u'i': u'ثَمَان', u'r': u'ثُمانُ', u'r2': u'ثَمَانٌ', u'n': u'ثَمَانَ',
              u'n2': u'', u'j': u'ثَمَانِ', u'j2': u'ثَمَانٍ', u's': u''},
    u'ثماني': {u'i': u'ثَمانِي', u'r': u'ثَمانِي', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'تسع': {u'i': u'تِسْع', u'r': u'تِسْعُ', u'r2': u'تِسْعٌ', u'n': u'تِسْعَ',
             u'n2': u'', u'j': u'تِسْعِ', u'j2': u'تِسْعٍ', u's': u''},
    u'عشر': {u'i': u'عَشْر', u'r': u'عَشْرُ', u'r2': u'عَشْرٌ', u'n': u'عَشَرَ',
             u'n2': u'', u'j': u'عَشْرِ', u'j2': u'عَشْرٍ', u's': u''},
    u'ثلاثا': {u'i': u'ثَلَاثًا', u'r': u'', u'r2': u'', u'n': u'',
               u'n2': u'ثَلَاثًا', u'j': u'', u'j2': u'', u's': u'*'},
    u'أربعا': {u'i': u'أَرْبَعًا', u'r': u'', u'r2': u'', u'n': u'',
               u'n2': u'أَرْبَعًا', u'j': u'', u'j2': u'', u's': u'*'},
    u'خمسا': {u'i': u'خَمْسًا', u'r': u'', u'r2': u'', u'n': u'', u'n2': u'خَمْسًا',
              u'j': u'', u'j2': u'', u's': u'*'},
    u'ستا': {u'i': u'سِتًّا', u'r': u'', u'r2': u'', u'n': u'', u'n2': u'سِتًّا',
             u'j': u'', u'j2': u'', u's': u'*'},
    u'سبعا': {u'i': u'سَبْعًا', u'r': u'', u'r2': u'', u'n': u'', u'n2': u'سَبْعًا',
              u'j': u'', u'j2': u'', u's': u'*'},
    u'تسعا': {u'i': u'تِسْعًا', u'r': u'', u'r2': u'', u'n': u'', u'n2': u'تِسْعًا',
              u'j': u'', u'j2': u'', u's': u'*'},
    u'عشرا': {u'i': u'عَشْرًا', u'r': u'', u'r2': u'', u'n': u'', u'n2': u'عَشْرًا',
              u'j': u'', u'j2': u'', u's': u'*'},
    u'عشرين': {u'i': u'عِشْرِينَ', u'r': u'عِشْرِينَ', u'r2': u'عِشْرِينَ',
               u'n': u'عِشْرِينَ', u'n2': u'عِشْرِينَ', u'j': u'عِشْرِينَ',
               u'j2': u'عِشْرِينَ', u's': u'*'},
    u'ثلاثين': {u'i': u'ثَلَاثِينَ', u'r': u'ثَلَاثِينَ', u'r2': u'ثَلَاثِينَ',
                u'n': u'ثَلَاثِينَ', u'n2': u'ثَلَاثِينَ', u'j': u'ثَلَاثِينَ',
                u'j2': u'ثَلَاثِينَ', u's': u'*'},
    u'أربعين': {u'i': u'أَرْبَعِينَ', u'r': u'أَرْبَعِينَ', u'r2': u'أَرْبَعِينَ',
                u'n': u'أَرْبَعِينَ', u'n2': u'أَرْبَعِينَ', u'j': u'أَرْبَعِينَ',
                u'j2': u'أَرْبَعِينَ', u's': u'*'},
    u'خمسين': {u'i': u'خَمْسِينَ', u'r': u'خَمْسِينَ', u'r2': u'خَمْسِينَ',
               u'n': u'خَمْسِينَ', u'n2': u'خَمْسِينَ', u'j': u'خَمْسِينَ',
               u'j2': u'خَمْسِينَ', u's': u'*'},
    u'ستين': {u'i': u'سِتِّينَ', u'r': u'سِتِّينَ', u'r2': u'سِتِّينَ', u'n': u'سِتِّينَ',
              u'n2': u'سِتِّينَ', u'j': u'سِتِّينَ', u'j2': u'سِتِّينَ', u's': u'*'},
    u'سبعين': {u'i': u'سَبْعِينَ', u'r': u'سَبْعِينَ', u'r2': u'سَبْعِينَ',
               u'n': u'سَبْعِينَ', u'n2': u'سَبْعِينَ', u'j': u'سَبْعِينَ',
               u'j2': u'سَبْعِينَ', u's': u'*'},
    u'ثمانين': {u'i': u'ثَمانِينَ', u'r': u'ثَمانِينَ', u'r2': u'ثَمانِينَ',
                u'n': u'ثَمانِينَ', u'n2': u'ثَمانِينَ', u'j': u'ثَمانِينَ',
                u'j2': u'ثَمانِينَ', u's': u'*'},
    u'تسعين': {u'i': u'تِسْعِينَ', u'r': u'تِسْعِينَ', u'r2': u'تِسْعِينَ',
               u'n': u'تِسْعِينَ', u'n2': u'تِسْعِينَ', u'j': u'تِسْعِينَ',
               u'j2': u'تِسْعِينَ', u's': u'*'},
    u'مائة': {u'i': u'مِائَة', u'r': u'مائة', u'r2': u'مِائَةٌ', u'n': u'مِائَةَ',
              u'n2': u'مِائَةً', u'j': u'مِائَةِ', u'j2': u'مِائَةٍ', u's': u''},
    u'مئتين': {u'i': u'مئتين', u'r': u'مئتين', u'r2': u'', u'n': u'',
               u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'آلاف': {u'i': u'آلاَف', u'r': u'آلاَفُ', u'r2': u'آلاَفٌ', u'n': u'آلاَفَ',
              u'n2': u'', u'j': u'آلاَفِ', u'j2': u'آلاَفٍ', u's': u''},
    u'ملايين': {u'i': u'مَلاَيِينُ', u'r': u'مَلاَيِينُ', u'r2': u'', u'n': u'',
                u'n2': u'', u'j': u'', u'j2': u'', u's': u'*'},
    u'مليارات': {u'i': u'مِلْيَارَات', u'r': u'مِلْيَارَاتُ', u'r2': u'مِلْيَارَاتٌ',
                 u'n': u'مِلْيَارَاتَ', u'n2': u'مِلْيَارَاتً', u'j': u'مِلْيَارَاتِ',
                 u'j2': u'مِلْيَارَاتٍ', u's': u''},
}

UNIT_WORDS = {
    # i: invariant vocalization ثابت
    # a: added case مضاف إليه
    # n: mansoub منصوب
    # p: plural: جمع
    u'أذرع': {'i': u'أّذْرُعٍ', 'a': u'', 'n': u'', 'p': u'أّذْرُعٍ', },
    u'أرطال': {'i': u'أَرْطَالٍ', 'a': u'', 'n': u'', 'p': u'أَرْطَالٍ', },
    u'أسابيع': {'i': u'أَسَابِيعَ', 'a': u'', 'n': u'', 'p': u'أَسَابِيعَ', },
    u'أسبوع': {'i': u'أُسْبُوع', 'a': u'أُسْبُوعٍ', 'n': u'', 'p': u'أَسَابِيعَ', },
    u'أسبوعا': {'i': u'أُسْبُوعًا', 'a': u'', 'n': u'', 'p': u'', },
    u'أشبار': {'i': u'أَشْبَارٍ', 'a': u'', 'n': u'', 'p': u'أَشْبَارٍ', },
    u'أشهر': {'i': u'أَشْهُرٍ', 'a': u'', 'n': u'', 'p': u'أَشْهُرٍ', },
    u'أعوام': {'i': u'أَعْوَامٍ', 'a': u'', 'n': u'', 'p': u'أَعْوَامٍ', },
    u'أميال': {'i': u'أَمْيَالٍ', 'a': u'', 'n': u'', 'p': u'أَمْيَالٍ', },
    u'أيام': {'i': u'أَيَّامٍ', 'a': u'', 'n': u'', 'p': u'أَيَّامٍ', },
    u'بوصات': {'i': u'بُوصَاتٍ', 'a': u'', 'n': u'', 'p': u'بُوصَاتٍ', },
    u'بوصة': {'i': u'بُوصَة', 'a': u'بُوصَةٍ', 'n': u'بُوصَةً', 'p': u'بُوصَاتٍ', },
    u'جنيه': {'i': u'جُنَيْه', 'a': u'جُنَيْهٍ', 'n': u'', 'p': u'', },
    u'جنيها': {'i': u'جُنَيْهًا', 'a': u'', 'n': u'جُنَيْهًا', 'p': u'جُنَيْهَات', },
    u'جنيهات': {'i': u'جُنَيْهَات', 'a': u'', 'n': u'', 'p': u'جُنَيْهَات', },
    u'دراهم': {'i': u'دَرَاهِمَ', 'a': u'', 'n': u'', 'p': u'دَرَاهِمَ', },
    u'درجات': {'i': u'دَرَجَاتٍ', 'a': u'', 'n': u'', 'p': u'دَرَجَاتٍ', },
    u'درجة': {'i': u'دَرَجَة', 'a': u'دَرَجَةٍ', 'n': u'دَرَجَةً', 'p': u'دَرَجَاتٍ', },
    u'درهم': {'i': u'دِرْهَم', 'a': u'دِرْهَمٍ', 'n': u'', 'p': u'', },
    u'درهما': {'i': u'دِرْهَمًا', 'a': u'', 'n': u'دِرْهَمًا', 'p': u'دَرَاهِمَ', },
    u'دنانير': {'i': u'دَنَانِيرَ', 'a': u'', 'n': u'', 'p': u'دَنَانِيرَ', },
    u'دولار': {'i': u'دُولَار', 'a': u'دُولَارٍ', 'n': u'', 'p': u'', },
    u'دولارا': {'i': u'دُولَارًا', 'a': u'', 'n': u'دُولَارًا', 'p': u'دُولَارَاتٍ', },
    u'دولارات': {'i': u'دُولَارَاتٍ', 'a': u'', 'n': u'', 'p': u'دُولَارَاتٍ', },
    u'دينار': {'i': u'دِينَار', 'a': u'دِينَارٍ', 'n': u'', 'p': u'', },
    u'دينارا': {'i': u'دِينَارًا', 'a': u'', 'n': u'دِينَارًا', 'p': u'دَنَانِيرَ', },
    u'ذراع': {'i': u'ذِرَاع', 'a': u'ذِرَاعٍ', 'n': u'', 'p': u'', },
    u'ذراعا': {'i': u'ذِرَاعًا', 'a': u'', 'n': u'ذِرَاعًا', 'p': u'أّذْرُعٍ', },
    u'رطل': {'i': u'رِطْل', 'a': u'رِطْلٍ', 'n': u'', 'p': u'', },
    u'رطلا': {'i': u'رِطْلًا', 'a': u'', 'n': u'رِطْلًا', 'p': u'أَرْطَالٍ', },
    u'ريال': {'i': u'رِيَال', 'a': u'رِيَالٍ', 'n': u'', 'p': u'', },
    u'ريالا': {'i': u'رِيَالًا', 'a': u'', 'n': u'رِيَالًا', 'p': u'رِيَالَاتٍ', },
    u'ريالات': {'i': u'رِيَالَاتٍ', 'a': u'', 'n': u'', 'p': u'رِيَالَاتٍ', },
    u'سنة': {'i': u'سَنَة', 'a': u'سَنَةٍ', 'n': u'سَنَةً', 'p': u'سَنَوَاتٍ', },
    u'سنتيم': {'i': u'سَنْتِيم', 'a': u'سَنْتِيمٍ', 'n': u'', 'p': u'', },
    u'سنتيما': {'i': u'سَنْتِيمًا', 'a': u'', 'n': u'سَنْتِيمًا', 'p': u'سَنْتِيماتٍ', },
    u'سنتيمات': {'i': u'سَنْتِيماتٍ', 'a': u'', 'n': u'', 'p': u'سَنْتِيماتٍ', },
    u'سنوات': {'i': u'سَنَوَاتٍ', 'a': u'', 'n': u'', 'p': u'سَنَوَاتٍ', },
    u'شبر': {'i': u'شِبْر', 'a': u'شِبْرٍ', 'n': u'', 'p': u'', },
    u'شبرا': {'i': u'شِبْرًا', 'a': u'', 'n': u'شِبْرًا', 'p': u'أَشْبَارٍ', },
    u'شهر': {'i': u'شَهْر', 'a': u'شَهْرٍ', 'n': u'', 'p': u'', },
    u'شهرا': {'i': u'شَهْرًا', 'a': u'', 'n': u'شَهْرًا', 'p': u'أَشْهُرٍ', },
    u'صفحات': {'i': u'صَفْحَاتٍ', 'a': u'', 'n': u'', 'p': u'صَفْحَاتٍ', },
    u'صفحة': {'i': u'صَفْحَة', 'a': u'صَفْحَةٍ', 'n': u'صَفْحَةً', 'p': u'صَفْحَاتٍ', },
    u'عام': {'i': u'عَام', 'a': u'عَامٍ', 'n': u'', 'p': u'', },
    u'عاما': {'i': u'عَامًا', 'a': u'', 'n': u'عَامًا', 'p': u'أَعْوَامٍ', },
    u'فراسخ': {'i': u'فَرَاسِخَ', 'a': u'', 'n': u'', 'p': u'فَرَاسِخَ', },
    u'فرسخ': {'i': u'فَرْسَخ', 'a': u'فَرْسَخٍ', 'n': u'', 'p': u'', },
    u'فرسخا': {'i': u'فَرْسَخًا', 'a': u'', 'n': u'فَرْسَخًا', 'p': u'فَرَاسِخَ', },
    u'فلس': {'i': u'فِلْس', 'a': u'فِلْسٍ', 'n': u'', 'p': u'', },
    u'فلسا': {'i': u'فِلْسًا', 'a': u'', 'n': u'فِلْسًا', 'p': u'فُلُوسٍ', },
    u'فلوس': {'i': u'فُلُوسٍ', 'a': u'', 'n': u'', 'p': u'فُلُوسٍ', },
    u'قرش': {'i': u'قِرْش', 'a': u'قِرْشٍ', 'n': u'', 'p': u'', },
    u'قرشا': {'i': u'قِرْشًا', 'a': u'', 'n': u'قِرْشًا', 'p': u'قُرُوشٍ', },
    u'قروش': {'i': u'قُرُوشٍ', 'a': u'', 'n': u'', 'p': u'قُرُوشٍ', },
    u'كيلوغرام': {'i': u'كِيلُوغَرَام', 'a': u'كِيلُوغَرَامٍ', 'n': u'', 'p': u'', },
    u'كيلوغراما': {'i': u'كِيلُوغَرَامًا', 'a': u'', 'n': u'كِيلُوغَرَامًا',
                   'p': u'كِيلُوغَرَامَاتٍ', },
    u'كيلوغرامات': {'i': u'كِيلُوغَرَامَاتٍ', 'a': u'', 'n': u'',
                    'p': u'كِيلُوغَرَامَاتٍ', },
    u'كيلومتر': {'i': u'كِيلُومِتْر', 'a': u'كِيلُومِتْرٍ', 'n': u'', 'p': u'', },
    u'كيلومترا': {'i': u'كِيلُومِتْرًا', 'a': u'', 'n': u'كِيلُومِتْرًا',
                  'p': u'كِيلُومِتْرَاتٍ', },
    u'كيلومترات': {'i': u'كِيلُومِتْرَاتٍ', 'a': u'', 'n': u'',
                   'p': u'كِيلُومِتْرَاتٍ', },
    u'لتر': {'i': u'لِتْر', 'a': u'لِتْرٍ', 'n': u'', 'p': u'', },
    u'لترا': {'i': u'لِتْرًا', 'a': u'', 'n': u'لِتْرًا', 'p': u'لِتْرَاتٍ', },
    u'لترات': {'i': u'لِتْرَاتٍ', 'a': u'', 'n': u'', 'p': u'لِتْرَاتٍ', },
    u'ليال': {'i': u'لَيَالٍ', 'a': u'', 'n': u'', 'p': u'لَيَالٍ', },
    u'ليرات': {'i': u'لِيرَاتٍ', 'a': u'', 'n': u'', 'p': u'لِيرَاتٍ', },
    u'ليرة': {'i': u'لِيرَة', 'a': u'لِيرَةٍ', 'n': u'لِيرَةً', 'p': u'لِيرَاتٍ', },
    u'ليلة': {'i': u'لَيْلَة', 'a': u'لَيْلَةٍ', 'n': u'لَيْلَةً', 'p': u'لَيَالٍ', },
    u'ميل': {'i': u'مِيل', 'a': u'مِيلٍ', 'n': u'', 'p': u'', },
    u'ميلا': {'i': u'مِيلًا', 'a': u'', 'n': u'مِيلًا', 'p': u'أَمْيَالٍ', },
    u'نقاط': {'i': u'نِقَاطٍ', 'a': u'', 'n': u'', 'p': u'نِقَاطٍ', },
    u'نقطة': {'i': u'نُقْطَة', 'a': u'نُقْطَةٍ', 'n': u'نُقْطَةً', 'p': u'نِقَاطٍ', },
    u'هللات': {'i': u'هَلَلَاتٍ', 'a': u'', 'n': u'', 'p': u'هَلَلَاتٍ', },
    u'هللة': {'i': u'هَلَلَة', 'a': u'هَلَلَةٍ', 'n': u'هَلَلَةً', 'p': u'هَلَلَاتٍ', },
    u'يورو': {'i': u'يُورُو', 'a': u'يُورُو', 'n': u'يُورُو', 'p': u'يُورُو', },
    # ~ u'يورو': {'i':u'يُورُو', 'a':u'', 'n':u'', 'p':u'يُورُو', },
    u'يوم': {'i': u'يَوْم', 'a': u'يَوْمٍ', 'n': u'', 'p': u'', },
    u'يوما': {'i': u'يَوْمًا', 'a': u'', 'n': u'يَوْمًا', 'p': u'أَيَّامٍ', },
}

INDIVIDUALS = {}
INDIVIDUALS[0] = {}
INDIVIDUALS[1] = {}
INDIVIDUALS[2] = {}
INDIVIDUALS[2][1] = {}
INDIVIDUALS[2][2] = {}
INDIVIDUALS[3] = {}
INDIVIDUALS[4] = {}
INDIVIDUALS[5] = {}
INDIVIDUALS[6] = {}
INDIVIDUALS[7] = {}
INDIVIDUALS[8] = {}
INDIVIDUALS[9] = {}
INDIVIDUALS[10] = {}
INDIVIDUALS[11] = {}
INDIVIDUALS[12] = {}
INDIVIDUALS[12][1] = {}
INDIVIDUALS[12][2] = {}
INDIVIDUALS[13] = {}
INDIVIDUALS[14] = {}
INDIVIDUALS[15] = {}
INDIVIDUALS[16] = {}
INDIVIDUALS[17] = {}
INDIVIDUALS[18] = {}
INDIVIDUALS[19] = {}
INDIVIDUALS[20] = {}
INDIVIDUALS[30] = {}
INDIVIDUALS[40] = {}
INDIVIDUALS[50] = {}
INDIVIDUALS[60] = {}
INDIVIDUALS[70] = {}
INDIVIDUALS[80] = {}
INDIVIDUALS[90] = {}
INDIVIDUALS[100] = {}
INDIVIDUALS[200] = {}
INDIVIDUALS[300] = {}
INDIVIDUALS[400] = {}
INDIVIDUALS[500] = {}
INDIVIDUALS[600] = {}
INDIVIDUALS[700] = {}
INDIVIDUALS[800] = {}
INDIVIDUALS[14] = {}
INDIVIDUALS[0][1] = u''
INDIVIDUALS[0][2] = u''
INDIVIDUALS[1][1] = u'واحد'
INDIVIDUALS[1][2] = u'واحدة'
INDIVIDUALS[2][1][1] = u'إثنان'
INDIVIDUALS[2][1][2] = u'إثنين'
INDIVIDUALS[2][2][1] = u'إثنتان'
INDIVIDUALS[2][2][2] = u'إثنتين'

INDIVIDUALS[3][1] = u'ثلاث'
INDIVIDUALS[4][1] = u'أربع'
INDIVIDUALS[5][1] = u'خمس'
INDIVIDUALS[6][1] = u'ست'
INDIVIDUALS[7][1] = u'سبع'
INDIVIDUALS[8][1] = u'ثماني'
INDIVIDUALS[9][1] = u'تسع'
INDIVIDUALS[10][1] = u'عشر'
INDIVIDUALS[3][2] = u'ثلاثة'
INDIVIDUALS[4][2] = u'أربعة'
INDIVIDUALS[5][2] = u'خمسة'
INDIVIDUALS[6][2] = u'ستة'
INDIVIDUALS[7][2] = u'سبعة'
INDIVIDUALS[8][2] = u'ثمانية'
INDIVIDUALS[9][2] = u'تسعة'
INDIVIDUALS[10][2] = u'عشرة'

INDIVIDUALS[11][1] = u'أحد عشر'
INDIVIDUALS[11][2] = u'إحدى عشرة'

INDIVIDUALS[12][1][1] = u'إثنا عشر'
INDIVIDUALS[12][1][2] = u'إثني عشر'
INDIVIDUALS[12][1][3] = u'إثنا عشرة'
INDIVIDUALS[12][1][4] = u'إثني عشرة'
INDIVIDUALS[12][2][1] = u'إثنتا عشرة'
INDIVIDUALS[12][2][2] = u'إثنتي عشرة'

INDIVIDUALS[13][1] = u'ثلاث عشرة'
INDIVIDUALS[14][1] = u'أربع عشرة'
INDIVIDUALS[15][1] = u'خمس عشرة'
INDIVIDUALS[16][1] = u'ست عشرة'
INDIVIDUALS[17][1] = u'سبع عشرة'
INDIVIDUALS[18][1] = u'ثماني عشرة'
INDIVIDUALS[19][1] = u'تسع عشرة'
INDIVIDUALS[13][2] = u'ثلاثة عشر'
INDIVIDUALS[14][2] = u'أربعة عشر'
INDIVIDUALS[15][2] = u'خمسة عشر'
INDIVIDUALS[16][2] = u'ستة عشر'
INDIVIDUALS[17][2] = u'سبعة عشر'
INDIVIDUALS[18][2] = u'ثمانية عشر'
INDIVIDUALS[19][2] = u'تسعة عشر'
INDIVIDUALS[13][3] = u'ثلاثة عشرة'
INDIVIDUALS[14][3] = u'أربعة عشرة'
INDIVIDUALS[15][3] = u'خمسة عشرة'
INDIVIDUALS[16][3] = u'ستة عشرة'
INDIVIDUALS[17][3] = u'سبعة عشرة'
INDIVIDUALS[18][3] = u'ثمانية عشرة'
INDIVIDUALS[19][3] = u'تسعة عشرة'
INDIVIDUALS[13][4] = u'ثلاث عشر'
INDIVIDUALS[14][4] = u'أربع عشر'
INDIVIDUALS[15][4] = u'خمس عشر'
INDIVIDUALS[16][4] = u'ست عشر'
INDIVIDUALS[17][4] = u'سبع عشر'
INDIVIDUALS[18][4] = u'ثماني عشر'
INDIVIDUALS[19][4] = u'تسع عشر'

INDIVIDUALS[20][1] = u'عشرون'
INDIVIDUALS[30][1] = u'ثلاثون'
INDIVIDUALS[40][1] = u'أربعون'
INDIVIDUALS[50][1] = u'خمسون'
INDIVIDUALS[60][1] = u'ستون'
INDIVIDUALS[70][1] = u'سبعون'
INDIVIDUALS[80][1] = u'ثمانون'
INDIVIDUALS[90][1] = u'تسعون'
INDIVIDUALS[20][2] = u'عشرين'
INDIVIDUALS[30][2] = u'ثلاثين'
INDIVIDUALS[40][2] = u'أربعين'
INDIVIDUALS[50][2] = u'خمسين'
INDIVIDUALS[60][2] = u'ستين'
INDIVIDUALS[70][2] = u'سبعين'
INDIVIDUALS[80][2] = u'ثمانين'
INDIVIDUALS[90][2] = u'تسعين'

INDIVIDUALS[200][1] = u'مئتان'
INDIVIDUALS[200][2] = u'مئتين'

INDIVIDUALS[100] = u'مئة'
INDIVIDUALS[300] = u'ثلاثمئة'
INDIVIDUALS[400] = u'أربعمئة'
INDIVIDUALS[500] = u'خمسمئة'
INDIVIDUALS[600] = u'ستمئة'
INDIVIDUALS[700] = u'سبعمئة'
INDIVIDUALS[800] = u'ثمانمئة'
INDIVIDUALS[900] = u'تسعمئة'
COMPLICATIONS = {1: {}, 2: {}, 3: {}}
COMPLICATIONS[1][1] = u'ألفان'
COMPLICATIONS[1][2] = u'ألفين'
COMPLICATIONS[1][3] = u'آلاف'
COMPLICATIONS[1][4] = u'ألف'
COMPLICATIONS[1][5] = u'الاف'

COMPLICATIONS[2][1] = u'مليونان'
COMPLICATIONS[2][2] = u'مليونين'
COMPLICATIONS[2][3] = u'ملايين'
COMPLICATIONS[2][4] = u'مليون'

COMPLICATIONS[3][1] = u'ملياران'
COMPLICATIONS[3][2] = u'مليارين'
COMPLICATIONS[3][3] = u'مليارات'
COMPLICATIONS[3][4] = u'مليار'

TIME_FRACTIONS={
    u'ربع' : u'خمس عشر',
    u'نصف' : u'ثلاثين',
    u'نص' : u'ثلاثين',
    u'تلت' : u'عشرين',
    u'ثلث' : u'عشرين',
    u'الربع' : u'خمس عشر',
    u'النصف' : u'ثلاثين',
    u'النص' : u'ثلاثين',
    u'التلت' : u'عشرين',
    u'الثلث' : u'عشرين'
}

UNITS_ORDINAL_WORDS={
u'ثمان' : u'ثامن',
u'تمان' : u'تامن',
u'ست' : u'سادس',
u'إثني' : u'ثاني',
u'إثني' : u'تاني',
u'ثلاث' : u'ثالث',
u'تلات' : u'تالت',
u'اثنين' : u'ثاني',
u'اتنين' : u'تاني',
u'اثني' : u'ثاني',
u'اتني' : u'تاني',
u'واحد' : u'حادي',
u'أربع' : u'رابع',
u'اربع' : u'رابع',
u'أحد' : u'حادي',
u'احد' : u'حادي',
u'أربعة' : u'رابع',
u'سبع' : u'سابع',
u'ثماني' : u'ثامن',
u'تماني' : u'تامن',
u'خمس' : u'خامس',
u'واحدة' : u'حادي',
u'ثمانية' : u'ثامن',
u'تمانية' : u'تامن',
u'ستة' : u'سادس',
u'تسع' : u'تاسع',
u'تسعة' : u'تاسع',
u'سبعة' : u'سابع',
u'ثلاثة' : u'ثالث',
u'تلاتة' : u'تالت',
u'اثنان' : u'ثاني',
u'اتنان' : u'تاني',
u'عشرة' : u'عاشر',
u'خمسة' : u'خامس',
u'عشر' : u'عاشر',
u'صفر' : u'صفر',
u'إحدى' : u'حادي',
u'احدى' : u'حادي',
u'اثنا' : u'ثاني',
u'إثنا' : u'ثاني',
u'إثنان' : u'ثاني',
u'اتنا' : u'تاني',
u'إتنا' : u'تاني',
u'إتنان' : u'تاني',
}
UNITS_ORDINAL_WORDS_FEMININ={
u'ثمان' : u'ثامنة',
u'ست' : u'سادسة',
u'إثني' : u'ثانية',
u'ثلاث' : u'ثالثة',
u'اثنين' : u'ثانية',
u'اثني' : u'ثانية',
u'واحد' : u'حادية',
u'أربع' : u'رابعة',
u'أحد' : u'حادية',
u'أربعة' : u'رابعة',
u'سبع' : u'سابعة',
u'ثماني' : u'ثامنة',
u'خمس' : u'خامسة',
u'واحدة' : u'حادية',
u'ثمانية' : u'ثامنة',
u'ستة' : u'سادسة',
u'تسع' : u'تاسعة',
u'تسعة' : u'تاسعة',
u'سبعة' : u'سابعة',
u'ثلاثة' : u'ثالثة',
u'اثنان' : u'ثانية',
u'عشرة' : u'عاشرة',
u'خمسة' : u'خامسة',
u'عشر' : u'عاشرة',
u'صفر' : u'صفرة',
u'إحدى' : u'حادية',
u'اثنا' : u'ثانية',
u'إثنا' : u'ثانية',
u'إثنان' : u'ثانية',
}
#~ def __build_normalizer():
    #~ normalizer = [araby.normalize_ligature,
                  #~ araby.normalize_alef,
                  #~ araby.normalize_teh,
                  #~ araby.strip_tashkeel,
                  #~ araby.strip_tatweel,
                  #~ ]
    #~ return util.Composer(normalizer)


def __normalize_composite_dict(le_dict, normalizer):
    res = {}
    for key, value in le_dict.items():
        if isinstance(value, dict):
            res[key] = __normalize_composite_dict(value, normalizer)
        else:
            res[key] = normalizer(value)
    return res


def normalize_constants():
    """
    builds a custom normalizer and applies it to the constants
    """
    # getting them
    global COMPLICATIONS, INDIVIDUALS, UNIT_WORDS, VOCALIZED_NUMBER_WORDS, NUMBER_TEN_FEMININ_UNITS, \
        NUMBER_TEN_MASCULIN_UNITS, NUMBER_WORDS
    # getting the normalizer and a helper function
    normalizer = normalize_searchtext()
    dict_keys_normalizer = lambda dict: {normalizer(key): value
                                         for key, value in dict.items()}

    # normalizing stuff
    UNIT_WORDS = dict_keys_normalizer(UNIT_WORDS)
    VOCALIZED_NUMBER_WORDS = dict_keys_normalizer(VOCALIZED_NUMBER_WORDS)
    NUMBER_WORDS = dict_keys_normalizer(NUMBER_WORDS)
    NUMBER_TEN_MASCULIN_UNITS = tuple(map(normalizer, NUMBER_TEN_MASCULIN_UNITS))
    NUMBER_TEN_FEMININ_UNITS = tuple(map(normalizer, NUMBER_TEN_FEMININ_UNITS))

    # complications are a bit harder
    COMPLICATIONS = {key: {sub_key: sub_value
                           for sub_key, sub_value in COMPLICATION.items()
                           }
                     for key, COMPLICATION in COMPLICATIONS.items()}

    # individual is a bit harder too
    INDIVIDUALS = __normalize_composite_dict(INDIVIDUALS, normalizer)


if __name__ == '__main__':
    print(INDIVIDUALS)
    normalize_constants()
    print(INDIVIDUALS)
