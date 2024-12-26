import logging
import var_v3
import time
from selenium.webdriver.common.by import By
import module_other_v3
from retry import retry
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC















class login:

    # def login_v2(self, user, password):
    #     var_v3.driver.implicitly_wait(5)
    #     var_v3.driver.maximize_window()
    #     var_v3.driver.delete_all_cookies()
    #     try:
    #         login.logout_v2(self)
    #         time.sleep(1)
    #     except:
    #         pass
    #
    #     var_v3.driver.set_page_load_timeout(10)
    #     try:
    #         var_v3.driver.find_element(By.XPATH, var_v3.login_user)
    #     except:
    #         print("1")
    #         try:
    #             var_v3.driver.get(var_v3.linktest)
    #             time.sleep(5)
    #             var_v3.driver.execute_script("window.stop();")
    #             logging.info("da dung tai trang 1")
    #             var_v3.driver.find_element(By.XPATH, var_v3.login_user)
    #             time.sleep(1)
    #         except:
    #             module_other_v3.swich_tab_0()
    #             var_v3.driver.get(var_v3.linktest)
    #             time.sleep(7)
    #             var_v3.driver.execute_script("window.stop();")
    #             logging.info("da dung tai trang 2")
    #             time.sleep(0.5)
    #
    #     time.sleep(3)
    #     try:
    #         var_v3.driver.find_element(By.XPATH, var_v3.login_user).clear()
    #     except:
    #         var_v3.driver.get(var_v3.linktest)
    #         time.sleep(7)
    #         var_v3.driver.find_element(By.XPATH, var_v3.login_user).clear()
    #     time.sleep(0.5)
    #     var_v3.driver.find_element(By.XPATH, var_v3.login_user).send_keys(user)
    #     var_v3.driver.find_element(By.XPATH, var_v3.login_password).clear()
    #     time.sleep(0.5)
    #     var_v3.driver.find_element(By.XPATH, var_v3.login_password).send_keys(password)
    #     var_v3.driver.find_element(By.XPATH, var_v3.dangnhap).click()
    #     time.sleep(10)
    #     # giamsat.xoacanhbao()

    def login_v2(self, user, password):
        # Cấu hình driver
        var_v3.driver.implicitly_wait(10)
        var_v3.driver.maximize_window()
        var_v3.driver.delete_all_cookies()

        # Thử đăng xuất nếu có thể
        try:
            login.logout_v2(self)
        except Exception as e:
            logging.warning(f"Lỗi khi đăng xuất: {e}")

        # Điều hướng đến trang đăng nhập
        try:
            var_v3.driver.set_page_load_timeout(10)
            WebDriverWait(var_v3.driver, 10).until(EC.presence_of_element_located((By.XPATH, var_v3.login_user)))
        except:
            logging.info("Không tìm thấy trường login_user, điều hướng lại trang.")
            var_v3.driver.get(var_v3.linktest)
            try:
                WebDriverWait(var_v3.driver, 10).until(EC.presence_of_element_located((By.XPATH, var_v3.login_user)))
            except:
                logging.warning("Thử lại sau khi chuyển tab.")
                module_other_v3.swich_tab_0()
                var_v3.driver.get(var_v3.linktest)

        # Nhập thông tin đăng nhập
        try:
            username_field = WebDriverWait(var_v3.driver, 10).until(EC.presence_of_element_located((By.XPATH, var_v3.login_user)))
            username_field.clear()
            username_field.send_keys(user)

            password_field = var_v3.driver.find_element(By.XPATH, var_v3.login_password)
            password_field.clear()
            password_field.send_keys(password)

            var_v3.driver.find_element(By.XPATH, var_v3.dangnhap).click()
            logging.info("Đã nhấn nút đăng nhập.")
        except Exception as e:
            logging.error(f"Lỗi trong quá trình đăng nhập: {e}")


        WebDriverWait(var_v3.driver, 15).until(EC.presence_of_element_located((By.XPATH, var_v3.minitor)))
        time.sleep(3)





    def logout_v2(self):
        var_v3.driver.implicitly_wait(1)
        var_v3.driver.find_element(By.XPATH, var_v3.profile).click()
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_logout).click()
        time.sleep(1.5)
        var_v3.driver.find_element(By.XPATH, var_v3.igree).click()
        time.sleep(3)



    def login_v2_account_customer_minitor(self, code, event, result):
        var_v3.driver.implicitly_wait(5)
        login.login_v2(self, "ungroup", "12341234")
        login.login_v2(self, var_v3.data['login']['khongnhom_quantri_tk'], var_v3.data['login']['khongnhom_quantri_mk'])

        module_other_v3.write_result_text_try_if_other(code, event, result, "Màn hình đăng nhập - Login vào hệ thống ",
                                              var_v3.check_login_v2_account_customer_minitor, "", "_Login_TaiKhoanKhachHangCoQuyenGianSat.png")
        logging.info("User: " + var_v3.data['login']['khongnhom_quantri_tk'])
        logging.info("Password: " + var_v3.data['login']['khongnhom_quantri_mk'])



    def login_v2_account_binhanh(self, code, event, result):
        var_v3.driver.implicitly_wait(5)
        login.login_v2(self, var_v3.data['login']['binhanh_tk'], var_v3.data['login']['binhanh_mk'])

        module_other_v3.write_result_text_try_if(code, event, result, "Màn hình đăng nhập - Login vào hệ thống ",
                                              var_v3.title_page, "DANH SÁCH PHƯƠNG TIỆN", "_Login_TaiKhoanBinhAnh.png")
        logging.info("User: " + var_v3.data['login']['binhanh_tk'])
        logging.info("Password: " + var_v3.data['login']['binhanh_mk'])



    def login_v2_account_agency(self, code, event, result):
        var_v3.driver.implicitly_wait(5)
        try:
            login.logout_v2(self)
        except:
            pass
        var_v3.driver.refresh()
        time.sleep(3)
        login.login_v2(self, var_v3.data['login']['conhom_quantri_tk'], var_v3.data['login']['conhom_quantri_mk'])

        module_other_v3.write_result_text_try_if_other(code, event, result, "Màn hình đăng nhập - Login vào hệ thống ",
                                              var_v3.check_login_v2_account_customer_minitor, "", "_Login_TaiKhoanDaiLy.png")
        logging.info("User: " + var_v3.data['login']['conhom_quantri_tk'])
        logging.info("Password: " + var_v3.data['login']['conhom_quantri_mk'])



    def login_v2_account_customer_not_minitor(self, code, event, result):
        var_v3.driver.implicitly_wait(5)
        login.login_v2(self, var_v3.data['login']['khongnhom_thuong_tk1'], var_v3.data['login']['khongnhom_thuong_mk1'])
        module_other_v3.write_result_text_try_if(code, event, result, "Màn hình đăng nhập - Login vào hệ thống ",
                                              var_v3.check_login_v2_account_customer_not_minitor, "Bạn không có quyền truy cập", "_Login_TaiKhoanKhachHangKhongCoQuyenGianSat.png")
        logging.info("User: " + var_v3.data['login']['khongnhom_thuong_tk1'])
        logging.info("Password: " + var_v3.data['login']['khongnhom_thuong_mk1'])



    def login_v2_wrong(self, code, event, result):
        var_v3.driver.implicitly_wait(5)
        var_v3.driver.maximize_window()
        var_v3.driver.get(var_v3.linktest)
        time.sleep(3)
        var_v3.driver.find_element(By.XPATH, var_v3.login_user).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.login_user).send_keys("truongvck2")
        var_v3.driver.find_element(By.XPATH, var_v3.login_password).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.login_password).send_keys("11111")
        var_v3.driver.find_element(By.XPATH, var_v3.dangnhap).click()
        time.sleep(3)
        module_other_v3.write_result_text_try_if(code, event, result, "Màn hình đăng nhập - Login vào hệ thống ",
                                              var_v3.check_login_v2_wrong, "Tên đăng nhập hoặc mật khẩu không đúng", "_Login_TaiKhoanDungMatKhauSai.png")
        logging.info("User: truongtq@bagroup.vn")
        logging.info("Password: 11111")



    def login_v2_remember(self, code, event, result, checkbox, desire, name_image):
        var_v3.driver.implicitly_wait(5)
        var_v3.driver.maximize_window()
        var_v3.driver.get(var_v3.linktest)
        time.sleep(3)
        var_v3.driver.find_element(By.XPATH, var_v3.login_user).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.login_user).send_keys(var_v3.data['login']['khongnhom_thuong_tk1'])
        var_v3.driver.find_element(By.XPATH, var_v3.login_password).clear()
        var_v3.driver.find_element(By.XPATH, var_v3.login_password).send_keys(var_v3.data['login']['khongnhom_thuong_mk1'])
        time.sleep(1)
        if var_v3.driver.find_element(By.XPATH, var_v3.login_remember).is_selected() == checkbox:
            button = var_v3.driver.find_element(By.XPATH, var_v3.login_remember)
            var_v3.driver.execute_script("arguments[0].click();", button)
            # var_v3.driver.find_element(By.XPATH, var_v3.login_remember).click()

        var_v3.driver.find_element(By.XPATH, var_v3.dangnhap).click()
        time.sleep(5)
        login.logout_v2(self)

        logging.info("-------------------------")
        logging.info("Màn hình đăng nhập - Ghi nhớ đăng nhập")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + event)
        logging.info("Kết quả - " + result)
        logging.info("User: " + var_v3.data['login']['khongnhom_thuong_tk1'])
        logging.info("Password: " + var_v3.data['login']['khongnhom_thuong_mk1'])
        checkbox_result = var_v3.driver.find_element(By.XPATH, var_v3.login_remember).is_selected()
        if checkbox_result == desire:
            logging.info("True")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            var_v3.driver.save_screenshot(var_v3.imagepath + code + name_image)
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 7, "Fail")
            module_other_v3.writeData(var_v3.checklistpath, "Checklist", code, 13, code + name_image)



    def login_v2_forget_password(self, code, event, result):
        var_v3.driver.implicitly_wait(5)
        var_v3.driver.maximize_window()
        var_v3.driver.get(var_v3.linktest)
        time.sleep(3)
        var_v3.driver.find_element(By.XPATH, var_v3.forget_password).click()
        time.sleep(2)

        var_v3.driver.find_element(By.XPATH, var_v3.forget_password_user).send_keys(var_v3.data['login']['quenmatkhau_tendangnhap1'])
        var_v3.driver.find_element(By.XPATH, var_v3.forget_password_phone).send_keys(var_v3.data['login']['quenmatkhau_dienthoaidung'])
        time.sleep(1)
        var_v3.driver.find_element(By.XPATH, var_v3.send_code_veryfine).click()
        time.sleep(1)
        module_other_v3.write_result_text_try_if_other(code, event, result, "Màn hình đăng nhập - Quên mật khẩu",
                                              var_v3.check_login_v2_forget_password, "Vui lòng nhập đúng số điện thoại đăng ký tài khoản", "_Login_QuenMatKhau.png")
        logging.info("User: " + var_v3.data['login']['quenmatkhau_tendangnhap1'])
        logging.info("phone: " + var_v3.data['login']['quenmatkhau_dienthoaidung'])




class link:

    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def change_language(self, code, event, result, language, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(10)
        var_v3.driver.maximize_window()
        var_v3.driver.get(var_v3.linktest)
        time.sleep(3)
        var_v3.driver.find_element(By.XPATH, var_v3.icon_change_language).click()
        time.sleep(1.3)
        var_v3.driver.find_element(By.XPATH, language).click()
        time.sleep(3)
        var_v3.driver.find_element(By.XPATH, path_check)

        if name_image == "_Login_DoiNgonNgu_Lao.png":
            module_other_v3.write_result_text_try_if_other(code, event, result, "Màn hình đăng nhập - Đổi ngôn ngữ",
                                                  path_check, desire, name_image)
            try:
                var_v3.driver.find_element(By.XPATH, path_check)
            except:
                link.change_language(self, "", "", "", var_v3.icon_tiengviet,  "", "", "")


        else:
            module_other_v3.write_result_text_try_if(code, event, result, "Màn hình đăng nhập - Đổi ngôn ngữ",
                                                  path_check, desire, name_image)


    def affiliate(self, code, event, result, link, desire, path_module, name_image):
        var_v3.driver.implicitly_wait(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        var_v3.driver.maximize_window()
        var_v3.driver.get(var_v3.linktest)
        time.sleep(3)
        # var_v3.driver.find_element(By.XPATH, link).click()
        button = var_v3.driver.find_element(By.XPATH, link)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(3)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])
        module_other_v3.write_result_text_try_if_title(code, event, result, path_module,
                                              desire, name_image)
        module_other_v3.close_tab()
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])


    def affiliate_appstore(self, code, event, result):
        var_v3.driver.implicitly_wait(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        var_v3.driver.maximize_window()
        var_v3.driver.get(var_v3.linktest)
        time.sleep(5)
        # var_v3.driver.find_element(By.XPATH, var_v3.app_store).click()
        button = var_v3.driver.find_element(By.XPATH, var_v3.app_store)
        var_v3.driver.execute_script("arguments[0].click();", button)

        time.sleep(3)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[1])


        module_other_v3.write_result_text_try_if(code, event, result, "Màn hình đăng nhập - Link liên kết",
                                                 var_v3.check_app_store, "BA GPS 4+", "_Login_AppStore.png")
        module_other_v3.close_tab()
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])



    def login_affiliate(self, code, event, result, link, path_check, desire, name_image):
        var_v3.driver.implicitly_wait(5)
        var_v3.driver.switch_to.window(var_v3.driver.window_handles[0])
        var_v3.driver.maximize_window()
        var_v3.driver.get(var_v3.linktest)
        time.sleep(3)
        try:
            var_v3.driver.find_element(By.XPATH, link).click()
            time.sleep(2.5)
        except:
            pass
        module_other_v3.write_result_text_try_if(code, event, result, "Màn hình đăng nhập - Link giới thiệu",
                                              path_check, desire, name_image)























