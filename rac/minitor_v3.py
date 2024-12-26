import logging
from selenium.webdriver.common.action_chains import ActionChains
import var_v3
import time
import json
from retry import retry
from selenium.webdriver.common.by import By
import module_other_v3
import login_v3
import os
import shutil
from seleniumwire.utils import decode as sw_decode
import mouse
import re


def goto(self, type_goto, data_goto, check_goto):
    var_v3.driver.implicitly_wait(1)
    login_v3.login.login_v2(self, var_v3.data['login']['binhanh_tk'], var_v3.data['login']['binhanh_mk'])
    try:
        var_v3.driver.find_element(By.XPATH, var_v3.icon_un_hide_goto).click()
        time.sleep(1)
    except:
        pass

    if type_goto == "Mã XN":
        var_v3.driver.find_element(By.XPATH, var_v3.goto_xn_checkbox).click()
    if type_goto == "Phương tiện":
        var_v3.driver.find_element(By.XPATH, var_v3.goto_vehicle_checkbox).click()
    if type_goto == "Người dùng":
        var_v3.driver.find_element(By.XPATH, var_v3.goto_user_checkbox).click()

    var_v3.driver.implicitly_wait(5)
    time.sleep(1)
    var_v3.driver.find_element(By.XPATH, var_v3.goto_input).send_keys(data_goto)
    time.sleep(0.5)
    var_v3.driver.find_element(By.XPATH, var_v3.icon_goto).click()
    time.sleep(3)

    try:
        var_v3.driver.find_element(By.XPATH, "//*[text()='" + check_goto + "']")
    except:
        var_v3.driver.find_element(By.XPATH, var_v3.icon_out_goto).click()
        time.sleep(3)




class list_vehicle:


    @retry(tries=3, delay=2, backoff=1, jitter=5)
    def right_click_vehicle(self, desire, check_popup):
        var_v3.driver.implicitly_wait(3)

        var_v3.driver.find_element(By.XPATH, var_v3.all_under).click()
        time.sleep(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        except:
            var_v3.driver.refresh()
            time.sleep(6)

        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        time.sleep(1)
        actions.context_click(button).perform()
        time.sleep(1)

        var_v3.driver.implicitly_wait(2)
        n = 1
        while (n < 15):
            n += 1
            n = str(n)
            pathmodule = "//*[@class='vehicle-context-menu ng-star-inserted']/ul/li[" + n + "]/div/label"
            try:
                name_module = var_v3.driver.find_element(By.XPATH, pathmodule).text
                print(name_module)
                if name_module == desire:
                    var_v3.driver.find_element(By.XPATH, pathmodule).click()
                    time.sleep(2)
                    break
            except:
                pass
            n = int(n)
        var_v3.driver.find_element(By.XPATH, check_popup)



    def right_click_vehicle_move(self, desire, check_popup):
        var_v3.driver.implicitly_wait(3)

        var_v3.driver.find_element(By.XPATH, var_v3.status_vehicle_move).click()
        time.sleep(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle1)
        except:
            var_v3.driver.refresh()
            time.sleep(6)

        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle1)
        actions = ActionChains(var_v3.driver)
        time.sleep(1)
        actions.context_click(button).perform()
        time.sleep(1)

        var_v3.driver.implicitly_wait(2)
        n = 1
        while (n < 15):
            n += 1
            n = str(n)
            pathmodule = "//*[@class='vehicle-context-menu ng-star-inserted']/ul/li[" + n + "]/div/label"
            try:
                name_module = var_v3.driver.find_element(By.XPATH, pathmodule).text
                print(name_module)
                if name_module == desire:
                    var_v3.driver.find_element(By.XPATH, pathmodule).click()
                    time.sleep(2)
                    break
            except:
                pass
            n = int(n)
        var_v3.driver.find_element(By.XPATH, check_popup)




    def search(self, type, data_search):
        var_v3.driver.implicitly_wait(5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_icon_search).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[text()='"+type+"']").click()
        time.sleep(1)
        if type == "Tìm tọa độ":
            var_v3.driver.find_element(By.XPATH, var_v3.search_location_input).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.search_location_input).send_keys(data_search)
            var_v3.driver.find_element(By.XPATH, var_v3.search_iconsearch).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.search_vehicle_input).send_keys(data_search)
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.search_vehicle_select1).click()
        time.sleep(2.5)



    def search_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.all)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        name_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle1).text
        print("tên phương tiên số 1: " +name_vehicle)
        list_vehicle.search(self, "Tìm phương tiện", name_vehicle)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Tìm xe",
                                              var_v3.check_open_search_vehicle, name_vehicle, "GiamSat_TimPhuongTien.png")



    def search_place(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.all)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        list_vehicle.search(self, "Tìm điểm", var_v3.data['minitor']['search_place'])
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Tìm điểm",
                                              var_v3.check_search_place, var_v3.data['minitor']['search_place'], "GiamSat_TimDiem.png")



    def search_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.all)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['search_location'])
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Tìm tọa độ",
                                              var_v3.check_search_location, "Cầu Vĩnh Tuy, P. Long Biên, Q. Long Biên, TP. Hà Nội", "GiamSat_TimToaDo.png")



    def group_select_group(self, code, eventname, result, type_group, path_module):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.all)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.select_group_vehicle).click()
        time.sleep(1.3)
        try:
            var_v3.driver.find_element(By.XPATH, type_group).click()
            time.sleep(1)
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.select_group_vehicle).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, type_group).click()
            time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search_iconsearch).click()
        time.sleep(1)

        count_move = var_v3.driver.find_element(By.XPATH, var_v3.count_move).text
        count_stop_on = var_v3.driver.find_element(By.XPATH, var_v3.count_stop_on).text
        count_stop_off = var_v3.driver.find_element(By.XPATH, var_v3.count_stop_off).text
        count_too_speed1 = var_v3.driver.find_element(By.XPATH, var_v3.count_too_speed1).text
        count_too_speed2 = var_v3.driver.find_element(By.XPATH, var_v3.count_too_speed2).text
        var_v3.driver.find_element(By.XPATH, var_v3.icon_next_status_vehicle).click()
        count_lost_gsm = var_v3.driver.find_element(By.XPATH, var_v3.count_lost_gsm).text
        count_lost_gps = var_v3.driver.find_element(By.XPATH, var_v3.count_lost_gps).text
        count_fee_debt = var_v3.driver.find_element(By.XPATH, var_v3.count_fee_debt).text
        count_all_on = var_v3.driver.find_element(By.XPATH, var_v3.count_all_on).text
        count_all_under = var_v3.driver.find_element(By.XPATH, var_v3.count_all_under).text

        logging.info("-------------------------")
        logging.info(path_module)
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        summary_all_status = int(count_move) \
                               + int(count_stop_on) + int(count_stop_off) \
                               + int(count_too_speed1) + int(count_too_speed2) \
                               + int(count_lost_gsm) + int(count_lost_gps) \
                               + int(count_fee_debt)
        logging.info("Di chuyển: " + str(count_move))
        logging.info("Dừng bật: " + str(count_stop_on))
        logging.info("Di tắt: " + str(count_stop_off))
        logging.info("Quá tốc độ mức 1: " + str(count_too_speed1))
        logging.info("Quá tốc độ mức 2: " + str(count_too_speed1))
        logging.info("Mất GSM: " + str(count_lost_gsm))
        logging.info("Mất GPS: " + str(count_lost_gps))
        logging.info("Nợ phí: " + str(count_fee_debt))
        logging.info("Tổng số xe các trạng thái: " + str(summary_all_status))
        if path_module == "Giám sát - Chọn 1 nhóm":
            logging.info("Tổng số xe trên: " + str(count_all_on))
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Tổng số xe: {}\nTổng trạng thái: {}".format(str(count_all_on), str(summary_all_status)))
            if str(summary_all_status) == str(count_all_on):
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_Chon1Nhom.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_Chon1Nhom.png")

        if path_module == "Giám sát - Chọn tất cả nhóm":
            logging.info("Tổng số xe trên: " + str(count_all_on))
            logging.info("Tổng số xe dưới: " + str(count_all_under))
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Tổng số xe: {}\nTổng trạng thái: {}".format(str(count_all_on), str(summary_all_status)))
            if str(summary_all_status) == str(count_all_on) == str(count_all_under):
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_Chon1Nhom.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_ChonTatCaNhom.png")



    def check_number_of_update_time(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.all)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])


        # var_v3.driver.find_element(By.XPATH, var_v3.status_vehicle_move).click()
        button = var_v3.driver.find_element(By.XPATH, var_v3.status_vehicle_move)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(1)
        double_click = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_vehicle1)
        actions = ActionChains(var_v3.driver)
        actions.double_click(double_click).perform()
        time.sleep(2)
        check_info_vehicle.get_info_vehicle(self, "Phương tiện:", 2)
        check_info_vehicle.get_info_vehicle(self, "Thời gian:", 7)
        time_start = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 7, 2))
        vehicle = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 2, 2))
        logging.info("-------------------------")
        logging.info("Giám sát - check thời gian cập nhật phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Phương tiện - " + vehicle)
        time_s = 0
        while (time_s < 120):
            var_v3.driver.implicitly_wait(1)
            time.sleep(1)
            time_s += 1
            time_s = str(time_s)
            pathtime = "//*[@class='detail-tab ng-star-inserted']/div[3]/div[2]/label"
            try:
                data_time = var_v3.driver.find_element(By.XPATH, pathtime).text
                print("Số giây cập nhật:", time_s, ":", data_time)
                logging.info("Thời gian ban đầu:     " + time_start)
                logging.info("Số giây cập nhật:" + time_s + "    " + data_time)

                if data_time != time_start:
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, vehicle)
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Phương tiện: {}\nTrước cập nhật: "
                                                                                          "{}\nSố giây cập nhật: {}".format(vehicle, time_start, time_s + "\nSau cập nhật: " + data_time))
                    break
            except:
                pass
            time_s = int(time_s)
            if time_s > 119:
                logging.info("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Phương tiện: {}\nTrước cập nhật: "
                                          "{} Số giây cập nhật {}".format(vehicle, time_start, time_s))





    def status_vehicle(self, code, eventname, result, position, group, status):
        var_v3.driver.implicitly_wait(3)

        if position == "quyền quản trị" and group == "công ty không có nhóm":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.ungroup)
            except:
                login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])

        if position == "quyền thường" and group == "công ty không có nhóm":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.ungroup_1)
            except:
                login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_thuong_tk2'], var_v3.data['login']['khongnhom_thuong_mk2'])

        if position == "quyền quản trị" and group == "công ty có nhóm":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            except:
                login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        if position == "quyền thường" and group == "công ty có nhóm":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.e43E02744)
            except:
                login_v3.login.login_v2(self, var_v3.data['login']['conhom_thuong_tk'], var_v3.data['login']['conhom_thuong_mk'])

        if position == "quyền quản trị" and group == "công ty không có nhóm2":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.ctyanhngocminh)
            except:
                login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk2'], var_v3.data['login']['conhom_quantri_mk2'])

        if position == "quyền thường" and group == "công ty không có nhóm2":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.truonganphat)
            except:
                login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_thuong_tk3'], var_v3.data['login']['khongnhom_thuong_mk3'])

        if position == "quyền quản trị" and group == "công ty có nhóm2":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.cttoancau)
            except:
                login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk3'], var_v3.data['login']['conhom_quantri_mk3'])

        if position == "quyền thường" and group == "công ty có nhóm2":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.tranquocdungdn)
            except:
                login_v3.login.login_v2(self, var_v3.data['login']['conhom_thuong_tk2'], var_v3.data['login']['conhom_thuong_mk2'])

        try:
            # var_v3.driver.find_element(By.XPATH, "//*[@title='"+status+"']/div[2]").click()
            button = var_v3.driver.find_element(By.XPATH, "//*[@title='"+status+"']/div[2]")
            var_v3.driver.execute_script("arguments[0].click();", button)
            print("n1")
        except:
            button = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_icon_right)
            var_v3.driver.execute_script("arguments[0].click();", button)
            # var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_icon_right).click()
            time.sleep(1)
            print("n2")
            try:
                # var_v3.driver.find_element(By.XPATH, "//*[@title='"+status+"']/div[2]").click()
                button = var_v3.driver.find_element(By.XPATH, "//*[@title='" + status + "']/div[2]")
                var_v3.driver.execute_script("arguments[0].click();", button)
                print("n3")
            except:
                # var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_icon_left).click()
                button = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_icon_left)
                var_v3.driver.execute_script("arguments[0].click();", button)
                time.sleep(1)
                # var_v3.driver.find_element(By.XPATH, "//*[@title='" + status + "']/div[2]").click()
                button = var_v3.driver.find_element(By.XPATH, "//*[@title='" + status + "']/div[2]")
                var_v3.driver.execute_script("arguments[0].click();", button)
                print("n4")
        time.sleep(1.5)
        count_vehicle_all_on = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_all_on).text
        count_vehicle_all_under = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_all_under).text


        logging.info("-------------------------")
        logging.info("Giám sát - check trạng thái phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)


        if status == "Nhấp để lọc Di chuyển":
            module_other_v3.write_result_text_try_if_status_vehicle(code, eventname, result, "Giám sát - check trạng thái phương tiện",
                                                     count_vehicle_all_on, status, var_v3.count_vehicle_move, count_vehicle_all_on,
                                                     "_GiamSat_DiChuyen.png")

        if status == "Nhấp để lọc Dừng - bật":
            module_other_v3.write_result_text_try_if_status_vehicle(code, eventname, result, "Giám sát - check trạng thái phương tiện",
                                                     count_vehicle_all_on, status, var_v3.count_vehicle_stop_on, count_vehicle_all_on,
                                                     "_GiamSat_DungBat.png")

        if status == "Nhấp để lọc Dừng - tắt":
            module_other_v3.write_result_text_try_if_status_vehicle(code, eventname, result, "Giám sát - check trạng thái phương tiện",
                                                     count_vehicle_all_on, status, var_v3.count_vehicle_stop_off, count_vehicle_all_on,
                                                     "_GiamSat_DungTat.png")

        if status == "Nhấp để lọc Quá tốc độ mức 1":
            module_other_v3.write_result_text_try_if_status_vehicle(code, eventname, result, "Giám sát - check trạng thái phương tiện",
                                                     count_vehicle_all_on, status, var_v3.count_vehicle_too_speed1, count_vehicle_all_on,
                                                     "_GiamSat_QuaTocDoMuc1.png")

        if status == "Nhấp để lọc Quá tốc độ mức 2":
            module_other_v3.write_result_text_try_if_status_vehicle(code, eventname, result, "Giám sát - check trạng thái phương tiện",
                                                     count_vehicle_all_on, status, var_v3.count_vehicle_too_speed2, count_vehicle_all_on,
                                                     "_GiamSat_QuaTocDoMuc2.png")

        if status == "Nhấp để lọc Mất GSM":
            module_other_v3.write_result_text_try_if_status_vehicle(code, eventname, result, "Giám sát - check trạng thái phương tiện",
                                                     count_vehicle_all_on, status, var_v3.count_vehicle_lost_gsm, count_vehicle_all_on,
                                                     "_GiamSat_MatGSM.png")

        if status == "Nhấp để lọc Mất GPS":
            module_other_v3.write_result_text_try_if_status_vehicle(code, eventname, result, "Giám sát - check trạng thái phương tiện",
                                                     count_vehicle_all_on, status, var_v3.count_vehicle_lost_gps, count_vehicle_all_on,
                                                     "_GiamSat_MatGPS.png")

        if status == "Nhấp để lọc Nợ phí":
            module_other_v3.write_result_text_try_if_status_vehicle(code, eventname, result, "Giám sát - check trạng thái phương tiện",
                                                     count_vehicle_all_on, status, var_v3.count_vehicle_fee_debt, count_vehicle_all_on,
                                                     "_GiamSat_NoPhi.png")



        if status == "Xem tất cả":
            count_vehicle_move = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_move).text
            count_vehicle_stop_on = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_stop_on).text
            count_vehicle_stop_off = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_stop_off).text
            count_vehicle_too_speed1 = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_too_speed1).text

            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_icon_right).click()
            time.sleep(1)
            count_vehicle_too_speed2 = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_too_speed2).text
            count_vehicle_lost_gsm = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_lost_gsm).text
            count_vehicle_lost_gps = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_lost_gps).text
            count_vehicle_fee_debt = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_fee_debt).text
            summary_status = int(count_vehicle_move) + int(count_vehicle_stop_on) + int(count_vehicle_stop_off)\
                            + int(count_vehicle_too_speed1) + int(count_vehicle_too_speed2) + int(count_vehicle_lost_gsm)\
                            + int(count_vehicle_lost_gps) + int(count_vehicle_fee_debt)

            logging.info("-------------------------")
            logging.info("Giám sát - check trạng thái phương tiện")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("Di chuyển: " + count_vehicle_move)
            logging.info("Dừng bật: " + count_vehicle_stop_on)
            logging.info("Dừng tắt: " + count_vehicle_stop_off)
            logging.info("Quá tốc độ mức 1: " + count_vehicle_too_speed1)
            logging.info("Quá tốc độ mức 2: " + count_vehicle_too_speed2)
            logging.info("Mất GSM: " + count_vehicle_lost_gsm)
            logging.info("Mất GPS: " + count_vehicle_lost_gps)
            logging.info("Nợ phí: " + count_vehicle_fee_debt)
            logging.info("Tất cả trên : " + count_vehicle_all_on)
            logging.info("Tất cả dưới : " + count_vehicle_all_under)
            logging.info("Tổng các phương tiện: " + str(summary_status))
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Di chuyển: {}\nDừng - bật: {}\nDừng - tắt: {}\nQuá tốc độ 1: {}\n"
                                                                                  "Quá tốc độ 2: {}\nMất GSM: {}\nMất GPS: {}\nNợ phí: {}\nTất cả trên: {}\n"
                                                                                  "Tất cả dưới: {}\nTổng các phương tiện: {}".format(str(count_vehicle_move),
                                                                                     str(count_vehicle_stop_on), str(count_vehicle_stop_off), str(count_vehicle_too_speed1),
                                                                                     str(count_vehicle_too_speed2), str(count_vehicle_lost_gsm), str(count_vehicle_lost_gps),
                                                                                     str(count_vehicle_fee_debt), str(count_vehicle_all_on), str(count_vehicle_all_under),
                                                                                     str(summary_status)))

            if count_vehicle_all_on == count_vehicle_all_under == str(summary_status):
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_TatCa.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_TatCa.png")

        check_color = var_v3.driver.find_element(By.XPATH, "//*[@title='" + status + "']/div[2]").value_of_css_property("color")
        if check_color == "rgba(45, 156, 219, 1)":
            # var_v3.driver.find_element(By.XPATH, "//*[@title='" + status + "']/div[2]").click()
            button = var_v3.driver.find_element(By.XPATH, "//*[@title='" + status + "']/div[2]")
            var_v3.driver.execute_script("arguments[0].click();", button)
        print("color: "+ check_color)
        time.sleep(1)



    # @retry(tries=3, delay=2, backoff=1, jitter=5)
    def check_onlinehandler(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        # del var_v3.driver.requests
        try:
            for request in var_v3.driver.requests:
                print(request.url)
                if request.url == "https://gps3.binhanh.vn/api/v1/vehicleonline":
                    data1 = sw_decode(request.response.body,
                                      request.response.headers.get('Content-Encoding', 'identity'))
                    data1 = data1.decode("utf8")
                    res = json.loads(data1)
                    i = 0
                    while (i < 500):
                        var_v3.driver.implicitly_wait(5)
                        try:
                            print("phương tiện be số: ", i + 1, res['data'][i]['1'])

                        except:
                            print("Tổng số xe be: ", i)
                            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 3, 2, i)
                            break
                        i += 1
                if request.url == "http://192.168.45.82:8000/api/v1/vehicleonline":
                    data1 = sw_decode(request.response.body,
                                      request.response.headers.get('Content-Encoding', 'identity'))
                    data1 = data1.decode("utf8")
                    res = json.loads(data1)
                    i = 0
                    while (i < 500):
                        var_v3.driver.implicitly_wait(5)
                        try:
                            print("phương tiện be số: ", i + 1, res['data'][i]['1'])

                        except:
                            print("Tổng số xe be: ", i)
                            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 3, 2, i)
                            break
                        i += 1





        except:
            var_v3.driver.refresh()
            time.sleep(6)
            # Tổng số xe api
            for request in var_v3.driver.requests:
                print(request.url)
                if request.url == "https://gps3.binhanh.vn/api/v1/vehicleonline":
                    data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                    data1 = data1.decode("utf8")
                    res = json.loads(data1)
                    i = 0
                    while (i < 500):
                        var_v3.driver.implicitly_wait(5)
                        try:
                            print("phương tiện be số: ", i + 1, res['data'][i]['1'])

                        except:
                            print("Tổng số xe be: ", i)
                            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 3, 2, i)
                            break
                        i += 1
                if request.url == "http://192.168.45.82:8000/api/v1/vehicleonline":
                    data1 = sw_decode(request.response.body,
                                      request.response.headers.get('Content-Encoding', 'identity'))
                    data1 = data1.decode("utf8")
                    res = json.loads(data1)
                    i = 0
                    while (i < 500):
                        var_v3.driver.implicitly_wait(5)
                        try:
                            print("phương tiện be số: ", i + 1, res['data'][i]['1'])

                        except:
                            print("Tổng số xe be: ", i)
                            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 3, 2, i)
                            break
                        i += 1

        count_be = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 3, 2))
        logging.info("-------------------------")
        logging.info("Giám sát - check số lượng danh sách phương tiện web - api")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        check_text = var_v3.driver.find_element(By.XPATH, var_v3.count_vehicle_all_under).text
        logging.info(check_text)
        logging.info(count_be)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Danh sách xe api: {}\nDanh sách xe web: {}".format(count_be, check_text))
        if check_text == count_be:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_CheckSoLuongPhuongtien.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_CheckSoLuongPhuongtien.png")


        #
        # module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - check số lượng danh sách phương tiện web - api",
        #                                          var_v3.count_vehicle_all_under, count_be, "_GiamSat_CheckSoLuongPhuongtien.png")







    def icon_share(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        var_v3.driver.find_element(By.XPATH, var_v3.icon_share).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Icon chia sẻ phương tiện",
                                              var_v3.check_icon_share, "CHIA SẺ PHƯƠNG TIỆN", "GiamSat_IconChiaSePhuongTien.png")



    def icon_share_create_copy(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_share_select_vehicle).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_share_select_vehicle1).click()
        except:
            list_vehicle.icon_share(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_share_select_vehicle).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_share_select_vehicle1).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_share_copy).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_share_create_copy).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Icon chia sẻ phương tiện - Tạo và sao chép",
                                              var_v3.check_icon_share_create_copy, "Thêm mới thành công", "GiamSat_IconChiaSePhuongTien_TaoVaSaoChep.png")



    def icon_share_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()
        except:
            list_vehicle.icon_share(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Icon chia sẻ phương tiện - Tạo và sao chép",
                                              var_v3.icon_close, "GiamSat_IconChiaSePhuongTien_Dong.png")



    def icon_system_status(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Icon hiện trạng hệ thống",
                                              var_v3.check_icon_system_status, "HIỆN TRẠNG HỆ THỐNG", "GiamSat_IconHienTrangHẹThong.png")



    def icon_system_status_group_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_group_vehicle).click()
        except:
            list_vehicle.icon_system_status(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_group_vehicle).click()
        time.sleep(1.3)


        var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_group_vehicle1).click()
        var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_refresh).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Icon hiện trạng hệ thống - Chọn nhóm",
                                              var_v3.check_icon_system_status_group_vehicle, "", "GiamSat_IconHienTrangHẹThong_ChonNhom.png")



    def icon_system_status_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_vehicle).click()
        except:
            list_vehicle.icon_system_status(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_vehicle).click()
        time.sleep(1.3)


        var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_vehicle1).click()
        var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_refresh).click()
        time.sleep(1)
        vehicle_list = var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_vehicle_list).text
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Icon hiện trạng hệ thống - Chọn Phương tiện",
                                              var_v3.icon_system_status_vehicle_input, vehicle_list, "GiamSat_IconHienTrangHẹThong_ChonPhuongTien.png")



    def icon_system_status_refresh(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        del var_v3.driver.requests
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_refresh).click()
        except:
            list_vehicle.icon_system_status(self, "", "", "")
            del var_v3.driver.requests
            var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_refresh).click()
        time.sleep(1.3)
        logging.info("-------------------------")
        logging.info("Giám sát - Icon hiện trạng hệ thống - Icon làm mới")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)

        for request in var_v3.driver.requests:
            if request.url == "https://gps3.binhanh.vn/api/v1/addresses":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                # print(res)
                print(res['statusCode'])
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Status code: {}".format(str(res['statusCode'])))
                if res['statusCode'] == 200:
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            if request.url == "http://192.168.45.82:8000/api/v1/addresses":
                data1 = sw_decode(request.response.body,
                                  request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                # print(res)
                print(res['statusCode'])
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6,
                                          "Status code: {}".format(str(res['statusCode'])))
                if res['statusCode'] == 200:
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")

    def icon_system_status_export_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        module_other_v3.delete_excel()

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_export_excel).click()
        except:
            list_vehicle.icon_system_status(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_export_excel).click()
        time.sleep(5)

        logging.info("Giám sát - Icon hiện trạng hệ thống - Xuất excel")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r"hientranghethong.xlsx"))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "hientranghethong.xlsx")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_HienTrangHeThong_XuatExcel.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_HienTrangHeThong_XuatExcel.png")




    def icon_system_status_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()
        except:
            list_vehicle.icon_system_status(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()
        time.sleep(1.3)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Icon Hiện trạng hệ thống",
                                              var_v3.icon_close, "GiamSat_IconHienTrangHeThong_Dong.png")



    def icon_setting(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Icon Cấu hình hiển thị danh sách phương tiện",
                                              var_v3.check_icon_setting, "CẤU HÌNH HIỂN THỊ DANH SÁCH PHƯƠNG TIỆN", "GiamSat_IconCauHinhHienThi.png")



    def icon_setting_display_all_field(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_all_field).click()
        except:
            list_vehicle.icon_setting(self, "", "", "")

        if var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_all_field1).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_all_field).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting).click()
        time.sleep(2)
        logging.info("-------------------------")
        logging.info("Icon Cấu hình hiển thị danh sách phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        if var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_all_field1).is_selected() == True:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Checkbox tất cả: True")

        else:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_IconCauHinhHienThi_TatCa.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Checkbox tất cả: False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_IconCauHinhHienThi_TatCa.png")



    def icon_setting_display_hide_all_field(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_all_field).click()
        except:
            list_vehicle.icon_setting(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_all_field).click()
        time.sleep(0.5)
        if var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_all_field1).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_all_field).click()
        time.sleep(0.5)


        print(var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_speed).is_selected())
        if var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_speed).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_speed1).click()
        time.sleep(0.5)
        print(var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_speed).is_selected())



        if var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_time).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_time1).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(2)
        # module_other_v3.write_result_not_displayed_try(code, eventname, result, "Icon Cấu hình hiển thị danh sách phương tiện",
        #                                         var_v3.check_icon_setting_display_hide_all_field, "GiamSat_IconCauHinhHienThi_AnTruong.png")

        logging.info("Icon Cấu hình hiển thị danh sách phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            icon_setting_display_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_vehicle2).text
            icon_setting_display_speed = var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_speed2).text
            icon_setting_display_time = var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_time2).text
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "{}, {}, {}".format(icon_setting_display_vehicle, icon_setting_display_speed, icon_setting_display_time))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_IconCauHinhHienThi_AnTruong.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_IconCauHinhHienThi_AnTruong.png")

        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting).click()
        time.sleep(2)



    def icon_setting_display_listvehicle_online(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_listvehicle_online).click()
        except:
            list_vehicle.icon_setting(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_listvehicle_online).click()


        if var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_listvehicle_online).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_listvehicle_online1).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Icon Cấu hình hiển thị danh sách phương tiện",
                                                var_v3.check_listvehicle_online, "", "GiamSat_IconCauHinhHienThi_HienThiDanhSachOnlineDuoiDangNhom.png")

        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting).click()
        time.sleep(2)
        # if var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_listvehicle_online).is_selected() == True:
        #     var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_listvehicle_online1).click()
        # time.sleep(1)



    def icon_setting_display_frame_width(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_frame_width_input).clear()
        except:
            list_vehicle.icon_setting(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_frame_width_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_frame_width_input).send_keys(var_v3.data['minitor']['setting_display_frame_width'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(2)
        logging.info("-------------------------")
        logging.info("Icon Cấu hình hiển thị danh sách phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        check_lframe_width = var_v3.driver.find_element(By.XPATH, var_v3.check_lframe_width).get_attribute("style")
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Độ rộng popup: {}".format(check_lframe_width))
        if check_lframe_width == "width: 651px;":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_IconCauHinhHienThi_DoRongKhung.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_IconCauHinhHienThi_DoRongKhung.png")

        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_frame_width_input).clear()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting_display_frame_width_input).send_keys(var_v3.data['minitor']['setting_display_frame_width_setup'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting).click()
        time.sleep(2)



    def icon_setting_display_save(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        time.sleep(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        except:
            list_vehicle.icon_setting(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Icon Cấu hình hiển thị danh sách phương tiện",
                                                var_v3.check_icon_setting_display_save, "Cập nhật thành công", "GiamSat_IconCauHinhHienThi_Luu.png")

        var_v3.driver.find_element(By.XPATH, var_v3.icon_setting).click()
        time.sleep(2)



    def icon_setting_display_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
        except:
            list_vehicle.icon_setting(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Icon Cấu hình hiển thị danh sách phương tiện",
                                              var_v3.close, "GiamSat_IconCauHinhHienThi_Dong.png")



    # @retry(tries=3, delay=2, backoff=1, jitter=5)
    def icon_refresh(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        del var_v3.driver.requests
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_refresh).click()
        time.sleep(2)
        logging.info("-------------------------")
        logging.info("Giám sát - Icon làm mới")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)

        for request in var_v3.driver.requests:
            if request.url == "https://gps3.binhanh.vn/api/v1/vehicleonline":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                # print(res)
                print(res['userMessage'])
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, res['userMessage'])
                if res['userMessage'] == "COMMON_MESSAGE_SUCCESS_GETDATA":
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            if request.url == "http://192.168.45.82:8000/api/v1/vehicleonline":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                # print(res)
                print(res['userMessage'])
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, res['userMessage'])
                if res['userMessage'] == "COMMON_MESSAGE_SUCCESS_GETDATA":
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")




    def icon_vehicle_color_meaning(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.all)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.close1).click()
            time.sleep(1)
        except:
            pass


        var_v3.driver.find_element(By.XPATH, var_v3.icon_vehicle_color_meaning).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Icon Ý nghĩa màu sắc phương tiện",
                                              var_v3.check_icon_vehicle_color_meaning, "Ý NGHĨA MÀU SẮC PHƯƠNG TIỆN", "GiamSat_IconYNghiaMauSacPhuongTien.png")



    def icon_vehicle_color_meaning_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close1).click()
        except:
            list_vehicle.icon_vehicle_color_meaning(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close1).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Icon Ý nghĩa màu sắc phương tiện",
                                              var_v3.close1, "GiamSat_IconYNghiaMauSacPhuongTien_Dong.png")



    def see_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        see_route_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_again_route)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_hover).perform()
        time.sleep(1)
        # module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Xem lại lộ trình",
        #                                       var_v3.check_right_vehicle_see_route, "4 giờ gần đây", "GiamSat_XemLaiLoTrinh.png")

        logging.info("-------------------------")
        logging.info("Giám sát - Xem lại lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            see_again_15p = var_v3.driver.find_element(By.XPATH, var_v3.see_again_15p).text
            see_again_30p = var_v3.driver.find_element(By.XPATH, var_v3.see_again_30p).text
            see_again_1h = var_v3.driver.find_element(By.XPATH, var_v3.see_again_1h).text
            see_again_2h = var_v3.driver.find_element(By.XPATH, var_v3.see_again_2h).text
            see_again_4h = var_v3.driver.find_element(By.XPATH, var_v3.see_again_4h).text
            see_again_8h = var_v3.driver.find_element(By.XPATH, var_v3.see_again_8h).text
            see_again_inday = var_v3.driver.find_element(By.XPATH, var_v3.see_again_inday).text
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "{}, {}, {}, {}, {}, {}, {}".format(see_again_15p, see_again_30p,
                                                                                                                      see_again_1h, see_again_2h,
                                                                                                                      see_again_4h, see_again_8h,
                                                                                                                      see_again_inday))
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_XemLaiLoTrinh.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_XemLaiLoTrinh.png")




    def see_route_8h_fast(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        except:
            list_vehicle.see_route(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.profile).click()
        time.sleep(1)

        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        see_route_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_again_route)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_hover).perform()
        time.sleep(1)



        see_route_8h_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_route_8h_hover)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_8h_hover).perform()
        time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.see_fast_8h).click()
        time.sleep(4)
        logging.info("-------------------------")
        logging.info("Giám sát - Xem lại lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        # module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Xem lại lộ trình",
        #                                       var_v3.check_right_vehicle_see_route_time, "", "GiamSat_XemLaiLoTrinh_8h_XemNhanh.png")

        try:
            popup = var_v3.driver.find_element(By.XPATH, var_v3.check_title_popup).text
            see_route_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.see_route_vehicle).text
            see_route_time = var_v3.driver.find_element(By.XPATH, var_v3.see_route_time).text
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "{}\n{}\n{}".format(popup, see_route_vehicle, see_route_time))
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_XemLaiLoTrinh_8h_XemNhanh.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_XemLaiLoTrinh_8h_XemNhanh.png")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
            time.sleep(1)
        except:
            pass



    def see_route_8h_newtab(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        except:
            list_vehicle.see_route(self, "", "", "")


        try:
            var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.profile).click()
            time.sleep(1)
        except:
            pass

        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        see_route_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_again_route)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_hover).perform()
        time.sleep(1)


        see_route_8h_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_route_8h_hover)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_8h_hover).perform()
        time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.newtab_8h).click()
        time.sleep(8)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Xem lại lộ trình",
                                              var_v3.check_right_vehicle_see_route_8h_newtab, "Lộ trình", "GiamSat_XemLaiLoTrinh_8h_XemCuaSoMoi.png")
        time.sleep(1)
        module_other_v3.close_tab()
        time.sleep(1)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)



    def see_route_inday_fast(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        except:
            list_vehicle.see_route(self, "", "", "")

        try:
            var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.profile).click()
            time.sleep(1)
        except:
            pass

        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        see_route_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_again_route)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_hover).perform()
        time.sleep(1)


        see_route_inday_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_route_inday_hover)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_inday_hover).perform()
        time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.see_fast_inday).click()
        time.sleep(5)

        logging.info("-------------------------")
        logging.info("Giám sát - Xem lại lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            popup = var_v3.driver.find_element(By.XPATH, var_v3.check_title_popup).text
            see_route_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.see_route_vehicle).text
            see_route_time = var_v3.driver.find_element(By.XPATH, var_v3.see_route_time).text
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "{}\n{}\n{}".format(popup, see_route_vehicle, see_route_time))
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_XemLaiLoTrinh_TrongNgay_XemNhanh.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_XemLaiLoTrinh_TrongNgay_XemNhanh.png")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
            time.sleep(1)
        except:
            pass





        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
            time.sleep(1)
        except:
            pass



    def see_route_inday_newtab(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_43e02740)
            var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        except:
            list_vehicle.see_route(self, "", "", "")


        try:
            var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.profile).click()
            time.sleep(1)
        except:
            pass


        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        see_route_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_again_route)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_hover).perform()
        time.sleep(1)



        see_route_inday_hover = var_v3.driver.find_element(By.XPATH, var_v3.see_route_inday_hover)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(see_route_inday_hover).perform()
        time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.newtab_inday).click()
        time.sleep(8)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Xem lại lộ trình",
                                              var_v3.check_right_vehicle_see_route_8h_newtab, "Lộ trình", "GiamSat_XemLaiLoTrinh_TrongNgay_XemCuaSoMoi.png")
        time.sleep(1)
        module_other_v3.close_tab()
        time.sleep(1)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)



    def share_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        list_vehicle.right_click_vehicle(self, "Chia sẻ phương tiện", var_v3.check_right_vehicle_share_vehicle)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Chia sẻ phương tiện",
                                              var_v3.check_right_vehicle_share_vehicle, "CHIA SẺ PHƯƠNG TIỆN", "GiamSat_ChiaSePhuongTien.png")



    def share_vehicle_x(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()
        except:
            list_vehicle.share_vehicle(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Chia sẻ phương tiện",
                                              var_v3.icon_close, "GiamSat_ChiaSePhuongTien_IconX.png")



    def calculate_distance(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        list_vehicle.right_click_vehicle(self, "Tính khoảng cách", var_v3.check_calculate_distance)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Đo khoảng cách",
                                              var_v3.check_calculate_distance, "TÍNH KHOẢNG CÁCH", "GiamSat_TinhKhoangCach.png")



    def from_vehicle_to_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()
        except:
            list_vehicle.calculate_distance(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.from_vehicle_to_vehicle).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.distance_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.distance_input).send_keys(var_v3.data['minitor']['distance'])

        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_vehicle).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_vehicle1).click()

        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_vehicle_iconcopy).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh).click()
        time.sleep(1.5)
        logging.info("-------------------------")
        logging.info("Giám sát - Đo khoảng cách")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            distance_from_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_from_vehicle).text
            distance_to_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_vehicle).text
            distance_to_km = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_km).text
            distance_to_status = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_status).text
            distance_to_speed = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_speed).text

            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Từ phương tiện: {}\nĐến phương tiện: {}\nKhoảng cách(km): {}"
                                                                                  "\nTrạng thái: {}\n Vận tốc: {}".format(distance_from_vehicle,
                                                                                 distance_to_vehicle, distance_to_km, distance_to_status, distance_to_speed))
            if distance_from_vehicle and distance_to_vehicle and distance_to_km and distance_to_status and distance_to_speed != None:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuXeToiXe.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuXeToiXe.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuXeToiXe.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuXeToiXe.png")


        # module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Đo khoảng cách",
        #                                       var_v3.check_distance, "", "GiamSat_TinhKhoangCach_TuXeToiXe.png")



    def from_vehicle_to_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()
        except:
            list_vehicle.calculate_distance(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.from_vehicle_to_location).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.distance_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.distance_input).send_keys(var_v3.data['minitor']['distance'])

        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_location).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_location1).click()

        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_vehicle_iconcopy).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh).click()
        time.sleep(1.5)
        # module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Đo khoảng cách",
        #                                       var_v3.check_distance, "", "GiamSat_TinhKhoangCach_TuXeToiDiem.png")
        logging.info("-------------------------")
        logging.info("Giám sát - Đo khoảng cách")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            distance_from_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_from_vehicle).text
            distance_to_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_vehicle).text
            distance_to_km = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_km).text
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Từ phương tiện: {}\nĐến điểm: {}\n"
                                                                                  "Khoảng cách(km): {}".format(distance_from_vehicle,
                                                                                     distance_to_vehicle, distance_to_km))
            if distance_from_vehicle and distance_to_vehicle and distance_to_km!= None:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuXeToiDiem.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuXeToiDiem.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuXeToiDiem.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuXeToiDiem.png")





    def from_location_to_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()
        except:
            list_vehicle.calculate_distance(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.from_location_to_location).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.distance_input1).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.distance_input1).send_keys(var_v3.data['minitor']['distance'])



        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_from_location).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_from_location1).click()

        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_location).click()
        time.sleep(1)

        if var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_location1a).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_location1).click()

        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_location2).click()
        time.sleep(2)
        button = var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh)
        var_v3.driver.execute_script("arguments[0].click();", button)

        # var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh).click()
        # time.sleep(1.5)
        # module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Đo khoảng cách",
        #                                       var_v3.check_distance, "", "GiamSat_TinhKhoangCach_TuDiemToiDiem.png")
        logging.info("-------------------------")
        logging.info("Giám sát - Đo khoảng cách")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            distance_from_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_from_vehicle).text
            distance_to_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_vehicle).text
            distance_to_km = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_km).text
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Từ điểm: {}\nĐến điểm: {}\n"
                                                                                  "Khoảng cách(km): {}".format(distance_from_vehicle,
                                                                                     distance_to_vehicle, distance_to_km))

            if distance_from_vehicle and distance_to_vehicle and distance_to_km != None:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuDiemToiDiem.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuDiemToiDiem.png")

        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuDiemToiDiem.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuDiemToiDiem.png")





    def from_location_to_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()
        except:
            list_vehicle.calculate_distance(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.from_location_to_vehicle).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.distance_input2).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.distance_input2).send_keys(var_v3.data['minitor']['distance'])


        var_v3.driver.find_element(By.XPATH, var_v3.from_location_to_vehicle_a).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_to_vehicle1).click()
        time.sleep(1)


        var_v3.driver.find_element(By.XPATH, var_v3.to_vehicle).click()
        time.sleep(1)
        if var_v3.driver.find_element(By.XPATH, var_v3.to_location1_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.to_location1_label).click()

        time.sleep(2)
        button = var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(1.5)
        # module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Đo khoảng cách",
        #                                       var_v3.check_distance, "", "GiamSat_TinhKhoangCach_TuDiemToiPhuongTien.png")
        logging.info("-------------------------")
        logging.info("Giám sát - Đo khoảng cách")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            distance_from_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_from_vehicle).text
            distance_to_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_vehicle).text
            distance_to_km = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_km).text
            distance_to_status = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_status).text
            distance_to_speed = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_speed).text

            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Từ Điểm: {}\nĐến phương tiện: {}\nKhoảng cách(km): {}"
                                                                                  "\nTrạng thái: {}\n Vận tốc: {}".format(distance_from_vehicle,
                                                                                 distance_to_vehicle, distance_to_km, distance_to_status, distance_to_speed))

            if distance_from_vehicle and distance_to_vehicle and distance_to_km and distance_to_status and distance_to_speed != None:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(
                    var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuDiemToiPhuongTien.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuDiemToiPhuongTien.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuDiemToiPhuongTien.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuDiemToiPhuongTien.png")





    def my_location_to_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()
        except:
            list_vehicle.calculate_distance(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.my_location_to_location).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.distance_input2).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.distance_input2).send_keys(var_v3.data['minitor']['distance'])
        time.sleep(1)
        try:
            var_v3.driver.switch_to.alert.accept()
            time.sleep(2)
        except:
            pass


        var_v3.driver.find_element(By.XPATH, var_v3.to_location2).click()
        time.sleep(1)
        if var_v3.driver.find_element(By.XPATH, var_v3.to_location1_input2).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.to_location1_label2).click()

        time.sleep(2)
        button = var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.type_distance).click()
        time.sleep(2)
        # module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Đo khoảng cách",
        #                                       var_v3.check_distance, "", "GiamSat_TinhKhoangCach_TuViTriCuaToiDenPhuongTien.png")
        logging.info("-------------------------")
        logging.info("Giám sát - Đo khoảng cách")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            distance_from_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_from_vehicle).text
            distance_to_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_vehicle).text
            distance_to_km = var_v3.driver.find_element(By.XPATH, var_v3.distance_to_km).text
            print("khoang cách: " + distance_to_km)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Từ vị trí của tôi: {}\nĐến phương tiện: {}\n"
                                                                                  "Khoảng cách(km): {}".format(distance_from_vehicle,
                                                                                     distance_to_vehicle, distance_to_km))

            if distance_from_vehicle and distance_to_vehicle and distance_to_km != None:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(
                    var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuViTriCuaToiDenPhuongTien.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuViTriCuaToiDenPhuongTien.png")

        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_TinhKhoangCach_TuViTriCuaToiDenPhuongTien.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_TinhKhoangCach_TuViTriCuaToiDenPhuongTien.png")




    def calculate_distance_refresh(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        del var_v3.driver.requests
        time.sleep(1)
        try:
            button = var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh)
            var_v3.driver.execute_script("arguments[0].click();", button)
        except:
            list_vehicle.my_location_to_location(self, "", "", "")
            # var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh).click()

        button = var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        button = var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_icon_refresh)
        var_v3.driver.execute_script("arguments[0].click();", button)
        logging.info("-------------------------")
        logging.info("Giám sát - Chuột phải xe - Tính khoảng cách")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for request in var_v3.driver.requests:
            print(request.url[23:41])
            if request.url[23:41] == "/api/v1/addresses/":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                # print(res)
                print(res['statusCode'])
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Status code: {}".format(str(res['statusCode'])))
                if res['statusCode'] == 200:
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            if request.url[25:43] == "/api/v1/addresses/":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                # print(res)
                print(res['statusCode'])
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Status code: {}".format(str(res['statusCode'])))
                if res['statusCode'] == 200:
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")






    def calculate_distance_export_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        module_other_v3.delete_excel()
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.distance_input2).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_export_excel).click()
        except:
            list_vehicle.calculate_distance(self, "", "", "")
            list_vehicle.from_vehicle_to_vehicle(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.calculate_distance_export_excel).click()
        time.sleep(5)

        logging.info("Giám sát - Chuột phải xe - Tính khoảng cách")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r"tinhkhoangcach.xlsx"))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_TinhKhoangCach_XuatExcel.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_TinhKhoangCach_XuatExcel.png")



    def calculate_distance_x(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()
        except:
            list_vehicle.calculate_distance(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Chuột phải xe - Tính khoảng cách",
                                              var_v3.icon_close, "GiamSat_TinhKhoangCach_IconX.png")



    def device_info(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        list_vehicle.right_click_vehicle(self, "Thông tin thiết bị", var_v3.check_device_info)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin thiết bị",
                                              var_v3.check_calculate_distance, "THÔNG TIN THIẾT BỊ", "GiamSat_ThongTinThietBi.png")



    def device_info_detail(self, code, eventname, result, path_check, path_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, path_check)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
            list_vehicle.right_click_vehicle(self, "Thông tin thiết bị", var_v3.check_device_info)

        if path_image == "GiamSat_ThongTinThietBi_VIN.png":
            logging.info("-------------------------")
            logging.info("Giám sát - Thông tin thiết bị")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            check_text = var_v3.driver.find_element(By.XPATH, path_check).text
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)


        else:
            module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Thông tin thiết bị",
                                                  path_check, "", path_image)



    def device_info_x(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()
        except:
            list_vehicle.device_info(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Thông tin thiết bị",
                                              var_v3.icon_close, "GiamSat_ThongTinThietBi_IconX.png")



    def quickly_view_images(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        list_vehicle.right_click_vehicle_move(self, "Xem nhanh hình ảnh", var_v3.check_quickly_view_images)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Xem nhanh hình ảnh",
                                              var_v3.check_calculate_distance, "XEM NHANH HÌNH ẢNH", "GiamSat_XemNhanhHinhAnh.png")



    @retry(tries=3, delay=2, backoff=1, jitter=5)
    def quickly_view_images_refresh(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        del var_v3.driver.requests
        time.sleep(2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.quickly_view_images_refresh).click()
        except:
            list_vehicle.quickly_view_images(self, "", "", "")
            del var_v3.driver.requests
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.quickly_view_images_refresh).click()
        time.sleep(2)
        logging.info("-------------------------")
        logging.info("Giám sát - Xem nhanh hình ảnh")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)

        for request in var_v3.driver.requests:
            if request.url == "https://gps3.binhanh.vn/api/v1/image":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                print(res['userMessage'])
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, res['userMessage'])
                if res['userMessage'] == "COMMON_MESSAGE_SUCCESS_GETDATA":
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            if request.url == "http://192.168.45.82:8000/api/v1/image":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                print(res['userMessage'])
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, res['userMessage'])
                if res['userMessage'] == "COMMON_MESSAGE_SUCCESS_GETDATA":
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")




    def view_photo_auto(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.view_photo_auto).click()
        except:
            list_vehicle.quickly_view_images(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.view_photo_auto).click()
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Xem nhanh hình ảnh",
                                              var_v3.check_view_photo_auto, "Dừng xem ảnh tự động", "GiamSat_XemNhanhHinhAnh_XemAnhTuDong.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_view_photo_auto).click()
            time.sleep(1)
        except:
            pass



    def quickly_view_images_detail(self, code, eventname, result, path_check, path_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, path_check)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
            list_vehicle.right_click_vehicle(self, "Xem nhanh hình ảnh", var_v3.check_quickly_view_images)

        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Giám sát - Xem nhanh hình ảnh",
                                              path_check, "", path_image)



    def dowload_images(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_images).click()
        except:
            list_vehicle.quickly_view_images(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_images).click()
        time.sleep(1.5)

        logging.info("Giám sát - Xem nhanh hình ảnh")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r"xemanhhinhanh_icontaianh.png"))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "xemanhhinhanh_icontaianh.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "GiamSat_XemNhanhHinhAnh_IconTaiAnh.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "GiamSat_XemNhanhHinhAnh_IconTaiAnh.png")



    def quickly_view_images_x(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()
        except:
            list_vehicle.quickly_view_images(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Xem nhanh hình ảnh",
                                              var_v3.icon_close, "GiamSat_XemNhanhHinhAnh_IconX.png")



    def online_image_minitor(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        var_v3.driver.find_element(By.XPATH, var_v3.all_under).click()
        time.sleep(1)
        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        time.sleep(1)
        actions.context_click(button).perform()
        time.sleep(1)
        n = 1
        while (n < 25):
            n += 1
            n = str(n)
            pathmodule = "//*[@class='vehicle-context-menu ng-star-inserted']/ul/li[" + n + "]/div/label"
            try:
                name_module = var_v3.driver.find_element(By.XPATH, pathmodule).text
                print(name_module)
                if name_module == "Giám sát hình ảnh trực tuyến":
                    var_v3.driver.find_element(By.XPATH, pathmodule).click()
                    time.sleep(2)
                    break
            except:
                pass
            n = int(n)

        time.sleep(4)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Giám sát hình ảnh trực tuyến",
                                              var_v3.check_online_image_minitor, "GIÁM SÁT HÌNH ẢNH TRỰC TUYẾN", "GiamSat_GiamSatHinhAnhTrucTuyen.png")

        module_other_v3.close_tab()
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)



    def camera_minitor(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        var_v3.driver.find_element(By.XPATH, var_v3.all_under).click()
        time.sleep(1)
        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        time.sleep(1)
        actions.context_click(button).perform()
        time.sleep(1)
        n = 1
        while (n < 25):
            n += 1
            n = str(n)
            pathmodule = "//*[@class='vehicle-context-menu ng-star-inserted']/ul/li[" + n + "]/div/label"
            try:
                name_module = var_v3.driver.find_element(By.XPATH, pathmodule).text
                print(name_module)
                if name_module == "Giám sát camera":
                    var_v3.driver.find_element(By.XPATH, pathmodule).click()
                    time.sleep(2)
                    break
            except:
                pass
            n = int(n)

        time.sleep(4)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Giám sát camera",
                                              var_v3.check_camera_minitor, "GIÁM SÁT CAMERA", "GiamSat_GiamSatCamera.png")

        module_other_v3.close_tab()
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)
        print(var_v3.driver.title)



    def hide_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        list_vehicle.right_click_vehicle(self, "Ẩn phương tiện", var_v3.check_hide_vehicle)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Ẩn phương tiện",
                                              var_v3.check_hide_vehicle, "ẨN PHƯƠNG TIỆN", "GiamSat_AnPhuongTien.png")



    def hidde_on_surveillance(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 2, 2, "")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hidde_on_surveillance).click()
        except:
            list_vehicle.hide_vehicle(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.hidde_on_surveillance).click()
        time.sleep(1)
        name_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.hidde_on_surveillance_vehicle).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        print(name_vehicle)

        var_v3.driver.find_element(By.XPATH, var_v3.no_transmit).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.select_season).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.select_season1).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.hidde_on_surveillance_note).send_keys(var_v3.data['minitor']['hide_vehicle_note'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Ẩn phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", "GiamSat_AnTrenGiamSat.png")
        time.sleep(1)



    def un_hidde_on_surveillance(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        name_vehicle = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 2, 2))

        try:
            var_v3.driver.find_element(By.XPATH, "//*[text()='"+name_vehicle+"']")
            list_vehicle.hidde_on_surveillance(self, "", "", "")
        except:

            hover_manager = var_v3.driver.find_element(By.XPATH, var_v3.hover_manager)
            actions = ActionChains(var_v3.driver)
            actions.move_to_element(hover_manager).perform()
            time.sleep(0.5)

            hover_manager_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.hover_manager_vehicle)
            actions = ActionChains(var_v3.driver)
            actions.move_to_element(hover_manager_vehicle).perform()
            time.sleep(0.5)

            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle).click()
            time.sleep(3.5)
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_input).send_keys(name_vehicle)
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search).click()
            time.sleep(1.5)

            name_vehicle1 = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search1).text
            if name_vehicle1 == name_vehicle:
                var_v3.driver.find_element(By.XPATH, var_v3.un_hidde_on_surveillance).click()
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
                time.sleep(1)
                module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Ẩn phương tiện",
                                                         var_v3.update_success, "Cập nhật thành công", "GiamSat_BoAnTrenGiamSat.png")



    def hide_vehicle_cancel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.cancel).click()
        except:
            list_vehicle.hide_vehicle(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.cancel).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Ẩn phương tiện",
                                              var_v3.cancel, "GiamSat_AnPhuongTien_Huy.png")







class check_info_vehicle:

    def get_info_vehicle(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        while (n < 20):
            n += 1
            n = str(n)
            pathname_detail = "//*[@class='detail-tab ng-star-inserted']/div[" + n + "]/div[1]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH, "//*[@class='detail-tab ng-star-inserted']/div[" + n + "]/div[2]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
        # get_info_vehicle("Thời gian:", 7)


    def get_info_vehicle1(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        while (n < 20):
            n += 1
            n = str(n)
            pathname_detail = "//*[@class='detail-tab ng-star-inserted']/div[7]/div[" + n + "]/label[1]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH,
                                                              "//*[@class='detail-tab ng-star-inserted']/div[7]/div[" + n + "]/label[2]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
        # get_info_vehicle("Thời gian:", 7)


    def get_info_vehicle_v(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        m = 1
        while (n < 25):
            n += 1
            m += 1
            n = str(n)
            m = str(m)
            pathname_detail = "//*[@class='detail-tab ng-star-inserted']/div[4]/div[" + n + "]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH,
                                                              "//*[@class='detail-tab ng-star-inserted']/div[4]/div[" + m + "]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
            m = int(m)
        # get_info_vehicle2("Sở quản lý:", 25)


    def get_info_vehicle_stop(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        m = 1
        while (n < 25):
            n += 1
            m += 1
            n = str(n)
            m = str(m)
            pathname_detail = "//*[@class='detail-tab ng-star-inserted']/div[6]/div[" + n + "]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH, "//*[@class='detail-tab ng-star-inserted']/div[6]/div[" + m + "]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
            m = int(m)
        # get_info_vehicle2("Sở quản lý:", 25)


    def get_info_vehicle_fuel(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        m = 1
        while (n < 25):
            n += 1
            m += 1
            n = str(n)
            m = str(m)
            pathname_detail = "//*[@class='detail-tab ng-star-inserted']/div[8]/div[" + n + "]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH, "//*[@class='detail-tab ng-star-inserted']/div[8]/div[" + m + "]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
            m = int(m)


    def get_info_vehicle_drive(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        m = 1
        while (n < 20):
            n += 1
            m += 1
            n = str(n)
            m = str(m)
            pathname_detail = "//*[@class='detail-tab ng-star-inserted']/div[13]/div[" + n + "]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH, "//*[@class='detail-tab ng-star-inserted']/div[13]/div[" + m + "]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
            m = int(m)
        # get_info_vehicle2("Sở quản lý:", 25)


    def get_info_vehicle2(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        m = 1
        while (n < 25):
            n += 1
            m += 1
            n = str(n)
            m = str(m)
            pathname_detail = "//*[@class='detail-tab ng-star-inserted']/div[11]/div[" + n + "]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH,
                                                              "//*[@class='detail-tab ng-star-inserted']/div[11]/div[" + m + "]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
            m = int(m)
        # get_info_vehicle2("Sở quản lý:", 25)


    def get_info_vehicle3(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.bacam).click()
            time.sleep(0.5)
        except:
            pass

        n = 0
        m = 1
        while (n < 20):
            n += 1
            n = str(n)
            m += 1
            m = str(m)
            pathname_detail = "//*[@class='bacam-data ng-star-inserted']/div[2]/div[" + n + "]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH,
                                                              "//*[@class='bacam-data ng-star-inserted']/div[2]/div[" + m + "]").text
                    time.sleep(0.5)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    print("data: " + name_detail1)
                    break

            except:
                pass
            n = int(n)
            m = int(m)
        # get_info_vehicle3("Tên gói cước:", 30)


    def get_info_vehicle4(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        m = 1
        while (n < 30):
            n += 1
            n = str(n)
            m += 1
            m = str(m)
            pathname_detail = "//*[@class='bacam-data ng-star-inserted']/div[5]/div[" + n + "]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH, "//*[@class='bacam-data ng-star-inserted']/div[5]/div[" + m + "]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 2, name_detail1)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 5, name_detail1)
                    print(name_detail1)
                    print("đã vao đây")
                    break

            except:
                pass
            n = int(n)
            m = int(m)
        # get_info_vehicle4("Kênh lắp camera:", 38)


    def get_status_system(self, field, row):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        while (n < 25):
            n += 1
            n = str(n)
            pathname_detail = "//*[@class='popup box-shadow popup-show']//*[@class='scrollable-content']/table/thead/tr/td[" + n + "]"
            print(n)
            try:
                name_detail = var_v3.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var_v3.driver.find_element(By.XPATH, "//*[@class='popup box-shadow popup-show']//*[@class='scrollable-content']/table/tbody/tr[1]/td[" + n + "]").text
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", row, 4, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
        # get_status_system("self, Thời gian:", 7)






    def get_info_vehicle_online(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        module_other_v3.clearData_luutamthoi(var_v3.path_luutamthoi, "Sheet1", "", "", "")

        #THÔNG TIN XE
        # button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        # actions = ActionChains(var_v3.driver)
        # actions.double_click(button).perform()
        # time.sleep(2)
        # var_v3.driver.find_element(By.XPATH, var_v3.info_vehicle_iconsetting).click()
        # time.sleep(2)
        # var_v3.driver.find_element(By.XPATH, var_v3.group_info_vehicle).click()
        # time.sleep(0.5)
        # var_v3.driver.find_element(By.XPATH, var_v3.group_info_vehicle).click()
        # time.sleep(0.5)
        #
        # var_v3.driver.find_element(By.XPATH, var_v3.group_info_BGT).click()
        # time.sleep(0.5)
        # var_v3.driver.find_element(By.XPATH, var_v3.group_info_BGT).click()
        # time.sleep(0.5)
        #
        # var_v3.driver.find_element(By.XPATH, var_v3.group_info_fee).click()
        # time.sleep(0.5)
        # var_v3.driver.find_element(By.XPATH, var_v3.group_info_fee).click()
        # time.sleep(0.5)
        # var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        # time.sleep(5)

        # var_v3.driver.find_element(By.XPATH, var_v3.status_vehicle_move1).click()
        # var_v3.driver.find_element(By.XPATH, var_v3.status_vehicle_stop_off).click()
        time.sleep(1)
        button = var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2)
        actions = ActionChains(var_v3.driver)
        actions.double_click(button).perform()
        time.sleep(2.5)

        #THÔNG TIN XE
        check_info_vehicle.get_info_vehicle(self, "Phương tiện:", 6)
        check_info_vehicle.get_info_vehicle(self, "Nhóm:", 7)
        check_info_vehicle.get_info_vehicle(self, "Thời gian:", 8)
        check_info_vehicle.get_info_vehicle(self, "Thời gian:", 8)
        check_info_vehicle.get_info_vehicle_v(self, "Vận tốc gps:", 9)
        check_info_vehicle.get_info_vehicle_v(self, "Vận tốc cơ:", 10)
        check_info_vehicle.get_info_vehicle(self, "Km trong ngày:", 11)
        check_info_vehicle.get_info_vehicle_stop(self, "Dừng đỗ:", 12)
        check_info_vehicle.get_info_vehicle_stop(self, "Thời gian dừng đỗ:", 13)
        check_info_vehicle.get_info_vehicle_stop(self, "Dừng đỗ bật máy:", 14)
        check_info_vehicle.get_info_vehicle1(self, "Cửa:", 15)
        check_info_vehicle.get_info_vehicle1(self, "Máy:", 16)
        check_info_vehicle.get_info_vehicle1(self, "Điều hòa:", 17)
        check_info_vehicle.get_info_vehicle1(self, "Bê tông:", 18)
        check_info_vehicle.get_info_vehicle_fuel(self, "Nhiên liệu:", 19)
        check_info_vehicle.get_info_vehicle_fuel(self, "Nhiệt độ:", 20)
        check_info_vehicle.get_info_vehicle(self, "Số VIN:", 21)
        check_info_vehicle.get_info_vehicle(self, "Địa chỉ:", 22)
        check_info_vehicle.get_info_vehicle_drive(self, "Lái xe:", 23)
        check_info_vehicle.get_info_vehicle_drive(self, "Giấy phép lái xe:", 24)
        check_info_vehicle.get_info_vehicle_drive(self, "Điện thoại:", 25)
        check_info_vehicle.get_info_vehicle_drive(self, "TG lái xe liên tục:", 26)
        check_info_vehicle.get_info_vehicle_drive(self, "TG lái xe trong ngày:", 27)
        check_info_vehicle.get_info_vehicle_drive(self, "Số lần quá tốc độ:", 28)
        check_info_vehicle.get_info_vehicle_drive(self, "Sở quản lý:", 29)
        check_info_vehicle.get_info_vehicle_drive(self, "Thông tin thẻ nhớ:", 30)
        try:
            type_of_transport = var_v3.driver.find_element(By.XPATH, var_v3.type_of_transport).text
            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 31, 2, type_of_transport)
        except:
            pass
        try:
            fee_payment_deadline = var_v3.driver.find_element(By.XPATH, var_v3.fee_payment_deadline).text
            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 32, 2, fee_payment_deadline)
        except:
            pass
        var_v3.driver.find_element(By.XPATH, var_v3.zoom_out).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.BACAM).click()
        time.sleep(2)
        check_info_vehicle.get_info_vehicle3(self, "Tên gói cước:", 33)
        check_info_vehicle.get_info_vehicle3(self, "Nhà mạng:", 34)
        check_info_vehicle.get_info_vehicle3(self, "Dung lượng gói cước:", 35)
        check_info_vehicle.get_info_vehicle3(self, "Ngày lưu trữ:", 36)
        check_info_vehicle.get_info_vehicle3(self, "Lưu trữ:", 37)
        check_info_vehicle.get_info_vehicle3(self, "Tính năng định vị:", 38)
        check_info_vehicle.get_info_vehicle3(self, "Tính năng ảnh:", 39)
        check_info_vehicle.get_info_vehicle3(self, "Tính năng video:", 40)
        check_info_vehicle.get_info_vehicle4(self, "Kênh lắp camera:", 41)
        check_info_vehicle.get_info_vehicle4(self, "Kênh hoạt động:", 42)
        check_info_vehicle.get_info_vehicle4(self, "Mạng kết nối:", 43)



        var_v3.driver.find_element(By.XPATH, var_v3.info_vehicle_iconx).click()
        time.sleep(1)
        del var_v3.driver.requests
        var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2).click()
        time.sleep(0.2)
        var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2).click()
        time.sleep(1.5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.info_vehicle_iconx)
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2).click()
            time.sleep(0.2)
            var_v3.driver.find_element(By.XPATH, var_v3.right_vehicle2).click()

        time.sleep(1.5)

        # GET INFO API
        for request in var_v3.driver.requests:
            if request.url == "https://gps3.binhanh.vn/api/v1/vehicleonline":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                var_v3.driver.implicitly_wait(0.05)
                try:
                    api_vehicle = res['data']['vehiclePlate']
                    print("Phương tiện api:", api_vehicle)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 6, 3, str(api_vehicle))

                    api_time = res['data']['vehicleTime']
                    print("Thời gian api:", api_time)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 8, 3, str(api_time))

                    api_v_gps = res['data']['velocityGPS']
                    print("Vận tốc gps api:", api_time)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 9, 3, str(api_v_gps))

                    api_v_co = res['data']['velocityMechanical']
                    print("Vận tốc cơ api:", api_v_co)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 10, 3, str(api_v_co))

                    api_km_in_day = res['data']['totalKm']
                    print("Km trong ngày api:", api_v_co)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 11, 3, int(api_km_in_day))

                    api_stop = res['data']['stopCount']
                    print("Dừng đỗ api:", api_stop)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 12, 3, str(api_stop))

                    api_time_stop = res['data']['lastTimeMove']
                    print("Thời gian dừng đỗ api:", api_time_stop)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 13, 3, str(api_time_stop))

                    api_stop_on_machine = res['data']['onlineExtend']['minuteStopOfManchineOn']
                    print("Thời gian dừng đỗ api:", api_stop_on_machine)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 14, 3, str(api_stop_on_machine))

                    api_fuel_on = res['data']['fuel'][0]['liters']
                    api_fuel_on = int(api_fuel_on)
                    print("Nhiên liệu trên api:", api_fuel_on)
                    api_fuel_under = res['data']['fuel'][0]['capacity']
                    api_fuel_under = int(api_fuel_under)
                    print("Nhiên liệu dưới api:", api_fuel_under)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 19, 3, str(api_fuel_on)+"/"+str(api_fuel_under))

                    api_temperature = res['data']['temperature'][0]
                    print("Nhiệt độ api:", api_temperature)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 20, 3, str(api_temperature))

                    api_vin = res['data']['vin']
                    print("Vin api:", api_vin)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 21, 3, str(api_vin))

                    api_adress = res['data']['vin']
                    print("Địa chỉ api:", api_adress)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 22, 3, str(api_adress))

                    api_drive = res['data']['extTransport']['name']
                    print("Lái xe api:", api_drive)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 23, 3, str(api_drive))

                    api_drive = res['data']['extTransport']['license']
                    print("Giấy phép lái xe api:", api_drive)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 24, 3, str(api_drive))

                    api_phone_number = res['data']['extTransport']['mobile']
                    print("Số điện thoại api:", api_phone_number)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 25, 3, str(api_phone_number))

                    api_time_continute = res['data']['extTransport']['t_continus']
                    print("Thời gian lái xe liên tục api:", api_time_continute)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 26, 3, str(api_time_continute))

                    api_time_day = res['data']['extTransport']['t_day']
                    print("Thời gian lái xe trong ngày api:", api_time_day)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 27, 3, str(api_time_day))

                    api_too_speed = res['data']['extTransport']['speed_o']
                    print("Số lần quá tốc độ api:", api_too_speed)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 28, 3, str(api_too_speed))

                    api_management_department = res['data']['extTransport']['d_name']
                    print("Sở quản lý api:", api_management_department)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 29, 3, str(api_management_department))

                    api_type_transport = res['data']['bgtTransportTypeName']
                    print("Loại hình vận tải api:", api_type_transport)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 31, 3, str(api_type_transport))

                    api_info_fee = res['data']['mcExpried']
                    print("Thông tin hạn đóng phí api:", api_info_fee)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 32, 3, str(api_info_fee))

                    api_package_name = res['data']['packageBAP']['simcardServiceInfo']['code']
                    print("Tên gói cước api:", api_package_name)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 33, 3, str(api_package_name))

                    api_home_network = res['data']['packageBAP']['simcardServiceInfo']['network']
                    print("Tên gói cước api:", api_home_network)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 34, 3, str(api_home_network))

                    api_package_capacity = res['data']['packageBAP']['simcardServiceInfo']['capacity']
                    print("Dung lượng gói cước api:", api_package_capacity)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 35, 3, str(api_package_capacity))

                    api_day_save = res['data']['packageBAP']['simcardServiceInfo']['bandwitdh']
                    print("Ngày lưu trữ api:", api_day_save)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 36, 3, str(api_day_save))

                    api_save = res['data']['packageBAP']['simcardServiceInfo']['smscount']
                    print("Lưu trữ api:", api_save)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 37, 3, str(api_save))

                    api_location = res['data']['packageBAP']['serverServiceInfo']['qcvn31']
                    print("Định vị api:", api_location)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 38, 3, str(api_location))

                    api_image = res['data']['packageBAP']['serverServiceInfo']['image']
                    print("Ảnh api:", api_image)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 39, 3, str(api_image))

                    api_video = res['data']['packageBAP']['serverServiceInfo']['video']
                    print("Định vị api:", api_video)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 40, 3, str(api_video))


                except:
                    print("Không tìm thấy phương tiện: ", )
            if request.url == "http://192.168.45.82:8000/api/v1/vehicleonline":
                data1 = sw_decode(request.response.body,
                                  request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                var_v3.driver.implicitly_wait(0.05)
                try:
                    api_vehicle = res['data']['vehiclePlate']
                    print("Phương tiện api:", api_vehicle)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 6, 3, str(api_vehicle))

                    api_time = res['data']['vehicleTime']
                    print("Thời gian api:", api_time)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 8, 3, str(api_time))

                    api_v_gps = res['data']['velocityGPS']
                    print("Vận tốc gps api:", api_time)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 9, 3, str(api_v_gps))

                    api_v_co = res['data']['velocityMechanical']
                    print("Vận tốc cơ api:", api_v_co)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 10, 3, str(api_v_co))

                    api_km_in_day = res['data']['totalKm']
                    print("Km trong ngày api:", api_v_co)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 11, 3, int(api_km_in_day))

                    api_stop = res['data']['stopCount']
                    print("Dừng đỗ api:", api_stop)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 12, 3, str(api_stop))

                    api_time_stop = res['data']['lastTimeMove']
                    print("Thời gian dừng đỗ api:", api_time_stop)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 13, 3, str(api_time_stop))

                    api_stop_on_machine = res['data']['onlineExtend']['minuteStopOfManchineOn']
                    print("Thời gian dừng đỗ api:", api_stop_on_machine)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 14, 3, str(api_stop_on_machine))

                    api_fuel_on = res['data']['fuel'][0]['liters']
                    api_fuel_on = int(api_fuel_on)
                    print("Nhiên liệu trên api:", api_fuel_on)
                    api_fuel_under = res['data']['fuel'][0]['capacity']
                    api_fuel_under = int(api_fuel_under)
                    print("Nhiên liệu dưới api:", api_fuel_under)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 19, 3,
                                     str(api_fuel_on) + "/" + str(api_fuel_under))

                    api_temperature = res['data']['temperature'][0]
                    print("Nhiệt độ api:", api_temperature)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 20, 3, str(api_temperature))

                    api_vin = res['data']['vin']
                    print("Vin api:", api_vin)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 21, 3, str(api_vin))

                    api_adress = res['data']['vin']
                    print("Địa chỉ api:", api_adress)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 22, 3, str(api_adress))

                    api_drive = res['data']['extTransport']['name']
                    print("Lái xe api:", api_drive)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 23, 3, str(api_drive))

                    api_drive = res['data']['extTransport']['license']
                    print("Giấy phép lái xe api:", api_drive)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 24, 3, str(api_drive))

                    api_phone_number = res['data']['extTransport']['mobile']
                    print("Số điện thoại api:", api_phone_number)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 25, 3, str(api_phone_number))

                    api_time_continute = res['data']['extTransport']['t_continus']
                    print("Thời gian lái xe liên tục api:", api_time_continute)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 26, 3, str(api_time_continute))

                    api_time_day = res['data']['extTransport']['t_day']
                    print("Thời gian lái xe trong ngày api:", api_time_day)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 27, 3, str(api_time_day))

                    api_too_speed = res['data']['extTransport']['speed_o']
                    print("Số lần quá tốc độ api:", api_too_speed)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 28, 3, str(api_too_speed))

                    api_management_department = res['data']['extTransport']['d_name']
                    print("Sở quản lý api:", api_management_department)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 29, 3, str(api_management_department))

                    api_type_transport = res['data']['bgtTransportTypeName']
                    print("Loại hình vận tải api:", api_type_transport)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 31, 3, str(api_type_transport))

                    api_info_fee = res['data']['mcExpried']
                    print("Thông tin hạn đóng phí api:", api_info_fee)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 32, 3, str(api_info_fee))

                    api_package_name = res['data']['packageBAP']['simcardServiceInfo']['code']
                    print("Tên gói cước api:", api_package_name)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 33, 3, str(api_package_name))

                    api_home_network = res['data']['packageBAP']['simcardServiceInfo']['network']
                    print("Tên gói cước api:", api_home_network)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 34, 3, str(api_home_network))

                    api_package_capacity = res['data']['packageBAP']['simcardServiceInfo']['capacity']
                    print("Dung lượng gói cước api:", api_package_capacity)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 35, 3, str(api_package_capacity))

                    api_day_save = res['data']['packageBAP']['simcardServiceInfo']['bandwitdh']
                    print("Ngày lưu trữ api:", api_day_save)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 36, 3, str(api_day_save))

                    api_save = res['data']['packageBAP']['simcardServiceInfo']['smscount']
                    print("Lưu trữ api:", api_save)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 37, 3, str(api_save))

                    api_location = res['data']['packageBAP']['serverServiceInfo']['qcvn31']
                    print("Định vị api:", api_location)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 38, 3, str(api_location))

                    api_image = res['data']['packageBAP']['serverServiceInfo']['image']
                    print("Ảnh api:", api_image)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 39, 3, str(api_image))

                    api_video = res['data']['packageBAP']['serverServiceInfo']['video']
                    print("Định vị api:", api_video)
                    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 40, 3, str(api_video))


                except:
                    print("Không tìm thấy phương tiện: ", )

        # LẤY THÔNG TIN POPUP HIỆN TRẠNG HỆ THỐNG
        name_vehicle = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 6, 2))
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.info_vehicle_iconx).click()
            time.sleep(1)
        except:
            pass

        var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status).click()
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.system_status_vehicle_input).send_keys(name_vehicle)
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_system_status_vehicle1).click()
        time.sleep(1.5)
        check_info_vehicle.get_status_system(self, "Phương tiện", 6)
        check_info_vehicle.get_status_system(self, "V(km/h)", 9)
        check_info_vehicle.get_status_system(self, "Thời gian", 8)
        check_info_vehicle.get_status_system(self, "Km trong ngày", 11)
        check_info_vehicle.get_status_system(self, "Khu vực", 22)
        check_info_vehicle.get_status_system(self, "Lái xe", 23)
        check_info_vehicle.get_status_system(self, "Giấy phép", 24)
        check_info_vehicle.get_status_system(self, "Điều hòa", 17)
        check_info_vehicle.get_status_system(self, "Nhiệt độ", 20)
        check_info_vehicle.get_status_system(self, "Nhiên liệu", 19)
        check_info_vehicle.get_status_system(self, "Trạng thái", 44)

        logging.info("-------------------------")
        logging.info("Giám sát - Lấy dữ liệu api, thông tin xe, hiện trạng hệ thống")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("True")
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_vehicle(self, code, eventname, result):
        info_vehicle = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 6, 2))
        api_vehicle = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 6, 3))
        status_system_vehicle = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 6, 4))
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_vehicle)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_vehicle)
        logging.info("Popup Hiện trạng hệ thống           - " + status_system_vehicle)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}\nHiện trạng: {}"
                                  .format(info_vehicle, api_vehicle, status_system_vehicle))
        if info_vehicle == api_vehicle == status_system_vehicle:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_group(self, code, eventname, result):
        info_vehicle = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 7, 2))
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_vehicle)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_vehicle))
        if info_vehicle != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_time(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 8, 2))
        info_detail1 = info_detail[0:4]
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 8, 3))
        api_detail1 = api_detail[11:15]
        status_system_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 8, 4))
        status_system_detai = status_system_detail[0:4]
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}\nHiện trạng: {}"
                                  .format(info_detail, api_detail, status_system_detail))
        if info_detail1 == api_detail1 == status_system_detai:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_v_gps(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 9, 2)
        info_detail1 = ''.join(re.findall(r'\d+', info_detail))
        info_detail1 = str(info_detail1)

        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 9, 3))

        status_system_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 9, 4))
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}\nHiện trạng: {}"
                                  .format(info_detail, api_detail, status_system_detail))
        if info_detail1 == api_detail == status_system_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_v_co(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 10, 2)
        info_detail1 = ''.join(re.findall(r'\d+', info_detail))
        info_detail1 = str(info_detail1)

        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 10, 3))
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail1 == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_km_in_day(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 11, 2)
        info_detail1 = ''.join(re.findall(r'\d+', info_detail))
        info_detail1 = str(info_detail1)

        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 11, 3))
        api_detail = ''.join(re.findall(r'\d+', api_detail))
        api_detail = str(api_detail)

        status_system_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 11, 4)
        status_system_detail = ''.join(re.findall(r'\d+', status_system_detail))
        status_system_detail = str(status_system_detail)

        print("thong tin: " + info_detail1)
        print("api: " + api_detail)
        print("hien trang: " + status_system_detail)


        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}\nHiện trạng: {}"
                                  .format(info_detail, api_detail, status_system_detail))
        if info_detail1[0:2] == api_detail[0:2] == status_system_detail[0:2]:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_stop(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 12, 2)
        info_detail1 = ''.join(re.findall(r'\d+', info_detail))
        info_detail1 = str(info_detail1)

        api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 12, 3)
        api_detail = ''.join(re.findall(r'\d+', api_detail))
        api_detail = str(api_detail)

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail1)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail1 == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_time_stop(self, code, eventname, result):
        try:
            info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 13, 2)
            info_detail1 = info_detail[11:16]

            api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 13, 3)
            api_detail1 = api_detail[11:16]

            logging.info("_____________________________")
            logging.info("Giám sát - Check thông tin xe")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("API trả về                          - " + api_detail1)
            logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail1)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                      .format(info_detail, api_detail))
            if info_detail1 == api_detail1:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
        except:
            pass



    def check_info_stop_on_machine(self, code, eventname, result):
        try:
            info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 14, 2)
            info_detail1 = str(''.join(re.findall(r'\d+', info_detail)))

            api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 14, 3)
            api_detail1 = str(''.join(re.findall(r'\d+', api_detail)))

            logging.info("_____________________________")
            logging.info("Giám sát - Check thông tin xe")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("API trả về                          - " + api_detail1)
            logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail1)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                      .format(info_detail, api_detail))
            if info_detail1 == api_detail1:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
        except:
            pass



    def check_info_door(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 15, 2)
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_machine(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 16, 2)
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_ari_conditional(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 17, 2)
        status_system_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 17, 4)

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nHiện trạng: {}"
                                  .format(info_detail, status_system_detail))
        if info_detail == status_system_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_concrete(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 18, 2)
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_fuel(self, code, eventname, result):
        try:
            info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 19, 2)
            info_detail1 = str(''.join(re.findall(r'\d+', info_detail)))

            api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 19, 3)
            api_detail1 = str(''.join(re.findall(r'\d+', api_detail)))

            status_system_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 19, 4)
            status_system_detail1 = str(''.join(re.findall(r'\d+', status_system_detail)))

            logging.info("_____________________________")
            logging.info("Giám sát - Check thông tin xe")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("API trả về                          - " + api_detail1)
            logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail1)
            logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail1)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}\nHiện trạng: {}"
                                      .format(info_detail, api_detail, status_system_detail))
            if info_detail1 == api_detail1 == status_system_detail1:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
        except:
            pass



    def check_info_temperature(self, code, eventname, result):
        try:
            info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 20, 2)
            api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 20, 3)
            status_system_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 20, 4)

            logging.info("_____________________________")
            logging.info("Giám sát - Check thông tin xe")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("API trả về                          - " + api_detail)
            logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
            logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}\nHiện trạng: {}"
                                      .format(info_detail, api_detail, status_system_detail))
            if info_detail == status_system_detail:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
        except:
            pass



    def check_info_vin(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 21, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 21, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_adress(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 22, 2)
        status_system_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 22, 4)

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nHiện trạng: {}"
                                  .format(info_detail, status_system_detail))
        if info_detail == status_system_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 23, 2)
        api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 23, 3)
        status_system_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 23, 4)

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}\nHiện trạng: {}"
                                  .format(info_detail, api_detail, status_system_detail))
        if info_detail == api_detail == status_system_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_liscense_plate(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 24, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 24, 3))
        status_system_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 24, 4))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        logging.info("Popup Hiện trạng hệ thống           - " + status_system_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}\nHiện trạng: {}"
                                  .format(info_detail, api_detail, status_system_detail))
        if info_detail == api_detail == status_system_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_phone_number(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 25, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 25, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_time_continute(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 26, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 26, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_time_day(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 27, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 27, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_too_speed(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 28, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 28, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_management_department(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 29, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 29, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_memory(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 30, 2))
        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_type_of_transport(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 31, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 31, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail and api_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_fee(self, code, eventname, result):
        try:
            info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 32, 2))
            api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 32, 3))

            logging.info("_____________________________")
            logging.info("Giám sát - Check thông tin xe")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("API trả về                          - " + api_detail)
            logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                      .format(info_detail, api_detail))
            if info_detail and api_detail != "None":
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
        except:
            pass



    def check_info_package_name(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 33, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 33, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_home_network(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 34, 2))
        api_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 34, 3))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_package_capacity(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 35, 2)
        info_detail1 = str(''.join(re.findall(r'\d+', info_detail)))

        api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 35, 3)
        api_detail1 = str(''.join(re.findall(r'\d+', api_detail)))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail1)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail1)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail1 == api_detail1:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_day_save(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 36, 2)
        info_detail1 = str(''.join(re.findall(r'\d+', info_detail)))

        api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 36, 3)
        api_detail1 = str(''.join(re.findall(r'\d+', api_detail)))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail1)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail1)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if info_detail1 == api_detail1:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_save(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 37, 2)
        info_detail1 = str(''.join(re.findall(r'\d+', info_detail)))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail1)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail1 != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_positioning(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 38, 2)

        api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 38, 3)

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if api_detail == "True":
            api_detail = "Có"
        elif api_detail == "False":
            api_detail = "Không"
        print("api: " + api_detail)

        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_image(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 39, 2)

        api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 39, 3)

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if api_detail == "True":
            api_detail = "Có"
        elif api_detail == "False":
            api_detail = "Không"
        print("api: " + api_detail)

        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_video(self, code, eventname, result):
        info_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 40, 2)

        api_detail = var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 40, 3)

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("API trả về                          - " + api_detail)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}\nApi: {}"
                                  .format(info_detail, api_detail))
        if api_detail == "True":
            api_detail = "Có"
        elif api_detail == "False":
            api_detail = "Không"
        print("api: " + api_detail)

        if info_detail == api_detail:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_channel_camera(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 41, 5))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_channel_activity(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 5))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_network_connect(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 5))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_status(self, code, eventname, result):
        info_detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 44, 4))

        logging.info("_____________________________")
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thông tin xe click 2 lần chuột trái - " + info_detail)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin xe: {}".format(info_detail))
        if info_detail != "None":
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")






class map:

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def map_right_mouse(self, desire, x, y, check_popup):
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.account).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.implicitly_wait(2)
        mouse.move(x, y)
        mouse.click(button='right')
        time.sleep(1.5)
        n = 0
        while (n < 15):
            n += 1
            n = str(n)
            pathcheck = "//*[@class='map-context-menu ng-star-inserted']/div[" + n + "]/label"
            try:
                name_module = var_v3.driver.find_element(By.XPATH, pathcheck).text

                print(name_module)
                if name_module == desire:
                    try:
                        var_v3.driver.find_element(By.XPATH, pathcheck).click()
                        time.sleep(1.5)
                    except:
                        pass
                    break
            except:
                pass
            n = int(n)
        var_v3.driver.find_element(By.XPATH, check_popup)
        time.sleep(1)
        #map.map_right_mouse(self, "Chỉ dẫn đường", "800", "800", var.check_popupchidanduong)



    def zoom_map(self, type, count_zoom):
        var_v3.driver.implicitly_wait(5)
        time.sleep(1)
        i = 0
        if type == "phóng to":
            for i in range(count_zoom):
                i = i + 1
                var_v3.driver.find_element(By.XPATH, var_v3.icon_zoom_in).click()
                print("đã phóng to {} lần".format(i))
                time.sleep(0.7)

        if type == "thu nhỏ":
            for i in range(count_zoom):
                i = i + 1
                var_v3.driver.find_element(By.XPATH, var_v3.icon_zoom_out).click()
                print("đã thu nhỏ {} lần".format(i))
                time.sleep(0.7)
        # map.zoom_map(self, "thu nhỏ", 13)



    def see_adress(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['search_location'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass
        map.map_right_mouse(self, "Xem địa chỉ", "800", "800", var_v3.see_adress_iconx)
        # module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Xem địa chỉ",
        #                                       var_v3.check_search_location, "Cầu Vĩnh Tuy, P. Long Biên, Q. Long Biên, TP. Hà Nội", "_GiamSat_XemDiaChi.png")
        time.sleep(1.5)
        logging.info("-------------------------")
        logging.info("Giám sát - Map - Xem địa chỉ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            see_adress_area = var_v3.driver.find_element(By.XPATH, var_v3.see_adress_area).text
            see_adress_longitude = var_v3.driver.find_element(By.XPATH, var_v3.see_adress_longitude).text #kinh độ
            see_adress_latitude = var_v3.driver.find_element(By.XPATH, var_v3.see_adress_latitude).text
            logging.info(see_adress_area)
            logging.info(see_adress_longitude)
            logging.info(see_adress_latitude)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Địa chỉ: {}\nKinh độ: {}\nVĩ độ: {}"
                                      .format(see_adress_area, see_adress_longitude, see_adress_latitude))

            # if (see_adress_area != "") and (see_adress_longitude != "") and (see_adress_latitude != ""):
            if see_adress_area and see_adress_longitude and see_adress_latitude != "":
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_XemDiaChi.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_XemDiaChi.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_XemDiaChi.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_XemDiaChi.png")



    def see_adress_x(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
        except:
            map.see_adress(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
        time.sleep(1)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Map - Xem địa chỉ",
                                              var_v3.see_adress_iconx, "_GiamSat_XemDiaChi_IconX.png")



    def center_here(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['center_here'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass

        map.map_right_mouse(self, "Trung tâm ở đây", "500", "600", var_v3.check_center_here)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Trung tâm ở đây",
                                              var_v3.check_center_here, "Bạn có chắc chắn muốn đặt vị trí click thành vị trí khởi động?", "_GiamSat_TrungTamODay.png")



    def center_here_igree(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        except:
            map.center_here(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Trung tâm ở đây",
                                              var_v3.update_success, "Cập nhật thành công", "_GiamSat_TrungTamODay_DongY1.png")
        time.sleep(2)
        module_other_v3.write_result_displayed_try(code, eventname, result, "Giám sát - Map - Trung tâm ở đây",
                                              var_v3.check_center_here_igree, "_GiamSat_TrungTamODay_DongY2.png")

        time.sleep(1)
        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['169hoangmai'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass
        map.map_right_mouse(self, "Trung tâm ở đây", "500", "600", var_v3.check_center_here)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(2)



    def center_here_cancel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.cancel1).click()
        except:
            map.center_here(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.cancel1).click()
        time.sleep(1)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Map - Trung tâm ở đây",
                                              var_v3.cancel1, "_GiamSat_TrungTamODay_Huy.png")



    def come_center(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['center_here'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass

        map.map_right_mouse(self, "Về trung tâm", "600", "600", var_v3.account)

        module_other_v3.write_result_displayed_try(code, eventname, result, "Giám sát - Map - Về trung tâm",
                                              var_v3.check_come_center, "_GiamSat_VeTrungTam.png")

        try:
            diem_check = var_v3.driver.find_element(By.XPATH, var_v3.check_come_center1).text
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, diem_check)
        except:
            pass





    def create_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['giangvolake'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.implicitly_wait(1.5)
        try:
            button = var_v3.driver.find_element(By.XPATH, var_v3.create_locationv3)
            action = ActionChains(var_v3.driver)
            action.context_click(button).perform()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.delete_location).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1.5)
        except:
            pass
        var_v3.driver.implicitly_wait(5)
        map.map_right_mouse(self, "Tạo điểm", "600", "800", var_v3.title_right_mouse)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                              var_v3.title_right_mouse, "TẠO ĐIỂM", "_GiamSat_TaoDiem.png")



    def fil_info_save(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.radius).clear()
        except:
            map.create_location(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.radius).clear()

        var_v3.driver.find_element(By.XPATH, var_v3.radius).send_keys(var_v3.data['minitor']['radius'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.type_location).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.type_location_electronic_lock).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.name_location1).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.name_location1).send_keys(var_v3.data['minitor']['name_location'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.name_private).send_keys(var_v3.data['minitor']['name_private'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.location).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.location).send_keys(var_v3.data['minitor']['location'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                              var_v3.add_new_success, "Thêm mới thành công", "_GiamSat_TaoDiem_Luu.png")



    def share_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.create_locationv3)
        except:
            map.fil_info_save(self, "", "", "")

        button = var_v3.driver.find_element(By.XPATH, var_v3.create_locationv3)
        action = ActionChains(var_v3.driver)
        action.context_click(button).perform()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.share_location).click()
        time.sleep(1.3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                              var_v3.check_share_location, "Sao chép liên kết chia sẻ thành công", "_GiamSat_TaoDiem_ChiaSeViTri.png")



    def update_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.create_locationv3)
        except:
            map.fil_info_save(self, "", "", "")

        button = var_v3.driver.find_element(By.XPATH, var_v3.create_locationv3)
        action = ActionChains(var_v3.driver)
        action.context_click(button).perform()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.update_location).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.name_location1).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.name_location1).send_keys(var_v3.data['minitor']['update_location'])
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(1)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                              var_v3.update_success, "Cập nhật thành công", "_GiamSat_TaoDiem_CapNhatDiem.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
            time.sleep(1)
        except:
            pass



    def delete_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.create_locationv3)
        except:
            map.fil_info_save(self, "", "", "")

        button = var_v3.driver.find_element(By.XPATH, var_v3.create_locationv3)
        action = ActionChains(var_v3.driver)
        action.context_click(button).perform()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.delete_location).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                              var_v3.delete_success, "Xóa thành công", "_GiamSat_TaoDiem_XoaDiem.png")



    def edit_drawing_area(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        map.create_location(self, "", "", "")
        var_v3.driver.find_element(By.XPATH, var_v3.edit_drawing_area).click()
        time.sleep(1.5)
        module_other_v3.write_result_displayed_try(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                                var_v3.check_edit_drawing_area, "_GiamSat_TaoDiem_SuaVungVe.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.cancel).click()
            time.sleep(1)
        except:
            pass



    def redraw(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.redraw).click()
        except:
            map.create_location(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.redraw).click()
        time.sleep(1.5)
        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                                var_v3.edit_drawing_area, "_GiamSat_TaoDiem_VeLai.png")



    def create_location_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
        except:
            map.create_location(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
        time.sleep(1)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                              var_v3.close, "_GiamSat_TaoDiem_Dong.png")



    def find_vehicle_in_area(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        map.zoom_map(self, "thu nhỏ", 4)
        time.sleep(2)
        map.map_right_mouse(self, "Tìm phương tiện trong vùng", "600", "800", var_v3.account)

        #điểm 1
        var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_location1).click()
        time.sleep(2)
        #điểm 2
        var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_location2).click()
        time.sleep(2)
        # #điểm 3
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_location3).click()
        except:
            pass
        button = var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_location3)
        action = ActionChains(var_v3.driver)
        action.double_click(button).perform()
        time.sleep(4)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Tìm phương tiện trong vùng",
                                              var_v3.title_right_mouse, "TÌM PHƯƠNG TIỆN TRONG VÙNG", "_GiamSat_TimPhuongTienTrongVung.png")



    def edit_drawing_area2(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.edit_drawing_area).click()
        except:
            map.find_vehicle_in_area(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.edit_drawing_area).click()
        time.sleep(1.5)
        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Giám sát - Map - Tìm phương tiện trong vùng",
                                                var_v3.redraw, "_GiamSat_TimPhuongTienTrongVung_SuaVungVe.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.cancel2).click()
            time.sleep(1.5)
        except:
            pass



    def redraw2(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.redraw).click()
        except:
            map.find_vehicle_in_area(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.redraw).click()
        time.sleep(1.5)
        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Giám sát - Map - Tìm phương tiện trong vùng",
                                                var_v3.edit_drawing_area, "_GiamSat_TimPhuongTienTrongVung_VeLai.png")

        time.sleep(1.5)
        #điểm 1
        var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_location1).click()
        time.sleep(2)
        #điểm 2
        var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_location2).click()
        time.sleep(2)
        # #điểm 3
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_location3).click()
        except:
            pass
        button = var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_location3)
        action = ActionChains(var_v3.driver)
        action.double_click(button).perform()
        time.sleep(5)



    def find_vehicle_in_area_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_search2)
        except:
            map.find_vehicle_in_area(self, "", "", "")

        name_vehicle2 = var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_search2).text
        var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_search_input).send_keys(name_vehicle2)
        time.sleep(1.5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_select1).click()
        except:
            name_vehicle2 = var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_search2).text
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_search_input).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_search_input).send_keys(name_vehicle2)
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_select1).click()
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Tìm phương tiện trong vùng",
                                              var_v3.check_find_vehicle_in_area_search, name_vehicle2, "_GiamSat_TimPhuongTienTrongVung_TimKiem.png")

        logging.info("-------------------------")
        logging.info("Giám sát - Map - Tìm phương tiện trong vùng")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            find_vehicle_in_area_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_search2).text
            popup_status_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.check_find_vehicle_in_area_search).text
            logging.info(find_vehicle_in_area_vehicle)
            logging.info(popup_status_vehicle)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Tìm phương tiện trong vùng: {}\nPopup hiện trạng: {}"
                                      .format(find_vehicle_in_area_vehicle, popup_status_vehicle))

            if find_vehicle_in_area_vehicle == popup_status_vehicle:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_TimPhuongTienTrongVung_TimKiem.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_TimPhuongTienTrongVung_TimKiem.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_TimPhuongTienTrongVung_TimKiem.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_TimPhuongTienTrongVung_TimKiem.png")




    def find_vehicle_in_area_refresh(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        # del var_v3.driver.requests
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_refresh).click()
        except:
            map.find_vehicle_in_area(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_refresh).click()
        logging.info("-------------------------")
        logging.info("Giám sát - Map - Tìm phương tiện trong vùng")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("False")
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
        time.sleep(3)
        # for request in var_v3.driver.requests:
        #     print(request.url[0:49])
        #     if request.url[0:49] == "https://gps3.binhanh.vn/api/v1/vehicleonline/sync":
        #         data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
        #         data1 = data1.decode("utf8")
        #         res = json.loads(data1)
        #         print(res['statusCode'])
        #         if res['statusCode'] == 200:
        #             logging.info("True")
        #             module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 8, "Pass")
        #             module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 11, "status code: 200")
        #         else:
        #             logging.info("False")
        #             module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 8, "Fail")
        #     if request.url[0:49] == "http://192.168.45.82:8000/api/v1/vehicleonline/sync":
        #         data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
        #         data1 = data1.decode("utf8")
        #         res = json.loads(data1)
        #         print(res['statusCode'])
        #         if res['statusCode'] == 200:
        #             logging.info("True")
        #             module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 8, "Pass")
        #             module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 11, "status code: 200")
        #         else:
        #             logging.info("False")
        #             module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 8, "Fail")




    def find_vehicle_in_area_export_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        module_other_v3.delete_excel()

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_export_excel).click()
        except:
            map.find_vehicle_in_area(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_export_excel).click()
        time.sleep(5)

        logging.info("Giám sát - Map - Tìm phương tiện trong vùng")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r"timxetrongvung.xlsx"))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_TimXeTrongVung_XuatExcel.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_TimXeTrongVung_XuatExcel.png")



    def find_vehicle_in_area_x(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_x).click()
        except:
            map.find_vehicle_in_area(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.find_vehicle_in_area_x).click()
        time.sleep(1)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Map - Tìm phương tiện trong vùng",
                                              var_v3.find_vehicle_in_area_x, "_GiamSat_TimXeTrongVung_IconX.png")







    def measure_distance(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['denlulake'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass
        map.map_right_mouse(self, "Đo khoảng cách", "650", "800", var_v3.title_right_mouse)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Tạo điểm",
                                              var_v3.title_right_mouse, "ĐO KHOẢNG CÁCH", "_GiamSat_DoKhoangCach.png")



    def total_distance(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.title_right_mouse)
        except:
            map.measure_distance(self, "", "", "")

        mouse.move("800", "800")
        mouse.click(button='left')
        time.sleep(1)

        mouse.move("1000", "800")
        mouse.click(button='left')
        time.sleep(2)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Chuột phải map - Đo khoảng cách",
                                              var_v3.check_total_distance, "Tổng quãng đường: 0,22 km", "_GiamSat_DoKhoangCach_TongQuangDuong.png")



    def measure_distance_delete_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_total_distance)
        except:
            map.total_distance(self, "", "", "")

        button = var_v3.driver.find_element(By.XPATH, var_v3.measure_distance_location2)
        actions = ActionChains(var_v3.driver)
        actions.double_click(button).perform()

        time.sleep(1)
        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Giám sát - Chuột phải map - Đo khoảng cách",
                                              var_v3.measure_distance_location2, "_GiamSat_DoKhoangCach_XoaDiem.png")



    def measure_distance_x(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_x).click()
        except:
            map.measure_distance(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.icon_x).click()
        time.sleep(1)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Chuột phải map - Đo khoảng cách",
                                              var_v3.icon_x, "_GiamSat_DoKhoangCach_IconX.png")



    def boot_config(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['denlulake'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass

        map.map_right_mouse(self, "Cấu hình khởi động", "650", "800", var_v3.title_right_mouse)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Cấu hình khởi động",
                                              var_v3.title_right_mouse, "CẤU HÌNH KHỞI ĐỘNG", "_GiamSat_CauHinhKhoiDong.png")



    def boot_config_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
        except:
            map.boot_config(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
        time.sleep(1)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Map - Cấu hình khởi động",
                                              var_v3.close, "_GiamSat_CauHinhKhoiDong_Dong.png")



    def boot_config_save(self, code, eventname, result, select_type_map, number_zoom, type_center, display_cluster, popup_cluster, apply, name_image):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.ungroup)
            var_v3.driver.find_element(By.XPATH, var_v3.status_vehicle_move)
        except:
            login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
            time.sleep(3)

        map.map_right_mouse(self, "Cấu hình khởi động", "650", "800", var_v3.title_right_mouse)

        var_v3.driver.find_element(By.XPATH, var_v3.type_map).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[text()='"+select_type_map+"']").click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.zoom_input).click()
        var_v3.driver.find_element(By.XPATH, var_v3.zoom_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.zoom_input).send_keys(number_zoom)

        var_v3.driver.find_element(By.XPATH, var_v3.type_center).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[text()='"+type_center+"']").click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.zoom_input).click()
        if type_center == "Phương tiện trung tâm":
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.select_vehicle).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.select_vehicle1).click()
            time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.zoom_input).click()
        time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.location).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.location).send_keys(var_v3.data['minitor']['169hoangmai'])
            time.sleep(1)
        except:
            pass

        if var_v3.driver.find_element(By.XPATH, var_v3.cluster_vehicle).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.cluster_vehicle1).click()
        if var_v3.driver.find_element(By.XPATH, var_v3.cluster_location).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.cluster_location1).click()

        if display_cluster == "1":
            var_v3.driver.find_element(By.XPATH, var_v3.cluster_vehicle1).click()
        if display_cluster == "2":
            var_v3.driver.find_element(By.XPATH, var_v3.cluster_location1).click()
        if display_cluster == "3":
            var_v3.driver.find_element(By.XPATH, var_v3.cluster_vehicle1).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.cluster_location1).click()
        time.sleep(1)

        if popup_cluster == "1":
            var_v3.driver.find_element(By.XPATH, var_v3.cluster1).click()
        if popup_cluster == "2":
            var_v3.driver.find_element(By.XPATH, var_v3.cluster2).click()

        time.sleep(1)
        if apply == "1":
            var_v3.driver.find_element(By.XPATH, var_v3.just_own).click()
        if apply == "2":
            var_v3.driver.find_element(By.XPATH, var_v3.user).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.select_user).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.select_user1).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.zoom_input).click()
        time.sleep(2.5)
        var_v3.driver.implicitly_wait(0.2)
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(0.3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Cấu hình khởi động",
                                              var_v3.update_success, "Cập nhật thành công", name_image)
        time.sleep(7)



    def config_display_group_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['denlulake'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass

        map.map_right_mouse(self, "Cấu hình hiển thị nhóm điểm", "650", "800", var_v3.title_right_mouse)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Cấu hình hiển thị nhóm điểm",
                                              var_v3.title_right_mouse, "CẤU HÌNH HIỂN THỊ NHÓM ĐIỂM", "_GiamSat_CauHinhHienThiNhomDiem.png")



    def config_display_group_location_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.title_right_mouse)
        except:
            map.config_display_group_location(self, "", "", "")


        name_group_company1 = var_v3.driver.find_element(By.XPATH, var_v3.name_group_company1).text
        var_v3.driver.find_element(By.XPATH, var_v3.find_group_location).send_keys(name_group_company1)
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Cấu hình hiển thị nhóm điểm",
                                              var_v3.check_config_display_group_location_search, name_group_company1, "_GiamSat_CauHinhHienThiNhomDiem_TimKiem.png")

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.location_system_label).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.location_system_label).click()
        time.sleep(1)



    def group_location_company(self, code, eventname, result, checkbox):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.title_right_mouse)
        except:
            map.config_display_group_location(self, "", "", "")

        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['center_here'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass

        if var_v3.driver.find_element(By.XPATH, var_v3.group_location_company_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.group_location_company_label).click()
        time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.group_location_company_area_input).is_selected() == checkbox:
            var_v3.driver.find_element(By.XPATH, var_v3.group_location_company_area_label).click()
        time.sleep(0.5)


        if var_v3.driver.find_element(By.XPATH, var_v3.group_location_company_namelocation_input).is_selected() == checkbox:
            var_v3.driver.find_element(By.XPATH, var_v3.group_location_company_namelocation_label).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(3.5)


        if checkbox == False:
            module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Cấu hình hiển thị nhóm điểm",
                                                  var_v3.check_group_location_company1, "Điểm check trung tâm ở đây",
                                                     "_GiamSat_CauHinhHienThiNhomDiem_NhomDiemCongTy_BatTatCa.png")
        if checkbox == True:
            module_other_v3.write_result_not_displayed_try(code, eventname, result, "Giám sát - Map - Cấu hình hiển thị nhóm điểm",
                                                  var_v3.check_group_location_company1, "_GiamSat_CauHinhHienThiNhomDiem_NhomDiemCongTy_TatTatCa.png")
        time.sleep(2)



    def group_location_system(self, code, eventname, result, checkbox):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.title_right_mouse)
        except:
            map.config_display_group_location(self, "", "", "")

        list_vehicle.search(self, "Tìm tọa độ", var_v3.data['minitor']['group_system'])
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_adress_iconx).click()
            time.sleep(1)
        except:
            pass

        if var_v3.driver.find_element(By.XPATH, var_v3.group_location_system_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.group_location_system_label).click()
        time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.group_location_system_area_input).is_selected() == checkbox:
            var_v3.driver.find_element(By.XPATH, var_v3.group_location_system_area_label).click()
        time.sleep(0.5)


        if var_v3.driver.find_element(By.XPATH, var_v3.group_location_system_namelocation_input).is_selected() == checkbox:
            var_v3.driver.find_element(By.XPATH, var_v3.group_location_system_namelocation_label).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(3.5)


        if checkbox == False:
            module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Cấu hình hiển thị nhóm điểm",
                                                  var_v3.group_location_system, "Giáp Bát - Nghi Tàm",
                                                     "_GiamSat_CauHinhHienThiNhomDiem_NhomDiemHeThong_BatTatCa.png")
        if checkbox == True:
            module_other_v3.write_result_not_displayed_try(code, eventname, result, "Giám sát - Map - Cấu hình hiển thị nhóm điểm",
                                              var_v3.group_location_system, "_GiamSat_CauHinhHienThiNhomDiem_NhomDiemHethong_TatTatCa.png")
        time.sleep(2)



    def config_display_group_location_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        except:
            map.config_display_group_location(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(1)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Map - Cấu hình hiển thị nhóm điểm",
                                              var_v3.close2, "_GiamSat_CauHinhHienThiNhomDiem__Dong.png")



    def see_route_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        goto(self, "Mã XN", "999999", " Công ty: PQA Company For Tester - 999999 - admin999999 ")

        #hover
        minitor = var_v3.driver.find_element(By.XPATH, var_v3.minitor)
        actions = ActionChains(var_v3.driver)
        actions.move_to_element(minitor).perform()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.general_minitor).click()
        time.sleep(5)
        map.map_right_mouse(self, "Xem lộ trình tuyến", "600", "800", var_v3.title_right_mouse)
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Xem lộ trình tuyến",
                                              var_v3.title_right_mouse, "XEM LỘ TRÌNH TUYẾN", "_GiamSat_XemLoTrinhTuyen.png")



    def go_comeback(self, code, eventname, result, radio, select):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, "//*[text()=' Công ty: PQA Company For Tester - 999999 - admin999999 ']")
            var_v3.driver.find_element(By.XPATH, var_v3.see_route_route_go)
        except:
            map.see_route_route(self, "", "", "")

        if radio == "Chiều đi":
            var_v3.driver.find_element(By.XPATH, var_v3.see_route_route_go).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.name_route_b).click()
            var_v3.driver.find_element(By.XPATH, select).click()
            time.sleep(2)

        if radio == "Chiều về":
            var_v3.driver.find_element(By.XPATH, var_v3.see_route_route_comeback).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.name_route_b).click()
        time.sleep(1)

        if radio == "Chiều đi":
            logging.info("-------------------------")
            logging.info("Giám sát - Map - Xem lộ trình tuyến")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            try:
                check_icongo_comeback1 = var_v3.driver.find_element(By.XPATH, var_v3.check_icongo_comeback).get_attribute('src')
                check_icongo_comeback2 = var_v3.driver.find_element(By.XPATH, var_v3.check_icongo_comeback2).get_attribute('src')
                logging.info(check_icongo_comeback1)
                logging.info(check_icongo_comeback1)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Icon điểm đi: {}\nIcon điểm đến: {}".format(check_icongo_comeback1, check_icongo_comeback2))
                if check_icongo_comeback1 and check_icongo_comeback2 != "":
                    logging.info("True")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    logging.info("False")
                    var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_XemLoTrinhTuyen_ChieuDi.png")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_XemLoTrinhTuyen_ChieuDi.png")
            except:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSat_XemLoTrinhTuyen_ChieuDi.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSat_XemLoTrinhTuyen_ChieuDi.png")

        if radio == "Chiều về":
            module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Xem lộ trình tuyến",
                                                  var_v3.check_go_comeback, "Chiều chưa đươc vẽ lộ trình. Vui lòng truy cập trang quản lý tuyến điểm",
                                                     "_GiamSat_XemLoTrinhTuyen_ChieuVe.png")
            var_v3.driver.find_element(By.XPATH, select).click()
            time.sleep(1.2)
        time.sleep(2)




    def management_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, "//*[text()=' Công ty: PQA Company For Tester - 999999 - admin999999 ']")

        except:
            map.see_route_route(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.management_route).click()
        time.sleep(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])

        module_other_v3.write_result_text_try_if(code, eventname, result, "Giám sát - Map - Xem lộ trình tuyến",
                                              var_v3.check_management_route, "Quản lý tuyến", "_GiamSat_XemLoTrinhTuyen_QuanLyTuyen.png")
        time.sleep(1)
        module_other_v3.close_tab()
        time.sleep(1)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)



    def see_route_route_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        except:
            map.see_route_route(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(1)
        module_other_v3.write_result_close_popup(code, eventname, result, "Giám sát - Map - Xem lộ trình tuyến",
                                              var_v3.close2, "_GiamSat_XemLoTrinhTuyen_Dong.png")













