import unittest
from detect_date import process_dates

class TestSum(unittest.TestCase):

    def test_day_month_year(self):
        rval, *_ = process_dates("يوم التلات الموافق تلتاشر سبعة الفين واحد وعشرين") 
        self.assertTrue("2021/7/13" in rval)
        rval, *_ = process_dates("يوم التلات الموافق تلتاشر خمسة الفين واحد وعشرين") 
        self.assertTrue("2021/5/13" in rval)

    def test_day_month(self):
        rval, *_ = process_dates("يوم التلات الموافق تلتاشر سبعة")
        self.assertTrue("7/13" in rval)

    def test_ordinal(self):
        rval, *_ = process_dates("يوم السابع من يناير عام عشرين عشرين")
        self.assertTrue("2020/1/7" in rval)

if __name__ == '__main__':
    unittest.main()