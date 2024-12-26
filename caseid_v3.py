import login_v3
import module_other_v3
import var_v3
import openpyxl
from retry import retry
import minitor_v3
import route
import administration
import report_v3
import video_v3
import image_v3
import utility_v3
import ai_v3



def get_datachecklist(ma):
    wordbook = openpyxl.load_workbook(var_v3.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 9
    while (rownum < 3000):
        rownum += 1
        rownum = str(rownum)
        if sheet["A" + rownum].value == ma:
            tensukien = sheet["B" + rownum].value
            ketqua = sheet["E" + rownum].value
            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 42, 2, tensukien)
            var_v3.writeData(var_v3.path_luutamthoi, "Sheet1", 43, 2, ketqua)
            return tensukien, ketqua
        rownum = int(rownum)







def caseid_login01(self):
    get_datachecklist("Login01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.login.login_v2_account_customer_minitor(self, "Login01", event, result)


def caseid_login02(self):
    get_datachecklist("Login02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.login.login_v2_account_binhanh(self, "Login02", event, result)


def caseid_login03(self):
    get_datachecklist("Login03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.login.login_v2_account_agency(self, "Login03", event, result)


def caseid_login04(self):
    get_datachecklist("Login04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.login.login_v2_account_customer_not_minitor(self, "Login04", event, result)


def caseid_login05(self):
    get_datachecklist("Login05")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.login.login_v2_wrong(self, "Login05", event, result)


def caseid_login06(self):
    get_datachecklist("Login06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.login.login_v2_remember(self, "Login06", event, result, False, True, "_Login_GhiNhoDangNhap.png")


def caseid_login07(self):
    get_datachecklist("Login07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.login.login_v2_remember(self, "Login07", event, result, True, False, "_Login_BoGhiNhoDangNhap.png")



def caseid_login08(self):
    get_datachecklist("Login08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.login.login_v2_forget_password(self, "Login08", event, result)



def caseid_login09(self):
    get_datachecklist("Login09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.change_language(self, "Login09", event, result, var_v3.icon_english,
                                  var_v3.check_english, "Forgot password?", "_Login_DoiNgonNgu_TiengAnh.png")

def caseid_login10(self):
    get_datachecklist("Login10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.change_language(self, "Login10", event, result, var_v3.icon_lao,
                                  var_v3.check_lao, "ADMIN_LOGIN_MENUHOME", "_Login_DoiNgonNgu_Lao.png")

def caseid_login11(self):
    get_datachecklist("Login11")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.change_language(self, "Login11", event, result, var_v3.icon_tiengviet,
                                  var_v3.check_tiengviet, "Quên mật khẩu?", "_Login_DoiNgonNgu_TiengViet.png")


def caseid_login12(self):
    get_datachecklist("Login12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login12", event, result, var_v3.home, "GIÁM SÁT HÀNH TRÌNH SỐ 1 VIỆT NAM - BA GPS",
                            "Màn hình đăng nhập - Link giới thiệu", "_Login_TrangChu.png")

def caseid_login13(self):
    get_datachecklist("Login13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login13", event, result, var_v3.product_sevice, "Sản phẩm và Giải pháp - BA GPS",
                            "Màn hình đăng nhập - Link giới thiệu", "_Login_SanPhamDichVu.png")

def caseid_login14(self):
    get_datachecklist("Login14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login14", event, result, var_v3.news, "Tin tức - BA GPS",
                            "Màn hình đăng nhập - Link giới thiệu", "_Login_TinTuc.png")

def caseid_login15(self):
    get_datachecklist("Login15")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login15", event, result, var_v3.fee, "Hướng dẫn đóng phí dịch vụ BA GPS - BA GPS",
                            "Màn hình đăng nhập - Link giới thiệu", "_Login_DongPhi.png")

def caseid_login16(self):
    get_datachecklist("Login16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login16", event, result, var_v3.help, "1. HDSD WEB GPS - HDSD HỆ THỐNG GPS - BAdoc",
                            "Màn hình đăng nhập - Link giới thiệu", "_Login_HuongDan.png")

def caseid_login17(self):
    get_datachecklist("Login17")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login17", event, result, var_v3.network, "Mạng lưới - BA GPS",
                            "Màn hình đăng nhập - Link giới thiệu", "_Login_Mangluoi.png")


def caseid_login18(self):
    get_datachecklist("Login18")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login18", event, result, var_v3.about_us, "Về chúng tôi - BA GPS",
                            "Màn hình đăng nhập - Link giới thiệu", "_Login_VeChungToi.png")


def caseid_login19(self):
    get_datachecklist("Login19")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.login_affiliate(self, "Login19", event, result, var_v3.zalo1, var_v3.check_zalo1,
                             "LIÊN HỆ VỚI TỔNG ĐÀI QUA ZALO", "_Login_Zalo1.png")

def caseid_login20(self):
    pass


def caseid_login21(self):
    get_datachecklist("Login21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.login_affiliate(self, "Login21", event, result, "", var_v3.adress_hn,
                             "Lô 14 Nguyễn Cảnh Dị, P. Đại Kim, Q. Hoàng Mai, TP. Hà Nội.", "_Login_DiaChiTruSoHn.png")


def caseid_login22(self):
    get_datachecklist("Login22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login22", event, result, var_v3.google_play, "BA GPS - Apps on Google Play",
                            "Màn hình đăng nhập - Link liên kết", "_Login_GooglePlay.png")


def caseid_login23(self):
    get_datachecklist("Login23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate_appstore(self, "Login23", event, result)



def caseid_login24(self):
    pass



def caseid_login25(self):
    get_datachecklist("Login25")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login25", event, result, var_v3.zalo2, "BA GPS trên Zalo",
                            "Màn hình đăng nhập - Link liên kết", "_Login_Zalo2.png")

# "Zalo - Nhắn Gửi Yêu Thương (Nhắn tin thoại - Trò chuyện nhóm ...)"or"BA GPS trên Zalo"


def caseid_login26(self):
    get_datachecklist("Login26")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    login_v3.link.affiliate(self, "Login26", event, result, var_v3.youtobe, "BA GPS - YouTube",
                            "Màn hình đăng nhập - Link liên kết", "_Login_Youtobe.png")



def caseid_giamsat01(self):
    get_datachecklist("GiamSat01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.search_vehicle(self, "GiamSat01", event, result)


def caseid_giamsat02(self):
    get_datachecklist("GiamSat02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.search_place(self, "GiamSat02", event, result)



def caseid_giamsat03(self):
    get_datachecklist("GiamSat03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.search_location(self, "GiamSat03", event, result)


def caseid_giamsat04(self):
    get_datachecklist("GiamSat04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.group_select_group(self, "GiamSat04", event, result, var_v3.group_select_onegroup, "Giám sát - Chọn 1 nhóm")


def caseid_giamsat05(self):
    get_datachecklist("GiamSat05")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.group_select_group(self, "GiamSat05", event, result, var_v3.group_select_allgroup, "Giám sát - Chọn tất cả nhóm")


def caseid_giamsat06(self):
    get_datachecklist("GiamSat06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.check_number_of_update_time(self, "GiamSat06", event, result)


def caseid_giamsat07(self):
    get_datachecklist("GiamSat07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat07", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Nhấp để lọc Di chuyển")

def caseid_giamsat08(self):
    get_datachecklist("GiamSat08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat08", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Nhấp để lọc Dừng - bật")

def caseid_giamsat09(self):
    get_datachecklist("GiamSat09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat09", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Nhấp để lọc Dừng - tắt")

def caseid_giamsat10(self):
    get_datachecklist("GiamSat10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat10", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Nhấp để lọc Quá tốc độ mức 1")

def caseid_giamsat11(self):
    get_datachecklist("GiamSat11")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat11", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Nhấp để lọc Quá tốc độ mức 2")

def caseid_giamsat12(self):
    get_datachecklist("GiamSat12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat12", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Nhấp để lọc Mất GSM")

def caseid_giamsat13(self):
    get_datachecklist("GiamSat13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat13", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Nhấp để lọc Mất GPS")

def caseid_giamsat14(self):
    get_datachecklist("GiamSat14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat14", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Nhấp để lọc Nợ phí")


def caseid_giamsat15(self):
    get_datachecklist("GiamSat15")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat15", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Xem tất cả")


def caseid_giamsat16(self):
    get_datachecklist("GiamSat16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat16", event, result, "quyền thường",
                                           "công ty không có nhóm", "Nhấp để lọc Di chuyển")

def caseid_giamsat17(self):
    get_datachecklist("GiamSat17")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat17", event, result, "quyền thường",
                                           "công ty không có nhóm", "Nhấp để lọc Dừng - bật")

def caseid_giamsat18(self):
    get_datachecklist("GiamSat18")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat18", event, result, "quyền thường",
                                           "công ty không có nhóm", "Nhấp để lọc Dừng - tắt")

def caseid_giamsat19(self):
    get_datachecklist("GiamSat19")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat19", event, result, "quyền thường",
                                           "công ty không có nhóm", "Nhấp để lọc Quá tốc độ mức 1")

def caseid_giamsat20(self):
    get_datachecklist("GiamSat20")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat20", event, result, "quyền thường",
                                           "công ty không có nhóm", "Nhấp để lọc Quá tốc độ mức 2")

def caseid_giamsat21(self):
    get_datachecklist("GiamSat21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat21", event, result, "quyền thường",
                                           "công ty không có nhóm", "Nhấp để lọc Mất GSM")

def caseid_giamsat22(self):
    get_datachecklist("GiamSat22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat22", event, result, "quyền thường",
                                           "công ty không có nhóm", "Nhấp để lọc Mất GPS")

def caseid_giamsat23(self):
    get_datachecklist("GiamSat23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat23", event, result, "quyền thường",
                                           "công ty không có nhóm", "Nhấp để lọc Nợ phí")


def caseid_giamsat24(self):
    get_datachecklist("GiamSat24")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat24", event, result, "quyền quản trị",
                                           "công ty không có nhóm", "Xem tất cả")


def caseid_giamsat25(self):
    get_datachecklist("GiamSat25")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat25", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Nhấp để lọc Di chuyển")

def caseid_giamsat26(self):
    get_datachecklist("GiamSat26")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat26", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Nhấp để lọc Dừng - bật")

def caseid_giamsat27(self):
    get_datachecklist("GiamSat27")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat27", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Nhấp để lọc Dừng - tắt")

def caseid_giamsat28(self):
    get_datachecklist("GiamSat28")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat28", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Nhấp để lọc Quá tốc độ mức 1")

def caseid_giamsat29(self):
    get_datachecklist("GiamSat29")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat29", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Nhấp để lọc Quá tốc độ mức 2")

def caseid_giamsat30(self):
    get_datachecklist("GiamSat30")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat30", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Nhấp để lọc Mất GSM")

def caseid_giamsat31(self):
    get_datachecklist("GiamSat31")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat31", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Nhấp để lọc Mất GPS")

def caseid_giamsat32(self):
    get_datachecklist("GiamSat32")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat32", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Nhấp để lọc Nợ phí")


def caseid_giamsat33(self):
    get_datachecklist("GiamSat33")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat33", event, result, "quyền quản trị",
                                           "công ty có nhóm", "Xem tất cả")


def caseid_giamsat34(self):
    get_datachecklist("GiamSat34")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat34", event, result, "quyền thường",
                                           "công ty có nhóm", "Nhấp để lọc Di chuyển")

def caseid_giamsat35(self):
    get_datachecklist("GiamSat35")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat35", event, result, "quyền thường",
                                           "công ty có nhóm", "Nhấp để lọc Dừng - bật")

def caseid_giamsat36(self):
    get_datachecklist("GiamSat36")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat36", event, result, "quyền thường",
                                           "công ty có nhóm", "Nhấp để lọc Dừng - tắt")

def caseid_giamsat37(self):
    get_datachecklist("GiamSat37")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat37", event, result, "quyền thường",
                                           "công ty có nhóm", "Nhấp để lọc Quá tốc độ mức 1")

def caseid_giamsat38(self):
    get_datachecklist("GiamSat38")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat38", event, result, "quyền thường",
                                           "công ty có nhóm", "Nhấp để lọc Quá tốc độ mức 2")

def caseid_giamsat39(self):
    get_datachecklist("GiamSat39")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat39", event, result, "quyền thường",
                                           "công ty có nhóm", "Nhấp để lọc Mất GSM")

def caseid_giamsat40(self):
    get_datachecklist("GiamSat40")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat40", event, result, "quyền thường",
                                           "công ty có nhóm", "Nhấp để lọc Mất GPS")

def caseid_giamsat41(self):
    get_datachecklist("GiamSat41")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat41", event, result, "quyền thường",
                                           "công ty có nhóm", "Nhấp để lọc Nợ phí")


def caseid_giamsat42(self):
    get_datachecklist("GiamSat42")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat42", event, result, "quyền thường",
                                           "công ty có nhóm", "Xem tất cả")


def caseid_giamsat43(self):
    get_datachecklist("GiamSat43")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat43", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Nhấp để lọc Di chuyển")

def caseid_giamsat44(self):
    get_datachecklist("GiamSat44")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat44", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Nhấp để lọc Dừng - bật")

def caseid_giamsat45(self):
    get_datachecklist("GiamSat45")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat45", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Nhấp để lọc Dừng - tắt")

def caseid_giamsat46(self):
    get_datachecklist("GiamSat46")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat46", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Nhấp để lọc Quá tốc độ mức 1")

def caseid_giamsat47(self):
    get_datachecklist("GiamSat47")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat47", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Nhấp để lọc Quá tốc độ mức 2")

def caseid_giamsat48(self):
    get_datachecklist("GiamSat48")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat48", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Nhấp để lọc Mất GSM")

def caseid_giamsat49(self):
    get_datachecklist("GiamSat49")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat49", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Nhấp để lọc Mất GPS")

def caseid_giamsat50(self):
    get_datachecklist("GiamSat50")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat50", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Nhấp để lọc Nợ phí")


def caseid_giamsat51(self):
    get_datachecklist("GiamSat51")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat51", event, result, "quyền quản trị",
                                           "công ty không có nhóm2", "Xem tất cả")

def caseid_giamsat52(self):
    get_datachecklist("GiamSat52")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat52", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Nhấp để lọc Di chuyển")

def caseid_giamsat53(self):
    get_datachecklist("GiamSat53")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat53", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Nhấp để lọc Dừng - bật")

def caseid_giamsat54(self):
    get_datachecklist("GiamSat54")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat54", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Nhấp để lọc Dừng - tắt")

def caseid_giamsat55(self):
    get_datachecklist("GiamSat55")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat55", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Nhấp để lọc Quá tốc độ mức 1")

def caseid_giamsat56(self):
    get_datachecklist("GiamSat56")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat56", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Nhấp để lọc Quá tốc độ mức 2")

def caseid_giamsat57(self):
    get_datachecklist("GiamSat57")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat57", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Nhấp để lọc Mất GSM")

def caseid_giamsat58(self):
    get_datachecklist("GiamSat58")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat58", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Nhấp để lọc Mất GPS")

def caseid_giamsat59(self):
    get_datachecklist("GiamSat59")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat59", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Nhấp để lọc Nợ phí")


def caseid_giamsat60(self):
    get_datachecklist("GiamSat60")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat60", event, result, "quyền thường",
                                           "công ty không có nhóm2", "Xem tất cả")

def caseid_giamsat61(self):
    get_datachecklist("GiamSat61")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat61", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Nhấp để lọc Di chuyển")

def caseid_giamsat62(self):
    get_datachecklist("GiamSat62")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat62", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Nhấp để lọc Dừng - bật")

def caseid_giamsat63(self):
    get_datachecklist("GiamSat63")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat63", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Nhấp để lọc Dừng - tắt")

def caseid_giamsat64(self):
    get_datachecklist("GiamSat64")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat64", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Nhấp để lọc Quá tốc độ mức 1")

def caseid_giamsat65(self):
    get_datachecklist("GiamSat65")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat65", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Nhấp để lọc Quá tốc độ mức 2")

def caseid_giamsat66(self):
    get_datachecklist("GiamSat66")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat66", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Nhấp để lọc Mất GSM")

def caseid_giamsat67(self):
    get_datachecklist("GiamSat67")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat67", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Nhấp để lọc Mất GPS")

def caseid_giamsat68(self):
    get_datachecklist("GiamSat68")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat68", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Nhấp để lọc Nợ phí")


def caseid_giamsat69(self):
    get_datachecklist("GiamSat69")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat69", event, result, "quyền quản trị",
                                           "công ty có nhóm2", "Xem tất cả")
def caseid_giamsat70(self):
    get_datachecklist("GiamSat70")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat70", event, result, "quyền thường",
                                           "công ty có nhóm2", "Nhấp để lọc Di chuyển")

def caseid_giamsat71(self):
    get_datachecklist("GiamSat71")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat71", event, result, "quyền thường",
                                           "công ty có nhóm2", "Nhấp để lọc Dừng - bật")

def caseid_giamsat72(self):
    get_datachecklist("GiamSat72")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat72", event, result, "quyền thường",
                                           "công ty có nhóm2", "Nhấp để lọc Dừng - tắt")

def caseid_giamsat73(self):
    get_datachecklist("GiamSat73")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat73", event, result, "quyền thường",
                                           "công ty có nhóm2", "Nhấp để lọc Quá tốc độ mức 1")

def caseid_giamsat74(self):
    get_datachecklist("GiamSat74")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat74", event, result, "quyền thường",
                                           "công ty có nhóm2", "Nhấp để lọc Quá tốc độ mức 2")

def caseid_giamsat75(self):
    get_datachecklist("GiamSat75")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat75", event, result, "quyền thường",
                                           "công ty có nhóm2", "Nhấp để lọc Mất GSM")

def caseid_giamsat76(self):
    get_datachecklist("GiamSat76")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat76", event, result, "quyền thường",
                                           "công ty có nhóm2", "Nhấp để lọc Mất GPS")


def caseid_giamsat77(self):
    get_datachecklist("GiamSat77")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat77", event, result, "quyền thường",
                                           "công ty có nhóm2", "Nhấp để lọc Nợ phí")


def caseid_giamsat78(self):
    get_datachecklist("GiamSat78")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.status_vehicle(self, "GiamSat78", event, result, "quyền thường",
                                           "công ty có nhóm2", "Xem tất cả")

def caseid_giamsat79(self):
    get_datachecklist("GiamSat79")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.check_onlinehandler(self, "GiamSat79", event, result)



def caseid_giamsat80(self):
    get_datachecklist("GiamSat80")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_share(self, "GiamSat80", event, result)


def caseid_giamsat81(self):
    get_datachecklist("GiamSat81")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_share_create_copy(self, "GiamSat81", event, result)



def caseid_giamsat82(self):
    pass



def caseid_giamsat83(self):
    get_datachecklist("GiamSat83")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_share_close(self, "GiamSat83", event, result)


def caseid_giamsat84(self):
    get_datachecklist("GiamSat84")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_system_status(self, "GiamSat84", event, result)


def caseid_giamsat85(self):
    get_datachecklist("GiamSat85")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_system_status_group_vehicle(self, "GiamSat85", event, result)


def caseid_giamsat86(self):
    get_datachecklist("GiamSat86")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_system_status_vehicle(self, "GiamSat86", event, result)


def caseid_giamsat87(self):
    get_datachecklist("GiamSat87")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_system_status_refresh(self, "GiamSat87", event, result)


def caseid_giamsat88(self):
    get_datachecklist("GiamSat88")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_system_status_export_excel(self, "GiamSat88", event, result)


def caseid_giamsat89(self):
    get_datachecklist("GiamSat89")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_system_status_close(self, "GiamSat89", event, result)


def caseid_giamsat90(self):
    get_datachecklist("GiamSat90")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_setting(self, "GiamSat90", event, result)


def caseid_giamsat91(self):
    get_datachecklist("GiamSat91")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_setting_display_all_field(self, "GiamSat91", event, result)


def caseid_giamsat92(self):
    get_datachecklist("GiamSat92")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_setting_display_hide_all_field(self, "GiamSat92", event, result)


def caseid_giamsat93(self):
    get_datachecklist("GiamSat93")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_setting_display_listvehicle_online(self, "GiamSat93", event, result)


def caseid_giamsat94(self):
    get_datachecklist("GiamSat94")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_setting_display_frame_width(self, "GiamSat94", event, result)


def caseid_giamsat95(self):
    get_datachecklist("GiamSat95")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_setting_display_save(self, "GiamSat95", event, result)


def caseid_giamsat96(self):
    get_datachecklist("GiamSat96")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_setting_display_close(self, "GiamSat96", event, result)


def caseid_giamsat97(self):
    get_datachecklist("GiamSat97")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_refresh(self, "GiamSat97", event, result)



def caseid_giamsat98(self):
    get_datachecklist("GiamSat98")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_vehicle_color_meaning(self, "GiamSat98", event, result)


def caseid_giamsat99(self):
    get_datachecklist("GiamSat99")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.icon_vehicle_color_meaning_close(self, "GiamSat99", event, result)


def caseid_giamsat100(self):
    get_datachecklist("GiamSat100")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.see_route(self, "GiamSat100", event, result)


def caseid_giamsat101(self):
    get_datachecklist("GiamSat101")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.see_route_8h_fast(self, "GiamSat101", event, result)


def caseid_giamsat102(self):
    get_datachecklist("GiamSat102")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.see_route_8h_newtab(self, "GiamSat102", event, result)


def caseid_giamsat103(self):
    get_datachecklist("GiamSat103")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.see_route_inday_fast(self, "GiamSat103", event, result)


def caseid_giamsat104(self):
    get_datachecklist("GiamSat104")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.see_route_inday_newtab(self, "GiamSat104", event, result)


def caseid_giamsat105(self):
    get_datachecklist("GiamSat105")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.share_vehicle(self, "GiamSat105", event, result)


def caseid_giamsat106(self):
    get_datachecklist("GiamSat106")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.share_vehicle_x(self, "GiamSat106", event, result)


def caseid_giamsat107(self):
    get_datachecklist("GiamSat107")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.calculate_distance(self, "GiamSat107", event, result)

def caseid_giamsat108(self):
    get_datachecklist("GiamSat108")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.from_vehicle_to_vehicle(self, "GiamSat108", event, result)


def caseid_giamsat109(self):
    get_datachecklist("GiamSat109")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.from_vehicle_to_location(self, "GiamSat109", event, result)


def caseid_giamsat110(self):
    get_datachecklist("GiamSat110")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.from_location_to_location(self, "GiamSat110", event, result)


def caseid_giamsat111(self):
    get_datachecklist("GiamSat111")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.from_location_to_vehicle(self, "GiamSat111", event, result)


def caseid_giamsat112(self):
    get_datachecklist("GiamSat112")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.my_location_to_location(self, "GiamSat112", event, result)


def caseid_giamsat113(self):
    get_datachecklist("GiamSat113")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.calculate_distance_refresh(self, "GiamSat113", event, result)


def caseid_giamsat114(self):
    get_datachecklist("GiamSat114")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.calculate_distance_export_excel(self, "GiamSat114", event, result)


def caseid_giamsat115(self):
    get_datachecklist("GiamSat115")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.calculate_distance_x(self, "GiamSat115", event, result)


def caseid_giamsat116(self):
    get_datachecklist("GiamSat116")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info(self, "GiamSat116", event, result)


def caseid_giamsat117(self):
    get_datachecklist("GiamSat117")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat117", event, result,
                                               var_v3.check_device_info_imei, "GiamSat_ThongTinThietBi_IMEI.png")


def caseid_giamsat118(self):
    get_datachecklist("GiamSat118")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat118", event, result,
                                               var_v3.check_device_info_vin, "GiamSat_ThongTinThietBi_VIN.png")


def caseid_giamsat119(self):
    get_datachecklist("GiamSat119")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat119", event, result,
                                               var_v3.check_device_info_vehicle, "GiamSat_ThongTinThietBi_PhuongTien.png")

def caseid_giamsat120(self):
    get_datachecklist("GiamSat120")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat120", event, result,
                                               var_v3.check_device_info_liscense_plate, "GiamSat_ThongTinThietBi_BienKiemSoat.png")


def caseid_giamsat121(self):
    get_datachecklist("GiamSat121")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat121", event, result,
                                               var_v3.check_device_info_first_time, "GiamSat_ThongTinThietBi_ThoiDiemHoatDongLanDau.png")


def caseid_giamsat122(self):
    get_datachecklist("GiamSat122")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat122", event, result,
                                               var_v3.check_device_info_send_recently, "GiamSat_ThongTinThietBi_ThoiDiemGuiTinGanNhat.png")


def caseid_giamsat123(self):
    get_datachecklist("GiamSat123")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat123", event, result,
                                               var_v3.check_device_info_gps, "GiamSat_ThongTinThietBi_TrangThaiGPS.png")


def caseid_giamsat124(self):
    get_datachecklist("GiamSat124")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat124", event, result,
                                               var_v3.check_device_info_number_phone, "GiamSat_ThongTinThietBi_SoDienThoai.png")


def caseid_giamsat125(self):
    get_datachecklist("GiamSat125")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat125", event, result,
                                               var_v3.check_device_info_subscriber_type, "GiamSat_ThongTinThietBi_LoaiThueBao.png")


def caseid_giamsat126(self):
    get_datachecklist("GiamSat126")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat126", event, result,
                                               var_v3.check_device_info_battery_level, "GiamSat_ThongTinThietBi_MucAcQuy.png")


def caseid_giamsat127(self):
    get_datachecklist("GiamSat127")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_detail(self, "GiamSat127", event, result,
                                               var_v3.check_device_info_power_status, "GiamSat_ThongTinThietBi_TrangThaiNguon.png")


def caseid_giamsat128(self):
    get_datachecklist("GiamSat128")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.device_info_x(self, "GiamSat128", event, result)


def caseid_giamsat129(self):
    get_datachecklist("GiamSat129")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images(self, "GiamSat129", event, result)


def caseid_giamsat130(self):
    get_datachecklist("GiamSat130")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images_refresh(self, "GiamSat130", event, result)


def caseid_giamsat131(self):
    get_datachecklist("GiamSat131")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.view_photo_auto(self, "GiamSat131", event, result)


def caseid_giamsat132(self):
    get_datachecklist("GiamSat132")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images_detail(self, "GiamSat132", event, result,
                                               var_v3.quickly_view_images_vehicle, "GiamSat_XemNhanhHinhAnh_PhuongTien.png")


def caseid_giamsat133(self):
    get_datachecklist("GiamSat133")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images_detail(self, "GiamSat133", event, result,
                                               var_v3.quickly_view_images_channel, "GiamSat_XemNhanhHinhAnh_Kenh.png")


def caseid_giamsat134(self):
    get_datachecklist("GiamSat134")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images_detail(self, "GiamSat134", event, result,
                                               var_v3.quickly_view_images_adress, "GiamSat_XemNhanhHinhAnh_DiaChi.png")


def caseid_giamsat135(self):
    get_datachecklist("GiamSat135")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images_detail(self, "GiamSat135", event, result,
                                               var_v3.quickly_view_images_time, "GiamSat_XemNhanhHinhAnh_ThoiGian.png")


def caseid_giamsat136(self):
    get_datachecklist("GiamSat136")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images_detail(self, "GiamSat136", event, result,
                                               var_v3.quickly_view_images_drive, "GiamSat_XemNhanhHinhAnh_LaiXe.png")


def caseid_giamsat137(self):
    get_datachecklist("GiamSat137")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images_detail(self, "GiamSat137", event, result,
                                               var_v3.quickly_view_images_speed, "GiamSat_XemNhanhHinhAnh_VanToc.png")


def caseid_giamsat138(self):
    get_datachecklist("GiamSat138")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.dowload_images(self, "GiamSat138", event, result)


def caseid_giamsat139(self):
    get_datachecklist("GiamSat139")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.quickly_view_images_x(self, "GiamSat139", event, result)


def caseid_giamsat140(self):
    get_datachecklist("GiamSat140")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.online_image_minitor(self, "GiamSat140", event, result)


def caseid_giamsat141(self):
    get_datachecklist("GiamSat141")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.camera_minitor(self, "GiamSat141", event, result)


def caseid_giamsat142(self):
    get_datachecklist("GiamSat142")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.hide_vehicle(self, "GiamSat142", event, result)


def caseid_giamsat143(self):
    get_datachecklist("GiamSat143")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.hidde_on_surveillance(self, "GiamSat143", event, result)


def caseid_giamsat144(self):
    get_datachecklist("GiamSat144")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.un_hidde_on_surveillance(self, "GiamSat144", event, result)


def caseid_giamsat145(self):
    get_datachecklist("GiamSat145")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.list_vehicle.hide_vehicle_cancel(self, "GiamSat145", event, result)


@retry(tries=3, delay=2, backoff=1, jitter=5)
def caseid_giamsat146(self):
    get_datachecklist("GiamSat146")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.get_info_vehicle_online(self, "GiamSat146", event, result)


def caseid_giamsat147(self):
    get_datachecklist("GiamSat147")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_vehicle(self, "GiamSat147", event, result)


def caseid_giamsat148(self):
    get_datachecklist("GiamSat148")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_group(self, "GiamSat148", event, result)


def caseid_giamsat149(self):
    get_datachecklist("GiamSat149")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_time(self, "GiamSat149", event, result)


def caseid_giamsat150(self):
    get_datachecklist("GiamSat150")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_v_gps(self, "GiamSat150", event, result)


def caseid_giamsat151(self):
    get_datachecklist("GiamSat151")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_v_co(self, "GiamSat151", event, result)


def caseid_giamsat152(self):
    get_datachecklist("GiamSat152")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_km_in_day(self, "GiamSat152", event, result)


def caseid_giamsat153(self):
    get_datachecklist("GiamSat153")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_stop(self, "GiamSat153", event, result)


def caseid_giamsat154(self):
    get_datachecklist("GiamSat154")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_time_stop(self, "GiamSat154", event, result)


def caseid_giamsat155(self):
    get_datachecklist("GiamSat155")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_stop_on_machine(self, "GiamSat155", event, result)


def caseid_giamsat156(self):
    get_datachecklist("GiamSat156")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_door(self, "GiamSat156", event, result)


def caseid_giamsat157(self):
    get_datachecklist("GiamSat157")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_machine(self, "GiamSat157", event, result)


def caseid_giamsat158(self):
    get_datachecklist("GiamSat158")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_ari_conditional(self, "GiamSat158", event, result)


def caseid_giamsat159(self):
    get_datachecklist("GiamSat159")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_concrete(self, "GiamSat159", event, result)


def caseid_giamsat160(self):
    get_datachecklist("GiamSat160")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_fuel(self, "GiamSat160", event, result)


def caseid_giamsat161(self):
    get_datachecklist("GiamSat161")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_temperature(self, "GiamSat161", event, result)


def caseid_giamsat162(self):
    get_datachecklist("GiamSat162")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_vin(self, "GiamSat162", event, result)


def caseid_giamsat163(self):
    get_datachecklist("GiamSat163")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_adress(self, "GiamSat163", event, result)


def caseid_giamsat164(self):
    get_datachecklist("GiamSat164")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_drive(self, "GiamSat164", event, result)


def caseid_giamsat165(self):
    get_datachecklist("GiamSat165")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_liscense_plate(self, "GiamSat165", event, result)


def caseid_giamsat166(self):
    get_datachecklist("GiamSat166")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_phone_number(self, "GiamSat166", event, result)


def caseid_giamsat167(self):
    get_datachecklist("GiamSat167")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_time_continute(self, "GiamSat167", event, result)


def caseid_giamsat168(self):
    get_datachecklist("GiamSat168")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_time_day(self, "GiamSat168", event, result)


def caseid_giamsat169(self):
    get_datachecklist("GiamSat169")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_too_speed(self, "GiamSat169", event, result)


def caseid_giamsat170(self):
    get_datachecklist("GiamSat170")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_management_department(self, "GiamSat170", event, result)


def caseid_giamsat171(self):
    get_datachecklist("GiamSat171")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_memory(self, "GiamSat171", event, result)


def caseid_giamsat172(self):
    get_datachecklist("GiamSat172")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_type_of_transport(self, "GiamSat172", event, result)


def caseid_giamsat173(self):
    get_datachecklist("GiamSat173")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_fee(self, "GiamSat173", event, result)


def caseid_giamsat174(self):
    get_datachecklist("GiamSat174")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_package_name(self, "GiamSat174", event, result)


def caseid_giamsat175(self):
    get_datachecklist("GiamSat175")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_home_network(self, "GiamSat175", event, result)


def caseid_giamsat176(self):
    get_datachecklist("GiamSat176")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_package_capacity(self, "GiamSat176", event, result)


def caseid_giamsat177(self):
    get_datachecklist("GiamSat177")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_day_save(self, "GiamSat177", event, result)


def caseid_giamsat178(self):
    get_datachecklist("GiamSat178")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_save(self, "GiamSat178", event, result)


def caseid_giamsat179(self):
    get_datachecklist("GiamSat179")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_positioning(self, "GiamSat179", event, result)


def caseid_giamsat180(self):
    get_datachecklist("GiamSat180")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_image(self, "GiamSat180", event, result)


def caseid_giamsat181(self):
    get_datachecklist("GiamSat181")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_video(self, "GiamSat181", event, result)


def caseid_giamsat182(self):
    get_datachecklist("GiamSat182")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_channel_camera(self, "GiamSat182", event, result)


def caseid_giamsat183(self):
    get_datachecklist("GiamSat183")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_channel_activity(self, "GiamSat183", event, result)


def caseid_giamsat184(self):
    get_datachecklist("GiamSat184")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_network_connect(self, "GiamSat184", event, result)


def caseid_giamsat185(self):
    get_datachecklist("GiamSat185")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.check_info_vehicle.check_info_status(self, "GiamSat185", event, result)


def caseid_giamsat186(self):
    get_datachecklist("GiamSat186")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.see_adress(self, "GiamSat186", event, result)


def caseid_giamsat187(self):
    get_datachecklist("GiamSat187")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.see_adress_x(self, "GiamSat187", event, result)


def caseid_giamsat188(self):
    get_datachecklist("GiamSat188")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.center_here(self, "GiamSat188", event, result)


def caseid_giamsat189(self):
    get_datachecklist("GiamSat189")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.center_here_igree(self, "GiamSat189", event, result)


def caseid_giamsat190(self):
    get_datachecklist("GiamSat190")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.center_here_cancel(self, "GiamSat190", event, result)


def caseid_giamsat191(self):
    get_datachecklist("GiamSat191")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.come_center(self, "GiamSat191", event, result)


def caseid_giamsat192(self):
    get_datachecklist("GiamSat192")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.create_location(self, "GiamSat192", event, result)



def caseid_giamsat193(self):
    pass



def caseid_giamsat194(self):
    get_datachecklist("GiamSat194")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.fil_info_save(self, "GiamSat194", event, result)


def caseid_giamsat195(self):
    get_datachecklist("GiamSat195")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.share_location(self, "GiamSat195", event, result)


def caseid_giamsat196(self):
    get_datachecklist("GiamSat196")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.update_location(self, "GiamSat196", event, result)


def caseid_giamsat197(self):
    get_datachecklist("GiamSat197")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.delete_location(self, "GiamSat197", event, result)


def caseid_giamsat198(self):
    get_datachecklist("GiamSat198")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.edit_drawing_area(self, "GiamSat198", event, result)


def caseid_giamsat199(self):
    get_datachecklist("GiamSat199")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.redraw(self, "GiamSat199", event, result)


def caseid_giamsat200(self):
    get_datachecklist("GiamSat200")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.create_location_close(self, "GiamSat200", event, result)


def caseid_giamsat201(self):
    get_datachecklist("GiamSat201")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.find_vehicle_in_area(self, "GiamSat201", event, result)


def caseid_giamsat202(self):
    get_datachecklist("GiamSat202")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.edit_drawing_area2(self, "GiamSat202", event, result)


def caseid_giamsat203(self):
    get_datachecklist("GiamSat203")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.redraw2(self, "GiamSat203", event, result)


def caseid_giamsat204(self):
    get_datachecklist("GiamSat204")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.find_vehicle_in_area_search(self, "GiamSat204", event, result)


def caseid_giamsat205(self):
    get_datachecklist("GiamSat205")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.find_vehicle_in_area_refresh(self, "GiamSat205", event, result)


def caseid_giamsat206(self):
    get_datachecklist("GiamSat206")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.find_vehicle_in_area_export_excel(self, "GiamSat206", event, result)


def caseid_giamsat207(self):
    get_datachecklist("GiamSat207")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.find_vehicle_in_area_x(self, "GiamSat207", event, result)



def caseid_giamsat208(self):
    get_datachecklist("GiamSat208")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.measure_distance(self, "GiamSat208", event, result)


def caseid_giamsat209(self):
    get_datachecklist("GiamSat209")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.total_distance(self, "GiamSat209", event, result)


def caseid_giamsat210(self):
    get_datachecklist("GiamSat210")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.measure_distance_delete_location(self, "GiamSat210", event, result)


def caseid_giamsat211(self):
    get_datachecklist("GiamSat211")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.measure_distance_x(self, "GiamSat211", event, result)


def caseid_giamsat212(self):
    get_datachecklist("GiamSat212")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.boot_config(self, "GiamSat212", event, result)


def caseid_giamsat213(self):
    get_datachecklist("GiamSat213")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.boot_config_close(self, "GiamSat213", event, result)


def caseid_giamsat214(self):
    get_datachecklist("GiamSat214")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.boot_config_save(self, "GiamSat214", event, result, "Bản đồ Bình Anh", "17", "Phương tiện trung tâm",
                                    "1", "1", "1", "_GiamSat_CauHinhKhoiDong_BanDoBinhAnh.png")


def caseid_giamsat215(self):
    get_datachecklist("GiamSat215")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.boot_config_save(self, "GiamSat215", event, result, "Vệ tinh Bình Anh", "15", "Phương tiện trung tâm",
                                    "2", "2", "2", "_GiamSat_CauHinhKhoiDong_VeTinhBinhAnh.png")


def caseid_giamsat216(self):
    get_datachecklist("GiamSat216")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.boot_config_save(self, "GiamSat216", event, result, "Vệ tinh Google", "17", "Vị trí trung tâm",
                                    "3", "2", "2", "_GiamSat_CauHinhKhoiDong_VeTinhGoogle.png")



def caseid_giamsat217(self):
    get_datachecklist("GiamSat217")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.boot_config_save(self, "GiamSat217", event, result, "Bản đồ Google", "17", "Vị trí trung tâm",
                                    "0", "1", "1", "_GiamSat_CauHinhKhoiDong_BanDoGoogle.png")


def caseid_giamsat218(self):
    get_datachecklist("GiamSat218")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.config_display_group_location(self, "GiamSat218", event, result)


def caseid_giamsat219(self):
    get_datachecklist("GiamSat219")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.config_display_group_location_search(self, "GiamSat219", event, result)


def caseid_giamsat220(self):
    get_datachecklist("GiamSat220")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.group_location_company(self, "GiamSat220", event, result, False)


def caseid_giamsat221(self):
    get_datachecklist("GiamSat221")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.group_location_company(self, "GiamSat221", event, result, True)


def caseid_giamsat222(self):
    get_datachecklist("GiamSat222")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.group_location_system(self, "GiamSat222", event, result, False)


def caseid_giamsat223(self):
    get_datachecklist("GiamSat223")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.group_location_system(self, "GiamSat223", event, result, True)


def caseid_giamsat224(self):
    get_datachecklist("GiamSat224")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.config_display_group_location_close(self, "GiamSat224", event, result)


def caseid_giamsat225(self):
    get_datachecklist("GiamSat225")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.see_route_route(self, "GiamSat225", event, result)


def caseid_giamsat226(self):
    get_datachecklist("GiamSat226")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.go_comeback(self, "GiamSat226", event, result, "Chiều đi", var_v3.name_route1)


def caseid_giamsat227(self):
    get_datachecklist("GiamSat227")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.go_comeback(self, "GiamSat227", event, result, "Chiều về", var_v3.name_route5)


def caseid_giamsat228(self):
    get_datachecklist("GiamSat228")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.management_route(self, "GiamSat228", event, result)


def caseid_giamsat229(self):
    get_datachecklist("GiamSat229")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_v3.map.see_route_route_close(self, "GiamSat229", event, result)



def caseid_route01(self):
    get_datachecklist("Route01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.open_route(self, "Route01", event, result)



def caseid_route02(self):
    get_datachecklist("Route02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.dowload_data(self, "Route02", event, result)


def caseid_route03(self):
    get_datachecklist("Route03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.icon_run_route(self, "Route03", event, result)


def caseid_route04(self):
    get_datachecklist("Route04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_status(self, "Route04", event, result, var_v3.route_status_stop, "_LoTrinh_DungDo.png")


def caseid_route05(self):
    get_datachecklist("Route05")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_status(self, "Route05", event, result, var_v3.route_status_too_speed, "_LoTrinh_QuaTocDo.png")


def caseid_route06(self):
    get_datachecklist("Route06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_status(self, "Route06", event, result, var_v3.route_status_on_conditional, "_LoTrinh_BatDieuHoa.png")


def caseid_route07(self):
    get_datachecklist("Route07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_status(self, "Route07", event, result, var_v3.route_status_open_door,"_LoTrinh_MoCua.png")


def caseid_route08(self):
    get_datachecklist("Route08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_status(self, "Route08", event, result, var_v3.route_status_on_machine, "_LoTrinh_BatMay.png")


def caseid_route09(self):
    get_datachecklist("Route09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.config_display_route(self, "Route09", event, result)


def caseid_route10(self):
    get_datachecklist("Route10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.config_display_route_close(self, "Route10", event, result)


def caseid_route11(self):
    get_datachecklist("Route11")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route11", event, result, var_v3.route_time_input, var_v3.route_time_label,
                                    "", var_v3.check_route_time, "0", "1", "Thời gian", "_LoTrinh_CauHinhHienThiLoTrinh_ThoiGian.png")


def caseid_route12(self):
    get_datachecklist("Route12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route12", event, result, var_v3.route_kmgps_input, var_v3.route_kmgps_label,
                                    "", var_v3.check_kmgps, "0", "1", "Km GPS", "_LoTrinh_CauHinhHienThiLoTrinh_KmGPS.png")

def caseid_route13(self):
    get_datachecklist("Route13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route13", event, result, var_v3.route_door_input, var_v3.route_door_label,
                                    "", var_v3.check_door, "0", "1", "Cửa", "_LoTrinh_CauHinhHienThiLoTrinh_Cua.png")

def caseid_route14(self):
    get_datachecklist("Route14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route14", event, result, var_v3.route_concrete_input, var_v3.route_concrete_label,
                                    "", var_v3.check_concrete, "0", "1", "Bê tông", "_LoTrinh_CauHinhHienThiLoTrinh_BeTong.png")


def caseid_route15(self):
    get_datachecklist("Route15")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route15", event, result, var_v3.route_adress_input, var_v3.route_adress_label,
                                    "", var_v3.check_adress, "0", "1", "", "_LoTrinh_CauHinhHienThiLoTrinh_DiaChi.png")


def caseid_route16(self):
    get_datachecklist("Route16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route16", event, result, var_v3.route_speed_input, var_v3.route_speed_label,
                                    "", var_v3.check_speed, "0", "1", "V Gps", "_LoTrinh_CauHinhHienThiLoTrinh_VanToc.png")


def caseid_route17(self):
    get_datachecklist("Route17")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route17", event, result, var_v3.route_sound_input, var_v3.route_sound_label,
                                    "", var_v3.check_sound, "0", "1", "Âm thanh", "_LoTrinh_CauHinhHienThiLoTrinh_AmThanh.png")


def caseid_route18(self):
    get_datachecklist("Route18")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route18", event, result, var_v3.route_machine_input, var_v3.route_machine_label,
                                    "", var_v3.check_machine, "0", "1", "Máy", "_LoTrinh_CauHinhHienThiLoTrinh_May.png")

def caseid_route19(self):
    get_datachecklist("Route19")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route19", event, result, var_v3.route_fuel_input, var_v3.route_fuel_label,
                                    "", var_v3.check_fuel, "0", "1", "Nhiên liệu", "_LoTrinh_CauHinhHienThiLoTrinh_NhienLieu.png")


def caseid_route20(self):
    get_datachecklist("Route20")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route20", event, result, var_v3.route_vco_input, var_v3.route_vco_label,
                                    "", var_v3.check_vco, "0", "1", "V Cơ", "_LoTrinh_CauHinhHienThiLoTrinh_VanTocCo.png")


def caseid_route21(self):
    get_datachecklist("Route21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route21", event, result, var_v3.route_coordinates_input, var_v3.route_coordinates_label,
                                    "", var_v3.check_coordinates, "0", "1", "Tọa độ", "_LoTrinh_CauHinhHienThiLoTrinh_ToaDo.png")


def caseid_route22(self):
    get_datachecklist("Route22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route22", event, result, var_v3.route_ari_conditional_input, var_v3.route_ari_conditional_label,
                                    "", var_v3.check_ari_conditional, "0", "1", "Điều hòa", "_LoTrinh_CauHinhHienThiLoTrinh_DieuHoa.png")


def caseid_route23(self):
    get_datachecklist("Route23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route23", event, result, var_v3.route_temperature_input, var_v3.route_temperature_label,
                                    "", var_v3.check_temperature, "0", "1", "Nhiệt độ", "_LoTrinh_CauHinhHienThiLoTrinh_NhietDo.png")


def caseid_route24(self):
    get_datachecklist("Route24")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route24", event, result, var_v3.route_time_stop_input, var_v3.route_time_stop_label,
                                    "", var_v3.check_time_stop, "0", "2", "Tổng thời gian dừng đỗ:", "_LoTrinh_CauHinhHienThiLoTrinh_TongThoiGianDungDo.png")


def caseid_route25(self):
    get_datachecklist("Route25")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route25", event, result, var_v3.route_summary_time_on_the_machine_input, var_v3.route_summary_time_on_the_machine_label,
                                    "", var_v3.check_summary_time_on_the_machine, "0", "2", "Tổng thời gian bật máy:", "_LoTrinh_CauHinhHienThiLoTrinh_TongThoiGianBatMay.png")


def caseid_route26(self):
    get_datachecklist("Route26")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route26", event, result, var_v3.route_total_distance_input, var_v3.route_total_distance_label,
                                    "", var_v3.check_total_distance1, "0", "2", "Tổng km di chuyển:", "_LoTrinh_CauHinhHienThiLoTrinh_TongQuangDuong.png")


def caseid_route27(self):
    get_datachecklist("Route27")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route27", event, result, var_v3.route_adress_input1, var_v3.route_adress_labe1l,
                                    var_v3.icon_arrow, var_v3.check_total_adress1, "1", "3", "Địa chỉ:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_DiaChi.png")


def caseid_route28(self):
    get_datachecklist("Route28")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route28", event, result, var_v3.route_vlimit_input3, var_v3.route_vlilit_label3,
                                    var_v3.icon_arrow, var_v3.check_vlimit3, "1", "3", "Vận tốc giới hạn:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_VGioiHan.png")


def caseid_route29(self):
    get_datachecklist("Route29")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route29", event, result, var_v3.route_machine_input3, var_v3.route_machine_label3,
                                    var_v3.icon_arrow, var_v3.check_machine3, "1", "3", "Máy:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_May.png")


def caseid_route30(self):
    get_datachecklist("Route30")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route30", event, result, var_v3.route_liscense_plate_input3, var_v3.route_liscense_plate_label3,
                                    var_v3.icon_arrow, var_v3.check_liscense_plate3, "1", "3", "Giấy phép lái xe:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_GiayPhepLaiXe.png")


def caseid_route31(self):
    get_datachecklist("Route31")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route31", event, result, var_v3.route_time_input3, var_v3.route_time_label3,
                                    var_v3.icon_arrow, var_v3.check_time3, "1", "3", "Thời gian:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_ThoiGian.png")



def caseid_route32(self):
    get_datachecklist("Route32")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route32", event, result, var_v3.route_speed_input3, var_v3.route_speed_label3,
                                    var_v3.icon_arrow, var_v3.check_speed3, "1", "3", "Vận tốc:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_VanToc.png")


def caseid_route33(self):
    get_datachecklist("Route33")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route33", event, result, var_v3.route_door_input3, var_v3.route_door_label3,
                                    var_v3.icon_arrow, var_v3.check_door3, "1", "3", "Cửa:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_Cua.png")


def caseid_route34(self):
    get_datachecklist("Route34")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route34", event, result, var_v3.route_kmgps_input3, var_v3.route_kmgps_label3,
                                    var_v3.icon_arrow, var_v3.check_kmgps3, "1", "3", "Km GPS:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_KmGps.png")

def caseid_route35(self):
    get_datachecklist("Route35")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route35", event, result, var_v3.route_coordinates_input3, var_v3.route_coordinates_label3,
                                    var_v3.icon_arrow, var_v3.check_coordinates3, "1", "3", "Tọa độ:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_ToaDo.png")


def caseid_route36(self):
    get_datachecklist("Route36")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route36", event, result, var_v3.route_drive_input3, var_v3.route_drive_label3,
                                    var_v3.icon_arrow, var_v3.check_drive3, "1", "3", "Lái xe:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_LaiXe.png")


def caseid_route37(self):
    get_datachecklist("Route37")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route37", event, result, var_v3.route_ari_conditional_input3, var_v3.route_ari_conditional_label3,
                                    var_v3.icon_arrow, var_v3.check_ari_conditional3, "1", "3", "Điều hòa:", "_LoTrinh_CauHinhHienThiLoTrinh_IconMuiTen_DieuHoa.png")



def caseid_route38(self):
    get_datachecklist("Route38")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route38", event, result, var_v3.route_adress_input4, var_v3.route_adress_label4,
                                    var_v3.icon_stop, var_v3.check_adress4, "2", "4", "Địa chỉ:", "_LoTrinh_CauHinhHienThiLoTrinh_IconDungDo_DiaChi.png")


def caseid_route39(self):
    get_datachecklist("Route39")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route39", event, result, var_v3.route_minute_stop_on_the_machine_input4, var_v3.route_minute_stop_on_the_machine_label4,
                                    var_v3.icon_stop, var_v3.check_minute_stop_on_the_machine4, "2", "4", "Số phút dừng đỗ bật máy:", "_LoTrinh_CauHinhHienThiLoTrinh_IconDungDo_SoPhutDungDoBatMay.png")


def caseid_route40(self):
    get_datachecklist("Route40")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route40", event, result, var_v3.route_time_input4, var_v3.route_time_label4,
                                    var_v3.icon_stop, var_v3.check_time4, "2", "4", "Thời gian:", "_LoTrinh_CauHinhHienThiLoTrinh_IconDungDo_ThoiGian.png")


def caseid_route41(self):
    get_datachecklist("Route41")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route41", event, result, var_v3.route_minute_stop_off_the_machine_input4, var_v3.route_minute_stop_off_the_machine_label4,
                                    var_v3.icon_stop, var_v3.check_minute_stop_off_the_machine4, "2", "4", "Số phút dừng đỗ tắt máy:", "_LoTrinh_CauHinhHienThiLoTrinh_IconDungDo_SoPhutDungDoTatMay.png")


def caseid_route42(self):
    get_datachecklist("Route42")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route42", event, result, var_v3.route_minute_stop_input4, var_v3.route_minute_stop_label4,
                                    var_v3.icon_stop, var_v3.check_minute_stop4, "2", "4", "Số phút dừng đỗ:", "_LoTrinh_CauHinhHienThiLoTrinh_IconDungDo_SoPhutDungDo.png")


def caseid_route43(self):
    get_datachecklist("Route43")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_checkbox(self, "Route43", event, result, var_v3.route_coordinates_input4, var_v3.route_coordinates_label4,
                                    var_v3.icon_stop, var_v3.check_coordinates_stop4, "2", "4", "Tọa độ:", "_LoTrinh_CauHinhHienThiLoTrinh_IconDungDo_ToaDo.png")


def caseid_route44(self):
    get_datachecklist("Route44")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.config_route_aggregation(self, "Route44", event, result)



def caseid_route45(self):
    get_datachecklist("Route45")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.config_route_aggregation_close(self, "Route45", event, result)



def caseid_route46(self):
    get_datachecklist("Route46")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.config_route_aggregation_checkbox(self, "Route46", event, result,
                                                       False, "_LoTrinh_CauHinhGopDungDo_BatTachMayKhiDung.png")

def caseid_route47(self):
    get_datachecklist("Route47")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.config_route_aggregation_checkbox(self, "Route47", event, result,
                                                       True, "_LoTrinh_CauHinhGopDungDo_TatTachMayKhiDung.png")

def caseid_route48(self):
    get_datachecklist("Route48")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.print_route(self, "Route48", event, result)


def caseid_route49(self):
    get_datachecklist("Route49")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.route_export_excel(self, "Route49", event, result)


def caseid_route50(self):
    get_datachecklist("Route50")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.create_location(self, "Route50", event, result)


def caseid_route51(self):
    get_datachecklist("Route51")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.create_location_close(self, "Route51", event, result)


def caseid_route52(self):
    get_datachecklist("Route52")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.see_route_route(self, "Route52", event, result)


def caseid_route53(self):
    get_datachecklist("Route53")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    route.left_popup.see_route_route_close(self, "Route53", event, result)



def caseid_admin01(self):
    get_datachecklist("Admin01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.list_company(self, "Admin01", event, result)


def caseid_admin02(self):
    get_datachecklist("Admin02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.list_company_search(self, "Admin02", event, result, "Mã XN", "950", False,
                                                              var_v3.check_xn, "950", "_DanhSachCongTy_TimKiem_MaXn.png")


def caseid_admin03(self):
    get_datachecklist("Admin03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.list_company_search(self, "Admin03", event, result, "Tên công ty", "Công ty Bình Anh Test", True,
                                                              var_v3.check_name_company, "Công ty Bình Anh Test", "_DanhSachCongTy_TimKiem_TenCongTy.png")


def caseid_admin04(self):
    get_datachecklist("Admin04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.list_company_search(self, "Admin04", event, result, "NVKD", "MT-Trần Quốc Đường", True,
                                                              var_v3.check_name_nvkd, "MT-Trần Quốc Đường", "_DanhSachCongTy_TimKiem_TenNVKD.png")


def caseid_admin05(self):
    get_datachecklist("Admin05")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.type_company(self, "Admin05", event, result, "Đại lý", "Đại lý Auto Track", True,
                                                              var_v3.check_name_company, "Đại lý Auto Track", "_DanhSachCongTy_TimKiem_DaiLy.png")


def caseid_admin06(self):
    get_datachecklist("Admin06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.type_company(self, "Admin06", event, result, "Công ty khách hàng", "Công ty cổ phần ngôi sao Quốc Tế VTP", True,
                                                              var_v3.check_name_company, "Công ty cổ phần ngôi sao Quốc Tế VTP", "_DanhSachCongTy_TimKiem_CongTyKhachHang.png")


def caseid_admin07(self):
    get_datachecklist("Admin07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.type_company(self, "Admin07", event, result, "Công ty khách lẻ", "1012 - Khách Lẻ đại lý Hoàng Gia - Viên Phát 0963.070.683", True,
                                                              var_v3.check_name_company, "1012 - Khách Lẻ đại lý Hoàng Gia - Viên Phát 0963.070.683", "_DanhSachCongTy_TimKiem_CongTyKhachLe.png")


def caseid_admin08(self):
    get_datachecklist("Admin08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.select_list_company(self, "Admin08", event, result, var_v3.select_agency,
                                                              var_v3.select_agency_all, var_v3.data['administration']['select_agency'],
                                                              True, True, var_v3.check_name_company,
                                                              var_v3.data['administration']['select_agency'], "_DanhSachCongTy_ChonDaiLy.png")

def caseid_admin09(self):
    get_datachecklist("Admin09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.select_list_company(self, "Admin09", event, result, var_v3.select_province,
                                                              var_v3.select_province1, var_v3.data['administration']['province'],
                                                              True, True, var_v3.check_name_company,
                                                              var_v3.data['administration']['province'], "_DanhSachCongTy_ChonTinhThanh.png")


def caseid_admin10(self):
    get_datachecklist("Admin10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.select_list_company(self, "Admin10", event, result, var_v3.select_system,
                                                              var_v3.select_system1, var_v3.data['administration']['system'],
                                                              True, True, var_v3.check_name_company,
                                                              var_v3.data['administration']['system'] , "_DanhSachCongTy_ChonHeThong.png")

def caseid_admin11(self):
    get_datachecklist("Admin11")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.select_list_company(self, "Admin11", event, result, var_v3.select_system,
                                                              var_v3.select_system1, var_v3.data['administration']['findexactly'],
                                                              False, True, var_v3.check_name_company,
                                                              var_v3.data['administration']['findexactly'], "_DanhSachCongTy_TimChinhXac.png")


def caseid_admin12(self):
    get_datachecklist("Admin12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.select_list_company(self, "Admin12", event, result, var_v3.select_system,
                                                              var_v3.select_system1, var_v3.data['administration']['child'],
                                                              True, False, var_v3.check_name_company,
                                                              var_v3.data['administration']['child'], "_DanhSachCongTy_CongTyKhachLeChoPhepThemCon.png")


def caseid_admin13(self):
    get_datachecklist("Admin13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.route_export_dowload(self, "Admin13", event, result, var_v3.export_excel,
                                                              "danhsachcongty.xlsx", "_DanhSachCongTy_XuatExcel.png")


def caseid_admin14(self):
    get_datachecklist("Admin14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.route_export_dowload(self, "Admin14", event, result, var_v3.export_pdf,
                                                              "danhsachcongty.pdf", "_DanhSachCongTy_XuatPdf.png")


def caseid_admin15(self):
    pass
    # get_datachecklist("Admin15")
    # event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    # administration.company_administration.list_company_print(self, "Admin15", event, result)


def caseid_admin16(self):
    get_datachecklist("Admin16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.hide_display_column(self, "Admin16", event, result)


def caseid_admin17(self):
    get_datachecklist("Admin17")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.list_company_goto(self, "Admin17", event, result)


def caseid_admin18(self):
    get_datachecklist("Admin18")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.create_agency(self, "Admin18", event, result)


def caseid_admin19(self):
    get_datachecklist("Admin19")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.create_customer_company(self, "Admin19", event, result)


def caseid_admin20(self):
    get_datachecklist("Admin20")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.create_retail_customer(self, "Admin20", event, result)


def caseid_admin21(self):
    get_datachecklist("Admin21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.company_administration.remove_company_to_agency(self, "Admin21", event, result)


def caseid_admin22(self):
    get_datachecklist("Admin22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle(self, "Admin22", event, result)


def caseid_admin23(self):
    get_datachecklist("Admin23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_search(self, "Admin23", event, result)


def caseid_admin24(self):
    get_datachecklist("Admin24")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_select_group(self, "Admin24", event, result)


def caseid_admin25(self):
    get_datachecklist("Admin25")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_select(self, "Admin25", event, result, var_v3.list_vehicle_select_agency,
                                                              var_v3.list_vehicle_select_agency2, var_v3.check_select_agency,
                                                              "Chọn đại lý", "_DanhSachPhuongTien_ChonDaiLy.png")

def caseid_admin26(self):
    get_datachecklist("Admin26")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_select(self, "Admin26", event, result, var_v3.list_vehicle_select_province,
                                                              var_v3.select1, var_v3.angiang,
                                                              "An Giang", "_DanhSachPhuongTien_ChonTinhThanh.png")


def caseid_admin27(self):
    get_datachecklist("Admin27")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_select(self, "Admin27", event, result, var_v3.select_type_of_transport,
                                                              var_v3.select1, var_v3.xekhachcodinh,
                                                              "Xe khách tuyến cố định", "_DanhSachPhuongTien_ChonLoaiHinhVanTai.png")

def caseid_admin28(self):
    get_datachecklist("Admin28")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_select(self, "Admin28", event, result, var_v3.list_vehicle_fee_select,
                                                              var_v3.select1a, var_v3.vehicle_day_fee, "Phương tiện sắp đến hạn thu phí", "_DanhSachPhuongTien_TrangThaiPhi.png")

def caseid_admin29(self):
    get_datachecklist("Admin29")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_time_not_signal(self, "Admin29", event, result)


def caseid_admin30(self):
    get_datachecklist("Admin30")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin30", event, result, var_v3.new_vehicle_input, var_v3.new_vehicle_label,
                                                                "1", var_v3.check_list_vehicle_company, "", "_DanhSachPhuongTien_PhuongTienLapMoi.png")

def caseid_admin31(self):
    get_datachecklist("Admin31")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin31", event, result, var_v3.activity_vehicle_input, var_v3.activity_vehicle_label,
                                                                "3", var_v3.check_list_vehicle_status, "Bình thường", "_DanhSachPhuongTien_PhuongTienHoatDong.png")

def caseid_admin32(self):
    get_datachecklist("Admin32")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin32", event, result, var_v3.vehicle_forwarded_input, var_v3.vehicle_forwarded_label,
                                                                "1", var_v3.check_list_vehicle_forwarded, "", "_DanhSachPhuongTien_PhuongTienDaTichtruyen.png")

def caseid_admin33(self):
    get_datachecklist("Admin33")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin33", event, result, var_v3.vehicle_not_forward_input, var_v3.vehicle_not_forward_label,
                                                                "2", var_v3.check_list_vehicle_forwarded, "", "_DanhSachPhuongTien_PhuongTienChuaTichtruyen.png")

def caseid_admin34(self):
    get_datachecklist("Admin34")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin34", event, result, var_v3.change_vehicle_input, var_v3.change_vehicle_label,
                                                                "1", var_v3.check_list_vehicle_company, "", "_DanhSachPhuongTien_PhuongTienDoiBien.png")


def caseid_admin35(self):
    get_datachecklist("Admin35")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin35", event, result, var_v3.Vehicle_not_approved_input, var_v3.Vehicle_not_approved_label,
                                                                "1", var_v3.check_list_vehicle_company, "", "_DanhSachPhuongTien_PhuongTienChuaDuyet.png")

def caseid_admin36(self):
    get_datachecklist("Admin36")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin36", event, result, var_v3.vehicle_unreported_input, var_v3.vehicle_unreported_label,
                                                                "1", var_v3.check_list_vehicle_company, "", "_DanhSachPhuongTien_PhuongTienChuaKhaiBao.png")

def caseid_admin37(self):
    get_datachecklist("Admin37")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin37", event, result, var_v3.not_sim_input, var_v3.not_sim_label,
                                                                "3", var_v3.check_list_vehicle_sim, "", "_DanhSachPhuongTien_PhuongTienThieuSim.png")

def caseid_admin38(self):
    get_datachecklist("Admin38")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin38", event, result, var_v3.vehicle_lack_driver_input, var_v3.vehicle_lack_driver_label,
                                                                "3", var_v3.check_list_vehicle_driver, "", "_DanhSachPhuongTien_PhuongTienThieuLaiXe.png")


def caseid_admin39(self):
    get_datachecklist("Admin39")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin39", event, result, var_v3.vehicle_lock_view_input, var_v3.vehicle_lock_view_label,
                                                                "3", var_v3.check_list_vehicle_status, "Khóa view", "_DanhSachPhuongTien_PhuongTienKhoaView.png")


def caseid_admin40(self):
    get_datachecklist("Admin40")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin40", event, result, var_v3.vehicle_lock_input, var_v3.vehicle_lock_label,
                                                                "3", var_v3.check_list_vehicle_status, "Khóa view", "_DanhSachPhuongTien_PhuongTienKhoa.png")


def caseid_admin41(self):
    get_datachecklist("Admin41")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin41", event, result, var_v3.vehicle_delete_input, var_v3.vehicle_delete_label,
                                                                "1", var_v3.check_list_vehicle_delete, "", "_DanhSachPhuongTien_PhuongTienXoa.png")

def caseid_admin42(self):
    get_datachecklist("Admin42")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_checkbox(self, "Admin42", event, result, var_v3.vehicle_hide_input, var_v3.vehicle_hide_label,
                                                                "1", var_v3.check_list_vehicle_hide, "", "_DanhSachPhuongTien_PhuongTienAn.png")


def caseid_admin43(self):
    get_datachecklist("Admin43")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_link_search(self, "Admin43", event, result, var_v3.search_company,
                                                                var_v3.title_page, "DANH SÁCH CÔNG TY", "_DanhSachPhuongTien_TraCuuCongTy.png")


def caseid_admin44(self):
    get_datachecklist("Admin44")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_link_search(self, "Admin44", event, result, var_v3.search_user,
                                                                var_v3.title_page, "DANH SÁCH NGƯỜI DÙNG", "_DanhSachPhuongTien_TraCuuNguoiDung.png")


def caseid_admin45(self):
    get_datachecklist("Admin45")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_change_icon(self, "Admin45", event, result)


def caseid_admin46(self):
    get_datachecklist("Admin46")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.update_to_excel(self, "Admin46", event, result)


def caseid_admin47(self):
    get_datachecklist("Admin47")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_export_file(self, "Admin47", event, result, var_v3.export_excel,
                                                                   "danhsachxe_xuat_excel.xlsx", "_DanhSachXe_XuatExcel.png")

def caseid_admin48(self):
    get_datachecklist("Admin48")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_export_file(self, "Admin48", event, result, var_v3.export_pdf,
                                                                   "danhsachxe_xuat_pdf.pdf", "_DanhSachXe_XuatPdf.png")

def caseid_admin49(self):
    pass
    # get_datachecklist("Admin49")
    # event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    # administration.vehicle_administration.print_list_vehicle(self, "Admin49", event, result)



def caseid_admin50(self):
    get_datachecklist("Admin50")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_hide(self, "Admin50", event, result)


def caseid_admin51(self):
    get_datachecklist("Admin51")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_lock(self, "Admin51", event, result, var_v3.lock_vehicle,
                                                            var_v3.data['administration']['reason_lock'],
                                                            "rgba(203, 0, 0, 1)", "_DanhSachPhuongTien_Khoa1PhuongTien.png")

def caseid_admin52(self):
    get_datachecklist("Admin52")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_lock(self, "Admin52", event, result, var_v3.un_lock_vehicle,
                                                            var_v3.data['administration']['reason_un_lock'],
                                                            "rgba(9, 89, 160, 1)", "_DanhSachPhuongTien_MoKhoa1PhuongTien.png")

def caseid_admin53(self):
    get_datachecklist("Admin53")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_delete(self, "Admin53", event, result)


def caseid_admin54(self):
    get_datachecklist("Admin54")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_goto(self, "Admin54", event, result)


def caseid_admin55(self):
    get_datachecklist("Admin55")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_user(self, "Admin55", event, result)


def caseid_admin56(self):
    pass
    # get_datachecklist("Admin56")
    # event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    # administration.vehicle_administration.list_vehicle_assign(self, "Admin56", event, result)


def caseid_admin57(self):
    get_datachecklist("Admin57")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_hide_vehicle(self, "Admin57", event, result)


def caseid_admin58(self):
    get_datachecklist("Admin58")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.list_vehicle_un_hide_vehicle(self, "Admin58", event, result)


def caseid_admin59(self):
    get_datachecklist("Admin59")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_group_management(self, "Admin59", event, result)


def caseid_admin60(self):
    get_datachecklist("Admin60")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_group_management_search(self, "Admin60", event, result, var_v3.list_group_vehicle_search,
                                                                          var_v3.data['administration']['group_vehicle'], var_v3.list_group_vehicle_search1,
                                                                          "Nhóm test tìm kiếm (5 xe)", "_QuanTriNhomPhuongTien_TimNhomPhuongTien.png",
                                                                          var_v3.list_group_vehicle_search_icondetele)

def caseid_admin61(self):
    get_datachecklist("Admin61")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.add_new_group1(self, "Admin61", event, result)


def caseid_admin62(self):
    get_datachecklist("Admin62")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.add_new_groupn(self, "Admin62", event, result)


def caseid_admin63(self):
    get_datachecklist("Admin63")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.remane_group(self, "Admin63", event, result)


def caseid_admin64(self):
    get_datachecklist("Admin64")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.delete_group(self, "Admin64", event, result)


def caseid_admin65(self):
    get_datachecklist("Admin65")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.search_list_vehicle(self, "Admin65", event, result)


def caseid_admin66(self):
    get_datachecklist("Admin66")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_group_vehicle(self, "Admin66", event, result,
                                                               var_v3.list_vehicle1_input, var_v3.list_vehicle2_input,
                                                               "_QuanTriNhomPhuongTien_Gan1Xe.png")


def caseid_admin67(self):
    get_datachecklist("Admin67")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_group_vehicle(self, "Admin67", event, result,
                                                               var_v3.list_vehicle1_all_input, var_v3.list_vehicle2_all_input,
                                                               "_QuanTriNhomPhuongTien_GanTatCaXe.png")


def caseid_admin68(self):
    get_datachecklist("Admin68")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.search_list_user(self, "Admin68", event, result)


def caseid_admin69(self):
    get_datachecklist("Admin69")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_group_vehicle1(self, "Admin69", event, result, var_v3.list_user1_input,
                                                               var_v3.list_user1_label, "_QuanTriNhomPhuongTien_Gan1NguoiDung.png")

def caseid_admin70(self):
    get_datachecklist("Admin70")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_group_vehicle1(self, "Admin70", event, result, var_v3.list_user_all_input,
                                                               var_v3.list_user_all_label, "_QuanTriNhomPhuongTien_GanTatCaNguoiDung.png")


def caseid_admin71(self):
    get_datachecklist("Admin71")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_group_management_cancel(self, "Admin71", event, result)


def caseid_admin72(self):
    get_datachecklist("Admin72")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.mark_special_groups(self, "Admin72", event, result)


def caseid_admin73(self):
    get_datachecklist("Admin73")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_belong_group(self, "Admin73", event, result)



def caseid_admin74(self):
    get_datachecklist("Admin74")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_group_permission(self, "Admin74", event, result)


def caseid_admin75(self):
    get_datachecklist("Admin75")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_group_permission_search(self, "Admin75", event, result, var_v3.list_user2_label,
                                                                          var_v3.list_user_search_input, "_PhanQuyenNhomPhuongTien_TimKiemDanhSachNguoiDung.png",
                                                                          var_v3.list_user_search_iconx)

def caseid_admin76(self):
    get_datachecklist("Admin76")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_group_permission_search(self, "Admin76", event, result, var_v3.list_group_vehicle2_label,
                                                                          var_v3.list_group_vehicle_search_input, "_PhanQuyenNhomPhuongTien_TimKiemChonNhomChoNguioiDung.png",
                                                                          var_v3.list_group_vehicle_search_iconx)


def caseid_admin77(self):
    get_datachecklist("Admin77")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_group_permission_search(self, "Admin77", event, result, var_v3.list_group_assigned_label,
                                                                          var_v3.list_group_assigned_input, "_PhanQuyenNhomPhuongTien_TimKiemNhomDaGanChoNguoiDung.png",
                                                                          var_v3.list_group_assigned_iconx)



def caseid_admin78(self):
    get_datachecklist("Admin78")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_group_vehicle_to_user(self, "Admin78", event, result,
                                                                       var_v3.permission1_input, var_v3.permission1_input,
                                                                       var_v3.permission2_input, var_v3.permission2_input,
                                                                       "_PhanQuyenNhomPhuongTien_Gan1NhomXe.png")



def caseid_admin79(self):
    get_datachecklist("Admin79")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_group_vehicle_to_user(self, "Admin79", event, result,
                                                                       var_v3.permission1_all_input, var_v3.permission1_all_label,
                                                                       var_v3.permission2_all_input, var_v3.permission2_all_label,
                                                                       "_PhanQuyenNhomPhuongTien_GanTatCaNhomXe.png")


def caseid_admin80(self):
    get_datachecklist("Admin80")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_group_permission_cancel(self, "Admin80", event, result)



def caseid_admin81(self):
    get_datachecklist("Admin81")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.permission_mark_special_groups(self, "Admin81", event, result)



def caseid_admin82(self):
    get_datachecklist("Admin82")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.permission_search_group(self, "Admin82", event, result)


def caseid_admin83(self):
    get_datachecklist("Admin83")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.permission_search_group_select_group(self, "Admin83", event, result)



def caseid_admin84(self):
    get_datachecklist("Admin84")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.permission_search_group_dowload(self, "Admin84", event, result, var_v3.export_excel,
                                                                        "danhmucloaiphuongtien_xuat_excel.xlsx", "_TimKiemNhom_XuatExcel.png")


def caseid_admin85(self):
    get_datachecklist("Admin85")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.permission_search_group_dowload(self, "Admin85", event, result, var_v3.export_pdf1,
                                                                        "danhmucloaiphuongtien_xuat_pdf.pdf", "_TimKiemNhom_XuatPdf.png")

def caseid_admin86(self):
    pass




def caseid_admin87(self):
    get_datachecklist("Admin87")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty(self, "Admin87", event, result)


def caseid_admin88(self):
    get_datachecklist("Admin88")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_search(self, "Admin88", event, result)


def caseid_admin89(self):
    get_datachecklist("Admin89")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_add_new(self, "Admin89", event, result)


def caseid_admin90(self):
    get_datachecklist("Admin90")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_delete(self, "Admin90", event, result)


def caseid_admin91(self):
    get_datachecklist("Admin91")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_edit(self, "Admin91", event, result)


def caseid_admin92(self):
    get_datachecklist("Admin92")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_dowload_excel(self, "Admin92", event, result)


def caseid_admin93(self):
    get_datachecklist("Admin93")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_upload_excel(self, "Admin93", event, result)


def caseid_admin94(self):
    get_datachecklist("Admin94")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_dowload(self, "Admin94", event, result, var_v3.export_excel,
                                                                        "danhmucloaiphuongtien_xuat_excel.xlsx", "_DanhMucLoaiPhuongTien_XuatExcel.png")


def caseid_admin95(self):
    get_datachecklist("Admin95")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_dowload(self, "Admin95", event, result, var_v3.export_pdf1,
                                                                        "danhmucloaiphuongtien_xuat_pdf.pdf", "_DanhMucLoaiPhuongTien_XuatPdf.png")


def caseid_admin96(self):
    pass



def caseid_admin97(self):
    get_datachecklist("Admin97")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.vehicle_type_categoty_hide(self, "Admin97", event, result)


def caseid_admin98(self):
    get_datachecklist("Admin98")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_type_vehicle(self, "Admin98", event, result)


def caseid_admin99(self):
    get_datachecklist("Admin99")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_type_vehicle_search(self, "Admin99", event, result, var_v3.assign_type_vehicle_search1,
                                                                     var_v3.assign_type_vehicle_search_select1, var_v3.check_assign_type_vehicle_search1,
                                                                      "Chọn nhóm phương tiện", "_GanLoaiPhuongTien_TimKiemNhomPhuongTien.png")

def caseid_admin100(self):
    get_datachecklist("Admin100")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_type_vehicle_search1(self, "Admin100", event, result, var_v3.assign_type_vehicle_search2a,
                                                                     var_v3.assign_type_vehicle_search_select2, var_v3.assign_type_vehicle_search2,
                                                                     "_GanLoaiPhuongTien_TimKiemPhuongTien.png")

def caseid_admin101(self):
    get_datachecklist("Admin101")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_type_vehicle_search1(self, "Admin101", event, result, var_v3.assign_type_vehicle_search3,
                                                                     var_v3.assign_type_vehicle_search_select2, var_v3.assign_type_vehicle_search3a,
                                                                     "_GanLoaiPhuongTien_TimKiemLoaiPhuongTien.png")

def caseid_admin102(self):
    get_datachecklist("Admin102")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.icon_assign_type_vehicle(self, "Admin102", event, result)


def caseid_admin103(self):
    get_datachecklist("Admin103")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.icon_delete_assign_type_vehicle(self, "Admin103", event, result)



def caseid_admin104(self):
    get_datachecklist("Admin104")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_type_vehicle_dowload(self, "Admin104", event, result, var_v3.export_excel,
                                                                        "ganloaiphuongtien_xuatexcel.xlsx", "_GanLoaiPhuongTien_XuatExcel.png")


def caseid_admin105(self):
    get_datachecklist("Admin105")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_type_vehicle_dowload(self, "Admin105", event, result, var_v3.export_pdf1,
                                                                        "ganloaiphuongtien_xuatpdf.pdf", "_GanLoaiPhuongTien__XuatPdf.png")


def caseid_admin106(self):
    pass



def caseid_admin107(self):
    get_datachecklist("Admin107")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_administration.assign_type_vehicle_hide(self, "Admin107", event, result)




def caseid_admin108(self):
    get_datachecklist("Admin108")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user(self, "Admin108", event, result)



def caseid_admin109(self):
    get_datachecklist("Admin109")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin109", event, result, "Tên đăng nhập", "", "",
                                                      var_v3.data['administration']['list_user_namelogin'], var_v3.list_field3, "1",
                                                      var_v3.data['administration']['list_user_namelogin'], "_DanhSachNguoiDung_TimKiemTenDangNhap.png")

def caseid_admin110(self):
    get_datachecklist("Admin110")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin110", event, result, "Họ tên", "", "",
                                                      var_v3.data['administration']['list_user_lastname'], var_v3.list_field4, "1",
                                                      var_v3.data['administration']['list_user_lastname'], "_DanhSachNguoiDung_TimKiemHoTen.png")


def caseid_admin111(self):
    get_datachecklist("Admin111")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin111", event, result, "Biển kiểm soát", "", "",
                                                      var_v3.data['administration']['list_user_liscenseplate'], var_v3.list_field3, "2",
                                                      "None", "_DanhSachNguoiDung_TimKiemBienKiemSoat.png")


def caseid_admin112(self):
    get_datachecklist("Admin112")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin112", event, result, "Tên đăng nhập", var_v3.type_account, var_v3.type_account_administration,
                                                      var_v3.data['administration']['list_user_administration'], var_v3.list_field3, "1",
                                                      var_v3.data['administration']['list_user_administration'], "_DanhSachNguoiDung_KieuTaiKhoan_QuanTri.png")

def caseid_admin113(self):
    get_datachecklist("Admin113")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin113", event, result, "Tên đăng nhập", var_v3.type_account, var_v3.type_account_normal,
                                                      var_v3.data['administration']['list_user_normal'], var_v3.list_field3, "1",
                                                      var_v3.data['administration']['list_user_normal'], "_DanhSachNguoiDung_KieuTaiKhoan_Binhthuong.png")


def caseid_admin114(self):
    get_datachecklist("Admin114")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin114", event, result, "Tên đăng nhập", var_v3.type_account, var_v3.type_account_driver,
                                                      var_v3.data['administration']['list_user_driver'], var_v3.list_field3, "1",
                                                      var_v3.data['administration']['list_user_driver'], "_DanhSachNguoiDung_KieuTaiKhoan_LaiXe.png")


def caseid_admin115(self):
    get_datachecklist("Admin115")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin115", event, result, "Tên đăng nhập", var_v3.type_status, var_v3.type_status_lock,
                                                      var_v3.data['administration']['list_user_lock'], var_v3.list_field3, "1",
                                                      var_v3.data['administration']['list_user_lock'], "_DanhSachNguoiDung_TrangThai_Khoa.png")


def caseid_admin116(self):
    get_datachecklist("Admin116")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin116", event, result, "Tên đăng nhập", var_v3.type_status, var_v3.type_status_un_lock,
                                                      var_v3.data['administration']['list_user_un_lock'], var_v3.list_field3, "1",
                                                      var_v3.data['administration']['list_user_un_lock'], "_DanhSachNguoiDung_TrangThai_MoKhoa.png")


def caseid_admin117(self):
    get_datachecklist("Admin117")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "Admin117", event, result, "Tên đăng nhập", var_v3.no_login, var_v3.no_login_30day,
                                                      var_v3.data['administration']['list_user_notlogin_30day'], var_v3.list_field3, "1",
                                                      var_v3.data['administration']['list_user_notlogin_30day'], "_DanhSachNguoiDung_KhongTruyCapTrong30Ngay.png")


def caseid_admin118(self):
    get_datachecklist("Admin118")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_dowload(self, "Admin118", event, result, var_v3.export_excel,
                                                                        "danhsachnguoidung_xuatexcel.xlsx", "_DanhSachNguoiDung_XuatExcel.png")


def caseid_admin119(self):
    get_datachecklist("Admin119")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_dowload(self, "Admin119", event, result, var_v3.export_pdf1,
                                                                        "danhsachnguoidung_xuatpdf.pdf", "_DanhSachNguoiDung__XuatPdf.png")


def caseid_admin120(self):
    pass



def caseid_admin121(self):
    get_datachecklist("Admin121")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_hide(self, "Admin121", event, result)


def caseid_admin122(self):
    get_datachecklist("Admin122")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_add_new(self, "Admin122", event, result)


def caseid_admin123(self):
    get_datachecklist("Admin123")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_delete(self, "Admin123", event, result)


def caseid_admin124(self):
    get_datachecklist("Admin124")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_edit(self, "Admin124", event, result)


def caseid_admin125(self):
    get_datachecklist("Admin125")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_assign_permission(self, "Admin125", event, result)


def caseid_admin126(self):
    get_datachecklist("Admin126")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_lock(self, "Admin126", event, result, var_v3.icon_lock,
                                                    var_v3.icon_un_lock, "_DanhSachNguoiDung_Khoa.png")


def caseid_admin127(self):
    get_datachecklist("Admin127")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_lock(self, "Admin127", event, result, var_v3.icon_un_lock,
                                                    var_v3.icon_lock, "_DanhSachNguoiDung_MoKhoa.png")

def caseid_admin128(self):
    get_datachecklist("Admin128")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_coppy_permission(self, "Admin128", event, result)


def caseid_admin129(self):
    get_datachecklist("Admin129")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_change_password(self, "Admin129", event, result)


def caseid_admin130(self):
    get_datachecklist("Admin130")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_unlock_login(self, "Admin130", event, result)


def caseid_admin131(self):
    get_datachecklist("Admin131")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_logout(self, "Admin131", event, result)


def caseid_admin132(self):
    get_datachecklist("Admin132")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.user_permission(self, "Admin132", event, result)


def caseid_admin133(self):
    get_datachecklist("Admin133")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.user_permission_chose_user(self, "Admin133", event, result)


def caseid_admin134(self):
    get_datachecklist("Admin134")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.user_permission_permission_1role(self, "Admin134", event, result)


def caseid_admin135(self):
    get_datachecklist("Admin135")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.user_permission_search(self, "Admin135", event, result)


def caseid_admin136(self):
    get_datachecklist("Admin136")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.chose_permission(self, "Admin136", event, result, True, True, False, True, True, True, True, True, True,
                                                      "_PhanQuyenNguoiDung_Chon1Quyen.png")


def caseid_admin137(self):
    get_datachecklist("Admin137")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.chose_permission(self, "Admin137", event, result, False, False, False, False, False, False, False, False, False,
                                                      "_PhanQuyenNguoiDung_ChonTatCaQuyen.png")


def caseid_admin138(self):
    get_datachecklist("Admin138")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.role_management(self, "Admin138", event, result)


def caseid_admin139(self):
    get_datachecklist("Admin139")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.role_management_search(self, "Admin139", event, result)


def caseid_admin140(self):
    get_datachecklist("Admin140")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.role_management_add_new(self, "Admin140", event, result)


def caseid_admin141(self):
    get_datachecklist("Admin141")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.role_management_delete(self, "Admin141", event, result)


def caseid_admin142(self):
    get_datachecklist("Admin142")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.role_management_edit(self, "Admin142", event, result)


def caseid_admin143(self):
    get_datachecklist("Admin143")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management(self, "Admin143", event, result)


def caseid_admin144(self):
    get_datachecklist("Admin144")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management_from_day_to_day(self, "Admin144", event, result)


def caseid_admin145(self):
    get_datachecklist("Admin145")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management_group(self, "Admin145", event, result)


def caseid_admin146(self):
    get_datachecklist("Admin146")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management_vehicle(self, "Admin146", event, result)


def caseid_admin147(self):
    get_datachecklist("Admin147")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management_type_warn(self, "Admin147", event, result, var_v3.warn_stop_on_conditonal, "1",
                                                           var_v3.field5b, "Cảnh báo dừng đỗ bật điều hòa (KPI)", "_DanhSachCanhBao_Chon1CanhBao.png")

def caseid_admin148(self):
    get_datachecklist("Admin148")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management_type_warn(self, "Admin148", event, result, var_v3.warn_all, "2",
                                                           var_v3.type_warn1, "Chọn Loại cảnh báo", "_DanhSachCanhBao_ChonTatCaCanhBao.png")


def caseid_admin149(self):
    get_datachecklist("Admin149")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management_status(self, "Admin149", event, result, var_v3.alert_management_not_see, "1",
                                                           var_v3.field9b, "Chưa xem", "_DanhSachCanhBao_TrangThai_ChuaXem.png")

def caseid_admin150(self):
    get_datachecklist("Admin150")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management_status(self, "Admin150", event, result, var_v3.alert_management_has_read, "2",
                                                           "", "", "_DanhSachCanhBao_TrangThai_DaDoc.png")


def caseid_admin151(self):
    get_datachecklist("Admin151")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.alert_management_status(self, "Admin151", event, result, var_v3.alert_management_has_handle, "2",
                                                           "", "", "_DanhSachCanhBao_TrangThai_DaXuLy.png")



def caseid_admin152(self):
    get_datachecklist("Admin152")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.history_warm_route(self, "Admin152", event, result)


def caseid_admin153(self):
    get_datachecklist("Admin153")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_user(self, "Admin153", event, result)


def caseid_admin154(self):
    get_datachecklist("Admin154")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_user_search(self, "Admin154", event, result, var_v3.config_warm_user_user,
                                                         var_v3.config_warm_user_truongvck2, var_v3.check_config_warm_user_user,
                                                        "truongvck2", "_CauHinhCanhBaoChoNguoiDung_timKiemNguoiDung.png")


def caseid_admin155(self):
    get_datachecklist("Admin155")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_user_search(self, "Admin155", event, result, var_v3.config_warm_user_warm,
                                                         var_v3.config_warm_lost_gps, var_v3.check_config_warm_lost_gps,
                                                        "Cảnh báo mất GPS", "_CauHinhCanhBaoChoNguoiDung_timKiemLoaiCanhBao.png")


def caseid_admin156(self):
    get_datachecklist("Admin156")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_user_add_new(self, "Admin156", event, result)



def caseid_admin157(self):
    get_datachecklist("Admin157")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_user_edit(self, "Admin157", event, result)



def caseid_admin158(self):
    get_datachecklist("Admin158")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_user_delete(self, "Admin158", event, result)


def caseid_admin159(self):
    get_datachecklist("Admin159")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_company(self, "Admin159", event, result)


def caseid_admin160(self):
    get_datachecklist("Admin160")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_company_search(self, "Admin160", event, result, "Cảnh báo bật động cơ")


def caseid_admin161(self):
    get_datachecklist("Admin161")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_company_add_new(self, "Admin161", event, result)


def caseid_admin162(self):
    get_datachecklist("Admin162")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_company_edit(self, "Admin162", event, result)


def caseid_admin163(self):
    get_datachecklist("Admin163")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.config_alert.config_warm_company_delete(self, "Admin163", event, result)



def caseid_admin164(self):
    get_datachecklist("Admin164")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver(self, "Admin164", event, result)


def caseid_admin165(self):
    get_datachecklist("Admin165")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_search(self, "Admin165", event, result, var_v3.data['administration']['listdriver_manv'], "Mã nhân viên",
                                                        var_v3.list_driver_search_manv, var_v3.data['administration']['listdriver_manv'], "_DanhSachLaiXe_TimKiemMaNV.png")

def caseid_admin166(self):
    get_datachecklist("Admin166")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_search(self, "Admin166", event, result, var_v3.data['administration']['listdriver_namenv'], "Tên nhân viên",
                                                        var_v3.list_driver_search_namenv, var_v3.data['administration']['listdriver_namenv'], "_DanhSachLaiXe_TimKiemTenNV.png")


def caseid_admin167(self):
    get_datachecklist("Admin167")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_search(self, "Admin167", event, result, var_v3.data['administration']['listdriver_vehicle'], "Phương tiện",
                                                        var_v3.list_driver_search_vehicle, var_v3.data['administration']['listdriver_vehicle'], "_DanhSachLaiXe_TimKiemPhuongTien.png")


def caseid_admin168(self):
    get_datachecklist("Admin168")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_search(self, "Admin168", event, result, var_v3.data['administration']['listdriver_ticket'], "Số thẻ",
                                                        var_v3.list_driver_search_ticket, var_v3.data['administration']['listdriver_ticket'], "_DanhSachLaiXe_TimKiemSoThe.png")


def caseid_admin169(self):
    get_datachecklist("Admin169")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_search(self, "Admin169", event, result, var_v3.data['administration']['listdriver_gplx'], "GPLX",
                                                        var_v3.list_driver_search_gplx, var_v3.data['administration']['listdriver_gplx'], "_DanhSachLaiXe_TimKiemGPLX.png")


def caseid_admin170(self):
    get_datachecklist("Admin170")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_dowload_excel(self, "Admin170", event, result)


def caseid_admin171(self):
    get_datachecklist("Admin171")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_upload_excel(self, "Admin171", event, result)


def caseid_admin172(self):
    get_datachecklist("Admin172")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_add_new(self, "Admin172", event, result)


def caseid_admin173(self):
    get_datachecklist("Admin173")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_edit(self, "Admin173", event, result)


def caseid_admin174(self):
    get_datachecklist("Admin174")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_lock(self, "Admin174", event, result, var_v3.list_driver_icon_lock,
                                                      "_DanhSachLaiXe_Khoa.png")


def caseid_admin175(self):
    get_datachecklist("Admin175")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_lock(self, "Admin175", event, result, var_v3.list_driver_icon_un_lock,
                                                      "_DanhSachLaiXe_MoKhoa.png")


def caseid_admin176(self):
    get_datachecklist("Admin176")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_delete(self, "Admin176", event, result)



def caseid_admin177(self):
    get_datachecklist("Admin177")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_dowload(self, "Admin177", event, result, var_v3.export_excel,
                                                                        "danhsachlaixe_xuatexcel.xlsx", "_DanhSachLaiXe_XuatExcel.png")


def caseid_admin178(self):
    get_datachecklist("Admin178")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_driver_dowload(self, "Admin178", event, result, var_v3.export_pdf1,
                                                                        "danhsachlaixe_xuatexcel.pdf", "_DanhSachLaiXe_XuatPDF.png")



def caseid_admin179(self):
    pass



def caseid_admin180(self):
    get_datachecklist("Admin180")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_user_hide(self, "Admin180", event, result)



def caseid_admin181(self):
    get_datachecklist("Admin181")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.list_user_history_driver(self, "Admin181", event, result)


def caseid_admin182(self):
    get_datachecklist("Admin182")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket(self, "Admin182", event, result)


def caseid_admin183(self):
    get_datachecklist("Admin183")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_search(self, "Admin183", event, result, var_v3.data['administration']['manage_ticketsearch'])


def caseid_admin184(self):
    get_datachecklist("Admin184")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_status(self, "Admin184", event, result, var_v3.mananage_activate_input, var_v3.mananage_activate_label,
                                                          "0", var_v3.check_mananage_activate, "_QuanLyThe_TrangThai_KichHoat.png")


def caseid_admin185(self):
    get_datachecklist("Admin185")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_status(self, "Admin185", event, result, var_v3.mananage_not_activate_input, var_v3.mananage_not_activate_label,
                                                          "1", var_v3.check_mananage_activate, "_QuanLyThe_TrangThai_ChuaKichHoat.png")


def caseid_admin186(self):
    get_datachecklist("Admin186")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_status(self, "Admin186", event, result, var_v3.mananage_lock_input, var_v3.mananage_lock_label,
                                                          "0", var_v3.check_mananage_lock, "_QuanLyThe_TrangThai_Khoa.png")


def caseid_admin187(self):
    get_datachecklist("Admin187")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_status(self, "Admin187", event, result, var_v3.mananage_un_lock_input, var_v3.mananage_un_lock_label,
                                                          "0", var_v3.check_mananage_un_lock, "_QuanLyThe_TrangThai_MoKhoa.png")


def caseid_admin188(self):
    get_datachecklist("Admin188")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_status(self, "Admin188", event, result, var_v3.mananage_assign_input, var_v3.mananage_assign_label,
                                                          "0", var_v3.check_mananage_assign, "_QuanLyThe_TrangThai_DaGan.png")


def caseid_admin189(self):
    get_datachecklist("Admin189")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_status(self, "Admin189", event, result, var_v3.mananage_not_assign_input, var_v3.mananage_not_assign_label,
                                                          "1", var_v3.check_mananage_assign, "_QuanLyThe_TrangThai_ChuaGan.png")


def caseid_admin190(self):
    get_datachecklist("Admin190")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_dowload_excel(self, "Admin190", event, result)


def caseid_admin191(self):
    get_datachecklist("Admin191")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_upload_excel(self, "Admin191", event, result)


def caseid_admin192(self):
    get_datachecklist("Admin192")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_add_new(self, "Admin192", event, result)


def caseid_admin193(self):
    get_datachecklist("Admin193")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_edit(self, "Admin193", event, result)


def caseid_admin194(self):
    get_datachecklist("Admin194")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_lock(self, "Admin194", event, result, var_v3.check_mananage_un_lock, "_QuanLyThe_Khoa.png")


def caseid_admin195(self):
    get_datachecklist("Admin195")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_lock(self, "Admin195", event, result, var_v3.check_mananage_lock, "_QuanLyThe_TrangThai_MoKhoa.png")


def caseid_admin196(self):
    get_datachecklist("Admin196")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_delete(self, "Admin196", event, result)


def caseid_admin197(self):
    get_datachecklist("Admin197")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_dowload(self, "Admin197", event, result, var_v3.export_excel,
                                                                        "quanlythe_xuatexcel.xlsx", "_QuanLyThe_XuatExcel.png")


def caseid_admin198(self):
    get_datachecklist("Admin198")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    administration.driver_management.manage_ticket_dowload(self, "Admin198", event, result, var_v3.export_pdf1,
                                                                        "dquanlythe_xuatexcel.pdf", "_QuanLyThe_XuatPDF.png")


def caseid_admin199(self):
    pass




def caseid_report01(self):
    get_datachecklist("Report01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.summary_report_of_activities(self, "Report01", event, result)


def caseid_report02(self):
    get_datachecklist("Report02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.summary_report_of_activities_search(self, "Report02", event, result)


def caseid_report03(self):
    get_datachecklist("Report03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.summary_report_of_activities_excel(self, "Report03", event, result)


def caseid_report04(self):
    get_datachecklist("Report04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.summary_report_of_activities_pdf(self, "Report04", event, result)


def caseid_report05(self):
    pass


def caseid_report06(self):
    get_datachecklist("Report06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.summary_report_of_activities_hide_column(self, "Report06", event, result)


def caseid_report07(self):
    get_datachecklist("Report07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.detailed_activity_reports(self, "Report07", event, result)


def caseid_report08(self):
    get_datachecklist("Report08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.detailed_activity_reports_search(self, "Report08", event, result)


def caseid_report09(self):
    get_datachecklist("Report09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.detailed_activity_reports_excel(self, "Report09", event, result)


def caseid_report10(self):
    get_datachecklist("Report10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.detailed_activity_reports_pdf(self, "Report10", event, result)


def caseid_report11(self):
    pass


def caseid_report12(self):
    get_datachecklist("Report12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.detailed_activity_reports_hide_column(self, "Report12", event, result)


def caseid_report13(self):
    get_datachecklist("Report13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.stop_report(self, "Report13", event, result)


def caseid_report14(self):
    get_datachecklist("Report14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.stop_report_search(self, "Report14", event, result)


def caseid_report15(self):
    get_datachecklist("Report15")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.stop_report_excel(self, "Report15", event, result)


def caseid_report16(self):
    get_datachecklist("Report16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.stop_report_pdf(self, "Report16", event, result)


def caseid_report17(self):
    pass


def caseid_report18(self):
    get_datachecklist("Report18")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.stop_report_hide_column(self, "Report18", event, result)


def caseid_report19(self):
    get_datachecklist("Report19")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.stop_report_icon(self, "Report19", event, result, var_v3.stopreport_iconsee, var_v3.stopreport_iconsee2, "0")


def caseid_report20(self):
    get_datachecklist("Report20")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.stop_report_icon(self, "Report20", event, result, var_v3.stopreport_iconselect, var_v3.stopreport_iconselect, "1")


def caseid_report21(self):
    get_datachecklist("Report21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.station_report(self, "Report21", event, result)


def caseid_report22(self):
    get_datachecklist("Report22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.station_report_search(self, "Report22", event, result)


def caseid_report23(self):
    get_datachecklist("Report23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.station_report_excel(self, "Report23", event, result)


def caseid_report24(self):
    get_datachecklist("Report24")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.station_report_pdf(self, "Report24", event, result)


def caseid_report25(self):
    pass


def caseid_report26(self):
    get_datachecklist("Report26")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.station_report_hide_column(self, "Report26", event, result)


def caseid_report27(self):
    get_datachecklist("Report27")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_business_trip(self, "Report27", event, result)

def caseid_report28(self):
    get_datachecklist("Report28")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_business_trip_search(self, "Report28", event, result)


def caseid_report29(self):
    get_datachecklist("Report29")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_business_trip_excel(self, "Report29", event, result)


def caseid_report30(self):
    get_datachecklist("Report30")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_business_trip_pdf(self, "Report30", event, result)


def caseid_report31(self):
    pass


def caseid_report32(self):
    get_datachecklist("Report32")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_business_trip_hide_column(self, "Report32", event, result)



def caseid_report33(self):
    get_datachecklist("Report33")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.too_speed_report(self, "Report33", event, result)


def caseid_report34(self):
    get_datachecklist("Report34")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.too_speed_report_search(self, "Report34", event, result)


def caseid_report35(self):
    get_datachecklist("Report35")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.too_speed_report_excel(self, "Report35", event, result)


def caseid_report36(self):
    get_datachecklist("Report36")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.too_speed_report_pdf(self, "Report36", event, result)


def caseid_report37(self):
    pass



def caseid_report38(self):
    get_datachecklist("Report38")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.too_speed_report_hide_column(self, "Report38", event, result)



def caseid_report39(self):
    get_datachecklist("Report39")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.trip_report(self, "Report39", event, result)


def caseid_report40(self):
    get_datachecklist("Report40")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.trip_report_search(self, "Report40", event, result)


def caseid_report41(self):
    get_datachecklist("Report41")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.trip_report_dowload(self, "Report41", event, result, var_v3.export_excel,
                                                                        "baocaohanhtrinh.xlsx", "_BaoCaoHanhtrinh_XuatExcel.png")


def caseid_report42(self):
    get_datachecklist("Report42")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.trip_report_dowload(self, "Report42", event, result, var_v3.export_pdf,
                                                                        "baocaohanhtrinh.pdf", "_BaoCaoHanhtrinh_XuatPDF.png")

def caseid_report43(self):
    pass


def caseid_report44(self):
    get_datachecklist("Report44")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.trip_report_icon_see(self, "Report44", event, result)


def caseid_report45(self):
    get_datachecklist("Report45")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.enable_control_table_report(self, "Report45", event, result)


def caseid_report46(self):
    get_datachecklist("Report46")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.enable_control_table_report_search(self, "Report46", event, result)


def caseid_report47(self):
    get_datachecklist("Report47")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.enable_control_table_report_excel(self, "Report47", event, result)


def caseid_report48(self):
    get_datachecklist("Report48")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.enable_control_table_report_pdf(self, "Report48", event, result)


def caseid_report49(self):
    pass


def caseid_report50(self):
    get_datachecklist("Report50")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_on_the_ari_condition_naer(self, "Report50", event, result)


def caseid_report51(self):
    get_datachecklist("Report51")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_on_the_ari_condition_naer_search(self, "Report51", event, result)


def caseid_report52(self):
    get_datachecklist("Report52")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_on_the_ari_condition_naer_excel(self, "Report52", event, result)


def caseid_report53(self):
    get_datachecklist("Report53")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_on_the_ari_condition_naer_pdf(self, "Report53", event, result)


def caseid_report54(self):
    pass


def caseid_report55(self):
    get_datachecklist("Report55")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.activity_report.report_on_the_ari_condition_naer_hide_column(self, "Report55", event, result)


def caseid_report56(self):
    get_datachecklist("Report56")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.summary_report.report_detail_checkin_checkout(self, "Report56", event, result)


def caseid_report57(self):
    get_datachecklist("Report57")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.summary_report.report_detail_checkin_checkout_search(self, "Report57", event, result)


def caseid_report58(self):
    get_datachecklist("Report58")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.summary_report.report_detail_checkin_checkout_excel(self, "Report58", event, result)

def caseid_report59(self):
    get_datachecklist("Report59")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.summary_report.report_detail_checkin_checkout_pdf(self, "Report59", event, result)



def caseid_report60(self):
    pass


def caseid_report61(self):
    get_datachecklist("Report61")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.summary_report.report_summary_checkin_checkout(self, "Report61", event, result)


def caseid_report62(self):
    get_datachecklist("Report62")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.summary_report.report_summary_checkin_checkout_search(self, "Report62", event, result)

def caseid_report63(self):
    get_datachecklist("Report63")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.summary_report.report_summary_checkin_checkout_excel(self, "Report63", event, result)


def caseid_report64(self):
    get_datachecklist("Report64")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.summary_report.report_summary_checkin_checkout_pdf(self, "Report64", event, result)


def caseid_report65(self):
    pass


def caseid_report66(self):
    get_datachecklist("Report66")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.engine_report(self, "Report66", event, result)


def caseid_report67(self):
    get_datachecklist("Report67")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.engine_report_search(self, "Report67", event, result)

def caseid_report68(self):
    get_datachecklist("Report68")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.engine_report_excel(self, "Report68", event, result)


def caseid_report69(self):
    get_datachecklist("Report69")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.engine_report_pdf(self, "Report69", event, result)


def caseid_report70(self):
    pass


def caseid_report71(self):
    get_datachecklist("Report71")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.engine_report_hide_column(self, "Report71", event, result)



def caseid_report72(self):
    get_datachecklist("Report72")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.report_status_engine(self, "Report72", event, result)


def caseid_report73(self):
    get_datachecklist("Report73")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.report_status_engine_search(self, "Report73", event, result)


def caseid_report74(self):
    get_datachecklist("Report74")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.report_status_engine_excel(self, "Report74", event, result)


def caseid_report75(self):
    get_datachecklist("Report75")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.report_status_engine_pdf(self, "Report75", event, result)


def caseid_report76(self):
    pass


def caseid_report77(self):
    get_datachecklist("Report77")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.engine_report.report_status_engine_hide_column(self, "Report77", event, result)


def caseid_report78(self):
    get_datachecklist("Report78")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.fuel_consumtion_report(self, "Report78", event, result)


def caseid_report79(self):
    get_datachecklist("Report79")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.fuel_consumtion_report_search(self, "Report79", event, result)


def caseid_report80(self):
    get_datachecklist("Report80")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.fuel_consumtion_report_excel(self, "Report80", event, result)


def caseid_report81(self):
    get_datachecklist("Report81")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.report_detail_checkin_checkout_pdf(self, "Report81", event, result)


def caseid_report82(self):
    pass


def caseid_report83(self):
    get_datachecklist("Report83")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.summary_report_of_activities_hide_column(self, "Report83", event, result)


def caseid_report84(self):
    get_datachecklist("Report84")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.report_fuel_spillage(self, "Report84", event, result)



def caseid_report85(self):
    get_datachecklist("Report85")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.report_fuel_spillage_search(self, "Report85", event, result)


def caseid_report86(self):
    get_datachecklist("Report86")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.report_fuel_spillage_excel(self, "Report86", event, result)


def caseid_report87(self):
    get_datachecklist("Report87")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.report_fuel_spillage_pdf(self, "Report87", event, result)


def caseid_report88(self):
    pass


def caseid_report89(self):
    get_datachecklist("Report89")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.fuel_report.report_fuel_spillage_hide_column(self, "Report89", event, result)

def caseid_report90(self):
    get_datachecklist("Report90")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.report_bgt.over_speed_detail_report(self, "Report90", event, result)


def caseid_report91(self):
    get_datachecklist("Report91")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.report_bgt.over_speed_detail_report_search(self, "Report91", event, result)


def caseid_report92(self):
    get_datachecklist("Report92")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.report_bgt.over_speed_detail_report_dowload(self, "Report92", event, result, var_v3.export_excel,
                                                              "chitietviphamtocdoxechay.xlsx", "_ChiTietViPhamTocDoXeChay_XuatExcel.png")

def caseid_report93(self):
    get_datachecklist("Report93")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.report_bgt.over_speed_detail_report_dowload(self, "Report93", event, result, var_v3.export_pdf,
                                                              "chitietviphamtocdoxechay.pdf", "_ChiTietViPhamTocDoXeChay_XuatPdf.png")


def caseid_report94(self):
    pass


def caseid_report95(self):
    get_datachecklist("Report95")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    report_v3.report_bgt.over_speed_detail_report_hide_column(self, "Report95", event, result)


def caseid_video01(self):
    get_datachecklist("Video01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring(self, "Video01", event, result)


def caseid_video02(self):
    get_datachecklist("Video02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_select_screen(self, "Video02", event, result)


def caseid_video03(self):
    get_datachecklist("Video03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_select_group(self, "Video03", event, result)


def caseid_video04(self):
    get_datachecklist("Video04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_select_vehicle(self, "Video04", event, result)


def caseid_video05(self):
    get_datachecklist("Video05")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_filter(self, "Video05", event, result)


def caseid_video06(self):
    get_datachecklist("Video06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_pdf(self, "Video06", event, result)


def caseid_video07(self):
    get_datachecklist("Video07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_add_new(self, "Video07", event, result)


def caseid_video08(self):
    get_datachecklist("Video08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_delete(self, "Video08", event, result)


def caseid_video09(self):
    get_datachecklist("Video09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_iconmap(self, "Video09", event, result)


def caseid_video10(self):
    get_datachecklist("Video10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.camera_monitoring_iconclose(self, "Video10", event, result)



def caseid_video11(self):
    get_datachecklist("Video11")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.see_again_video(self, "Video11", event, result)


def caseid_video12(self):
    get_datachecklist("Video12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.see_again_video_refresh(self, "Video12", event, result)


def caseid_video13(self):
    get_datachecklist("Video13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.see_again_device(self, "Video13", event, result)


def caseid_video14(self):
    get_datachecklist("Video14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.see_again_device_search(self, "Video14", event, result)


def caseid_video15(self):
    get_datachecklist("Video15")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.see_again_device_iconrun(self, "Video15", event, result)


def caseid_video16(self):
    get_datachecklist("Video16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.see_again_device_iconsever(self, "Video16", event, result)


def caseid_video17(self):
    get_datachecklist("Video17")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.dowload_cloud(self, "Video17", event, result)



def caseid_video18(self):
    get_datachecklist("Video18")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.minotor_video.dowload_cloud_search(self, "Video18", event, result)



def caseid_video19(self):
    get_datachecklist("Video19")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.channel_categories(self, "Video19", event, result)


def caseid_video20(self):
    get_datachecklist("Video20")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.channel_categories_search(self, "Video20", event, result, "Kênh 2", "Kích hoạt", "ma02")


def caseid_video21(self):
    get_datachecklist("Video21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.channel_categories_search(self, "Video21", event, result, "Kênh 3", "Chưa kích hoạt", "ma03")


def caseid_video22(self):
    get_datachecklist("Video22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.channel_categories_add_new(self, "Video22", event, result)


def caseid_video23(self):
    get_datachecklist("Video23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.channel_categories_edit(self, "Video23", event, result)


def caseid_video24(self):
    get_datachecklist("Video24")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.channel_categories_delete(self, "Video24", event, result)


def caseid_video25(self):
    get_datachecklist("Video25")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.config_channel_camera(self, "Video25", event, result)


def caseid_video26(self):
    get_datachecklist("Video26")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.config_channel_camera_search(self, "Video26", event, result, var_v3.data['video']['config_camera_search'])


def caseid_video27(self):
    get_datachecklist("Video27")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.config_channel_camera_edit(self, "Video27", event, result)


def caseid_video28(self):
    get_datachecklist("Video28")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    video_v3.channel_categories_management.config_channel_camera_iconcopy(self, "Video28", event, result)


def caseid_image01(self):
    get_datachecklist("Image01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring(self, "Image01", event, result)


def caseid_image02(self):
    get_datachecklist("Image02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_select_screen(self, "Image02", event, result)


def caseid_image03(self):
    get_datachecklist("Image03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_select_group(self, "Image03", event, result)


def caseid_image04(self):
    get_datachecklist("Image04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_select_vehicle(self, "Image04", event, result)


def caseid_image05(self):
    get_datachecklist("Image05")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_filter(self, "Image05", event, result)


def caseid_image06(self):
    get_datachecklist("Image06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_excel(self, "Image06", event, result)


def caseid_image07(self):
    get_datachecklist("Image07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_add_new(self, "Image07", event, result)


def caseid_image08(self):
    get_datachecklist("Image08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_delete(self, "Image08", event, result)


def caseid_image09(self):
    get_datachecklist("Image09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_see_image(self, "Image09", event, result)


def caseid_image10(self):
    get_datachecklist("Image10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.image.online_image_monitoring_dowload_image(self, "Image10", event, result)


def caseid_image11(self):
    get_datachecklist("Image11")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.image_library(self, "Image11", event, result)


def caseid_image12(self):
    get_datachecklist("Image12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.image_library_search(self, "Image12", event, result)



def caseid_image13(self):
    get_datachecklist("Image13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.image_library_download_image(self, "Image13", event, result)


def caseid_image14(self):
    get_datachecklist("Image14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.get_info_image_library(self, "Image14", event, result)


def caseid_image15(self):
    get_datachecklist("Image15")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.check_info_image_library(self, "Image15", event, result, 151, 2, 3, "ThuVienAnh_PhuongTien.png")


def caseid_image16(self):
    get_datachecklist("Image16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.check_info_image_library(self, "Image16", event, result, 152, 2, 3, "ThuVienAnh_ThoiGian.png")


def caseid_image17(self):
    get_datachecklist("Image17")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.check_info_image_library(self, "Image17", event, result, 153, 2, 3, "ThuVienAnh_VanToc.png")

def caseid_image18(self):
    get_datachecklist("Image18")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.check_info_image_library(self, "Image18", event, result, 154, 2, 3, "ThuVienAnh_Kenh.png")


def caseid_image19(self):
    get_datachecklist("Image19")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.check_info_image_library(self, "Image19", event, result, 155, 2, 3, "ThuVienAnh_DiaChi.png")


def caseid_image20(self):
    get_datachecklist("Image20")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.view_images_by_channel(self, "Image20", event, result)


def caseid_image21(self):
    get_datachecklist("Image21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.view_images_by_channel_search(self, "Image21", event, result)


def caseid_image22(self):
    get_datachecklist("Image22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.see_image_detail(self, "Image22", event, result)

def caseid_image23(self):
    get_datachecklist("Image23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.see_image_detail_search(self, "Image23", event, result)


def caseid_image24(self):
    get_datachecklist("Image24")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.see_image_detail_check_info(self, "Image24", event, result, var_v3.see_image_detail_vehicle1,
                                                            var_v3.see_image_detail_vehicle2, "_XemAnhChiTiet_PhuongTien.png")

def caseid_image25(self):
    get_datachecklist("Image25")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    image_v3.see_image_vehicle1.see_image_detail_check_info(self, "Image25", event, result, var_v3.see_image_detail_adress1,
                                                            var_v3.see_image_detail_adress2, "_XemAnhChiTiet_DiaChi.png")


def caseid_utility01(self):
    get_datachecklist("Utility01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1(self, "Utility01", event, result)


def caseid_utility02(self):
    get_datachecklist("Utility02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1_search_location(self, "Utility02", event, result)


def caseid_utility03(self):
    get_datachecklist("Utility03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1_search_adress(self, "Utility03", event, result)


def caseid_utility04(self):
    get_datachecklist("Utility04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1_search_toado(self, "Utility04", event, result)


def caseid_utility05(self):
    get_datachecklist("Utility05")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1_select_location(self, "Utility05", event, result)


def caseid_utility06(self):
    get_datachecklist("Utility06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1_select_group(self, "Utility06", event, result)


def caseid_utility07(self):
    get_datachecklist("Utility07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1_select_landmark_in_list(self, "Utility07", event, result)


def caseid_utility08(self):
    get_datachecklist("Utility08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1_eport_excel(self, "Utility08", event, result)


def caseid_utility09(self):
    get_datachecklist("Utility09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.vehicle_type_categoty_dowload_excel(self, "Utility09", event, result)


def caseid_utility10(self):
    get_datachecklist("Utility10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.vehicle_type_categoty_upload_excel(self, "Utility10", event, result)


def caseid_utility11(self):
    get_datachecklist("Utility11")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_management1_refresh(self, "Utility11", event, result)


def caseid_utility12(self):
    get_datachecklist("Utility12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_management(self, "Utility12", event, result)


def caseid_utility13(self):
    get_datachecklist("Utility13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_management_search(self, "Utility13", event, result, var_v3.search_group_landmark_input,
                                                                    var_v3.data['utility']['group_landmark1'], "_QuanTriNhomDiem_TimNhomDiem.png")

def caseid_utility14(self):
    get_datachecklist("Utility14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_management_search(self, "Utility14", event, result, var_v3.search_group_input,
                                                                    var_v3.data['utility']['group_landmark2'], "_QuanTriNhomDiem_TimDiem.png")

def caseid_utility15(self):
    get_datachecklist("Utility15")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_management_search(self, "Utility15", event, result, var_v3.search_user_input,
                                                                    var_v3.data['utility']['group_landmark3'], "_QuanTriNhomDiem_TimNguoiDùng.png")

def caseid_utility16(self):
    get_datachecklist("Utility16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_management_add_new_group(self, "Utility16", event, result)


def caseid_utility17(self):
    get_datachecklist("Utility17")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_management_coppy(self, "Utility17", event, result)


def caseid_utility18(self):
    get_datachecklist("Utility18")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_management_edit(self, "Utility18", event, result)


def caseid_utility19(self):
    get_datachecklist("Utility19")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_management_delete(self, "Utility19", event, result)


def caseid_utility20(self):
    get_datachecklist("Utility20")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_assign(self, "Utility20", event, result)



def caseid_utility21(self):
    get_datachecklist("Utility21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_permission(self, "Utility21", event, result)


def caseid_utility22(self):
    get_datachecklist("Utility22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_permission_search(self, "Utility22", event, result, var_v3.permission_user_input,
                                                                    var_v3.data['utility']['permission_user'], "_PhanQuyenNhomDiem_TimNguoiDung.png")


def caseid_utility23(self):
    get_datachecklist("Utility23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_permission_search(self, "Utility23", event, result, var_v3.permission_grouplandmark_input,
                                                                    var_v3.data['utility']['permission_grouplandmark'], "_PhanQuyenNhomDiem_TimNhomDiem.png")


def caseid_utility24(self):
    get_datachecklist("Utility24")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.landmark_management.landmark_group_permission_assign(self, "Utility24", event, result)


def caseid_utility25(self):
    get_datachecklist("Utility25")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    utility_v3.managament_router.managament_router1(self, "Utility25", event, result)



def caseid_ai01(self):
    get_datachecklist("Ai01")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_sumnary_action_vehicle(self, "Ai01", event, result)


def caseid_ai02(self):
    get_datachecklist("Ai02")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_sumnary_action_vehicle_search(self, "Ai02", event, result)


def caseid_ai03(self):
    get_datachecklist("Ai03")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_sumnary_action_vehicle_excel(self, "Ai03", event, result)


def caseid_ai04(self):
    get_datachecklist("Ai04")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_sumnary_action_vehicle_pdf(self, "Ai04", event, result)


def caseid_ai05(self):
    pass



def caseid_ai06(self):
    get_datachecklist("Ai06")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_sumnary_action_vehicle_hide_column(self, "Ai06", event, result)


def caseid_ai07(self):
    get_datachecklist("Ai07")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation(self, "Ai07", event, result)


def caseid_ai08(self):
    get_datachecklist("Ai08")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_search(self, "Ai08", event, result)


def caseid_ai09(self):
    get_datachecklist("Ai09")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_get_info(self, "Ai09", event, result)



def caseid_ai10(self):
    get_datachecklist("Ai10")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_check_info(self, "Ai10", event, result, 151, 2, 3, "BaoCaoViPhamLaiXe_LaiXe.png")



def caseid_ai11(self):
    get_datachecklist("Ai11")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_check_info(self, "Ai11", event, result, 152, 2, 3, "BaoCaoViPhamLaiXe_ThoiGian.png")



def caseid_ai12(self):
    get_datachecklist("Ai12")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_check_info(self, "Ai12", event, result, 153, 2, 3, "BaoCaoViPhamLaiXe_PhuongTien.png")


def caseid_ai13(self):
    get_datachecklist("Ai13")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_check_info(self, "Ai13", event, result, 154, 2, 3, "BaoCaoViPhamLaiXe_Nhiptim.png")


def caseid_ai14(self):
    get_datachecklist("Ai14")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_check_info(self, "Ai14", event, result, 155, 2, 3, "BaoCaoViPhamLaiXe_VanToc.png")


def caseid_ai15(self):
    get_datachecklist("Ai15")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_check_info(self, "Ai15", event, result, 156, 2, 3, "BaoCaoViPhamLaiXe_Kenh.png")


def caseid_ai16(self):
    get_datachecklist("Ai16")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_check_info(self, "Ai16", event, result, 157, 2, 3, "BaoCaoViPhamLaiXe_DiaChi.png")


def caseid_ai17(self):
    get_datachecklist("Ai17")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_a_driving_violation_check_info(self, "Ai17", event, result, 158, 2, 3, "BaoCaoViPhamLaiXe_LoaiViPham.png")


def caseid_ai18(self):
    pass

def caseid_ai19(self):
    pass

def caseid_ai20(self):
    pass


def caseid_ai21(self):
    get_datachecklist("Ai21")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_driver_rank_month(self, "Ai21", event, result)


def caseid_ai22(self):
    get_datachecklist("Ai22")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_driver_rank_month_search(self, "Ai22", event, result)


def caseid_ai23(self):
    get_datachecklist("Ai23")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_driver_rank_month_excel(self, "Ai23", event, result)


def caseid_ai24(self):
    get_datachecklist("Ai24")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_driver_rank_month_pdf(self, "Ai24", event, result)


def caseid_ai25(self):
    pass


def caseid_ai26(self):
    get_datachecklist("Ai26")
    event = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var_v3.readData(var_v3.path_luutamthoi, 'Sheet1', 43, 2))
    ai_v3.ai_cam.report_driver_rank_month_hide_column(self, "Ai26", event, result)

