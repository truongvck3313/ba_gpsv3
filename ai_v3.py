import logging
import random
import var_v3
import time
import json
from retry import retry
import administration
from selenium.webdriver.common.by import By
import module_other_v3
import login_v3
import os
import shutil
import re
import openpyxl
from xls2xlsx import XLS2XLSX
from retry import retry
from selenium.webdriver.common.keys import Keys
import minitor_v3
import report_v3



def get_info_web():
    var_v3.driver.implicitly_wait(0.05)
    row = 119
    n = 0
    while (n < 50):
        n += 1
        n = str(n)
        row += 1
        path_column = "//*[@aria-label='Data table']/div[1]/div/table/thead/tr/th[" + n + "]"
        path_data = "//*[@class='k-table-tbody']/tr[2]/td[" + n + "]"
        print(n)
        try:
            name_colum = var_v3.driver.find_element(By.XPATH, path_column).text
            name_data = var_v3.driver.find_element(By.XPATH, path_data).text
            print("ten cot web:" .format(name_colum))
            print("data cot web:" .format(name_data))
            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 1, name_colum)
            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_data)
        except:
            pass
        n = int(n)


def get_info_excel(row, sheet):
    row2 = row + 2

    try:
        filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var_v3.excelpath, r"baocao_v3.xlsx"))
    except:
        var_v3.driver.find_element(By.XPATH, var_v3.export_excel).click()
        time.sleep(15)
        filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var_v3.excelpath, r"baocao_v3.xlsx"))

    # #Đọc check file excel
    bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    print("r0")
    try:
        wordbook = openpyxl.load_workbook(var_v3.excelpath + "/baocao_v3.xlsX")
        sheet = wordbook.get_sheet_by_name(sheet)
    except:
        var_v3.driver.find_element(By.XPATH, var_v3.export_excel).click()
        time.sleep(15)
        filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var_v3.excelpath, r"baocao_v3.xlsx"))
        wordbook = openpyxl.load_workbook(var_v3.excelpath + "/baocao_v3.xlsX")
        sheet = wordbook.get_sheet_by_name(sheet)

    print("r1")
    row_tamthoi = 119
    for i in bangchucai:
        row_tamthoi += 1
        if str(sheet[str(i + str(row))].value) == "None":
            break

        cloumn = str(i + str(row))
        print("vị trí tên cột excel: ".format(cloumn))

        cloumn2 = str(i + str(row2))
        print("vị trí data cột excel: ".format(cloumn2))

        name_column = str(sheet[cloumn].value)
        print("Tên cột excel: ".format(name_column))

        data_column = str(sheet[cloumn2].value)
        print(data_column)
        print("Data cột excel: ".format(data_column))

        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row_tamthoi, 3, name_column)
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row_tamthoi, 4, data_column)
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row_tamthoi, 5, cloumn)
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row_tamthoi, 6, cloumn2)



def check_info_web_excel(code, eventname, result, path_module):
    row = 119
    logging.info("-------------------------")
    logging.info(path_module)
    logging.info("Mã - " + code)
    logging.info("Tên sự kiện - " + eventname)
    logging.info("Kết quả - " + result)


    while (row < 150):
        row += 2
        name_column_web = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, 1))
        data_column_web = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, 2))
        name_column_excel = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, 3))
        data_column_excel = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, 4))
        location_name_coloumn = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, 5))
        location_data_coloumn = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, 6))

        if name_column_web == "None":
            break
        logging.info("-------------------------")
        logging.info("Tên cột web: " + name_column_web)
        logging.info("Tên cột excel: " + name_column_excel)
        if name_column_web == name_column_excel:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            if name_column_web in ['Video', 'Lộ trình', 'Hình ảnh', 'Chi tiết']:
                pass
            else:
                logging.error("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Tên cột web: {}\nTên cột excel: {} \nDòng: {}"
                                          .format(name_column_web, name_column_excel, location_name_coloumn))
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                logging.error("Dòng: {}".format(location_name_coloumn))





        logging.info("Dữ liệu web: " + data_column_web)
        logging.info("Dữ liệu excel: " + data_column_excel)
        if name_column_web in ["STT", "Phương tiện", "Thời điểm bắt đầu", "Thời điểm kết thúc", "Thời gian lăn bánh (hh:mm)", "% Thời gian lăn bánh",
                "Thời gian dừng đỗ (hh:mm)", "Thời gian làm thêm tăng ca (hh:mm)", "Số lần dừng đỗ", "Vận tốc trung bình", "Số lần vi phạm lái xe liên tục", "Số lần quá tốc độ",
                               "Địa chỉ đi", "Địa chỉ đến", "Giờ đi", "Giờ đến", "TG hoạt động (giờ:phút)", "Giấy phép lái xe", "Thời gian đăng nhập", "Địa điểm đăng nhập",
                                "Định mức NL/km", "NL tiêu thụ định mức", "Tên trạm", "Thời điểm vào trạm", "Thời điểm ra trạm", "Thời gian trong trạm (HH:mm:ss)",
                               "Lái xe", "Mã nhân viên", "Điện thoại", "Thời điểm dừng đỗ", "Thời gian dừng đỗ (phút)", "Thời gian dừng đỗ (HH:mm:ss)", "Nổ máy khi dừng (phút)",
                               "Bật điều hòa khi dừng (phút)", "Vị trí dừng", "Định mức nhiên liệu trên 1 km", "Thời gian hoạt động (phút)", "Ngày tháng", "Giờ đến - Giờ đi",
                               "Thời gian hoạt động (phút)", "Nhiên liệu tiêu thụ định mức", "Địa điểm bắt đầu", "Địa điểm kết thúc", "Thời gian (s)", "Vận tốc cực đại (km/h)",
                               "Tốc độ cho phép (km/h)", "Thời điểm bắt đầu bật", "Thời gian bật điều hòa khi dừng đỗ (hh:mm)", "Thời gian đăng xuất", "Địa điểm đăng xuất",
                               "Thời gian di chuyển (hh:mm)", "Thời gian dừng đỗ (hh:mm)", "Ngày", "Số lần đăng nhập", "Số lần đăng xuất", "Tổng số lần", "Số phút",
                               "Thời gian bật máy (giờ:phút)", "Thời gian tắt máy (giờ:phút)", "Thời gian mất tín hiệu (giờ:phút)", "Tổng thời gian", "Số lần bật máy",
                               "Số lần tắt máy", "TG bật máy (hh:mm)", "TG lăn bánh (hh:mm)", "TG dừng đỗ bật máy (hh:mm)", "Số lần đổ", "Số lần hút", "Định mức TT bật máy",
                               "Chênh lệch TT và QĐ", "Hành động", "Địa chỉ", "Thời gian", "Loại vi phạm", "Số vi phạm", "Ngày"]:
            print("name vao 1" + name_column_web)
            if data_column_web == data_column_excel:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.error("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Dữ liệu web: {}\nDữ liệu excel: {}\n Dòng: {}"
                                          .format(data_column_web, data_column_excel, location_data_coloumn))
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                logging.error("Dòng: {}".format(location_data_coloumn))


        if name_column_web in ["Km GPS", "Số lít đầu kỳ", "Số lít đổ trong kỳ", "Số lít hút trong kỳ", "Số lít cuối kỳ", "Nhiên liệu tiêu thụ thực tế (lít)", "Định mức thực tế",
                               "Nhiên liệu tiêu thụ", "Quãng đường (m)", "Km cơ", "Vận tốc hành trình (km/h)", "Vận tốc trung bình (km/h)", 'Thời gian dừng đỗ bật điều hòa (hh:mm)',
                               "Tổng thời gian bật điều hòa (hh:mm:ss)", "Từ ngày", "Đến ngày", "Số lít tồn", "Số lít hút", "Số lít đổ", "Số lít tiêu hao", "Định mức QĐ",
                               "Định mức TT km", "Số lít trước", "Số lít sau", "Số lít thay đổi", "NL tiêu thụ"]:
            print("name vao 2" + name_column_web)
            try:
                data_column_web = ''.join(re.findall(r'\d+', data_column_web))[:3]
                data_column_excel = ''.join(re.findall(r'\d+', data_column_excel))[:3]
            except Exception as e:
                logging.error(f"Lỗi khi xử lý dữ liệu: {e}")
            if data_column_web == data_column_excel:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.error("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Dữ liệu web: {}\nDữ liệu excel: {}\n Dòng: {}"
                                          .format(data_column_web, data_column_excel, location_data_coloumn))
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                logging.error("Dòng: {}".format(location_data_coloumn))



def write_from_moth1(fromdate_mon_input1):
    var_v3.driver.implicitly_wait(1)

    from_date = time.strftime("%d/%m/%Y, ", time.localtime())
    from_date = str(from_date)
    print(from_date)

    from_date_year = from_date[6:10]
    print(from_date_year)

    from_moth = from_date[3:5]
    from_moth = int(from_moth)

    from_date_day = from_date[0:2]
    print(from_date_day)
    from_date_day = int(from_date_day)
    if from_date_day == 31 or from_date_day == 30 or from_date_day == 29 or from_date_day == 28:
        from_date_day = "01"

        print("vao 0")
        from_full = str(from_date_day) + str(from_moth) + str(from_date_year)
        print(from_full)
        delete = var_v3.driver.find_element(By.XPATH, fromdate_mon_input1)
        delete.send_keys(Keys.CONTROL, "a")
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, fromdate_mon_input1).send_keys(from_full)
        time.sleep(2)
    else:
        from_moth1 = from_moth - 1
        if from_moth1 == 10:
            from_moth1 = "10"
        if from_moth1 == 9:
            from_moth1 = "09"
        if from_moth1 == 8:
            from_moth1 = "08"
        if from_moth1 == 7:
            from_moth1 = "07"
        if from_moth1 == 6:
            from_moth1 = "06"
        if from_moth1 == 5:
            from_moth1 = "05"
        if from_moth1 == 4:
            from_moth1 = "04"
        if from_moth1 == 3:
            from_moth1 = "03"
        if from_moth1 == 2:
            from_moth1 = "02"
        if from_moth1 == 1:
            from_moth1 = "01"
        if from_moth1 == 0:
            from_moth1 = "01"

        if from_date_day == 10:
            from_date_day = "10"
        if from_date_day == 9:
            from_date_day = "09"
        if from_date_day == 8:
            from_date_day = "08"
        if from_date_day == 7:
            from_date_day = "07"
        if from_date_day == 6:
            from_date_day = "06"
        if from_date_day == 5:
            from_date_day = "05"
        if from_date_day == 4:
            from_date_day = "04"
        if from_date_day == 3:
            from_date_day = "03"
        if from_date_day == 2:
            from_date_day = "02"
        if from_date_day == 1:
            from_date_day = "01"


        print(from_moth1)
        print("vào 1")
        from_full = str(from_date_day) + str(from_moth1) + str(from_date_year)
        print(from_full)
        delete = var_v3.driver.find_element(By.XPATH, fromdate_mon_input1)
        delete.send_keys(Keys.CONTROL, "a")
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, fromdate_mon_input1).send_keys(from_full)
        time.sleep(2)




class ai_cam:



    def report_sumnary_action_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", " 2533_6", " Công ty: 2533 - Công Ty TNHH Vận Tải A Khoa - 2533_6 - akhoa ")

        administration.hover(var_v3.ai)
        administration.hover(var_v3.ai_cam)
        var_v3.driver.find_element(By.XPATH, var_v3.report_sumnary_action_vehicle).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "AI - Báo cáo AI CAM -  Báo cáo tổng hợp hành vi lái xe ",
                                              var_v3.title_page, "BÁO CÁO TỔNG HỢP HÀNH VI LÁI XE", "_BaoCaoTongHopHanhViLaiXe.png")


    def report_sumnary_action_vehicle_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.number_of_violation)
        except:
            ai_cam.report_sumnary_action_vehicle(self, "", "", "")

        write_from_moth1(var_v3.from_day5)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        time.sleep(10)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_report_data2)
        except:
            var_v3.driver.refresh()
            time.sleep(5)
            var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
            time.sleep(10)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "AI - Báo cáo AI CAM -  Báo cáo tổng hợp hành vi lái xe",
                                              var_v3.check_report_data2, "", "_BaoCaoTongHopHanhViLaiXe_TimKiem.png")


    def report_sumnary_action_vehicle_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        module_other_v3.delete_excel()
        report_v3.clearData_luutamthoi_checkexcel(var_v3.path_luutamthoi, "Sheet1", "", "", "", "")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.number_of_violation)
            var_v3.driver.find_element(By.XPATH, var_v3.check_report_data2)
        except:
            ai_cam.report_sumnary_action_vehicle_search(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.export_excel).click()
        time.sleep(15)
        get_info_web()
        try:
            get_info_excel(5, "BAOCAOTONGHOPHANHVILAIXE")
        except:
            var_v3.driver.refresh()
            time.sleep(7)
            ai_cam.report_sumnary_action_vehicle_search(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.export_excel).click()
            time.sleep(15)
            get_info_web()
            get_info_excel(5, "BAOCAOTONGHOPHANHVILAIXE")

        check_info_web_excel(code, eventname, result, "AI - Báo cáo AI CAM -  Báo cáo tổng hợp hành vi lái xe")


    def report_sumnary_action_vehicle_pdf(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        module_other_v3.delete_excel()
        # try:
        #     login_v3.login.logout_v2(self)
        # except:
        #     pass
        #
        # ai_cam.report_sumnary_action_vehicle_search(self, "", "", "")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.number_of_violation)
            var_v3.driver.find_element(By.XPATH, var_v3.check_report_data2)
        except:
            ai_cam.report_sumnary_action_vehicle_search(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.export_pdf1).click()
        time.sleep(10)
        module_other_v3.write_result_dowload_file(code, eventname, result, "AI - Báo cáo AI CAM -  Báo cáo tổng hợp hành vi lái xe",
                                               "baocaotonghophanhvilaixe.pdf", "_BaoCaoTongHopHanhViLaiXe_XuatPDF.png")


    def report_sumnary_action_vehicle_hide_column(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.number_of_violation)
        except:
            ai_cam.report_sumnary_action_vehicle(self, "", "", "")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        except:
            button = var_v3.driver.find_element(By.XPATH, var_v3.hide_column1)
            var_v3.driver.execute_script("arguments[0].click();", button)


        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(2.3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "AI - Báo cáo AI CAM -  Báo cáo tổng hợp hành vi lái xe",
                                                       var_v3.update_success, "Cập nhật thành công", "_BaoCaoTongHopHanhViLaiXe_AnHienCot_Message.png")

        module_other_v3.write_result_displayed_try(code, eventname, result, "AI - Báo cáo AI CAM -  Báo cáo tổng hợp hành vi lái xe",
                                              var_v3.liscense_plate, "_BaoCaoTongHopHanhViLaiXeAnHienCot.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_column1).click()
            time.sleep(2)
            if var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).is_selected() == True:
                var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).click()
                time.sleep(0.5)
                var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            else:
                var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(3)









    def report_a_driving_violation(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", " 2533_6", " Công ty: 2533 - Công Ty TNHH Vận Tải A Khoa - 2533_6 - akhoa ")

        administration.hover(var_v3.ai)
        administration.hover(var_v3.ai_cam)
        var_v3.driver.find_element(By.XPATH, var_v3.report_a_driving_violation).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "AI - Báo cáo AI CAM - Báo cáo vi phạm lái xe",
                                              var_v3.title_page4, "BÁO CÁO VI PHẠM LÁI XE", "_BaoCaoViPhamLaiXe.png")


    def report_a_driving_violation_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.search1)
        except:
            ai_cam.report_a_driving_violation(self, "", "", "")

        write_from_moth1(var_v3.from_day6)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search1).click()
        time.sleep(10)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "AI - Báo cáo AI CAM -  Báo cáo vi phạm lái xe",
                                              var_v3.check_report_a_driving_violation_search, "", "_BaoCaoViPhamLaiXe_TimKiem.png")


    def report_a_driving_violation_get_info(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 152, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 153, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 154, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 155, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 156, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 157, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 152, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 153, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 154, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 155, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 156, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 157, 3, "")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.search1)
        except:
            ai_cam.report_a_driving_violation(self, "", "", "")


        driver_ai_out = var_v3.driver.find_element(By.XPATH, var_v3.driver_ai_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 2, driver_ai_out)

        time_ai_out = var_v3.driver.find_element(By.XPATH, var_v3.time_ai_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 152, 2, time_ai_out)

        vehicle_ai_out = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_ai_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 153, 2, vehicle_ai_out)

        heart_ai_out = var_v3.driver.find_element(By.XPATH, var_v3.heart_ai_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 154, 2, heart_ai_out)

        speed_ai_out = var_v3.driver.find_element(By.XPATH, var_v3.speed_ai_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 155, 2, speed_ai_out)

        channel_ai_out = var_v3.driver.find_element(By.XPATH, var_v3.channel_ai_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 156, 2, channel_ai_out)

        adress_ai_out = var_v3.driver.find_element(By.XPATH, var_v3.adress_ai_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 157, 2, adress_ai_out)

        loaivipham_ai_out = var_v3.driver.find_element(By.XPATH, var_v3.loaivipham_ai_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 158, 2, loaivipham_ai_out)



        var_v3.driver.find_element(By.XPATH, var_v3.get_info_ai_library).click()
        time.sleep(2)
        driver_ai_in = var_v3.driver.find_element(By.XPATH, var_v3.driver_ai_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 3, driver_ai_in)

        time_ai_in = var_v3.driver.find_element(By.XPATH, var_v3.time_ai_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 152, 3, time_ai_in)

        vehicle_ai_in = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_ai_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 153, 3, vehicle_ai_in)

        heart_ai_in = var_v3.driver.find_element(By.XPATH, var_v3.heart_ai_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 154, 3, heart_ai_in)

        speed_ai_in = var_v3.driver.find_element(By.XPATH, var_v3.speed_ai_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 155, 3, speed_ai_in)

        channel_ai_in = var_v3.driver.find_element(By.XPATH, var_v3.channel_ai_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 156, 3, channel_ai_in)

        adress_ai_in = var_v3.driver.find_element(By.XPATH, var_v3.adress_ai_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 157, 3, adress_ai_in)

        logging.info("-------------------------")
        logging.info("AI - Báo cáo AI CAM -  Báo cáo vi phạm lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("True")
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring_see_image_icon_x).click()
            time.sleep(1)
        except:
            pass


    def report_a_driving_violation_check_info(self, code, eventname, result, row , column_out, column_in, name_image):
        logging.info("-------------------------")
        logging.info("AI - Báo cáo AI CAM -  Báo cáo vi phạm lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)

        data_out = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, column_out))
        data_in = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, column_in))
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Màn hình: {}\nKhi click vào ảnh: {}".format(data_out, data_in))
        if name_image == "BaoCaoViPhamLaiXe_LoaiViPham.png":
            if data_in == "None":
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)

        else:
            if data_in == data_out:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)









    def report_driver_rank_month(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", " 2533_6", " Công ty: 2533 - Công Ty TNHH Vận Tải A Khoa - 2533_6 - akhoa ")

        administration.hover(var_v3.ai)
        administration.hover(var_v3.ai_cam)
        var_v3.driver.find_element(By.XPATH, var_v3.report_driver_rank_month).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "AI - Báo cáo AI CAM - Báo cáo xếp hạng lái xe",
                                              var_v3.title_page, "BÁO CÁO XẾP HẠNG LÁI XE", "_BaoCaoXepHangLaiXe.png")


    def report_driver_rank_month_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.average_score)
        except:
            ai_cam.report_driver_rank_month(self, "", "", "")


        # var_v3.driver.find_element(By.XPATH, var_v3.report_driver_rank_month_search).clear()
        # time.sleep(0.5)
        # var_v3.driver.find_element(By.XPATH, var_v3.report_driver_rank_month_search).send_keys("11/2024")
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(7)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "AI - Báo cáo AI CAM - Báo cáo xếp hạng lái xe",
                                              var_v3.check_report_data3, "", "_BaoCaoXepHangLaiXe_TimKiem.png")
        try:
            nodata = var_v3.driver.find_element(By.XPATH, var_v3.nodata).text
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, nodata)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "")
        except:
            pass





    def report_driver_rank_month_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        module_other_v3.delete_excel()
        report_v3.clearData_luutamthoi_checkexcel(var_v3.path_luutamthoi, "Sheet1", "", "", "", "")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.average_score)
            var_v3.driver.find_element(By.XPATH, var_v3.check_report_data3)
        except:
            ai_cam.report_driver_rank_month_search(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.export_excel).click()
        time.sleep(10)
        module_other_v3.write_result_dowload_file(code, eventname, result, "AI - Báo cáo AI CAM - Báo cáo xếp hạng lái xe",
                                               "baocaoxephanglaixe.xlsx", "_BaoCaoXepHangLaiXe_XuatExcel.png")

        # report_v3.get_info_web()
        # report_v3.get_info_excel(6, "BAGPS")
        # report_v3.check_info_web_excel(code, eventname, result, "AI - Báo cáo AI CAM - Báo cáo xếp hạng lái xe")


    def report_driver_rank_month_pdf(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        module_other_v3.delete_excel()
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.average_score)
            var_v3.driver.find_element(By.XPATH, var_v3.check_report_data3)
        except:
            ai_cam.report_driver_rank_month_search(self, "", "", "")
        # try:
        #     login_v3.login.logout_v2(self)
        # except:
        #     pass
        #
        # ai_cam.report_sumnary_action_vehicle_search(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.export_pdf1).click()
        time.sleep(10)
        module_other_v3.write_result_dowload_file(code, eventname, result, "AI - Báo cáo AI CAM - Báo cáo xếp hạng lái xe",
                                               "baocaoxephanglaixe.pdf", "_BaoCaoXepHangLaiXe_XuatPDF.png")


    def report_driver_rank_month_hide_column(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.average_score)
        except:
            ai_cam.report_driver_rank_month(self, "", "", "")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        except:
            button = var_v3.driver.find_element(By.XPATH, var_v3.hide_column1)
            var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(2)

        module_other_v3.write_result_text_try_if(code, eventname, result, "AI - Báo cáo AI CAM - Báo cáo xếp hạng lái xe",
                                                       var_v3.check_title_popup, "TÙY CHỈNH CỘT DỮ LIỆU", "_BaoCaoXepHangLaiXe_AnHienCot.png")

        var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(2)



















