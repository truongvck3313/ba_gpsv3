import logging
import minitor_v3
import var_v3
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import module_other_v3
import login_v3
from retry import retry
import administration
import image_v3
import subprocess
from seleniumwire.utils import decode as sw_decode
import json







class  landmark_management:


    def landmark_management_search(self, type, data_search):
        var_v3.driver.implicitly_wait(5)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_management_icon_search).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[text()='"+type+"']").click()
        time.sleep(1)
        if type == "Tìm tọa độ":
            var_v3.driver.find_element(By.XPATH, var_v3.search_location_input2).send_keys(data_search)
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.search_location_input2).send_keys(Keys.ENTER)
        else:
            var_v3.driver.find_element(By.XPATH, var_v3.search_location_input1).clear()
            var_v3.driver.find_element(By.XPATH, var_v3.search_location_input1).send_keys(data_search)
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.search_location_input1).send_keys(Keys.ENTER)
        time.sleep(2.5)


    def landmark_management1_iconx(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_iconx1).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_iconx2).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_iconx3).click()
            time.sleep(0.5)
        except:
            pass


    def landmark_management1(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'],  var_v3.data['login']['khongnhom_quantri_mk'])

        administration.hover(var_v3.utility)
        administration.hover(var_v3.landmark_management)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result,  "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                                 var_v3.check_landmark_management1, "Hiển thị tên điểm",  "_QuanTriDiem.png")


    def landmark_management1_search_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1)
        except:
            landmark_management.landmark_management1(self, "", "", "")

        landmark_management.landmark_management_search(self, "Tìm điểm", var_v3.data['utility']['search_location'])

        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                              var_v3.check_landmark_management1_search_location, var_v3.data['utility']['search_location'],
                                                 "_QuanTriDiem_TimKiem_TimDiem.png")


    def landmark_management1_search_adress(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1)
        except:
            landmark_management.landmark_management1(self, "", "", "")

        landmark_management.landmark_management_search(self, "Tìm địa chỉ", var_v3.data['utility']['search_adress'])

        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                              var_v3.check_landmark_management1_search_location, "Nhà của Trường1",
                                                 "_QuanTriDiem_TimKiem_TimDiaChi.png")


    def landmark_management1_search_toado(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1)
        except:
            landmark_management.landmark_management1(self, "", "", "")

        landmark_management.landmark_management_search(self, "Tìm tọa độ", var_v3.data['utility']['search_toado'])

        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                              var_v3.check_landmark_management1_search_location, "Địa chỉ :  Phòng trọ cũ trường",
                                                 "_QuanTriDiem_TimKiem_TimToaDo.png")


    def landmark_management1_select_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1)
        except:
            landmark_management.landmark_management1(self, "", "", "")

        var_v3.driver.refresh()
        time.sleep(5)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_select_location).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_select_location_home).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_management_icon_search).click()

        module_other_v3.write_result_text_try_if_src(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                              var_v3.check_landmark_management1_select_location, "/assets/images/utility/landmark-management/point/1.png",
                                                 "_QuanTriDiem_ChonLoaiDiem.png", -54)


    def landmark_management1_select_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1)
        except:
            landmark_management.landmark_management1(self, "", "", "")

        landmark_management.landmark_management1_iconx(self)

        var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_select_group).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_select_group_all).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_management_icon_search).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                              var_v3.check_landmark_management1_select_group, "Chọn nhóm điểm",
                                                 "_QuanTriDiem_ChonNhomDiem.png")


    def landmark_management1_select_landmark_in_list(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1)
        except:
            landmark_management.landmark_management1(self, "", "", "")

        var_v3.driver.refresh()
        time.sleep(7)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1_select_location).click()
        except:
            var_v3.driver.refresh()
            time.sleep(7)
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1_select_location).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.my_home).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                              var_v3.check_landmark_management1_select_landmark_in_list, "Phòng trọ cũ trường",
                                                 "_QuanTriDiem_ChonDiemTrenDanhSachDiem.png")


    def landmark_management1_eport_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1)
        except:
            landmark_management.landmark_management1(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.export_excel).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                               "quantridiem.xlsx", "_QuanTriDiem_XuatExcel.png")


    def vehicle_type_categoty_dowload_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_landmark_management1)
        except:
            landmark_management.landmark_management1(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.upload_excel).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.dowload_example_excel).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                               "quantridiem_taifilemau.xlsx", "_QuanTriDiem_TaiMauExel.png")


    def vehicle_type_categoty_upload_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_example_excel)
        except:
            landmark_management.vehicle_type_categoty_dowload_excel(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.type_landmark).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.type_landmark_stop).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.chose_file1).click()
        time.sleep(1)
        subprocess.Popen(var_v3.uploadpath+"template_landmark.exe")
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.save2).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị điểm",
                                                 var_v3.checl_vehicle_type_categoty_upload_excel,
                                                 "Có một số điểm không thể nhập do thông tin không hợp lệ. Vui lòng kiểm tra file tải về và thử lại",
                                                 "_QuanTriDiem_Upload.png")

        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
            time.sleep(1.5)
        except:
            pass


    def landmark_management1_refresh(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_refresh).click()
        except:
            landmark_management.landmark_management1(self, "", "", "")
            del var_v3.driver.requests
            var_v3.driver.find_element(By.XPATH, var_v3.landmark_management1_refresh).click()
        time.sleep(1.3)
        logging.info("-------------------------")
        logging.info("TIỆN ÍCH - Quản trị điểm - Quản trị điểm")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)

        for request in var_v3.driver.requests:
            print(request.url[-23::])
            if request.url[-23::] == "api/v1/landmarks/user/1":
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
            else:
                print("không có  response")








    def landmark_group_management(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'],  var_v3.data['login']['khongnhom_quantri_mk'])

        administration.hover(var_v3.utility)
        administration.hover(var_v3.landmark_management)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_group_management).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result,  "TIỆN ÍCH - Quản trị điểm - Quản trị nhóm điểm",
                                                 var_v3.title_page1, "QUẢN TRỊ NHÓM ĐIỂM",  "_QuanTriNhomDiem.png")



    def landmark_group_management_search(self, code, eventname, result, search_input, data, path_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmark)
        except:
            landmark_management.landmark_group_management(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmarkc).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, search_input).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, search_input).send_keys(data)
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị nhóm điểm",
                                              var_v3.check_landmark_group_management_search, data, path_image)



    def landmark_group_management_add_new_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmark)
        except:
            landmark_management.landmark_group_management(self, "", "", "")


        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.group_e_edit).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(3)
        except:
            pass
        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.group_e).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(3)
        except:
            pass
        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.group_e_coppy).click()
            time.sleep(1.5)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(3)
        except:
            pass



        var_v3.driver.find_element(By.XPATH, var_v3.icon_add_new).click()
        time.sleep(3)
        var_v3.driver.find_element(By.XPATH, var_v3.add_new_group_input).click()
        var_v3.driver.find_element(By.XPATH, var_v3.add_new_group_input).send_keys(var_v3.data['utility']['group_addnew'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_save1).click()
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị nhóm điểm",
                                              var_v3.add_new_success, "Thêm mới thành công", "_QuanTriNhomDiem_ThemMoiNhom.png")


        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.icon_cancel1).click()
            time.sleep(1)
        except:
            pass



    def landmark_group_management_coppy(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmark)
        except:
            landmark_management.landmark_group_management(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.group_e).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_coppy).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị nhóm điểm",
                                              var_v3.add_new_success, "Thêm mới thành công", "_QuanTriNhomDiem_SaoChep.png")



    def landmark_group_management_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmark)
        except:
            landmark_management.landmark_group_management(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.group_e_coppy).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_edit).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.add_new_group_input6).clear()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.add_new_group_input6).send_keys(var_v3.data['utility']['group_edit'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_save6).click()
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị nhóm điểm",
                                              var_v3.update_success, "Cập nhật thành công", "_QuanTriNhomDiem_Sua.png")



    def landmark_group_management_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmark)
        except:
            landmark_management.landmark_group_management(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.group_e_edit).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(1.3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị nhóm điểm",
                                              var_v3.delete_success, "Xóa thành công", "_QuanTriNhomDiem_Xoa.png")



    def landmark_group_assign(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmark)
        except:
            landmark_management.landmark_group_management(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.group_e).click()
        time.sleep(1)


        if var_v3.driver.find_element(By.XPATH, var_v3.list_land_mark1_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.list_land_mark1_label).click()
            time.sleep(1)


        if var_v3.driver.find_element(By.XPATH, var_v3.list_user1_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user1_label).click()
            time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1.3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Quản trị nhóm điểm",
                                              var_v3.saved, "Đã lưu", "_QuanTriNhomDiem_GanNhomDiem.png")
        time.sleep(1)


        if var_v3.driver.find_element(By.XPATH, var_v3.list_land_mark1_input).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.list_land_mark1_label).click()
            time.sleep(1)

        if var_v3.driver.find_element(By.XPATH, var_v3.list_user1_input).is_selected() == True:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user1_label).click()
            time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2)
        var_v3.driver.refresh()
        time.sleep(6)
        var_v3.driver.find_element(By.XPATH, var_v3.group_e).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_delete).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(2)







    def landmark_group_permission(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'],  var_v3.data['login']['khongnhom_quantri_mk'])

        administration.hover(var_v3.utility)
        administration.hover(var_v3.landmark_management)
        var_v3.driver.find_element(By.XPATH, var_v3.landmark_group_permission).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result,  "TIỆN ÍCH - Quản trị điểm - Phân quyền nhóm điểm",
                                                 var_v3.title_page1, "PHÂN QUYỀN NHÓM ĐIỂM",  "_PhanQuyenNhomDiem.png")


    def landmark_group_permission_search(self, code, eventname, result, search_input, data, path_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmark)
        except:
            landmark_management.landmark_group_permission(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, search_input).click()
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, search_input).send_keys(data)
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Phân quyền nhóm điểm",
                                              var_v3.check_landmark_group_management_search, data, path_image)


    def landmark_group_permission_assign(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_group_landmark)
        except:
            landmark_management.landmark_group_permission(self, "", "", "")


        if var_v3.driver.find_element(By.XPATH, var_v3.list_user1_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.list_user1_label).click()
            time.sleep(1)


        if var_v3.driver.find_element(By.XPATH, var_v3.group1_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.group1_label).click()
            time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(1.3)
        module_other_v3.write_result_text_try_if(code, eventname, result, "TIỆN ÍCH - Quản trị điểm - Phân quyền nhóm điểm",
                                              var_v3.update_success, "Cập nhật thành công", "_PhanQuyenNhomDiem_GanNhomDiem.png")
        time.sleep(1)


class managament_router:


    def managament_router1(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'],  var_v3.data['login']['conhom_quantri_mk'])

        administration.hover(var_v3.utility)
        administration.hover(var_v3.managament_router)
        var_v3.driver.find_element(By.XPATH, var_v3.managament_router1).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result,  "TIỆN ÍCH - Quản lý tuyến - Quản lý tuyến",
                                                 var_v3.check_managament_router1, "Chế độ xem nhiều tuyến",  "_QuanTriDiem.png")










