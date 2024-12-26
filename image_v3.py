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
import video_v3





class image:

    def online_image_monitoring_x(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x1).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x2).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x3).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x4).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x5).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x6).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x7).click()
            time.sleep(0.5)
        except:
            pass


    def online_image_monitoring(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'],  var_v3.data['login']['conhom_quantri_mk'])

        administration.hover(var_v3.image)
        var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result,  "HÌNH ẢNH - Giám sát hình ảnh trực tuyến",
                                                 var_v3.title_page3, "GIÁM SÁT HÌNH ẢNH TRỰC TUYẾN",  "_GiamSatHinhAnhTrucTuyen.png")


    def online_image_monitoring_select_screen(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.auto_update)
        except:
            image.online_image_monitoring(self, "", "", "")

        image.online_image_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_screen).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_screen_manhinh1).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "HÌNH ẢNH - Giám sát hình ảnh trực tuyến",
                                                 var_v3.check_online_image_monitoring_select_screen, "", "_GiamSatHinhAnhTrucTuyen_ChonManHinh.png")


    def online_image_monitoring_select_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.auto_update)
        except:
            image.online_image_monitoring(self, "", "", "")

        image.online_image_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_group).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.select_group_all).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "HÌNH ẢNH - Giám sát hình ảnh trực tuyến",
                                                 var_v3.check_camera_monitoring_select_group, "Chọn nhóm phương tiện",
                                                       "_GiamSatHinhAnhTrucTuyen_ChonNhom.png")


    def online_image_monitoring_select_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.auto_update)
        except:
            image.online_image_monitoring(self, "", "", "")

        image.online_image_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.auto_update_input).click()

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[@class='ng-dropdown-panel-items scroll-host']/div[2]//*[text()='"+var_v3.data['image']['search']+"']").click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_change_language).click()
        time.sleep(1)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_online_image_monitoring_select_vehicle)
        except:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_run_image).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "HÌNH ẢNH - Giám sát hình ảnh trực tuyến",
                                                 var_v3.check_online_image_monitoring_select_vehicle1, "", "_GiamSatHinhAnhTrucTuyen_ChonPhuongTien.png")


    def online_image_monitoring_filter(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.auto_update)
        except:
            image.online_image_monitoring(self, "", "", "")

        image.online_image_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter).click()
        time.sleep(1.5)
        logging.info("-------------------------")
        logging.info("HÌNH ẢNH - Giám sát hình ảnh trực tuyến")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            location = var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter_location).text
            status_all = var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter_status_all).text
            channel = var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter_channel).text
            status_channel = var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter_status).text
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "{}, {}, {}, {}".format(status_all, location, channel, status_channel))

            if status_all and location and channel and status_channel != "":
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSatHinhAnhTrucTuyen_Filter.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSatHinhAnhTrucTuyen_Filter.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSatHinhAnhTrucTuyen_Filter.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSatHinhAnhTrucTuyen_Filter.png")


    def online_image_monitoring_excel(self, code, eventname, result):
        module_other_v3.delete_excel()
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.auto_update)
        except:
            image.online_image_monitoring(self, "", "", "")

        image.online_image_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.export_excel1).click()
        time.sleep(7)
        module_other_v3.write_result_dowload_file(code, eventname, result, "HÌNH ẢNH - Giám sát hình ảnh trực tuyến",
                                               "giamsathinhanhtructuyen.xlsx", "_GiamSatHinhAnhTrucTuyen_XuatExcel.png")


    def online_image_monitoring_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.auto_update)
        except:
            image.online_image_monitoring(self, "", "", "")


        var_v3.driver.refresh()
        time.sleep(5)
        try:
            var_v3.driver.implicitly_wait(1)
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_screen).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_screen_manhinh3).click()
            time.sleep(2)
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_delete).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree2).click()
            time.sleep(2)
        except:
            var_v3.driver.refresh()
            time.sleep(5)


        image.online_image_monitoring_select_vehicle(self, "", "", "")
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring_add_new).click()
        except:
            var_v3.driver.refresh()
            time.sleep(5)
            var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring_add_new).click()
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_add_new_name).send_keys(var_v3.data['video']['addnew_screen'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "HÌNH ẢNH - Giám sát hình ảnh trực tuyến",
                                              var_v3.update_success, "Cập nhật thành công", "_GiamSatHinhAnhTrucTuyen_ThemMoiManHinh.png")
        time.sleep(2)


    def online_image_monitoring_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.auto_update)
        except:
            image.online_image_monitoring(self, "", "", "")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring_delete).click()
        except:
            image.online_image_monitoring_add_new(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring_delete).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.igree2).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "HÌNH ẢNH - Giám sát hình ảnh trực tuyến",
                                              var_v3.update_success, "Cập nhật thành công", "_GiamSatHinhAnhTrucTuyen_XoaManHinh.png")


    def online_image_monitoring_see_image(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.auto_update)
        except:
            image.online_image_monitoring(self, "", "", "")


        var_v3.driver.refresh()
        time.sleep(6)
        var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring_see_image1).click()
        time.sleep(2)
        logging.info("-------------------------")
        logging.info("HÌNH ẢNH - Giám sát hình ảnh trực tuyến")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            vehicle = var_v3.driver.find_element(By.XPATH, var_v3.see_image_vehicle).text
            channel = var_v3.driver.find_element(By.XPATH, var_v3.see_image_channel).text
            adress = var_v3.driver.find_element(By.XPATH, var_v3.see_image_adress).text
            time1 = var_v3.driver.find_element(By.XPATH, var_v3.see_image_time1).text
            driver1 = var_v3.driver.find_element(By.XPATH, var_v3.see_image_driver1).text
            speed = var_v3.driver.find_element(By.XPATH, var_v3.see_image_speed).text

            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "{}, {}, {}, {}, {}, {}"
                                      .format(vehicle, channel, adress, time1, driver1, speed))

            if vehicle and channel and adress and time1 and driver1 and speed != "":
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSatHinhAnhTrucTuyen_Filter.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSatHinhAnhTrucTuyen_Filter.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSatHinhAnhTrucTuyen_Filter.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSatHinhAnhTrucTuyen_Filter.png")


    def online_image_monitoring_dowload_image(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_image_vehicle)
        except:
            image.online_image_monitoring_see_image(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring_dowload_image).click()
        time.sleep(5)
        module_other_v3.write_result_dowload_file(code, eventname, result, "HÌNH ẢNH - Giám sát hình ảnh trực tuyến",
                                               "giamsathinhanhtructuyen.png", "_GiamSatHinhAnhTrucTuyen.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.online_image_monitoring_see_image_icon_x).click()
            time.sleep(1)
        except:
            pass




class see_image_vehicle1:


    def image_library(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'],  var_v3.data['login']['conhom_quantri_mk'])

        administration.hover(var_v3.image)
        var_v3.driver.find_element(By.XPATH, var_v3.see_image_vehicle1).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result,  "HÌNH ẢNH - Xem ảnh phương tiện",
                                                 var_v3.title_page4, "XEM ẢNH PHƯƠNG TIỆN",  "_XemAnhPhuongTien_ThuVienAnh.png")


    def image_library_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.photo_per_page)
        except:
            see_image_vehicle1.image_library(self, "", "", "")

        video_v3.write_from_date(var_v3.image_library_day)


        var_v3.driver.implicitly_wait(3)
        n = 0
        while (n < 12):
            n += 1
            n = str(n)
            path_vehicle = "//*[@aria-label='Options list']/div/div[2]/div[" + n + "]/label"
            print(n)
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.image_library_vehicle).click()
                time.sleep(1)
                vehicle = var_v3.driver.find_element(By.XPATH, path_vehicle)
                name_vehicle = vehicle.text
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 2, name_vehicle)
                vehicle.click()
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.search1).click()
                time.sleep(2.5)
                var_v3.driver.find_element(By.XPATH, var_v3.chek_image_library_search)
                module_other_v3.write_result_text_try_if_other(code, eventname, result, "HÌNH ẢNH - Xem ảnh phương tiện",
                                                         var_v3.chek_image_library_search, "", "_XemAnhPhuongTien_TimKiem.png")
                break
            except:
                pass
            n = int(n)


    def image_library_download_image(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.chek_image_library_search)
        except:
            see_image_vehicle1.image_library_search(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.image_library_download_image).click()
        time.sleep(4)
        module_other_v3.write_result_dowload_file(code, eventname, result, "HÌNH ẢNH - Xem ảnh phương tiện(thư viện ảnh)",
                                               "xemanhphuongtien_thuvienanh.png", "_XemAnhPhuongTien_ThuVienAnh.png")


    def get_info_image_library(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 152, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 153, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 154, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 155, 2, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 152, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 153, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 154, 3, "")
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 155, 3, "")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.chek_image_library_search)
        except:
            see_image_vehicle1.image_library_search(self, "", "", "")


        time_image_out = var_v3.driver.find_element(By.XPATH, var_v3.time_image_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 152, 2, time_image_out)

        speed_image_out = var_v3.driver.find_element(By.XPATH, var_v3.speed_image_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 153, 2, speed_image_out)

        channel_image_out = var_v3.driver.find_element(By.XPATH, var_v3.channel_image_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 154, 2, channel_image_out)

        address_image_out = var_v3.driver.find_element(By.XPATH, var_v3.address_image_out).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 155, 2, address_image_out)



        var_v3.driver.find_element(By.XPATH, var_v3.get_info_image_library).click()
        time.sleep(2)
        vehicle_image_in = var_v3.driver.find_element(By.XPATH, var_v3.vehicle_image_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 3, vehicle_image_in)

        time_image_in = var_v3.driver.find_element(By.XPATH, var_v3.time_image_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 152, 3, time_image_in)

        speed_image_in = var_v3.driver.find_element(By.XPATH, var_v3.speed_image_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 153, 3, speed_image_in)

        channel_image_in = var_v3.driver.find_element(By.XPATH, var_v3.channel_image_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 154, 3, channel_image_in)

        address_image_in = var_v3.driver.find_element(By.XPATH, var_v3.address_image_in).text
        var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 155, 3, address_image_in)

        logging.info("-------------------------")
        logging.info("HÌNH ẢNH - Xem ảnh phương tiện(thư viện ảnh)")
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


    def check_info_image_library(self, code, eventname, result, row , column_out, column_in, name_image):
        logging.info("-------------------------")
        logging.info("HÌNH ẢNH - Xem ảnh phương tiện(thư viện ảnh)")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)

        data_out = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, column_out))
        data_in = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', row, column_in))
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Màn hình: {}\nKhi click vào ảnh: {}".format(data_out, data_in))

        if data_in == data_out:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)






    def view_images_by_channel(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.view_images_by_channel).click()
        except:
            see_image_vehicle1.image_library(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.view_images_by_channel).click()

        time.sleep(2)
        module_other_v3.write_result_displayed_try(code, eventname, result,  "HÌNH ẢNH - Xem ảnh phương tiện(Xem ảnh theo kênh)",
                                                 var_v3.view_images_by_channel_day,  "_XemAnhPhuongTien_XemAnhTheoKenh.png")

        var_v3.driver.refresh()
        time.sleep(6)


    def view_images_by_channel_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.view_images_by_channel_day)
        except:
            see_image_vehicle1.view_images_by_channel(self, "", "", "")

        video_v3.write_from_date(var_v3.view_images_by_channel_day)

        var_v3.driver.implicitly_wait(3)
        n = 0
        while (n < 12):
            n += 1
            n = str(n)
            path_vehicle = "//*[@aria-label='Options list']/div/div[2]/div[" + n + "]/label"
            print(n)
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.image_library_vehicle).click()
                time.sleep(1)
                vehicle = var_v3.driver.find_element(By.XPATH, path_vehicle)
                name_vehicle = vehicle.text
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 2, name_vehicle)
                vehicle.click()
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.search1).click()
                time.sleep(2.5)
                var_v3.driver.find_element(By.XPATH, var_v3.check_view_images_by_channel_search)
                module_other_v3.write_result_text_try_if_other(code, eventname, result, "HÌNH ẢNH - Xem ảnh phương tiện(Xem ảnh theo kênh)",
                                                         var_v3.check_view_images_by_channel_search, "", "_XemAnhPTheoKenh_TimKiem.png")
                break
            except:
                pass
            n = int(n)







    def see_image_detail(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.see_image_detail).click()
        except:
            see_image_vehicle1.image_library(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.see_image_detail).click()

        time.sleep(2)
        module_other_v3.write_result_displayed_try(code, eventname, result,  "HÌNH ẢNH - Xem ảnh phương tiện(Xem ảnh chi tiết)",
                                                 var_v3.view_images_by_channel_day,  "_XemAnhPhuongTien_XemAnhChiTiet.png")

        var_v3.driver.refresh()
        time.sleep(6)


    def see_image_detail_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.view_images_by_channel_day)
        except:
            see_image_vehicle1.view_images_by_channel(self, "", "", "")

        video_v3.write_from_date(var_v3.view_images_by_channel_day)

        var_v3.driver.implicitly_wait(3)
        n = 0
        while (n < 12):
            n += 1
            n = str(n)
            path_vehicle = "//*[@aria-label='Options list']/div/div[2]/div[" + n + "]/label"
            print(n)
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.image_library_vehicle).click()
                time.sleep(1)
                vehicle = var_v3.driver.find_element(By.XPATH, path_vehicle)
                name_vehicle = vehicle.text
                var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 151, 2, name_vehicle)
                vehicle.click()
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.search1).click()
                time.sleep(2.5)
                var_v3.driver.find_element(By.XPATH, var_v3.check_see_image_detail_search)
                module_other_v3.write_result_text_try_if_other(code, eventname, result, "HÌNH ẢNH - Xem ảnh phương tiện(Xem ảnh chi tiết)",
                                                         var_v3.check_see_image_detail_search, "", "_XemAnhChiTiet_TimKiem.png")
                break
            except:
                pass
            n = int(n)


    def see_image_detail_check_info(self, code, eventname, result, path_image, path_map, name_image):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_see_image_detail_search)
        except:
            see_image_vehicle1.see_image_detail(self, "", "", "")

        detail_image = var_v3.driver.find_element(By.XPATH, path_image).text
        detail_map = var_v3.driver.find_element(By.XPATH, path_map).text
        logging.info("-------------------------")
        logging.info("HÌNH ẢNH - Xem ảnh phương tiện(Xem ảnh chi tiết)")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "Thông tin ảnh: {}\nThông tin map: {}".format(detail_image, detail_map))
        if detail_image == detail_map:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)
