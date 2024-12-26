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




def write_from_date(fromdate_day_input):
    var_v3.driver.implicitly_wait(1)

    from_date = time.strftime("%d/%m/%Y, ", time.localtime())
    from_date = str(from_date)

    print(from_date)
    from_date_day = from_date[0:2]
    from_date_day = int(from_date_day)
    from_date_day = from_date_day - 1


    if from_date_day == 10:
        from_date_day = "09"
    if from_date_day == 9:
        from_date_day = "08"
    if from_date_day == 8:
        from_date_day = "07"
    if from_date_day == 7:
        from_date_day = "06"
    if from_date_day == 6:
        from_date_day = "05"
    if from_date_day == 5:
        from_date_day = "04"
    if from_date_day == 4:
        from_date_day = "03"
    if from_date_day == 3:
        from_date_day = "02"
    if from_date_day == 2:
        from_date_day = "01"
    if from_date_day == 1:
        from_date_day = "01"
    if from_date_day == 0:
        from_date_day = "01"

    fromdate_moth_year = from_date[3::]
    from_date = str(from_date_day) + fromdate_moth_year

    time.sleep(1)
    delete = var_v3.driver.find_element(By.XPATH, fromdate_day_input)
    delete.send_keys(Keys.CONTROL, "a")
    var_v3.driver.find_element(By.XPATH, fromdate_day_input).send_keys(from_date)


def write_from_time(write_from_time_input, time_from):
    var_v3.driver.implicitly_wait(1)
    time.sleep(1)
    delete = var_v3.driver.find_element(By.XPATH, write_from_time_input)
    delete.send_keys(Keys.CONTROL, "a")
    var_v3.driver.find_element(By.XPATH, write_from_time_input).send_keys(time_from)


def write_to_time(write_to_time_input, time_to):
    var_v3.driver.implicitly_wait(1)
    time.sleep(1)
    delete = var_v3.driver.find_element(By.XPATH, write_to_time_input)
    delete.send_keys(Keys.CONTROL, "a")
    var_v3.driver.find_element(By.XPATH, write_to_time_input).send_keys(time_to)








class minotor_video:


    def camera_monitoring_x(self):
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
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x8).click()
            time.sleep(0.5)
        except:
            pass


    def camera_monitoring(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        administration.hover(var_v3.video)
        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Giám sát camera",
                                                 var_v3.title_page2, "GIÁM SÁT CAMERA", "_GiamSatCamera.png")


    def camera_monitoring_select_screen(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")

        minotor_video.camera_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_screen).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_screen_manhinh1).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "VIDEO - Giám sát camera",
                                                 var_v3.check_camera_monitoring_select_screen, "", "_GiamSatCamera_ChonManHinh.png")


    def camera_monitoring_select_group(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")

        minotor_video.camera_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_group).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.select_group_all).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "VIDEO - Giám sát camera",
                                                 var_v3.check_camera_monitoring_select_group, "", "_GiamSatCamera_ChonNhom.png")


    def camera_monitoring_select_vehicle(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")

        minotor_video.camera_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle).click()
        time.sleep(1)

        if var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle1).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle1).click()
            time.sleep(0.5)
        if var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle2).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle2).click()
            time.sleep(0.5)
        if var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle3).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle3).click()
            time.sleep(0.5)
        if var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle4).is_selected() == False:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_select_vehicle4).click()
            time.sleep(0.5)

        var_v3.driver.find_element(By.XPATH, var_v3.icon_auto).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.on_full_screen).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "VIDEO - Giám sát camera",
                                                 var_v3.check_camera_monitoring_select_screen, "", "_GiamSatCamera_ChonPhuongTien.png")


    def camera_monitoring_filter(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")

        minotor_video.camera_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter).click()
        time.sleep(1.5)
        logging.info("-------------------------")
        logging.info("VIDEO - Giám sát camera")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            status_all = var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter_status_all).text
            location = var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter_location).text
            channel = var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter_channel).text
            status_channel = var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_filter_status).text
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, "{}, {}, {}, {}".format(status_all, location, channel, status_channel))

            if status_all and location and channel and status_channel != "":
                logging.info("True")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
            else:
                logging.info("False")
                var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSatCamera_Filter.png")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
                module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSatCamera_Filter.png")
        except:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + "_GiamSatCamera_Filter.png")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + "_GiamSatCamera_Filter.png")


    def camera_monitoring_pdf(self, code, eventname, result):
        module_other_v3.delete_excel()
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")

        minotor_video.camera_monitoring_x(self)

        var_v3.driver.find_element(By.XPATH, var_v3.export_excel1).click()
        time.sleep(7)
        module_other_v3.write_result_dowload_file(code, eventname, result, "VIDEO - Giám sát camera",
                                               "giamsatcamera.xlsx", "_GiamSatCamera_XuatExcel.png")


    def camera_monitoring_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")

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


        minotor_video.camera_monitoring_select_vehicle(self, "", "", "")
        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_add_new).click()
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_add_new_name).send_keys(var_v3.data['video']['addnew_screen'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Giám sát camera",
                                              var_v3.update_success, "Cập nhật thành công", "Video_ThemMoiManHinh.png")
        time.sleep(2)


    def camera_monitoring_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")


        try:
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_delete).click()
        except:
            minotor_video.camera_monitoring_add_new(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_delete).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.igree2).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Giám sát camera",
                                              var_v3.update_success, "Cập nhật thành công", "Video_XoaManHinh.png")


    def camera_monitoring_iconmap(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")

        minotor_video.camera_monitoring_select_screen(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_iconmap).click()
        time.sleep(2.5)

        module_other_v3.write_result_not_displayed_try(code, eventname, result, "VIDEO - Giám sát camera",
                                              var_v3.check_camera_monitoring_iconmap, "Video_IconMap.png")


    def camera_monitoring_iconclose(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.icon_auto)
        except:
            minotor_video.camera_monitoring(self, "", "", "")

        minotor_video.camera_monitoring_select_screen(self, "", "", "")

        var_v3.driver.find_element(By.XPATH, var_v3.camera_monitoring_x8).click()
        time.sleep(2.5)

        module_other_v3.write_result_not_displayed_try(code, eventname, result, "VIDEO - Giám sát camera",
                                              var_v3.check_camera_monitoring_iconclose, "Video_IconMap.png")









    def see_again_video(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        administration.hover(var_v3.video)
        var_v3.driver.find_element(By.XPATH, var_v3.see_again_video).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Xem lại video",
                                                 var_v3.title_page, "XEM LẠI VIDEO", "_XemLaiViDeo.png")


    def see_again_video_refresh(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.time_have_video)
        except:
            minotor_video.see_again_video_refresh(self, "", "", "")

        try:
            write_from_date(var_v3.see_again_video_day6)
        except:
            write_from_date(var_v3.see_again_video_day)


        var_v3.driver.implicitly_wait(3)
        n = 0
        while (n < 12):
            n += 1
            n = str(n)
            path_vehicle = "//*[@aria-label='Options list']/div/div[2]/div[" + n + "]/label"
            print(n)
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.overview_chart_select_vehicle).click()
                time.sleep(1)
                vehicle = var_v3.driver.find_element(By.XPATH, path_vehicle)
                name_vehicle = vehicle.text
                vehicle.click()
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.refresh).click()
                time.sleep(2.5)
                var_v3.driver.find_element(By.XPATH, var_v3.check_see_again_video_refresh)
                module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Xem lại video",
                                                         var_v3.check_see_again_video_refresh, name_vehicle,
                                                         "_BieuDoTongQuan_LamMoi.png")
                break
            except:
                var_v3.driver.find_element(By.XPATH, var_v3.see_again_video_refresh_iconx).click()
                time.sleep(1)
            n = int(n)









    def see_again_device(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.time_have_video)
            var_v3.driver.find_element(By.XPATH, var_v3.see_again_device).click()
        except:
            minotor_video.see_again_video(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.see_again_device).click()
        time.sleep(2)

        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Xem lại video(Xem lại từ thiết bị)",
                                                 var_v3.check_see_again_device1, "Phát tự động theo kênh", "_XemLaiTuThietBi.png")


    def see_again_device_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_see_again_device1)
        except:
            minotor_video.see_again_device(self, "", "", "")

        time.sleep(2)
        write_from_date(var_v3.see_again_video_day1)

        write_from_time(var_v3.see_again_device_from_time, "00:00")
        write_to_time(var_v3.see_again_device_to_time, "23:00")
        time.sleep(1)
        n = 0
        while (n < 10):
            n += 1
            n = str(n)
            path_vehicle = "//*[@aria-label='Options list']/div/div[2]/div[" + n + "]/label"
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.see_again_device_select_vehicle).click()
                time.sleep(1)
                vehicle = var_v3.driver.find_element(By.XPATH, path_vehicle)
                name_vehicle = vehicle.text
                print(name_vehicle)
                vehicle.click()
                time.sleep(1)
                var_v3.driver.find_element(By.XPATH, var_v3.search1).click()
                time.sleep(3.5)
                var_v3.driver.find_element(By.XPATH, var_v3.check_see_again_device)
                break
            except:
                pass
            n = int(n)

        module_other_v3.write_result_text_try_if_other(code, eventname, result, "VIDEO - Xem lại video(Xem lại từ thiết bị)",
                                                 var_v3.check_see_again_device, "", "_XemLaiTuThietBi_TimKiem.png")


    def see_again_device_iconrun(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_see_again_device)
        except:
            minotor_video.see_again_device(self, "", "", "")

        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.see_again_device_iconrun).click()
        time.sleep(2.5)

        module_other_v3.write_result_text_try_if_other(code, eventname, result, "VIDEO - Xem lại video(Xem lại từ thiết bị)",
                                                 var_v3.check_see_again_device_iconrun, "", "_XemLaiTuThietBi_Icon_Phat.png")


    def see_again_device_iconsever(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_see_again_device)
        except:
            minotor_video.see_again_device_search(self, "", "", "")

        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.see_again_device_iconsever).click()
        time.sleep(2.5)
        var_v3.driver.find_element(By.XPATH, var_v3.dowload_sever).click()
        time.sleep(2)
        try:
            var_v3.driver.implicitly_wait(0.2)
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_sever)
            module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Xem lại video(Xem lại từ thiết bị)",
                                                     var_v3.check_see_again_device_iconsever, "Video đang được tải về server. Quý khách vui lòng xem video đã tải trong tab BA-Cloud",
                                                     "_XemLaiTuThietBi_Icon_TaiSeVer.png")
        except:
            check_text = var_v3.driver.find_element(By.XPATH, var_v3.check_see_again_device_iconsever1).text
            logging.info(check_text)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 6, check_text)




    def dowload_cloud(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_see_again_device1)
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_cloud).click()
        except:
            minotor_video.see_again_video(self, "", "", "")
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_cloud).click()
        time.sleep(2)

        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Xem lại video(Xem lại từ thiết bị)",
                                                 var_v3.check_dowload_cloud, "Thời gian lưu trữ tối đa trên server là 30 ngày", "_TaiVeCloud.png")


    def dowload_cloud_search(self, code, eventname, result):
        var_v3.driver.implicitly_wait(3)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.check_dowload_cloud)
        except:
            minotor_video.dowload_cloud(self, "", "", "")

        time.sleep(2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.dowload_cloud_search_iconx1).click()
            time.sleep(0.5)
        except:
            pass

        write_from_date(var_v3.see_again_video_day2)
        write_from_time(var_v3.see_again_device_from_time1, "00:00")
        write_to_time(var_v3.see_again_device_to_time1, "23:00")
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search2).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if_other(code, eventname, result, "VIDEO - Xem lại video(Xem lại từ thiết bị)",
                                                 var_v3.check_dowload_cloud_search, "", "_TaiVeCloud_TimKiem.png")





class channel_categories_management:


    def channel_categories_x(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.channel_categories_iconx1).click()
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.channel_categories_iconx2).click()
        except:
            pass


    def channel_categories(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        minitor_v3.goto(self, "Mã XN", "1010_87", " Công ty: 1010_Công ty không có nhóm đội - 1010_87 - ungroup ")

        administration.hover(var_v3.video)
        administration.hover(var_v3.channel_categories_management)
        var_v3.driver.find_element(By.XPATH, var_v3.channel_categories).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera -  Danh sách tên kênh",
                                                 var_v3.title_page, "DANH SÁCH TÊN KÊNH", "_DanhSachTenKenh.png")


    def channel_categories_search(self, code, eventname, result, data, status, desire):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_edit)
        except:
            channel_categories_management.channel_categories(self, "", "", "")

        channel_categories_management.channel_categories_x(self)


        var_v3.driver.find_element(By.XPATH, var_v3.channel_categories_input).send_keys(data)
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.select_channel_categories).click()

        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='"+status+"']").click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search3).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera -  Danh sách tên kênh",
                                              var_v3.check_config_warm_user_search, desire, "_DanhSachTenKenh_Timkiem.png")


    def channel_categories_add_new(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_edit)
        except:
            channel_categories_management.channel_categories(self, "", "", "")

        try:
            channel_categories_management.channel_categories_delete(self, "", "", "")
        except:
            var_v3.driver.refresh()
            time.sleep(5)


        var_v3.driver.find_element(By.XPATH, var_v3.add_new).click()
        time.sleep(2)
        var_v3.driver.find_element(By.XPATH, var_v3.create_channel_code).send_keys(var_v3.data['video']['create_channel_code'])
        time.sleep(0.5)
        var_v3.driver.find_element(By.XPATH, var_v3.create_channel_name).send_keys(var_v3.data['video']['create_channel_name'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.channel_categories_save).click()
        time.sleep(1.5)

        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera -  Danh sách tên kênh",
                                                 var_v3.add_new_success, "Thêm mới thành công", "_DanhSachTenKenh_ThemMoi.png")

        time.sleep(1)


    def channel_categories_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_edit)
        except:
            channel_categories_management.channel_categories(self, "", "", "")

        channel_categories_management.channel_categories_search(self, "", "", "", "Kênh 4", "Kích hoạt", "")


        name = var_v3.driver.find_element(By.XPATH, var_v3.check_config_warm_user_search).text
        if name == "ma04":

            var_v3.driver.find_element(By.XPATH, var_v3.channel_categories_name).clear()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.channel_categories_name).send_keys(var_v3.data['video']['create_channel_name_edit'])
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.save1).click()
            time.sleep(1.5)
            module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera -  Danh sách tên kênh",
                                                     var_v3.update_success, "Cập nhật thành công", "_DanhSachTenKenh_Sua.png")

        time.sleep(1)


    def channel_categories_delete(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.day_edit)
        except:
            channel_categories_management.channel_categories(self, "", "", "")

        channel_categories_management.channel_categories_search(self, "", "", "", "Kênh 4", "Kích hoạt", "")


        name = var_v3.driver.find_element(By.XPATH, var_v3.check_config_warm_user_search).text
        if name == "ma04":
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.channel_categories_delete).click()
            except:
                var_v3.driver.find_element(By.XPATH, var_v3.channel_categories_delete1).click()

            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
            time.sleep(1)
            module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera -  Danh sách tên kênh",
                                                     var_v3.delete_success, "Xóa thành công", "_DanhSachTenKenh_Xoa.png")

        time.sleep(1)









    def config_channel_camera_iconx(self):
        var_v3.driver.implicitly_wait(0.2)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.config_channel_camera_search_iconx1).click()
            time.sleep(0.5)
        except:
            pass
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.config_channel_camera_search_iconx2).click()
            time.sleep(0.5)
        except:
            pass


    def config_channel_camera(self, code, eventname, result):
        var_v3.driver.implicitly_wait(5)
        login_v3.login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        administration.hover(var_v3.video)
        administration.hover(var_v3.channel_categories_management)
        var_v3.driver.find_element(By.XPATH, var_v3.config_channel_camera).click()
        time.sleep(2.5)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera - Cấu hình kênh camera",
                                                 var_v3.title_page1, "CẤU HÌNH KÊNH CAMERA", "_CauHinhKenhCamera.png")


    def config_channel_camera_search(self, code, eventname, result, vehicle):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_channel)
        except:
            channel_categories_management.config_channel_camera(self, "", "", "")


        channel_categories_management.config_channel_camera_iconx(self)



        var_v3.driver.find_element(By.XPATH, var_v3.config_channel_camera_search_select).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, "//*[@aria-label='Options list']//*[text()='"+vehicle+"']").click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.search3).click()
        time.sleep(2)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera - Cấu hình kênh camera",
                                              var_v3.check_config_channel_camera_search, vehicle, "_CauHinhKenhCamera_Timkiem.png")


    def config_channel_camera_edit(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_channel)
        except:
            channel_categories_management.config_channel_camera(self, "", "", "")



        channel_categories_management.config_channel_camera_search(self, "", "", "", var_v3.data['video']['config_camera_search'])


        name = var_v3.driver.find_element(By.XPATH, var_v3.check_config_channel_camera_search).text
        if name == var_v3.data['video']['config_camera_search']:

            var_v3.driver.find_element(By.XPATH, var_v3.select_module_camera).click()
            time.sleep(1)
            var_v3.driver.find_element(By.XPATH, var_v3.select_module_camera_kenh1).click()
            time.sleep(0.5)
            if var_v3.driver.find_element(By.XPATH, var_v3.see_image_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, var_v3.see_image_label).click()
                time.sleep(1)

            if var_v3.driver.find_element(By.XPATH, var_v3.see_video_input).is_selected() == False:
                var_v3.driver.find_element(By.XPATH, var_v3.see_video_label).click()
                time.sleep(1)

            var_v3.driver.find_element(By.XPATH, var_v3.corner).clear()
            time.sleep(0.5)
            var_v3.driver.find_element(By.XPATH, var_v3.corner).send_keys("90")
            time.sleep(1)
            try:
                var_v3.driver.find_element(By.XPATH, var_v3.cancel4).click()
            except:
                var_v3.driver.find_element(By.XPATH, var_v3.cancel4b).click()
            time.sleep(1.5)
            module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera - Cấu hình kênh camera",
                                                     var_v3.check_config_channel_camera_edit, "Bạn chưa lưu thay đổi này, bạn có chắc chắn quay về ban đầu?",
                                                     "_CauHinhKenhCamera_Sua.png")
            var_v3.driver.refresh()
            time.sleep(6)


    def config_channel_camera_iconcopy(self, code, eventname, result):
        var_v3.driver.implicitly_wait(4)
        try:
            var_v3.driver.find_element(By.XPATH, var_v3.list_channel)
        except:
            channel_categories_management.config_channel_camera(self, "", "", "")


        var_v3.driver.find_element(By.XPATH, var_v3.config_channel_camera_iconcopy).click()
        time.sleep(4)
        module_other_v3.write_result_text_try_if(code, eventname, result, "VIDEO - Quản lý tên kênh camera - Cấu hình kênh camera",
                                              var_v3.title_right_mouse, "SAO CHÉP THÔNG TIN KÊNH", "_CauHinhKenhCamera_IconSaoChep.png")

        try:
            var_v3.driver.find_element(By.XPATH, var_v3.close2).click()
            time.sleep(1)
        except:
            pass






