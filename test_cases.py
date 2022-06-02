import unittest
from detect_date import process_dates

class TestSum(unittest.TestCase):
    def setUp(self):
        self.testfile_path = "Test_Cases.txt"
        f = open(self.testfile_path, 'r')
        test_cases = f.readlines()
        self.test_cases_list = []
        for t in test_cases:
            test_dict = dict()
            t = t.strip()
            if t=="": continue
            t = t.split('|')
            test_dict['sentence'] = t[0]
            test_dict['values'] = t[1:]
            self.test_cases_list.append(test_dict)

    def test_from_file(self):
        for i, tc in enumerate(self.test_cases_list):
            with self.subTest(i=i):
                rval, *_ = process_dates(tc['sentence']) 
                success_flag = 1
                for v in tc['values']:
                    v = '(' + str(v).strip() + ')'
                    if not v in rval: success_flag = 0
                    self.assertIn(v, rval)
                if success_flag == 1: print("SUCCEDED i: ", i, " SENT: ", rval)

    # def test_day_month_year(self):
    #     with self.subTest(i=1):
    #         rval, *_ = process_dates("يوم التلات الموافق تلتاشر سبعة الفين واحد وعشرين") 
    #         self.assertIn("2021/7/13", rval)
    #     with self.subTest(i=2):
    #         rval, *_ = process_dates("يوم التلات الموافق تلتاشر خمسة الفين واحد وعشرين") 
    #         self.assertIn("2021/5/13", rval)

    # def test_day_month(self):
    #     rval, *_ = process_dates("يوم التلات الموافق تلتاشر سبعة")
    #     self.assertIn("7/13", rval)

    # def test_ordinal(self):
    #     rval, *_ = process_dates("يوم السابع من يناير عام عشرين عشرين")
    #     self.assertIn("2020/1/7", rval)

if __name__ == '__main__':
    unittest.main()