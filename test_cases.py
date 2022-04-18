import unittest
from detect_date import process_dates

class TestSum(unittest.TestCase):

    def test_day_month_year(self):
        rval, *_ = process_dates("يوم التلات الموافق تلتاشر سبعة الفين واحد وعشرين") 
        self.assertTrue("2021/7/13" in rval)

    # def test_day_month(self):
    #     self.assertTrue("13/7/2021" in process_dates("يوم التلات الموافق تلتاشر سبعة الفين واحد وعشرين"), "Should contain 13/7/2021")

if __name__ == '__main__':
    unittest.main()