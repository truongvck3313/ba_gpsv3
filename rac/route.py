import logging
import var_v3
import time
from retry import retry
from selenium.webdriver.common.by import By
import module_other_v3
import login_v3
import os
import shutil
import minitor_v3



def get_info_km(field):
    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 111, 2, "")
    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 112, 2, "")
    var_v3.driver.implicitly_wait(0.05)
    n = 0
    while (n < 10):
        n += 1
        n = str(n)
        path_name = "//*[@class='summary-info ng-star-inserted']/div[" + n + "]/div[1]"
        path_detail = "//*[@class='summary-info ng-star-inserted']/div[" + n + "]/div[2]"
        print(n)
        try:
            name = var_v3.driver.find_element(By.XPATH, path_name).text
            detail = var_v3.driver.find_element(By.XPATH, path_detail).text
            print(name)
            print(detail)
            if name == field:
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 111, 2, name)
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 112, 2, detail)
                print("đã ghi vào excel: " + name)
                print("đã ghi vào excel: " + detail)
                break
        except:
            pass
        n = int(n)
    # get_info_location1("Địa chỉ:")


def get_info_location1(field):
    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 111, 2, "")
    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 112, 2, "")
    var_v3.driver.implicitly_wait(0.05)
    n = 0
    while (n < 20):
        n += 1
        n = str(n)
        path_name = "//*[@class='panel panel-primary popup-panel']/div/table/tr[" + n + "]/td[1]/label"
        path_detail = "//*[@class='panel panel-primary popup-panel']/div/table/tr[" + n + "]/td[2]/label"
        print(n)
        try:
            name = var_v3.driver.find_element(By.XPATH, path_name).text
            detail = var_v3.driver.find_element(By.XPATH, path_detail).text
            print(name)
            print(detail)
            if name == field:
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 111, 2, name)
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 112, 2, detail)
                print("đã ghi vào excel: " + name)
                print("đã ghi vào excel: " + detail)
                break
        except:
            pass
        n = int(n)
    # get_info_location1("Địa chỉ:")


def get_info_stop(field):
    var_v3.driver.implicitly_wait(0.05)
    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 111, 2, "")
    var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 112, 2, "")
    n = 0
    while (n < 20):
        n += 1
        n = str(n)
        path_name = "//*[@class='panel-body']/table/tr[" + n + "]/td[1]/label"
        path_detail = "//*[@class='panel-body']/table/tr[" + n + "]/td[2]/label"
        print(n)
        try:
            name = var_v3.driver.find_element(By.XPATH, path_name).text
            detail = var_v3.driver.find_element(By.XPATH, path_detail).text
            print(name)
            print(detail)
            if name == field:
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 111, 2, name)
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 112, 2, detail)
                print("đã ghi vào excel: " + name)
                print("đã ghi vào excel: " + detail)
                break
        except:
            pass
        n = int(n)
    # get_info_location1("Địa chỉ:")




class left_popup:


    def open_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])
        var_v3.driver.find_element(By.XPATH, var_v3.route).click()
        time.sleep(3.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Lộ trình",
                                              var_v3.check_open_route, "Lộ trình", "_LoTrinh.png")



    def dowload_data(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_data)
        except:
            left_popup.open_route(self, "", "", "")


        n = 0
        while (n < 15):
            n += 1
            n = str(n)
            var_v3.driver.find_element(By.XPATH, var_v3.route_select_vehicle).click()
            time.sleep(1)

            pathname_detail = "//*[@class='ng-dropdown-panel-items scroll-host']/div[2]/div[" + n + "]"
            print(n)
            try:
                vehicle = var_v3.driver.find_element(By.XPATH, pathname_detail)
                name_vehicle = vehicle.text
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
                print(name_vehicle)
                vehicle.click()
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.dowload_data).click()
                time.sleep(5)
                var_v3.driver.find_element(By.XPATH, var_v3.location_start)
                break
            except:
                pass
            n = int(n)

        vehicle_excel = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 2, 2))
        check_dowload_data = "//*[@id='route-map']//*[text()='"+vehicle_excel+"']"
        module_other_v3.write_result_text_try_if(code, eventname, result, "Lộ trình - Tìm kiếm",
                                              check_dowload_data, vehicle_excel, "_LoTrinh_TaiDuLieu.png")



    def icon_run_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_route)
        except:
            left_popup.dowload_data(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.icon_run_route).click()
        time.sleep(3)
        module_other_v3.write_result_displayed_try(code, eventname, result, "Lộ trình - Danh sách lộ trình",
                                              var_v3.icon_stop_route, "_LoTrinh_IconRunLoTrinh.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_stop_route).click()
            time.sleep(1)
        except:
            pass



    def route_status(self, code, eventname, result, select_status, name_image):
        var_v3.driver.implicitly_wait(2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_route)
        except:
            left_popup.dowload_data(self, "", "", "")
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.route_status).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, select_status).click()
        time.sleep(1.5)
        logging.info("-------------------------")
        logging.info("Lộ trình - Danh sách lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)

        try:
            check_text = var_v3.driver.find_element(By.XPATH, var_v3.route_status1).text
            logging.info(check_text)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            try:
                check_text = var_v3.driver.find_element(By.XPATH, var_v3.no_data).text
                logging.info(check_text)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            except:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)

        if name_image == "_LoTrinh_BatMay.png":
            var_v3.driver.find_element(By.XPATH, var_v3.route_delele).click()
            time.sleep(1)




    def config_display_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_route)
        except:
            left_popup.dowload_data(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.config_display_route).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Lộ trình - Cấu hình hiển thị lộ trình",
                                              var_v3.check_title_popup, "CẤU HÌNH HIỂN THỊ LỘ TRÌNH", "_LoTrinh_CauHinhHienThiLoTrinh.png")



    def config_display_route_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
        except:
            left_popup.config_display_route(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Lộ trình - Cấu hình hiển thị lộ trình",
                                              var_v3.close, "_LoTrinh_CauHinhHienThiLoTrinh_Dong.png")



    @retry(tries=3, delay=2, backoff=1, jitter=5)
    def route_checkbox(self, code, eventname, result, check_box_input, check_box_label, button_other, path_check, button_type, type_desire, desire, name_image):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_route)
        except:
            left_popup.dowload_data(self, "", "", "")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.route_icon_stop)
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_data).click()
            time.sleep(4)


        var_v3.driver.find_element(By.XPATH, var_v3.config_display_route).click()
        time.sleep(2)

        print(var_v3.driver.find_element(By.XPATH, var_v3.route_board_input).is_selected())
        if var_v3.driver.find_element(By.XPATH, var_v3.route_board_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.route_board_label).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.route_board_label).click()
            time.sleep(0.5)



        print(var_v3.driver.find_element(By.XPATH, var_v3.sum_input).is_selected())
        if var_v3.driver.find_element(By.XPATH, var_v3.sum_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.sum_label).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.sum_label).click()
            time.sleep(0.5)



        print(var_v3.driver.find_element(By.XPATH, var_v3.move_location_input).is_selected())
        if var_v3.driver.find_element(By.XPATH, var_v3.move_location_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.move_location_label).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.move_location_label).click()
            time.sleep(0.5)


        print(var_v3.driver.find_element(By.XPATH, var_v3.stop_location_input).is_selected())
        if var_v3.driver.find_element(By.XPATH, var_v3.stop_location_input).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.stop_location_label).click()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.stop_location_label).click()
            time.sleep(0.5)


        try:
            if var_v3.driver.find_element(By.XPATH, check_box_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, check_box_label).click()
                time.sleep(1)
        except:
            pass
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(3)


        if button_type == "1":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.icon_arrow)
                var_v3.driver.find_element(By.XPATH, var_v3.dowload_data).click()
                time.sleep(3.5)
            except:
                n = 0
                while (n < 15):
                    n += 1
                    n = str(n)

                    var_v3.driver.find_element(By.XPATH, var_v3.route_select_vehicle).click()
                    time.sleep(1)

                    pathname_detail = "//*[@class='ng-dropdown-panel-items scroll-host']/div[2]/div[" + n + "]"
                    print(n)
                    try:
                        vehicle = var_v3.driver.find_element(By.XPATH, pathname_detail)
                        name_vehicle = vehicle.text
                        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
                        print(name_vehicle)
                        vehicle.click()
                        time.sleep(1)
                        var_v3.driver.find_element(By.XPATH, var_v3.dowload_data).click()
                        time.sleep(3.5)
                        var_v3.driver.find_element(By.XPATH, var_v3.icon_arrow)
                        break
                    except:
                        pass
                    n = int(n)


        if button_type == "2":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.icon_stop)
                var_v3.driver.find_element(By.XPATH, var_v3.dowload_data).click()
                time.sleep(3.5)
            except:
                n = 0
                while (n < 15):
                    n += 1
                    n = str(n)

                    var_v3.driver.find_element(By.XPATH, var_v3.route_select_vehicle).click()
                    time.sleep(1)

                    pathname_detail = "//*[@class='ng-dropdown-panel-items scroll-host']/div[2]/div[" + n + "]"
                    print(n)
                    try:
                        vehicle = var_v3.driver.find_element(By.XPATH, pathname_detail)
                        name_vehicle = vehicle.text
                        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
                        print(name_vehicle)
                        vehicle.click()
                        time.sleep(1)
                        var_v3.driver.find_element(By.XPATH, var_v3.dowload_data).click()
                        time.sleep(3.5)
                        var_v3.driver.find_element(By.XPATH, var_v3.icon_stop)
                        break
                    except:
                        pass
                    n = int(n)

        try:
            button = var_v3.driver.find_element(By.XPATH, button_other)
            var_v3.driver.execute_script("arguments[0].click();", button)
            time.sleep(2)
        except:
            pass

        if type_desire == "1":
            module_other_v3.write_result_text_try_if(code, eventname, result, "Lộ trình - Cấu hình hiển thị lộ trình",
                                                  path_check, desire, name_image)


        if type_desire == "2":
            # module_other_v3.write_result_displayed_try(code, eventname, result, "Lộ trình - Cấu hình hiển thị lộ trình",
            #                                       path_check, name_image)
            get_info_km(desire)
            name = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 111, 2))
            detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 112, 2))

            logging.info("-------------------------")
            logging.info("Lộ trình - Cấu hình hiển thị lộ trình")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Trường {} {}".format(name, detail))
            if (name == desire) and (detail != "None"):
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)


        if type_desire == "3":
            get_info_location1(desire)
            name = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 111, 2))
            detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 112, 2))

            logging.info("-------------------------")
            logging.info("Lộ trình - Cấu hình hiển thị lộ trình")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Trường {} {}".format(name, detail))
            if (name == desire) and (detail != "None"):
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)


        if type_desire == "4":
            get_info_stop(desire)
            name = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 111, 2))
            detail = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 112, 2))

            logging.info("-------------------------")
            logging.info("Lộ trình - Cấu hình hiển thị lộ trình")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Trường {} {}".format(name, detail))
            if (name == desire) and (detail != "None"):
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)


        try:
            var_v3.driver.implicitly_wait(0.2)
            var_v3.driver.find_element(By.XPATH, var_v3.route_icon_x1).click()
            time.sleep(1)
        except:
            pass





    def config_route_aggregation(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_route)
        except:
            left_popup.dowload_data(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.config_route_aggregation).click()
        time.sleep(1.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Lộ trình - Cấu hình gộp dừng đỗ",
                                                var_v3.title_right_mouse, "CẤU HÌNH GỘP DỪNG ĐỖ", "_LoTrinh_CauHinhGopDungDo.png")



    def config_route_aggregation_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
        except:
            left_popup.config_route_aggregation(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Lộ trình - Cấu hình gộp dừng đỗ",
                                              var_v3.close, "_LoTrinh_CauHinhGopDungDo_Dong.png")



    def config_route_aggregation_checkbox(self, code, eventname, result, checkbox, name_image):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.title_right_mouse)
        except:
            left_popup.config_route_aggregation(self, "", "", "")


        if var_v3.driver.find_element(By.XPATH, var_v3.config_route_aggregation_input).is_selected() == checkbox:
            var_v3.driver.find_element(By.XPATH, var_v3.config_route_aggregation_label).click()
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.time_stop_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.time_stop_input).send_keys(var_v3.data['route']['time_stop_input'])
        time.sleep(1)

        var_v3.driver.find_element(By.XPATH, var_v3.time_lost_signal_input).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.time_lost_signal_input).send_keys(var_v3.data['route']['time_lost_signal_input'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Lộ trình - Cấu hình gộp dừng đỗ",
                                              var_v3.update_success, "Cập nhật thành công", name_image)
        time.sleep(3)



    def print_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_route)
        except:
            left_popup.dowload_data(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.print_route).click()
        time.sleep(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])

        module_other_v3.write_result_text_try_if_other(code, eventname, result, "Lộ trình - In lộ trình",
                                                var_v3.check_print_route, "None", "_LoTrinh_InLoTrinh.png")

        time.sleep(1)
        module_other_v3.close_tab()
        time.sleep(1)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        time.sleep(1)



    def route_export_excel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        module_other_v3.delete_excel()

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_list_route)
        except:
            left_popup.dowload_data(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.route_export_excel).click()
        time.sleep(7)

        logging.info("Lộ trình - Xuất excel")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var_v3.excelpath + "\\" + f for f in os.listdir(var_v3.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var_v3.excelpath, r"lotrinh_xuat_excel.xlsx"))
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_LoTrinh_XuatExcel.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_LoTrinh_XuatExcel.png")



    def create_location(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        left_popup.open_route(self, "", "", "")

        minitor_v3.map.map_right_mouse(self, "Tạo điểm", "600", "800", var_v3.title_right_mouse)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Lộ trình - Map - Tạo điểm",
                                              var_v3.title_right_mouse, "TẠO ĐIỂM", "_LoTrinh_TaoDiem.png")



    def create_location_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()
        except:
            left_popup.create_location(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Lộ trình - Map - Tạo điểm",
                                              var_v3.close, "_LoTrinh_TaoDiem_Dong.png")



    def see_route_route(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        left_popup.open_route(self, "", "", "")

        minitor_v3.map.map_right_mouse(self, "Xem lộ trình tuyến", "600", "800", var_v3.title_right_mouse)
        time.sleep(1)
        module_other_v3.write_result_text_try_if(code, eventname, result, "Lộ trình - Map - Xem lộ trình tuyến",
                                              var_v3.title_right_mouse, "XEM LỘ TRÌNH TUYẾN", "_LoTrinh_XemLoTrinhTuyen.png")



    def see_route_route_close(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
        except:
            left_popup.see_route_route(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()

        module_other_v3.write_result_close_popup(code, eventname, result, "Lộ trình - Map - Xem lộ trình tuyến",
                                              var_v3.close2, "_LoTrinh_XemLoTrinhTuyen_Dong.png")














