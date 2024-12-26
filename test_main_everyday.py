import time

import module_other_v3
import login_v3
import var_v3
import unittest
import caseid_v3
module_other_v3.timerun()
import module_gpsv3
import report_v3
import ai_v3

# var.writeData(var.path_luutamthoi, "Sheet2", 5, 2, day)




class Test(unittest.TestCase):
    def test_run(self):
        day = 0
        while True:
            module_other_v3.timerun()
            day += 1
            module_other_v3.clearData(var_v3.checklistpath, "Checklist", "", "", "")
            module_other_v3.delete_image()
            module_other_v3.clear_log()
            module_gpsv3.ModuleTest()
            module_gpsv3.retest_casenone(self)
            module_gpsv3.retest_casenone(self)
            module_gpsv3.retest_casefail(self)
            module_gpsv3.retest_casefail(self)
            try:
                module_other_v3.notification_telegram()
            except:
                pass
            print("đang chạy ngày thứ n: ", day)
            if day == 7:
                module_other_v3.clear_log()
                day = 0


if __name__ == "__main__":
    unittest.main()

