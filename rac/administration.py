import logging
from selenium.webdriver.common.action_chains import ActionChains
import random
import minitor_v3
import var_v3
import time
from selenium.webdriver.common.keys import Keys
import json
from retry import retry
from selenium.webdriver.common.by import By
import module_other_v3
import login_v3
import os
import shutil
import re
import subprocess
from retry import retry



def hover(path_hover):
    var_v3.driver.implicitly_wait(3)
    button_hover = var_v3.driver.find_element(By.XPATH, path_hover)
    actions = ActionChains(var_v3.driver)
    actions.move_to_element(button_hover).perform()
    time.sleep(0.5)





class company_administration:



    def list_company_x(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_input_x).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_company_x).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.agency_x).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.province_x).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.system_x).click()
            time.sleep(0.5)
        except:
            pass



    def list_company(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['binhanh_tk'], var_v3.data['login']['binhanh_mk'])

        hover(var_v3.administration)
        hover(var_v3.company_administration)
        var_v3.driver.find_element(By.XPATH, var_v3.list_company).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Danh sách công ty",
                                              var_v3.title_page, "DANH SÁCH CÔNG TY", "_DanhSachCongTy.png")



    def list_company_search(self, code, eventname, result, type, data, findexactly, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_company1)
        except:
            company_administration.list_company(self, "", "", "")
        company_administration.list_company_x(self)
        company_administration.list_company_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_type).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='"+type+"']").click()
        time.sleep(1)
        # var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_input).clear()
        # time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_input).send_keys(data)
        time.sleep(1)

        if var_v3.driver.find_element(By.XPATH, var_v3.findexactly_input).is_selected() == findexactly:
            var_v3.driver.find_element(By.XPATH, var_v3.findexactly_label).click()

        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Danh sách công ty",
                                              path_check, desire, name_image)



    def type_company(self, code, eventname, result, type, data, findexactly, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_company1)
        except:
            company_administration.list_company(self, "", "", "")

        company_administration.list_company_x(self)
        company_administration.list_company_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_type).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.type_company_name_company).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.select_type_company).click()
        time.sleep(1)
        try:
            var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='"+type+"']").click()
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.select_type_company).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='"+type+"']").click()
        time.sleep(1)

        # var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_input).clear()
        # time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_input).send_keys(data)
        time.sleep(1)

        if var_v3.driver.find_element(By.XPATH, var_v3.findexactly_input).is_selected() == findexactly:
            var_v3.driver.find_element(By.XPATH, var_v3.findexactly_label).click()

        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Danh sách công ty",
                                              path_check, desire, name_image)



    def select_list_company(self, code, eventname, result, select, selec1, data, findexactly, child, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_company1)
        except:
            company_administration.list_company(self, "", "", "")

        company_administration.list_company_x(self)
        company_administration.list_company_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_type).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.type_company_name_company).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, select).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, selec1).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_company_search_input).send_keys(data)
        time.sleep(1)

        if var_v3.driver.find_element(By.XPATH, var_v3.findexactly_input).is_selected() == findexactly:
            var_v3.driver.find_element(By.XPATH, var_v3.findexactly_label).click()

        if var_v3.driver.find_element(By.XPATH, var_v3.child_input).is_selected() == child:
            var_v3.driver.find_element(By.XPATH, var_v3.fchild_label).click()

        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Danh sách công ty",
                                              path_check, desire, name_image)



    def route_export_dowload(self, code, eventname, result, button, type_file, name_image):
        var_v3.driver.implicitly_wait(5)
        module_other_v3.delete_excel()
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_xn)
        except:
            company_administration.list_company_search(self, "Admin03", eventname, result, "Tên công ty",
                                                       "1010_Công ty không có nhóm đội", True,
                                                       var_v3.check_name_company, "1010_Công ty không có nhóm đội",
                                                       "_DanhSachCongTy_TimKiem_TenCongTy.png")

        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(10)

        logging.info("Quản trị - Quản trị công ty - Danh sách công ty")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r""+type_file+""))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)



    def list_company_print(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_xn)
        except:
            company_administration.list_company_search(self, "Admin03", eventname, result, "Tên công ty",
                                                       "1010_Công ty không có nhóm đội", True,
                                                       var_v3.check_name_company, "1010_Công ty không có nhóm đội",
                                                       "_DanhSachCongTy_TimKiem_TenCongTy.png")

        var_v3.driver.find_element(By.XPATH, var_v3.print).click()
        time.sleep(3)
        logging.info("Quản trị - Quản trị công ty - Danh sách công ty")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("False")
        var_v3.driver.save_screenshot(var_v3.imagepath + code + "_DanhSachCongTy_TimKiem_TenCongTy.png")
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_DanhSachCongTy_TimKiem_TenCongTy.png")



    def hide_display_column(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_xn)
        except:
            company_administration.list_company_search(self, "Admin03", eventname, result, "Tên công ty",
                                                       "1010_Công ty không có nhóm đội", True,
                                                       var_v3.check_name_company, "1010_Công ty không có nhóm đội",
                                                       "_DanhSachCongTy_TimKiem_TenCongTy.png")

        #Check cột xem có không
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.tax_code)
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_display_column).click()
            time.sleep(2)
            if var_v3.driver.find_element(By.XPATH, var_v3.tax_code_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, var_v3.tax_code_input).click()
                time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(3)


        #Ẩn cột
        var_v3.driver.find_element(By.XPATH, var_v3.hide_display_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.tax_code_input).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.tax_code_input).click()
            time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(3)
        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị công ty - Danh sách công ty",
                                              var_v3.tax_code, "_DanhSachCongTy_AnHienCot.png")


        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.hide_display_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.tax_code_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.tax_code_input).click()
            time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(3)



    def list_company_goto(self, code, eventname, result):
        var_v3.driver.implicitly_wait(0.5)
        try:
            if var_v3.driver.find_element(By.XPATH, var_v3.child_input).is_selected() == True:
                var_v3.driver.find_element(By.XPATH, var_v3.fchild_label).click()
        except:
            pass

        try:
            if var_v3.driver.find_element(By.XPATH, var_v3.findexactly_input).is_selected() == True:
                var_v3.driver.find_element(By.XPATH, var_v3.findexactly_label).click()
        except:
            pass


        var_v3.driver.implicitly_wait(3)
        company_administration.list_company_search(self, "Admin03", eventname, result, "Tên công ty",
                                                   "1010_Công ty không có nhóm đội", True,
                                                   var_v3.check_name_company, "1010_Công ty không có nhóm đội",
                                                   "_DanhSachCongTy_TimKiem_TenCongTy.png")

        var_v3.driver.find_element(By.XPATH, var_v3.list_company_goto).click()
        time.sleep(7)
        # module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị công ty - Danh sách công ty",
        #                                       var_v3.check_list_company_goto, "Bạn chưa truy cập vào công ty nào",
        #                                          "_DanhSachCongTy_GoTo.png")
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Danh sách công ty",
                                              var_v3.check_list_company_goto, "Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup",
                                                 "_DanhSachCongTy_GoTo.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_out_goto).click()
            time.sleep(4)
        except:
            pass



    def create_agency(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['binhanh_tk'], var_v3.data['login']['binhanh_mk'])

        hover(var_v3.administration)
        hover(var_v3.company_administration)
        hover(var_v3.create_new_company)

        var_v3.driver.find_element(By.XPATH, var_v3.create_agency).click()
        time.sleep(2.5)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Tạo công ty mới",
                                              var_v3.check_title_popup1, "TẠO ĐẠI LÝ", "_TaoCongTyMoi_TaoDaiLy.png")



    def create_customer_company(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['binhanh_tk'], var_v3.data['login']['binhanh_mk'])

        hover(var_v3.administration)
        hover(var_v3.company_administration)
        hover(var_v3.create_new_company)

        var_v3.driver.find_element(By.XPATH, var_v3.create_customer_company).click()
        time.sleep(2.5)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Tạo công ty mới",
                                              var_v3.check_title_popup1, "TẠO CÔNG TY KHÁCH HÀNG", "_TaoCongTyMoi_TaoCongTyKhachHang.png")



    def create_retail_customer(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['binhanh_tk'], var_v3.data['login']['binhanh_mk'])

        hover(var_v3.administration)
        hover(var_v3.company_administration)
        hover(var_v3.create_new_company)

        var_v3.driver.find_element(By.XPATH, var_v3.create_retail_customer).click()
        time.sleep(2.5)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Tạo công ty mới",
                                              var_v3.check_title_popup1, "TẠO KHÁCH LẺ", "_TaoCongTyMoi_TaoKhachLe.png")



    def remove_company_to_agency(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['binhanh_tk'], var_v3.data['login']['binhanh_mk'])

        hover(var_v3.administration)
        hover(var_v3.company_administration)

        var_v3.driver.find_element(By.XPATH, var_v3.remove_company_to_agency).click()
        time.sleep(2.5)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị công ty - Chuyển công ty cho đại lý",
                                              var_v3.check_title_popup1, "CHUYỂN CÔNG TY CHO ĐẠI LÝ", "_ChuyenCongTyChoDaiLy.png")





class vehicle_administration:


    def list_vehicle_x(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_input_x).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_input_x1).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).clear()
            time.sleep(0.5)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_group_x).click()
            time.sleep(0.5)
        except:
            pass


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_agency_x).click()
            time.sleep(0.5)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_province_x1).click()
            time.sleep(0.5)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_type_of_transportx).click()
            time.sleep(0.5)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_type_of_transportx1).click()
            time.sleep(0.5)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_type_of_transportx2).click()
            time.sleep(0.5)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_status_x).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_status_x1).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_status_x2).click()
            time.sleep(0.5)
        except:
            pass


    def list_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        hover(var_v3.administration)
        hover(var_v3.vehicle_administration)

        button = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.title_page1, "DANH SÁCH PHƯƠNG TIỆN", "_DanhSachPhuongTien.png")



    def list_vehicle1(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['binhanh_tk'], var_v3.data['login']['binhanh_mk'])

        hover(var_v3.administration)
        hover(var_v3.vehicle_administration)

        button = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.title_page1, "DANH SÁCH PHƯƠNG TIỆN", "_DanhSachPhuongTien.png")



    def list_vehicle_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
        except:
            vehicle_administration.list_vehicle(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        license_plate2 = var_v3.driver.find_element(By.XPATH, var_v3.license_plate2).text
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(license_plate2)
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.check_list_vehicle_search, license_plate2, "_DanhSachPhuongTien_TimKiem.png")

        # vehicle_administration.list_vehicle_x(self)
        # time.sleep(1)
        # var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        # time.sleep(2)



    def list_vehicle_select_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
        except:
            vehicle_administration.list_vehicle(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        button = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_select_group)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_select_group1).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.check_list_vehicle_select_group, "Chọn nhóm phương tiện", "_DanhSachPhuongTien_ChonNhom.png")

        # vehicle_administration.list_vehicle_x(self)
        # var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        # time.sleep(2)


    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def list_vehicle_select(self, code, eventname, result, select, select1, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.truongtq)
        except:
            vehicle_administration.list_vehicle1(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, select).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, select1).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).click()
        time.sleep(1)
        if code == "Admin25" or code == "Admin28":
            if code == "Admin28":
                pass
            else:
                module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                      path_check, desire, name_image)

        else:
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                  path_check, desire, name_image)
            print("1")

        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(7)
        if name_image == "_DanhSachPhuongTien_TrangThaiPhi.png":
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                  path_check, desire, name_image)
        else:
            module_other_v3.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                  var_v3.check_list_vehicle_search1, name_image)
            print("2")

        # vehicle_administration.list_vehicle_x(self)
        # var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        # time.sleep(7)



    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def list_vehicle_time_not_signal(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.truongtq)
        except:
            vehicle_administration.list_vehicle1(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.time_not_signal_input1).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.time_not_signal_input1).send_keys(var_v3.data['administration']['time_not_signal_hours'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.time_not_signal_input2).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.time_not_signal_input2).send_keys(var_v3.data['administration']['time_not_signal_minute'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(7)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                 var_v3.check_list_vehicle_search1, "", "_DanhSachPhuongTien_ChonThoiGianMatTinHieu.png")

        var_v3.driver.find_element(By.XPATH, var_v3.time_not_signal_input1).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.time_not_signal_input2).clear()
        # var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        # time.sleep(7)


    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def list_vehicle_checkbox(self, code, eventname, result, checkbox_input, checkbox_label, type_check, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.truongtq)
        except:
            vehicle_administration.list_vehicle1(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys("20")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.more).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.implicitly_wait(3)
        try:
            if var_v3.driver.find_element(By.XPATH, checkbox_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, checkbox_label).click()
                time.sleep(1)
        except:
            pass
        var_v3.driver.implicitly_wait(1)
        try:
            if var_v3.driver.find_element(By.XPATH, checkbox_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, checkbox_label).click()
                time.sleep(1)
        except:
            pass
        var_v3.driver.implicitly_wait(3)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(8)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                 var_v3.check_list_vehicle_search1, "", name_image)

        if type_check == "1":
            module_other_v3.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                  path_check, name_image)

        if type_check == "2":
            module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                  path_check, name_image)

        if type_check == "3":
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                  path_check, desire, name_image)

        if var_v3.driver.find_element(By.XPATH, checkbox_input).is_selected() == True:
            try:
                var_v3.driver.find_element(By.XPATH, checkbox_label).click()
            except:
                var_v3.driver.find_element(By.XPATH, checkbox_label).click()
            time.sleep(0.5)



    def list_vehicle_link_search(self, code, eventname, result, button, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_company)
            var_v3.driver.find_element(By.XPATH, var_v3.truongtq)
        except:
            vehicle_administration.list_vehicle_checkbox(self, "Admin30", eventname, result, var_v3.new_vehicle_input,
                                                         var_v3.new_vehicle_label,
                                                         "1", var_v3.check_list_vehicle_company, "",
                                                         "_DanhSachPhuongTien_PhuongTienLapMoi.png")

        vehicle_administration.list_vehicle_x(self)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                       path_check, desire, name_image)

        time.sleep(1)
        module_other_v3.close_tab()
        time.sleep(1)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)


    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def list_vehicle_change_icon(self, code, eventname, result):
        var_v3.driver.implicitly_wait(1)
        minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
        hover(var_v3.administration)
        hover(var_v3.vehicle_administration)
        #
        # try:
        #     var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
        #     var_v3.driver.find_element(By.XPATH, var_v3.truongtq)
        # except:
        #     vehicle_administration.list_vehicle1(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['change_icon'])
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(7)
        try:
            var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Data table']/kendo-grid-list/div/div/table/tbody/tr[1]//*[text()='"+var_v3.data['administration']['change_icon']+"']")
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['change_icon'])
            var_v3.driver.find_element(By.XPATH, var_v3.search).click()
            time.sleep(7)

        if var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).click()
            time.sleep(0.5)
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.change_icon).click()
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.change_icon_green).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                       var_v3.update_success, "Cập nhật thành công", "_DanhSachPhuongTien_DoiIcon.png")
        time.sleep(4)
        module_other_v3.write_result_displayed_try(code, eventname, result,"Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                   var_v3.check_list_vehicle_change_icon, "_DanhSachPhuongTien_DoiIcon.png")


        if var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).click()
            time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.change_icon).click()
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.change_icon_blue).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(3)




    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def update_to_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_goto)
        except:
            minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
            hover(var_v3.administration)
            hover(var_v3.vehicle_administration)
            # vehicle_administration.list_vehicle1(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.update_to_excel).click()
        time.sleep(3)
        var_v3.driver.find_element(By.XPATH, var_v3.chose_file).click()
        time.sleep(1)
        subprocess.Popen(var_v3.uploadpath+"templateImportvehicle.xlsx.exe")
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2)

        print("đã xong")




        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.not_vehicle, "Biển kiểm soát không tồn tại!", "_DanhSachPhuongTien_CapNhatTuExcel.png")

        # time.sleep(5)
        # module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
        #                                       var_v3.update_success, "Cập nhật thành công", "_DanhSachPhuongTien_CapNhatTuExcel.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
            time.sleep(2)
        except:
            pass


    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def list_vehicle_export_file(self, code, eventname, result, button, name_file, name_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_goto)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_status)
        except:
            vehicle_administration.list_vehicle_checkbox(self, "Admin30", eventname, result, var_v3.new_vehicle_input,
                                                         var_v3.new_vehicle_label,
                                                         "1", var_v3.check_list_vehicle_company, "",
                                                         "_DanhSachPhuongTien_PhuongTienLapMoi.png")
        vehicle_administration.list_vehicle_x(self)
        time.sleep(0.5)
        try:
            var_v3.driver.find_element(By.XPATH, button).click()
        except:
            button1 = var_v3.driver.find_element(By.XPATH, button)
            var_v3.driver.execute_script("arguments[0].click();", button1)
        time.sleep(10)
        logging.info("Quản trị - Quản trị phương tiện - Danh sách phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r""+name_file+""))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)



    def print_list_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_status)
            var_v3.driver.find_element(By.XPATH, var_v3.truongtq)
        except:
            vehicle_administration.list_vehicle_checkbox(self, "Admin30", eventname, result, var_v3.new_vehicle_input,
                                                         var_v3.new_vehicle_label,
                                                         "1", var_v3.check_list_vehicle_company, "",
                                                         "_DanhSachPhuongTien_PhuongTienLapMoi.png")
        vehicle_administration.list_vehicle_x(self)
        time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.print).click()
        time.sleep(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])

        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                var_v3.check_print_route, "None", "_LoTrinh_InLoTrinh.png")

        time.sleep(1)
        module_other_v3.close_tab()
        time.sleep(1)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)



    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def list_vehicle_hide(self, code, eventname, result):
        var_v3.driver.implicitly_wait(1)
        try:
            # var_v3.driver.find_element(By.XPATH, var_v3.goto)
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_goto)
        except:
            minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
            hover(var_v3.administration)
            hover(var_v3.vehicle_administration)
            # vehicle_administration.list_vehicle1(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
            time.sleep(2)
        except:
            button = var_v3.driver.find_element(By.XPATH, var_v3.hide_column)
            var_v3.driver.execute_script("arguments[0].click();", button)


        try:
            if var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).click()
                time.sleep(0.5)
                var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
                time.sleep(7)
        except:
            pass
        try:
            if var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).is_selected() == True:
                var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
                time.sleep(2)
        except:
            pass

        var_v3.driver.implicitly_wait(5)
        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                       var_v3.update_success, "Cập nhật thành công", "_DanhSachPhuongTien_DoiIcon.png")

        time.sleep(4)
        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.assign_vehicle_column, "_DanhSachPhuongTien_AnHienCot.png")


        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(7)


    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def list_vehicle_lock(self, code, eventname, result, button, reason, desire, name_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_goto)
        except:
            # vehicle_administration.list_vehicle1(self, "", "", "")
            minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
            hover(var_v3.administration)
            hover(var_v3.vehicle_administration)

        vehicle_administration.list_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['lock_vehicle'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(6)
        try:
            var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Data table']/kendo-grid-list/div/div/table/tbody/tr[1]//*[text()='"+var_v3.data['administration']['lock_vehicle']+"']")
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['lock_vehicle'])
            var_v3.driver.find_element(By.XPATH, var_v3.search).click()
            time.sleep(7)

        if reason == var_v3.data['administration']['reason_lock']:
            element1 = var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_search1_button)
            check_color = element1.value_of_css_property("color")
            if check_color == "rgba(203, 0, 0, 1)":
                if var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).is_selected() == False:
                    var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).click()
                var_v3.driver.find_element(By.XPATH, var_v3.un_lock_vehicle).click()
                time.sleep(2)
                var_v3.driver.find_element(By.XPATH, var_v3.reason).send_keys(reason)
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
                time.sleep(7)

        if var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).click()
            time.sleep(0.5)
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.reason).send_keys(reason)
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(1.2)
        message = var_v3.driver.find_element(By.XPATH, var_v3.update_success).text
        # module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
        #                                                var_v3.update_success, "Cập nhật thành công", "_DanhSachPhuongTien_Khoa1PhuongTien.png")

        time.sleep(2.5)
        element1 = var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_search1_button)
        check_color = element1.value_of_css_property("color")
        # module_other_v3.write_result_text_try_if_color(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
        #                                       var_v3.check_list_vehicle_search1_button, desire, "_DanhSachPhuongTien_Khoa1PhuongTien.png")

        logging.info("-------------------------")
        logging.info("Quản trị - Quản trị phương tiện - Danh sách phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            logging.info(message)
            logging.info(check_color)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Phương tiện: {}\nMàu: {}\nMessage: {}"
                                      .format(var_v3.data['administration']['lock_vehicle'], check_color, message))
            if check_color == desire:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_DanhSachPhuongTien_Khoa1PhuongTien.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)











    def list_vehicle_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        # try:
        #     var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
        # except:
        #     vehicle_administration.list_vehicle1(self, "", "", "")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_goto)
        except:
            # vehicle_administration.list_vehicle1(self, "", "", "")
            minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
            hover(var_v3.administration)
            hover(var_v3.vehicle_administration)


        vehicle_administration.list_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['delete'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(6)
        if var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_select1).click()
            time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_delete).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                       var_v3.check_list_vehicle_delete1, "Bạn có chắc chắn muốn xóa 1 mục đã chọn?", "_DanhSachPhuongTien_IconXoa.png")

        var_v3.driver.find_element(By.XPATH, var_v3.cancel1).click()
        time.sleep(1)



    def list_vehicle_goto(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_goto)
        except:
            minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
            hover(var_v3.administration)
            hover(var_v3.vehicle_administration)



        var_v3.driver.refresh()
        time.sleep(6)
        vehicle_administration.list_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['goto'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(6)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_goto).click()
        time.sleep(3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                       var_v3.check_list_vehicle_goto, "Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup", "_DanhSachPhuongTien_GoTo.png")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_out_goto).click()
            time.sleep(3)
        except:
            pass



    def list_vehicle_user(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
        except:
            vehicle_administration.list_vehicle1(self, "", "", "")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_out_goto).click()
            time.sleep(3)
        except:
            pass

        vehicle_administration.list_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['goto'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(6)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_user).click()
        time.sleep(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                                       var_v3.title_page, "DANH SÁCH NGƯỜI DÙNG", "_DanhSachPhuongTien_User.png")


        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.check_list_vehicle_user, "", "_DanhSachPhuongTien_User.png")

        time.sleep(1)
        module_other_v3.close_tab()
        time.sleep(1)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)



    def list_vehicle_assign(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
        except:
            vehicle_administration.list_vehicle1(self, "", "", "")

        vehicle_administration.list_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['goto'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(6)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_assign).click()
        time.sleep(5)



    def list_vehicle_hide_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_goto)
        except:
            # vehicle_administration.list_vehicle1(self, "", "", "")
            minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
            hover(var_v3.administration)
            hover(var_v3.vehicle_administration)


        button = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)

        vehicle_administration.list_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['hide_vehicle'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)
        try:
            var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Data table']/kendo-grid-list/div/div/table/tbody/tr[1]/td[10]//*[text()='"+var_v3.data['administration']['hide_vehicle']+"']")
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['hide_vehicle'])
            var_v3.driver.find_element(By.XPATH, var_v3.search).click()
            time.sleep(3)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_hide)
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_un_hide).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(5)


        var_v3.driver.find_element(By.XPATH, var_v3.icon_hide).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.hide_all_page).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.no_transmit).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.select_season).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.select_season1).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.hidde_on_surveillance_note).send_keys(var_v3.data['administration']['hide_all_page'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", "_DanhSachPhuongTien_AnPhuongTien.png")
        time.sleep(3)

        module_other_v3.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.icon_un_hide, "_DanhSachPhuongTien_AnPhuongTien.png")

        var_v3.driver.find_element(By.XPATH, var_v3.icon_out_goto).click()
        time.sleep(3)



    def list_vehicle_un_hide_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_fee)
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_vehicle_goto)
        except:
            # vehicle_administration.list_vehicle1(self, "", "", "")
            minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
            hover(var_v3.administration)
            hover(var_v3.vehicle_administration)



        button = var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)

        vehicle_administration.list_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['hide_vehicle'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)
        try:
            var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Data table']/kendo-grid-list/div/div/table/tbody/tr[1]/td[10]//*[text()='"+var_v3.data['administration']['hide_vehicle']+"']")
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys(var_v3.data['administration']['hide_vehicle'])
            var_v3.driver.find_element(By.XPATH, var_v3.search).click()
            time.sleep(3)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_un_hide)
        except:
            vehicle_administration.list_vehicle_hide_vehicle(self, "", "", "")
            minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
            vehicle_administration.list_vehicle_x(self)
            var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle_search_input).send_keys( var_v3.data['administration']['hide_vehicle'])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.search).click()
            time.sleep(2.5)



        var_v3.driver.find_element(By.XPATH, var_v3.icon_un_hide).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", "_DanhSachPhuongTien_BoAnPhuongTien.png")
        time.sleep(3)
        module_other_v3.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh sách phương tiện",
                                              var_v3.icon_hide, "_DanhSachPhuongTien_BoAnPhuongTien.png")

        var_v3.driver.find_element(By.XPATH, var_v3.icon_out_goto).click()
        time.sleep(3)




    def vehicle_group_management (self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", "1100", " Công ty: 1100 - Khách Lẻ Xe Khách - 1100 - admin1100 ")
        hover(var_v3.administration)
        hover(var_v3.vehicle_administration)

        button = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_group_management)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.title_page, "QUẢN TRỊ NHÓM PHƯƠNG TIỆN", "_QuanTriNhomPhuongTien.png")



    def vehicle_group_management_search(self, code, eventname, result, search_input, data, path_check, desire, name_image, icon_xoa):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_1100)
            var_v3.driver.find_element(By.XPATH, var_v3.original_category)
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, search_input).send_keys(data)
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              path_check, desire, name_image)

        var_v3.driver.find_element(By.XPATH, path_check).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, icon_xoa).click()
        time.sleep(1)



    def add_new_group1(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.goto_1100)
            var_v3.driver.find_element(By.XPATH, var_v3.original_category)
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")



        var_v3.driver.implicitly_wait(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.select_group_icon_show).click()
            time.sleep(1)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.group_n_edit_0).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.igree1).click()
            time.sleep(2)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.group_n_0).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.igree1).click()
            time.sleep(2)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.group_1_0).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.igree1).click()
            time.sleep(2)
        except:
            pass




        var_v3.driver.implicitly_wait(3)
        var_v3.driver.refresh()
        time.sleep(5)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_add_new).click()
        time.sleep(3)
        var_v3.driver.find_element(By.XPATH, var_v3.gourp_level1_input).send_keys(var_v3.data['administration']['group_level1'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_save).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.add_new_success, "Thêm mới thành công", "_QuanTriNhomPhuongTien_ThemNhomBac1.png")

        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.group_1_0, "Nhóm bậc 1 (0 xe)", "_QuanTriNhomPhuongTien_ThemNhomBac1.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_cancel).click()
            time.sleep(1)
        except:
            pass



    def add_new_groupn(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.group_1_0)
        except:
            vehicle_administration.add_new_group1(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.group_1_0).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_add_new).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.gourp_level1_input).send_keys(var_v3.data['administration']['group_leveln'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_save).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.add_new_success, "Thêm mới thành công", "_QuanTriNhomPhuongTien_ThemNhomBacN.png")

        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.group_n_0, "Nhóm bậc n (0 xe)", "_QuanTriNhomPhuongTien_ThemNhomBacN.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_cancel).click()
            time.sleep(1)
        except:
            pass



    def remane_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.group_n_0)
        except:
            vehicle_administration.add_new_groupn(self, "", "", "")

        try:
            button = var_v3.driver.find_element(By.XPATH, var_v3.icon_show)
            var_v3.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
        except:
            pass

        var_v3.driver.find_element(By.XPATH, var_v3.group_n_0).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_remane_group).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.gourp_level1_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.gourp_level1_input).send_keys(var_v3.data['administration']['group_rename'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_save).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", "_QuanTriNhomPhuongTien_DoiTenNhom.png")

        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.group_n_edit_0, "Nhóm bậc n đã đổi tên (0 xe)", "_QuanTriNhomPhuongTien_DoiTenNhom.png")



    def select_group(self, desire, field):
        var_v3.driver.implicitly_wait(0.05)
        try:
            button = var_v3.driver.find_element(By.XPATH, var_v3.select_group_icon_show)
            var_v3.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
        except:
            pass

        n = 0
        while (n < 10):
            n += 1
            n = str(n)
            path_group = "//*[@class='content-right-body row']/div[1]//*[@class='angular-tree-component']/tree-node-collection/div/tree-node[" + n + "]/div/tree-node-wrapper"
            print(n)
            try:
                # if var_v3.driver.find_element(By.XPATH, path_group).is_selected() == False:
                #     var_v3.driver.find_element(By.XPATH, path_group).click()
                #     time.sleep(0.5)

                var_v3.driver.find_element(By.XPATH, path_group).click()
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
                time.sleep(1.3)
                try:
                    var_v3.driver.find_element(By.XPATH, "//*[text()='"+field+"']")
                    time.sleep(1)
                    if desire == "Đồng ý":
                        var_v3.driver.find_element(By.XPATH, var_v3.igree1).click()
                        time.sleep(2)
                        break
                    if desire == "Hủy":
                        var_v3.driver.find_element(By.XPATH, var_v3.cancel1).click()
                        time.sleep(2)
                        break
                except:
                    var_v3.driver.find_element(By.XPATH, var_v3.cancel1).click()
                    time.sleep(2)
                    # if var_v3.driver.find_element(By.XPATH, path_group).is_selected() == True:
                    #     var_v3.driver.find_element(By.XPATH, path_group).click()
                    #     time.sleep(0.5)
            except:
                break
            n = int(n)



    def delete_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.group_n_edit_0)
        except:
            # vehicle_administration.remane_group(self, "", "", "")
            vehicle_administration.vehicle_group_management(self, "", "", "")

        try:
            button = var_v3.driver.find_element(By.XPATH, var_v3.icon_show)
            var_v3.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
        except:
            pass
        vehicle_administration.select_group(self, "Đồng ý", "Nhóm bậc 1")
        vehicle_administration.select_group(self, "Đồng ý", "Nhóm bậc n đã đổi tên")
        time.sleep(1.5)
        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.check_remane_group, "_QuanTriNhomPhuongTien_XoaNhom.png")



    def search_list_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search_list_vehicle3).send_keys(var_v3.data['administration']['manager_group'])

        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.check_search_list_vehicle, var_v3.data['administration']['manager_group'], "_QuanTriNhomPhuongTien_TimKiemDanhSachPhuonghTien.png")

        var_v3.driver.refresh()
        time.sleep(5)




    def assign_group_vehicle(self, code, eventname, result, button1, button2, name_image):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()

        time.sleep(1.5)
        var_v3.driver.implicitly_wait(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_hide_goto).click()
            time.sleep(1)
        except:
            pass

        # var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle1_input).click()
        # time.sleep(1)
        var_v3.driver.find_element(By.XPATH, button1).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.icon_right).click()
        time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(1.5)
        except:
            pass

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", name_image)

        time.sleep(2)
        # var_v3.driver.find_element(By.XPATH, var_v3.list_vehicle2_input).click()
        # time.sleep(1)
        var_v3.driver.find_element(By.XPATH, button2).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.icon_left).click()
        time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(2.5)
        except:
            pass




    def search_list_user(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()

        time.sleep(1)
        list_user2 = var_v3.driver.find_element(By.XPATH, var_v3.search_list_user2).text
        var_v3.driver.find_element(By.XPATH, var_v3.search_list_user_input).send_keys(list_user2)
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.check_user_1, list_user2, "_QuanTriNhomPhuongTien_TimKiemDanhSachNguoiDung.png")

        var_v3.driver.refresh()
        time.sleep(4.5)




    def assign_group_vehicle1(self, code, eventname, result, button_input, button_label, name_image):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()
        time.sleep(1)

        # vehicle_administration.select_group(self, "Hủy", "Nhóm test tìm kiếm")
        time.sleep(1.5)
        var_v3.driver.implicitly_wait(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_hide_goto).click()
            time.sleep(1)
        except:
            pass

        var_v3.driver.implicitly_wait(4)
        if var_v3.driver.find_element(By.XPATH, button_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, button_label).click()
            time.sleep(1)


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(1.5)
        except:
            pass

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", name_image)
        time.sleep(2)



        if var_v3.driver.find_element(By.XPATH, button_input).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, button_label).click()
            time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(2.5)
        except:
            pass



    def vehicle_group_management_cancel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1).click()


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_hide_goto).click()
            time.sleep(1)
        except:
            pass

        try:
            if var_v3.driver.find_element(By.XPATH, var_v3.list_user_all_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, var_v3.list_user_all_label).click()
                time.sleep(1)
        except:
            pass

        try:
            if var_v3.driver.find_element(By.XPATH, var_v3.check_search_list_vehicle1).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, var_v3.check_search_list_vehicle).click()
                time.sleep(1)
        except:
            pass

        var_v3.driver.find_element(By.XPATH, var_v3.cancel3).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if_boolean(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.list_user_all_input, False, "_QuanTriNhomPhuongTien_Huy.png")



    def mark_special_groups(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1)
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")

        vehicle_administration.select_group(self, "Hủy", "Nhóm bậc 1")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.un_mark_special_groups).click()
            time.sleep(3)
            var_v3.driver.refresh()
            time.sleep(5)
        except:
            pass

        vehicle_administration.select_group(self, "Hủy", "Nhóm bậc 1")
        var_v3.driver.find_element(By.XPATH, var_v3.mark_special_groups).click()
        time.sleep(1.2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", "_QuanTriNhomPhuongTien_DanhDauNhomDacBiet.png")

        var_v3.driver.refresh()
        time.sleep(5)
        module_other_v3.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.check_mark_special_groups, "_QuanTriNhomPhuongTien_DanhDauNhomDacBiet1.png")



        time.sleep(3)
        try:
            vehicle_administration.select_group(self, "Hủy", "Nhóm bậc 1")
            var_v3.driver.find_element(By.XPATH, var_v3.un_mark_special_groups).click()
            time.sleep(2)
            var_v3.driver.refresh()
            time.sleep(5)
        except:
            pass




    def vehicle_belong_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.original_category1)
        except:
            vehicle_administration.vehicle_group_management(self, "", "", "")

        vehicle_administration.select_group(self, "Hủy", "Nhóm bậc 1")

        vehicle_belong_group2 = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_belong_group2).text
        var_v3.driver.find_element(By.XPATH, var_v3.vehicle_belong_group_input).send_keys(vehicle_belong_group2)
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.vehicle_belong_group1, vehicle_belong_group2, "_QuanTriNhomPhuongTien_TimKiemPhuongTienThuocNhom.png")







    def vehicle_group_permission_select_user(self, desire):
        var_v3.driver.implicitly_wait(0.05)
        n = 0
        while (n < 10):
            n += 1
            n = str(n)
            path_user = "//*[@class='list-user-container']//*[@role='rowgroup']/tr[" + n + "]/td/label"
            print(n)
            try:
                name = var_v3.driver.find_element(By.XPATH, path_user).text
                print("name: " + name)
                if name == desire:
                    var_v3.driver.find_element(By.XPATH, path_user).click()
                    time.sleep(1)
                    break
            except:
                pass
            n = int(n)



    def vehicle_group_permission(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", "1100", " Công ty: 1100 - Khách Lẻ Xe Khách - 1100 - admin1100 ")
        hover(var_v3.administration)
        hover(var_v3.vehicle_administration)

        button = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_group_administration)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)

        button = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_group_permission)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Phân quyền nhóm phương tiện",
                                              var_v3.vehicle_group_permission, "Phân quyền nhóm phương tiện", "_PhanQuyenNhomPhuongTien.png")



    def vehicle_group_permission_search(self, code, eventname, result, path_text, path_search_input, name_image, iconx):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user2_label)
        except:
            vehicle_administration.vehicle_group_permission(self, "", "", "")

        vehicle_administration.vehicle_group_permission_select_user(self, "nguyen van b (adhanoi4)")
        #
        # var_v3.driver.find_element(By.XPATH, var_v3.assign_group_vehicle_to_user4).click()
        # time.sleep(1)

        time.sleep(1)
        name2 = var_v3.driver.find_element(By.XPATH, path_text).text
        var_v3.driver.find_element(By.XPATH, path_search_input).send_keys(name2[0:8])

        time.sleep(1.5)
        logging.info("-------------------------")
        logging.info("Quản trị - Quản trị phương tiện - Phân quyền nhóm phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_text = var_v3.driver.find_element(By.XPATH, var_v3.search_list_vehicle1).text
            logging.info(check_text[0:8])
            logging.info(name2[0:8])
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)

            if check_text[0:8] == name2[0:8]:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)


        var_v3.driver.find_element(By.XPATH, var_v3.search_list_vehicle1).click()
        time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, iconx).click()
            time.sleep(1)
        except:
            pass



    def assign_group_vehicle_to_user(self, code, eventname, result, button1_input, button1_label, button2_input, button2_label, name_image):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user2_label)
        except:
            vehicle_administration.vehicle_group_permission(self, "", "", "")
        time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_hide_goto).click()
            time.sleep(1)
        except:
            pass

        vehicle_administration.vehicle_group_permission_select_user(self, "nguyen van a (adhanoi3)")


        if var_v3.driver.find_element(By.XPATH, button1_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, button1_label).click()
            time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.icon_right).click()
        time.sleep(1)


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(1.5)
        except:
            pass

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Phân quyền nhóm phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", name_image)
        time.sleep(2)


        if var_v3.driver.find_element(By.XPATH, button2_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, button2_label).click()
            time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.icon_left).click()
        time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(3)
        except:
            pass



    def vehicle_group_permission_cancel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_list_user2_label)
        except:
            vehicle_administration.vehicle_group_permission(self, "", "", "")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_hide_goto).click()
            time.sleep(1)
        except:
            pass

        vehicle_administration.vehicle_group_permission_select_user(self, "nguyen van b (adhanoi4)")



        if var_v3.driver.find_element(By.XPATH, var_v3.permission1_all_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.permission1_all_label).click()
            time.sleep(1)


        if var_v3.driver.find_element(By.XPATH, var_v3.permission2_all_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.permission2_all_label).click()
            time.sleep(1)



        var_v3.driver.find_element(By.XPATH, var_v3.icon_left).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.cancel3).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(2)

        module_other_v3.write_result_text_try_if_boolean(code, eventname, result, "Quản trị - Quản trị phương tiện - Phân quyền nhóm phương tiện",
                                              var_v3.permission1_all_input, False, "_PhanQuyenNhomPhuongTien_Huy.png")



    def permission_mark_special_groups(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_list_user2_label)
        except:
            vehicle_administration.vehicle_group_permission(self, "", "", "")



        vehicle_administration.vehicle_group_permission_select_user(self, "nguyen van b (adhanoi4)")

        var_v3.driver.find_element(By.XPATH, var_v3.list_group_vehicle2_label).click()
        time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_un_mark_special_groups).click()
            time.sleep(4)
        except:
            pass

        var_v3.driver.find_element(By.XPATH, var_v3.permission_mark_special_groups).click()
        time.sleep(1.3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.update_success, "Cập nhật thành công", "_PhanQuyenNhomPhuongTien_DanhDauNhomDacBiet.png")


        module_other_v3.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Quản trị nhóm phương tiện",
                                              var_v3.check_permission_mark_special_groups, "_PhanQuyenNhomPhuongTien_DanhDauNhomDacBiet1.png")


        time.sleep(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_un_mark_special_groups).click()
            time.sleep(2)
        except:
            pass








    def permission_search_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", "1100", " Công ty: 1100 - Khách Lẻ Xe Khách - 1100 - admin1100 ")
        hover(var_v3.administration)
        hover(var_v3.vehicle_administration)

        button = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_group_administration)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)

        button = var_v3.driver.find_element(By.XPATH, var_v3.permission_search_group)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Tìm kiếm nhóm",
                                              var_v3.permission_search_group, "Tìm kiếm nhóm", "_TimKiemNhom.png")



    def permission_search_group_select_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.manager)
        except:
            vehicle_administration.permission_search_group(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.permission_select_group).click()

        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.select_list1).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)

        logging.info("-------------------------")
        logging.info("Quản trị - Quản trị phương tiện - Tìm kiếm nhóm")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            vehicle = var_v3.driver.find_element(By.XPATH, var_v3.permission_search_group_vehicle).text
            liscense_plate = var_v3.driver.find_element(By.XPATH, var_v3.permission_search_group_liscense_plate).text
            group = var_v3.driver.find_element(By.XPATH, var_v3.permission_search_group_group).text
            manager = var_v3.driver.find_element(By.XPATH, var_v3.permission_search_group_manager).text
            logging.info(vehicle)
            logging.info(liscense_plate)
            logging.info(group)
            logging.info(manager)

            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Phương tiện: {}\nBiển kiểm soát: {}\nNhóm phương tiện: {}\nNgười quản lý: {}"
                                      .format(vehicle, liscense_plate, group, manager))
            if vehicle and liscense_plate and group and manager != "":
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_TimKiemNhom_ChonNhom.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_TimKiemNhom_ChonNhom.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_TimKiemNhom_ChonNhom.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_TimKiemNhom_ChonNhom.png")



    def permission_search_group_dowload(self, code, eventname, result, button, file, name_image):
        module_other_v3.delete_excel()
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.manager)
        except:
            vehicle_administration.permission_search_group(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "Quản trị - Quản trị phương tiện - Tìm kiếm nhóm",
                                               file, name_image)








    def vehicle_type_categoty(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", "1100", " Công ty: 1100 - Khách Lẻ Xe Khách - 1100 - admin1100 ")
        hover(var_v3.administration)
        hover(var_v3.vehicle_administration)

        button = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                              var_v3.title_page, "DANH MỤC LOẠI PHƯƠNG TIỆN", "_DanhMucLoaiPhuongTien.png")



    def vehicle_type_categoty_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search2)
        except:
            vehicle_administration.vehicle_type_categoty(self, "", "", "")


        name_type_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search2).text
        var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search_input).send_keys(name_type_vehicle)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                              var_v3.vehicle_type_categoty_search1, name_type_vehicle, "_DanhMucLoaiPhuongTien_TimKiem.png")

        var_v3.driver.refresh()
        time.sleep(5)



    def vehicle_type_categoty_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search2)
        except:
            vehicle_administration.vehicle_type_categoty(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.add_new).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.name_type_vehicle_input).send_keys(var_v3.data['administration']['type_vehicle'])
        var_v3.driver.find_element(By.XPATH, var_v3.describe).send_keys(var_v3.data['administration']['describe'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                              var_v3.add_new_success, "Thêm mới thành công", "_DanhMucLoaiPhuongTien_ThemMoi.png")
        time.sleep(2)
        var_v3.driver.refresh()
        time.sleep(5)



    def vehicle_type_categoty_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            # var_v3.driver.find_element(By.XPATH, "//*[text()='"+var_v3.data['administration']['type_vehicle']+"']")
            var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search2)
        except:
            vehicle_administration.vehicle_type_categoty_add_new(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search_input).send_keys(var_v3.data['administration']['type_vehicle'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(1.5)
        name_type_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search1).text
        if name_type_vehicle == var_v3.data['administration']['type_vehicle']:
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_icon_delete).click()
            except:
                var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_icon_delete1).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                              var_v3.delete_success, "Xóa thành công", "_DanhMucLoaiPhuongTien_Xoa.png")

        time.sleep(2)
        var_v3.driver.refresh()
        time.sleep(5)



    def vehicle_type_categoty_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search2)
        except:
            vehicle_administration.vehicle_type_categoty(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search_input).send_keys(var_v3.data['administration']['type_vehicle1'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(1.5)
        name_type_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search1).text
        if name_type_vehicle == var_v3.data['administration']['type_vehicle1']:
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_icon_edit).click()
            except:
                var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_icon_edit1).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.name_type_vehicle_input).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.name_type_vehicle_input).send_keys(var_v3.data['administration']['type_vehicle_edit'])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                                 var_v3.update_success, "Cập nhật thành công", "_DanhMucLoaiPhuongTien_Sua.png")
        time.sleep(2)

        var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_icon_edit).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.name_type_vehicle_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.name_type_vehicle_input).send_keys(var_v3.data['administration']['type_vehicle1'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2.5)
        var_v3.driver.refresh()
        time.sleep(5)



    def vehicle_type_categoty_dowload_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search2)
        except:
            vehicle_administration.vehicle_type_categoty(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.add_quickly).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.dowload_example_excel).click()
        time.sleep(5)
        logging.info("Quản trị - Quản trị phương tiện - Danh mục loại phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r"danhmucloaiphuongtien_taimau_excel.xlsx"))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_DanhMucLoaiPhuongTien_XuatExcel.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_DanhMucLoaiPhuongTien_XuatExcel.png")



    def vehicle_type_categoty_upload_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_example_excel)
        except:
            vehicle_administration.vehicle_type_categoty_dowload_excel(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.chose_file).click()
        time.sleep(1)
        subprocess.Popen(var_v3.uploadpath+"template_vehiclebrand.exe")
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                                 var_v3.check_vehicle_type_categoty_upload_excel, "Tên loại phương tiện đã tồn tại", "_DanhMucLoaiPhuongTien_UpLoad.png")

        var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(1.5)



    def vehicle_type_categoty_dowload(self, code, eventname, result, button, file, name_image):
        var_v3.driver.implicitly_wait(5)
        module_other_v3.delete_excel()
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search2)
        except:
            vehicle_administration.vehicle_type_categoty(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                               file, name_image)



    def vehicle_type_categoty_hide(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.vehicle_type_categoty_search2)
        except:
            vehicle_administration.vehicle_type_categoty(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        try:
            if var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).is_selected() == True:
                var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).click()
                time.sleep(0.5)
                var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
                time.sleep(2)
        except:
            pass
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                                       var_v3.update_success, "Cập nhật thành công", "_DanhMucLoaiPhuongTien_AnHienCot_Message.png")

        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                              var_v3.check_vehicle_type_categoty_hide, "_DanhMucLoaiPhuongTien_AnHienCot.png")



        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(3)









    def assign_type_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", "1100", " Công ty: 1100 - Khách Lẻ Xe Khách - 1100 - admin1100 ")
        hover(var_v3.administration)
        hover(var_v3.vehicle_administration)

        button = var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Gán loại phương tiện",
                                              var_v3.title_page, "GÁN LOẠI PHƯƠNG TIỆN", "_GanLoaiPhuongTien.png")



    def assign_type_vehicle_x(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle_x1).click()
            time.sleep(1)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle_x2).click()
            time.sleep(1)
        except:
            pass

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle_x3).click()
            time.sleep(1)
        except:
            pass



    def assign_type_vehicle_search(self, code, eventname, result, type_search, search_select, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.fixer)
        except:
            vehicle_administration.assign_type_vehicle(self, "", "", "")

        vehicle_administration.assign_type_vehicle_x(self)

        var_v3.driver.find_element(By.XPATH, type_search).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, search_select).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị phương tiện - Gán loại phương tiện",
                                              path_check, desire, name_image)



    def assign_type_vehicle_search1(self, code, eventname, result, type_search, search_select_label, path_check, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.fixer)
        except:
            vehicle_administration.assign_type_vehicle(self, "", "", "")

        vehicle_administration.assign_type_vehicle_x(self)

        var_v3.driver.find_element(By.XPATH, type_search).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, search_select_label).click()
        time.sleep(1)
        desire = var_v3.driver.find_element(By.XPATH, search_select_label).text
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Gán loại phương tiện",
                                              path_check, desire, name_image)



    def icon_assign_type_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.fixer)
        except:
            vehicle_administration.assign_type_vehicle(self, "", "", "")

        vehicle_administration.assign_type_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        try:
            # var_v3.driver.find_element(By.XPATH, var_v3.check_icon_assign_type_vehicle)
            vehicle_administration.icon_delete_assign_type_vehicle(self, "", "", "")
        except:
            pass

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_assign_type_vehicle).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.chose_type_vehicle).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.chose_type_vehicle_mazda).click()
        time.sleep(0.5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.chose_group_vehicle).click()
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.chose_group_vehicle1).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.chose_group_vehicle_all).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle_search_vehicle).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle_QCPASSED_CUONGDT).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Gán loại phương tiện",
                                              var_v3.add_new_success, "Thêm mới thành công", "_GanLoaiPhuongTien_IconGanLoaiPhuongTien_Message.png")


        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Gán loại phương tiện",
                                              var_v3.check_icon_assign_type_vehicle, "QCPASSED_CUONGDT", "_GanLoaiPhuongTien_IconGanLoaiPhuongTien.png")



    def icon_delete_assign_type_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.fixer)
        except:
            vehicle_administration.icon_assign_type_vehicle(self, "", "", "")

        vehicle_administration.assign_type_vehicle_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle_search2b).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle_search2a_cuongdt).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        name_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.assign_type_vehicle_search2).text
        if name_vehicle == "QCPASSED_CUONGDT":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.icon_delete_assign_type_vehicle).click()
            except:
                var_v3.driver.find_element(By.XPATH, var_v3.icon_delete_assign_type_vehicle1).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Gán loại phương tiện",
                                              var_v3.delete_success, "Xóa thành công", "_GanLoaiPhuongTien_IconXoa.png")

        time.sleep(2)
        vehicle_administration.assign_type_vehicle_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)



    def assign_type_vehicle_dowload(self, code, eventname, result, button, file, name_image):
        var_v3.driver.implicitly_wait(5)
        module_other_v3.delete_excel()
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.fixer)
        except:
            vehicle_administration.assign_type_vehicle(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "Quản trị - Quản trị phương tiện - Gán loại phương tiện",
                                               file, name_image)



    def assign_type_vehicle_hide(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.fixer)
        except:
            vehicle_administration.assign_type_vehicle(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                                       var_v3.update_success, "Cập nhật thành công", "_DanhMucLoaiPhuongTien_AnHienCot_Message.png")

        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị phương tiện - Danh mục loại phương tiện",
                                              var_v3.check_assign_type_vehicle_hide, "_DanhMucLoaiPhuongTien_AnHienCot.png")


        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.assign_vehicle_input).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(3)





class system_management:


    def list_user(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        hover(var_v3.administration)
        hover(var_v3.system_management)
        button = var_v3.driver.find_element(By.XPATH, var_v3.list_user)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                              var_v3.title_page1, "DANH SÁCH NGƯỜI DÙNG", "_DanhSachNguoiDung.png")



    def list_user_x(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_x1).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_x2).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_x3).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_x4).click()
            time.sleep(1)
        except:
            pass



    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def list_user_search(self, code, eventname, result, type_search, button, button_select, data, path_check, type_check, desire, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.login_recently)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_x(self)
        system_management.list_user_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_type_search).click()
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_type_search1).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='"+type_search+"']").click()
        time.sleep(1)
        var_v3.driver.implicitly_wait(1)
        try:
            var_v3.driver.find_element(By.XPATH, button).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, button_select).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.implicitly_wait(4)
        var_v3.driver.find_element(By.XPATH, var_v3.list_user_search_input1).clear()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_user_search_input1).send_keys(data)
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)
        if type_check == "1":
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                  path_check, desire, name_image)
        if type_check == "2":
            module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                  path_check, desire, name_image)
        if type_check == "3":
            module_other_v3.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                  path_check, name_image)
        if type_check == "4":
            module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                  path_check, name_image)

        # system_management.list_user_x(self)
        # var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        # time.sleep(2)



    def list_user_search1(self, data):
        var_v3.driver.implicitly_wait(3)
        system_management.list_user_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        # time.sleep(1.5)
        # button = var_v3.driver.find_element(By.XPATH, var_v3.list_user_type_search)
        # var_v3.driver.execute_script("arguments[0].click();", button)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_type_search).click()
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_type_search2).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.chose_user).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_user_search_input1).clear()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_user_search_input1).send_keys(data)
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)



    def list_user_dowload(self, code, eventname, result, button, file, name_image):
        var_v3.driver.implicitly_wait(5)
        module_other_v3.delete_excel()
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                               file, name_image)



    def list_user_hide(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                       var_v3.update_success, "Cập nhật thành công", "_DanhSachNguoiDung_AnHienCot_Message.png")

        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                              var_v3.check_list_user_hide, "_DanhSachNguoiDung_AnHienCot.png")


        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(3)



    def list_user_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 14, "")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.add_new).click()
        time.sleep(2)
        number = random.randint(1, 99999999)
        copyaccount_user = "ngocmai" + str(number)

        var_v3.driver.find_element(By.XPATH, var_v3.create_user_user).send_keys(copyaccount_user)
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_name).send_keys(var_v3.data['administration']['create_user_fullname'])
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_phone).send_keys(var_v3.data['administration']['create_user_number_phone'])
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_email).send_keys(var_v3.data['administration']['create_user_email'])
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_password1).send_keys(var_v3.data['administration']['create_user_password'])
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_password2).send_keys(var_v3.data['administration']['create_user_password'])
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_password3).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_password3_no_change).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_type).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_type_driver).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_position).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_position_customer).click()
        time.sleep(1)
        # var_v3.driver.find_element(By.XPATH, var_v3.create_user_group_vehicle).send_keys()
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_group_location).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.create_user_group_location_all).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                              var_v3.add_new_success, "Thêm mới thành công", "_DanhSachNguoiDung_ThemMoi.png")
        time.sleep(2)
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 45, 2, copyaccount_user)
        nameuser = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 45, 2))
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 14, nameuser)





    def list_user_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        nameuser = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 45, 2))

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_user_type_search).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='Tên đăng nhập']").click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_user_search_input1).clear()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_user_search_input1).send_keys(nameuser)
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)

        field3 = var_v3.driver.find_element(By.XPATH, var_v3.list_field3a).text
        print(field3)
        print(nameuser)
        if field3 == nameuser:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_icon_delete).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                              var_v3.delete_success, "Xóa thành công", "_DanhSachNguoiDung_Xoa.png")



    def list_user_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_search1(self, var_v3.data['administration']['assign_edit'])

        field3 = var_v3.driver.find_element(By.XPATH, var_v3.list_field3a).text
        print(field3)
        print(var_v3.data['administration']['assign_edit'])

        if field3 == var_v3.data['administration']['assign_edit']:
            var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Data table']/kendo-grid-list/div//*[@role='rowgroup']/tr[1]//*[text()='"+var_v3.data['administration']['assign_edit']+"']").click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.create_user_name).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.create_user_name).send_keys(var_v3.data['administration']['assign_edit1'])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                     var_v3.update_success, "Cập nhật thành công", "_DanhSachNguoiDung_Sua.png")

            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Data table']/kendo-grid-list/div//*[@role='rowgroup']/tr[1]//*[text()='"+var_v3.data['administration']['assign_edit']+"']").click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.create_user_name).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.create_user_name).send_keys(var_v3.data['administration']['assign_edit2'])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(2.5)



    def list_user_assign_permission(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_search1(self, var_v3.data['administration']['assign_permission'])

        field3 = var_v3.driver.find_element(By.XPATH, var_v3.list_field3a).text
        print(field3)
        print(var_v3.data['administration']['assign_permission'])

        if field3 == var_v3.data['administration']['assign_permission']:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_assign_permission).click()
            time.sleep(5)
            var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])

            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                     var_v3.title_page, "PHÂN QUYỀN NGƯỜI DÙNG", "_DanhSachNguoiDung_PhanQuyen.png")
            time.sleep(1)
            module_other_v3.close_tab()
            time.sleep(1)
            var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
            time.sleep(1)



    def list_user_lock(self, code, eventname, result, button1, button2, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_search1(self, var_v3.data['administration']['lock'])

        field3 = var_v3.driver.find_element(By.XPATH, var_v3.list_field3a).text
        print(field3)
        print(var_v3.data['administration']['lock'])
        try:
            print("vao1")
            var_v3.driver.find_element(By.XPATH, button1)
        except:
            print("vao2")
            var_v3.driver.find_element(By.XPATH, button2).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(3)

        if field3 == var_v3.data['administration']['lock']:
            print("vao3")
            var_v3.driver.find_element(By.XPATH, button1).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                     var_v3.update_success, "Cập nhật thành công", name_image)
            time.sleep(2)



    def list_user_coppy_permission(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_search1(self, var_v3.data['administration']['copy_permission'])

        field3 = var_v3.driver.find_element(By.XPATH, var_v3.list_field3a).text
        print(field3)
        print(var_v3.data['administration']['copy_permission'])
        if field3 == var_v3.data['administration']['copy_permission']:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_coppy_permission).click()
            time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                 var_v3.check_list_user_coppy_permission, "Trường chưa đổi tên (truongvck2)", "_DanhSachNguoiDung_SaoChep.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.cancel3).click()
            time.sleep(1.5)
        except:
            pass



    def list_user_change_password(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_search1(self, var_v3.data['administration']['change_password'])

        field3 = var_v3.driver.find_element(By.XPATH, var_v3.list_field3a).text
        print(field3)
        print(var_v3.data['administration']['change_password'])
        if field3 == var_v3.data['administration']['change_password']:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_change_password).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                 var_v3.update_success, "Cập nhật thành công", "_DanhSachNguoiDung_DoiMatKhau.png")
        time.sleep(2)



    def list_user_unlock_login(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_search1(self, var_v3.data['administration']['unlock_login'])

        field3 = var_v3.driver.find_element(By.XPATH, var_v3.list_field3a).text
        print(field3)
        print(var_v3.data['administration']['unlock_login'])
        if field3 == var_v3.data['administration']['unlock_login']:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_unlock_login).click()
            time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                 var_v3.check_list_user_unlock_login, "Mở khóa đăng nhập cho truongvck2 thành công",
                                                 "_DanhSachNguoiDung_MoKhoaDangNhap.png")
        time.sleep(2)



    def list_user_logout(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_field3)
        except:
            system_management.list_user(self, "", "", "")

        system_management.list_user_search1(self, var_v3.data['administration']['logout'])

        field3 = var_v3.driver.find_element(By.XPATH, var_v3.list_field3a).text
        print(field3)
        print(var_v3.data['administration']['logout'])
        if field3 == var_v3.data['administration']['logout']:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user_logout).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Danh sách người dùng",
                                                 var_v3.check_list_user_logout, "Đăng xuất tất cả thiết bị thành công",
                                                 "_DanhSachNguoiDung_DangXuat.png")
        time.sleep(2)












    def user_permission(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        hover(var_v3.administration)
        hover(var_v3.system_management)
        button = var_v3.driver.find_element(By.XPATH, var_v3.user_permission)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống -Phân quyền người dùng",
                                              var_v3.title_page1, "PHÂN QUYỀN NGƯỜI DÙNG", "_PhanQuyenNguoiDung.png")



    def user_permission_x(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.user_permission_x1).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.user_permission_x2).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.user_permission_x3).click()
            time.sleep(1)
        except:
            pass



    def user_permission_chose_user(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.user_permission2)
        except:
            system_management.user_permission(self, "", "", "")

        system_management.user_permission_x(self)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.user_permission_chose_user).click()
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.user_permission_chose_user1).click()

        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống -Phân quyền người dùng",
                                              var_v3.user_permission_chose_user_truongvck2, "Trường chưa đổi tên (truongvck2)", "_PhanQuyenNguoiDung_ChonTaiKhoan.png")

        var_v3.driver.find_element(By.XPATH, var_v3.user_permission_chose_user_truongvck2).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(4)



    def user_permission_permission_1role(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_user_permission)
        except:
            system_management.user_permission_chose_user(self, "", "", "")


        time.sleep(1)
        if var_v3.driver.find_element(By.XPATH, var_v3.role_customer_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.role_customer_label).click()
            time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống -Phân quyền người dùng",
                                              var_v3.saved, "Đã lưu", "_PhanQuyenNguoiDung_Chon1VaiTro.png")

        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.role_customer_input).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.role_customer_label).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2)



    def user_permission_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_user_permission)
        except:
            system_management.user_permission_chose_user(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.user_permission_search_input).send_keys(var_v3.data['administration']['permission_search'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống -Phân quyền người dùng",
                                              var_v3.check_user_permission_search, var_v3.data['administration']['permission_search'],
                                                 "_PhanQuyenNguoiDung_TimKiem.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.user_permission_x2).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.user_permission_x3).click()
            time.sleep(1)
        except:
            pass
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)



    def chose_permission(self, code, eventname, result, image, ai, minitor, route, report_bgt, report_business,
                         bus, utilities, administration, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_user_permission)
        except:
            system_management.user_permission_chose_user(self, "", "", "")

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_image_input).is_selected() == image:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_image_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_ai_input).is_selected() == ai:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_ai_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_minitor_input).is_selected() == minitor:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_minitor_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_route_input).is_selected() == route:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_route_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_report_bgt_input).is_selected() == report_bgt:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_report_bgt_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_report_business_input).is_selected() == report_business:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_report_business_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_bus_input).is_selected() == bus:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_bus_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_utilities_input).is_selected() == utilities:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_utilities_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_administration_input).is_selected() == administration:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_administration_label).click()
            time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống -Phân quyền người dùng",
                                              var_v3.saved, "Đã lưu", name_image)

        time.sleep(3)










    def role_management(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        hover(var_v3.administration)
        hover(var_v3.system_management)
        button = var_v3.driver.find_element(By.XPATH, var_v3.role_management)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Quản lý vai trò",
                                              var_v3.title_page1, "QUẢN LÝ VAI TRÒ", "_QuanLyVaiTro.png")



    def role_management_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_name)
        except:
            system_management.role_management(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_input).send_keys(var_v3.data['administration']['role_search'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Quản lý vai trò",
                                              var_v3.list_field2, var_v3.data['administration']['role_search'], "_QuanLyVaiTro_TimKiem.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_iconx).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)



    def role_management_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_name)
        except:
            system_management.role_management(self, "", "", "")

        time.sleep(2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_role_management_add_new)
            print("vao case xoa")
            system_management.role_management_delete(self, "", "", "")
        except:
            pass

        var_v3.driver.implicitly_wait(4)
        var_v3.driver.find_element(By.XPATH, var_v3.add_new).click()
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.create_role_name).send_keys(var_v3.data['administration']['create_role_name'])
        var_v3.driver.find_element(By.XPATH, var_v3.create_role_describe).send_keys(var_v3.data['administration']['create_role_description'])

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_image_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_image_label).click()
            time.sleep(0.5)

        if var_v3.driver.find_element(By.XPATH, var_v3.permission_ai_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.permission_ai_label).click()
            time.sleep(0.5)

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Quản lý vai trò",
                                              var_v3.add_new_success, "Thêm mới thành công", "_QuanLyVaiTro_ThemMoi_message.png")

        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Quản lý vai trò",
                                              var_v3.check_role_management_add_new, "vai trò test", "_QuanLyVaiTro_ThemMoi.png")



    def role_management_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_name)
        except:
            system_management.role_management(self, "", "", "")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_iconx).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.implicitly_wait(4)

        var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_input).send_keys(var_v3.data['administration']['create_role_name'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)

        role_name = var_v3.driver.find_element(By.XPATH, var_v3.list_field2).text
        if role_name == var_v3.data['administration']['create_role_name']:
            var_v3.driver.find_element(By.XPATH, var_v3.role_management_delete).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Quản lý vai trò",
                                              var_v3.delete_success, "Xóa thành công", "_QuanLyVaiTro_Xoa.png")

        time.sleep(2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_iconx).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)



    def role_management_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_name)
        except:
            system_management.role_management(self, "", "", "")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_iconx).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.implicitly_wait(4)

        var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_input).send_keys(var_v3.data['administration']['role_edit'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)

        role_name = var_v3.driver.find_element(By.XPATH, var_v3.list_field2).text
        if role_name == var_v3.data['administration']['role_edit']:
            var_v3.driver.find_element(By.XPATH, var_v3.role_management_edit).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.create_role_describe).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.create_role_describe).send_keys(var_v3.data['administration']['create_role_description_edit'])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.permission_image_label).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.permission_image_label).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(1)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Quản lý vai trò",
                                              var_v3.update_success, "Cập nhật thành công", "_QuanLyVaiTro_Sua_Message.png")

        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị hệ thống - Quản lý vai trò",
                                              var_v3.check_role_management_edit, var_v3.data['administration']['create_role_description_edit'], "_QuanLyVaiTro_Sua.png")



        try:
            var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_iconx).click()
            time.sleep(1)
        except:
            pass
        var_v3.driver.find_element(By.XPATH, var_v3.role_management_search_input).send_keys(var_v3.data['administration']['role_edit'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.role_management_edit).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.create_role_describe).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.create_role_describe).send_keys(var_v3.data['administration']['create_role_description_edit1'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.permission_image_label).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.permission_image_label).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2.5)





class config_alert:


    def alert_management(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        hover(var_v3.administration)
        hover(var_v3.config_alert)
        button = var_v3.driver.find_element(By.XPATH, var_v3.alert_management)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo -  Lịch sử cảnh báo ",
                                              var_v3.title_page1, "LỊCH SỬ CẢNH BÁO", "_LichSuCanhBao.png")



    def alert_management_x(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.alert_management_x1).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.alert_management_x2).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.alert_management_x3).click()
            time.sleep(1)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.alert_management_x4).click()
            time.sleep(1)
        except:
            pass



    def alert_management_from_day_to_day(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.note_handle)
        except:
            config_alert.alert_management(self, "", "", "")

        config_alert.alert_management_x(self)

        delete = var_v3.driver.find_element(By.XPATH, var_v3.alert_management_from_day)
        delete.send_keys(Keys.CONTROL, "a")
        var_v3.driver.find_element(By.XPATH, var_v3.alert_management_from_day).send_keys(var_v3.data['administration']['from_day_to_day'])
        time.sleep(1)

        delete = var_v3.driver.find_element(By.XPATH, var_v3.alert_management_to_day)
        delete.send_keys(Keys.CONTROL, "a")
        var_v3.driver.find_element(By.XPATH, var_v3.alert_management_to_day).send_keys(var_v3.data['administration']['from_day_to_day'])
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        time.sleep(3)
        logging.info("-------------------------")
        logging.info("Quản trị - Cấu hình cảnh báo -  Lịch sử cảnh báo")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_text = var_v3.driver.find_element(By.XPATH, var_v3.list_field3b).text
            logging.info(check_text)
            logging.info(check_text[6::])
            logging.info(var_v3.data['administration']['from_day_to_day'])
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)

            if check_text[6::] == var_v3.data['administration']['from_day_to_day']:
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_LichSuCanhBao_TuNgayDenNgay.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_LichSuCanhBao_TuNgayDenNgay.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_LichSuCanhBao_TuNgayDenNgay.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_LichSuCanhBao_TuNgayDenNgay.png")



    def alert_management_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.note_handle)
        except:
            config_alert.alert_management(self, "", "", "")

        config_alert.alert_management_x(self)

        button = var_v3.driver.find_element(By.XPATH, var_v3.alert_management_group)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.group_select_onegroup).click()
        except:
            button = var_v3.driver.find_element(By.XPATH, var_v3.alert_management_group)
            var_v3.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.group_select_onegroup).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Lịch sử cảnh báo",
                                              var_v3.check_alert_management_group, "Chọn nhóm phương tiện", "_LichSuCanhBao_ChonNhom.png")
        config_alert.alert_management_x(self)



    def alert_management_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.note_handle)
        except:
            config_alert.alert_management(self, "", "", "")

        config_alert.alert_management_x(self)


        var_v3.driver.find_element(By.XPATH, var_v3.alert_management_vehicle).click()

        time.sleep(1)
        # name_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.combobox_checkbox1_label).text
        var_v3.driver.find_element(By.XPATH, var_v3.alert_management_vehicle).send_keys(var_v3.data['administration']['vehicle'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.combobox_checkbox1_label).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Lịch sử cảnh báo",
                                              var_v3.field2b, var_v3.data['administration']['vehicle'], "_LichSuCanhBao_ChonPhuongTien.png")
        config_alert.alert_management_x(self)



    def alert_management_type_warn(self, code, eventname, result, button_select, type_check, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.note_handle)
        except:
            config_alert.alert_management(self, "", "", "")

        config_alert.alert_management_x(self)


        var_v3.driver.find_element(By.XPATH, var_v3.alert_management_type_warn).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, button_select).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        time.sleep(2.5)
        if type_check == "1":
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Lịch sử cảnh báo",
                                                  path_check, desire, name_image)
        if type_check == "2":
            module_other_v3.write_result_text_try_if_other(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Lịch sử cảnh báo",
                                                  path_check, desire, name_image)
        config_alert.alert_management_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        time.sleep(1.5)



    def alert_management_status(self, code, eventname, result, button_select, type_check, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.note_handle)
        except:
            config_alert.alert_management(self, "", "", "")

        config_alert.alert_management_x(self)
        var_v3.driver.find_element(By.XPATH, var_v3.alert_management_status).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, button_select).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        time.sleep(2.5)
        if type_check == "1":
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo -  Lịch sử cảnh báo",
                                                  path_check, desire, name_image)
        if type_check == "2":
            logging.info("-------------------------")
            logging.info("Quản trị - Cấu hình cảnh báo - Lịch sử cảnh báo")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            try:
                check_text = var_v3.driver.find_element(By.XPATH, var_v3.has_read).text
                logging.info(check_text)
                logging.info(desire)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            except:
                pass
            try:
                check_text = var_v3.driver.find_element(By.XPATH, var_v3.has_handle).text
                logging.info(check_text)
                logging.info(desire)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            except:
                pass
            try:
                check_text = var_v3.driver.find_element(By.XPATH, var_v3.no_data1).text
                logging.info(check_text)
                logging.info(desire)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            except:
                pass

        # config_alert.alert_management_x(self)
        # var_v3.driver.find_element(By.XPATH, var_v3.see_report).click()
        # time.sleep(1.5)



    def history_warm_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.note_handle)
        except:
            config_alert.alert_management(self, "", "", "")

        config_alert.alert_management_from_day_to_day(self, "", "", "")

        name_vehicle = var_v3.driver.find_element(By.XPATH, var_v3.field2b).text
        var_v3.driver.find_element(By.XPATH, var_v3.history_warm_route).click()
        time.sleep(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Lịch sử cảnh báo",
                                              var_v3.check_history_warm_route, name_vehicle, "_LichSuCanhBao_IconLoTrinh.png")

        time.sleep(1)
        module_other_v3.close_tab()
        time.sleep(1)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)









    def config_warm_user(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        hover(var_v3.administration)
        hover(var_v3.config_alert)
        button = var_v3.driver.find_element(By.XPATH, var_v3.config_warm_user)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo -  Cấu hình cảnh báo người dùng ",
                                              var_v3.title_page1, "CẤU HÌNH CẢNH BÁO CHO NGƯỜI DÙNG", "_CauHinhCanhBaoChoNguoiDung.png")



    def config_warm_user_iconx(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.config_warm_user_iconx1).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.config_warm_user_iconx2).click()
            time.sleep(0.5)
        except:
            pass



    def config_warm_user_search(self, code, eventname, result, type, select, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hour_warm)
        except:
            config_alert.config_warm_user(self, "", "", "")

        config_alert.config_warm_user_iconx(self)
        config_alert.config_warm_user_iconx(self)

        var_v3.driver.find_element(By.XPATH, type).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, select).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Cấu hình cảnh báo cho người dùng",
                                              path_check, desire, name_image)



    def config_warm_user_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hour_warm)
        except:
            config_alert.config_warm_user(self, "", "", "")

        config_alert.config_warm_user_iconx(self)
        var_v3.driver.find_element(By.XPATH, var_v3.add_new).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.info_setting_select_user).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.info_setting_select_truongvck4).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.info_setting_select_vehicle).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.info_setting_select_all).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.info_setting_set_warm_web_label).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.info_setting_time_all).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.info_setting_warm_on_the_machine).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save_and_back).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Cấu hình cảnh báo cho người dùng",
                                              var_v3.add_new_success, "Thêm mới thành công", "_CauHinhCanhBaoChoNguoiDung_ThemMoi.png")
        time.sleep(1)



    def config_warm_user_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hour_warm)
        except:
            config_alert.config_warm_user(self, "", "", "")


        var_v3.driver.refresh()
        time.sleep(6)
        config_alert.config_warm_user_search(self, "", "", "", var_v3.config_warm_user_user,
                                                            var_v3.info_setting_select_truongvck4,
                                                            var_v3.check_config_warm_user_user, "", "")

        name = var_v3.driver.find_element(By.XPATH, var_v3.check_config_warm_user_user).text
        if name == "truongvck4":
            var_v3.driver.find_element(By.XPATH, var_v3.config_warm_user_edit).click()
            time.sleep(2)
            if var_v3.driver.find_element(By.XPATH, var_v3.info_setting_warm_on_the_machine_input).is_selected() == True:
                var_v3.driver.find_element(By.XPATH, var_v3.info_setting_warm_on_the_machine_label).click()
            time.sleep(1)

            if var_v3.driver.find_element(By.XPATH, var_v3.info_setting_warm_urgent_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, var_v3.info_setting_warm_urgent_label).click()
            time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.save_and_back).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Cấu hình cảnh báo cho người dùng",
                                              var_v3.check_config_warm_lost_gps, "Cảnh báo cua gấp", "_CauHinhCanhBaoChoNguoiDung_Sua.png")



    def config_warm_user_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.hour_warm)
        except:
            config_alert.config_warm_user(self, "", "", "")

        var_v3.driver.refresh()
        time.sleep(6)
        config_alert.config_warm_user_search(self, "", "", "", var_v3.config_warm_user_user,
                                                            var_v3.info_setting_select_truongvck4,
                                                            var_v3.check_config_warm_user_user, "", "")

        name = var_v3.driver.find_element(By.XPATH, var_v3.check_config_warm_user_user).text
        if name == "truongvck4":
            var_v3.driver.find_element(By.XPATH, var_v3.config_warm_user_delete).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result,
                                                     "Quản trị - Cấu hình cảnh báo - Cấu hình cảnh báo cho người dùng",
                                                     var_v3.delete_success, "Xóa thành công", "_CauHinhCanhBaoChoNguoiDung_Xoa.png")
            time.sleep(1)








    def config_warm_company(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")
        hover(var_v3.administration)
        hover(var_v3.config_alert)
        button = var_v3.driver.find_element(By.XPATH, var_v3.config_warm_company)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo -  Cấu hình cảnh báo công ty ",
                                              var_v3.title_page, "CẤU HÌNH CẢNH BÁO CÔNG TY", "_CauHinhCanhBaoCongTy.png")



    def config_warm_company_search(self, code, eventname, result, name_warm):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.minutes_to_repeat)
        except:
            config_alert.config_warm_company(self, "", "", "")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.config_warm_company_iconx).click()
            time.sleep(1)
        except:
            pass

        var_v3.driver.find_element(By.XPATH, var_v3.select_warm).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='"+name_warm+"']").click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Cấu hình cảnh báo công ty",
                                              var_v3.check_config_warm_user_search, name_warm, "_CauHinhCanhBaoCongTy_Timkiem.png")



    def config_warm_company_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.minutes_to_repeat)
        except:
            config_alert.config_warm_company(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.add_new).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.add_new_warm_company_select).click()
        time.sleep(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.add_new_warm_company_ha_ben).click()
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.add_new_warm_company_select).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.add_new_warm_company_value).send_keys("5")
        time.sleep(0.5)
        if var_v3.driver.find_element(By.XPATH, var_v3.warm_timeline_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.warm_timeline_label).click()
            time.sleep(1)

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.save).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Cấu hình cảnh báo công ty",
                                                     var_v3.add_new_success, "Thêm mới thành công",
                                                     "_CauHinhCanhBaoCongTy_ThemMoi.png")
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.cancel3).click()
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Không tạo được Cảnh báo hạ ben do đang lõi chưa xóa được")

        time.sleep(1)



    def config_warm_company_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.minutes_to_repeat)
        except:
            config_alert.config_warm_company(self, "", "", "")


        config_alert.config_warm_company_search(self, "", "", "", "Cảnh báo hạ ben")
        name = var_v3.driver.find_element(By.XPATH, var_v3.check_config_warm_user_search).text
        if name == "Cảnh báo hạ ben":
            var_v3.driver.find_element(By.XPATH, var_v3.config_warm_user_edit).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.add_new_warm_company_value).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.add_new_warm_company_value).send_keys("13")
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(2.5)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Cấu hình cảnh báo công ty",
                                                     var_v3.check_config_warm_company_edit, "13", "_CauHinhCanhBaoCongTy_Sua.png")



    def config_warm_company_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(2.5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.minutes_to_repeat)
        except:
            config_alert.config_warm_company(self, "", "", "")


        config_alert.config_warm_company_search(self, "", "", "", "Cảnh báo hạ ben")
        name = var_v3.driver.find_element(By.XPATH, var_v3.check_config_warm_user_search).text
        if name == "Cảnh báo hạ ben":
            var_v3.driver.find_element(By.XPATH, var_v3.config_warm_user_delete).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Cấu hình cảnh báo - Cấu hình cảnh báo công ty",
                                                     var_v3.delete_success, "Xóa thành công", "_CauHinhCanhBaoCongTy_Xoa.png")
            time.sleep(1)





class driver_management:



    def list_driver(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        hover(var_v3.administration)
        hover(var_v3.driver_management)
        button = var_v3.driver.find_element(By.XPATH, var_v3.list_driver)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                              var_v3.title_page1, "DANH SÁCH LÁI XE", "_DanhSachLaiXe.png")



    def list_driver_search(self, code, eventname, result, data, type_search, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_search_iconx).click()
            time.sleep(0.5)
        except:
            pass
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_input).send_keys(data)
        time.sleep(0.5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_select_search).click()
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_select_search1).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='"+type_search+"']").click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                              path_check, desire, name_image)



    def list_driver_dowload_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")

        var_v3.driver.refresh()
        time.sleep(5)
        var_v3.driver.find_element(By.XPATH, var_v3.add_fast).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.dowload_example_excel).click()
        time.sleep(5)
        logging.info("Quản trị - Quản lý lái xe - Danh sách lái xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r"danhsachlaixe_taimau_excel.xlsx"))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_DanhSachLaiXe_XuatExcel.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_DanhSachLaiXe_XuatExcel.png")



    def list_driver_upload_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_example_excel)
        except:
            driver_management.list_driver_dowload_excel(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.chose_file).click()
        time.sleep(1)
        subprocess.Popen(var_v3.uploadpath+"template_drivers.exe")
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.save2).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                                 var_v3.check_list_driver_search_upload_excel, "Mã nhân viên đã tồn tại\nSố chứng minh nhân dân đã tồn tại\nSố giấy phép lái xe đã tồn tại\nThẻ đã được gán cho lái xe", "_DanhSachLaiXe_UpLoad.png")

        try:
            var_v3.driver.implicitly_wait(2)
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
            time.sleep(1.5)
        except:
            pass



    def list_driver_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.add_new).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_code).send_keys("BA023232")
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_name).send_keys("Vương Lâm")
        time.sleep(0.5)
        delete = var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_brithday)
        delete.send_keys(Keys.CONTROL, "a")
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_brithday).send_keys("25/03/1996")
        time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_phone).send_keys("083728351")
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_phone1).send_keys("083728352")
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_phone2).send_keys("083728353")
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_adress).send_keys("250 Phan Trọng Tuệ, Thanh Trì, Hà Nội")
        time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_assign).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_assign_truongvck1).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_vehicle).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_vehicle_33B30822).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_cmnd).send_keys("0827232322")

        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_liscense_plate).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_liscense_plate_b1).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_liscense_plate_number).send_keys("00329549594")
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_adress2).send_keys("Tổng cục Đường bộ Việt Nam")

        delete = var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_day1)
        delete.send_keys(Keys.CONTROL, "a")
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_day1).send_keys("23/02/2013")

        delete = var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_day2)
        delete.send_keys(Keys.CONTROL, "a")
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_day2).send_keys("23/02/2033")
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.save_and_addnew).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                              var_v3.add_new_success, "Thêm mới thành công", "_DanhSachLaiXe_ThemMoi.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.cancel3).click()
            time.sleep(1)
        except:
            pass



    def list_driver_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")

        driver_management.list_driver_search(self, "", "", "", "Vương Lâm", "Tên nhân viên", "", "", "")


        name = var_v3.driver.find_element(By.XPATH, var_v3.list_driver_search_namenv).text
        if name == "Vương Lâm":
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_edit).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_cmnd).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_add_new_cmnd).send_keys(var_v3.data['administration']['listdriver_edit'])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(2.5)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                                     var_v3.list_driver_search_cmnd, var_v3.data['administration']['listdriver_edit'], "_DanhSachLaiXe_Sua.png")



    def list_driver_lock(self, code, eventname, result, button, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")


        driver_management.list_driver_search(self, "", "", "", "Vương Lâm", "Tên nhân viên", "", "", "")
        if var_v3.driver.find_element(By.XPATH, var_v3.list_driver_lock1).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_lock1).click()
            time.sleep(1)

        name = var_v3.driver.find_element(By.XPATH, var_v3.list_driver_search_namenv).text
        if name == "Vương Lâm":
            var_v3.driver.find_element(By.XPATH, button).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                                     var_v3.update_success, "Cập nhật thành công", name_image)
            time.sleep(2)



    def list_driver_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")


        driver_management.list_driver_search(self, "", "", "", "Vương Lâm", "Tên nhân viên", "", "", "")
        if var_v3.driver.find_element(By.XPATH, var_v3.list_driver_lock1).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_lock1).click()
            time.sleep(1)

        name = var_v3.driver.find_element(By.XPATH, var_v3.list_driver_search_namenv).text
        if name == "Vương Lâm":
            var_v3.driver.find_element(By.XPATH, var_v3.list_driver_icon_delete).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                                     var_v3.delete_success, "Xóa thành công", "_DanhSachLaiXe_Xoa.png")
        time.sleep(1)
        var_v3.driver.refresh()
        time.sleep(5)



    def list_driver_dowload(self, code, eventname, result, button, file, name_image):
        module_other_v3.delete_excel()
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                               file, name_image)



    def list_user_hide(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                                       var_v3.update_success, "Cập nhật thành công", "_DanhSachLaiXe_AnHienCot_Message.png")

        module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                              var_v3.check_list_user_hide, "_DanhSachLaiXe_AnHienCot.png")


        var_v3.driver.find_element(By.XPATH, var_v3.hide_column).click()
        time.sleep(2)
        if var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.hide_field4).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(3)



    def list_user_history_driver(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.gplx)
        except:
            driver_management.list_driver(self, "", "", "")

        var_v3.driver.refresh()
        time.sleep(5)
        var_v3.driver.find_element(By.XPATH, var_v3.list_user_history_driver).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Danh sách lái xe",
                                              var_v3.check_title_popup, "LỊCH SỬ LÁI XE", "_DanhSachLaiXe_LichSuLaiXe.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
            time.sleep(1)
        except:
            pass







    def manage_ticket(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])
        hover(var_v3.administration)
        hover(var_v3.driver_management)
        button = var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket)
        var_v3.driver.execute_script("arguments[0].click();", button)
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                              var_v3.title_page1, "QUẢN LÝ THẺ", "_QuanLyThe.png")



    def manage_ticket_search(self, code, eventname, result, data):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_ticket)
        except:
            driver_management.manage_ticket(self, "", "", "")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.title_xoa).click()
            time.sleep(0.5)
        except:
            pass
        var_v3.driver.find_element(By.XPATH, var_v3.list_driver_input).send_keys(data)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                              var_v3.check_manage_ticket_search, data, "_QuanLyThe_TimKiem.png")



    def manage_ticket_status(self, code, eventname, result, checkbox_input, checkbox_label, type_check, path_check, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_ticket)
        except:
            driver_management.manage_ticket(self, "", "", "")

        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.title_xoa).click()
            time.sleep(0.5)
        except:
            pass

        if var_v3.driver.find_element(By.XPATH, checkbox_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, checkbox_label).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search).click()
        time.sleep(2)
        if type_check == "0":
            module_other_v3.write_result_displayed_try(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                                  path_check, name_image)

        if type_check == "1":
            module_other_v3.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                                  path_check, name_image)


        if var_v3.driver.find_element(By.XPATH, checkbox_input).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, checkbox_label).click()
        time.sleep(1)



    def manage_ticket_dowload_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_ticket)
        except:
            driver_management.manage_ticket(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.add_fast).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.dowload_example_excel).click()
        time.sleep(5)
        logging.info("Quản trị - Quản lý lái xe - Quản lý thẻ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r"quanlythe_taimau_excel.xlsx"))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_QuanLyThe_XuatExcel.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_QuanLyThe_XuatExcel.png")



    def manage_ticket_upload_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_example_excel)
        except:
            driver_management.manage_ticket_dowload_excel(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.chose_file).click()
        time.sleep(1)
        subprocess.Popen(var_v3.uploadpath+"template_rfid.exe")
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                                 var_v3.check_manage_ticket_upload_excel, "Mã số thẻ đã tồn tại!", "_QuanLyThe_UpLoad.png")

        var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        time.sleep(1.5)



    def manage_ticket_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 14, "")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_ticket)
        except:
            driver_management.manage_ticket(self, "", "", "")
        try:
            driver_management.manage_ticket_delete(self, "", "", "")
        except:
            pass
        var_v3.driver.refresh()
        time.sleep(5)

        var_v3.driver.find_element(By.XPATH, var_v3.add_new).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket_add_new_code).send_keys(var_v3.data['administration']['manage_ticket_code'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket_add_new_type).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket_add_new_type_rfid).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket_add_new_describe).send_keys(var_v3.data['administration']['manage_ticket_describe'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 14, var_v3.data['administration']['manage_ticket_code'])

        module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                              var_v3.add_new_success, "Thêm mới thành công", "_QuanLyThe_ThemMoi.png")

        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.cancel3).click()
            time.sleep(1)
        except:
            pass



    def manage_ticket_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_ticket)
        except:
            driver_management.manage_ticket(self, "", "", "")

        driver_management.manage_ticket_search(self, "", "", "", var_v3.data['administration']['manage_ticket_code'])

        code_check = var_v3.driver.find_element(By.XPATH, var_v3.check_manage_ticket_search).text
        if code_check == var_v3.data['administration']['manage_ticket_code']:
            var_v3.driver.find_element(By.XPATH, var_v3.check_manage_ticket_search).click()
            var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket_add_new_describe).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket_add_new_describe).send_keys(var_v3.data['administration']['manage_ticket_describe_edit'])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(2.5)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                                     var_v3.check_manage_ticket_describe, var_v3.data['administration']['manage_ticket_describe_edit'],
                                                     "_QuanLyThe_Sua.png")



    def manage_ticket_lock(self, code, eventname, result, button, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_ticket)
        except:
            driver_management.manage_ticket(self, "", "", "")

        driver_management.manage_ticket_search(self, "", "", "", var_v3.data['administration']['manage_ticket_code'])


        code_check = var_v3.driver.find_element(By.XPATH, var_v3.check_manage_ticket_search).text
        if code_check == var_v3.data['administration']['manage_ticket_code']:
            var_v3.driver.find_element(By.XPATH, button).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                                     var_v3.update_success, "Cập nhật thành công", name_image)
            time.sleep(2)



    def manage_ticket_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_ticket)
        except:
            driver_management.manage_ticket(self, "", "", "")

        driver_management.manage_ticket_search(self, "", "", "", var_v3.data['administration']['manage_ticket_code'])


        code_check = var_v3.driver.find_element(By.XPATH, var_v3.check_manage_ticket_search).text
        if code_check == var_v3.data['administration']['manage_ticket_code']:
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.list_driver_icon_delete).click()
            except:
                try:
                    var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket_delete).click()
                except:
                    var_v3.driver.find_element(By.XPATH, var_v3.manage_ticket_delete1).click()

            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                                     var_v3.delete_success, "Xóa thành công", "_QuanLyThe_Xoa.png")
        var_v3.driver.refresh()
        time.sleep(5)



    def manage_ticket_dowload(self, code, eventname, result, button, file, name_image):
        module_other_v3.delete_excel()
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.type_ticket)
        except:
            driver_management.manage_ticket(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, button).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "Quản trị - Quản lý lái xe - Quản lý thẻ",
                                               file, name_image)




