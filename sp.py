class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.giam_gia = giam_gia
    def thue_nhap_khau(self):
        return self.gia * 0.1
    def nhap_sp(self):
        self.ten_san_pham = input("Tên sản phẩm: ")
        self.gia = float(input("Giá: "))
        self.giam_gia = float(input("Giảm giá: "))
    def xuat_tt_sp(self):
        print(f"Sản phẩm: {self.ten_san_pham} có giá: {self.gia} và được giảm giá: {self.giam_gia}, thuế nhập khẩu: {self.thue_nhap_khau()}")
    def __str__(self):
        return f"Sản phẩm: {self.ten_san_pham} có giá: {self.gia} và được giảm giá: {self.giam_gia}, thuế nhập khẩu: {self.thue_nhap_khau()}"


class SanPham_Bai3:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia

    def thue_nhap_khau(self):
        return self.__gia * 0.1

    def nhap_sp(self):
        self.__ten_san_pham = input("Tên sản phẩm: ")
        self.__gia = float(input("Giá: "))
        self.__giam_gia = float(input("Giảm giá: "))

    def set_ten(self, ten_san_pham):
        self.__ten_san_pham = ten_san_pham

    def get_ten(self):
        return self.__ten_san_pham

    def set_gia(self, gia):
        self.__gia = gia

    def get_gia(self):
        return self.__gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia
    def get_giam_gia(self):
        return self.__giam_gia
    def xuat_tt_sp(self):
        print(f"Sản phẩm: {self.get_ten()} có giá: {self.get_gia()} và được giảm giá: {self.get_giam_gia()}, thuế nhập khẩu: {self.thue_nhap_khau()}")

    def __str__(self):
        return f"Sản phẩm: {self.get_ten()} có giá: {self.get_gia()} và được giảm giá: {self.get_giam_gia()}, thuế nhập khẩu: {self.thue_nhap_khau()}"

class SanPham_Bai4:
    def __init__(self, _ten_san_pham, _gia, _giam_gia):
        self.__ten_san_pham = _ten_san_pham
        self.__gia = _gia
        self.__giam_gia = _giam_gia

    def thue_nhap_khau(self):
        return self.__gia * 0.1

    def nhap_sp(self):
        self.__ten_san_pham = input("Tên sản phẩm: ")
        self.__gia = float(input("Giá: "))
        self.__giam_gia = float(input("Giảm giá: "))

    def set_ten(self, ten_san_pham):
        self.__ten_san_pham = ten_san_pham

    def get_ten(self):
        return self.__ten_san_pham

    def set_gia(self, gia):
        self.__gia = gia

    def get_gia(self):
        return self.__gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia
    def get_giam_gia(self):
        return self.__giam_gia
    def xuat_tt_sp(self):
        print(f"Sản phẩm: {self.get_ten()} có giá: {self.get_gia()} và được giảm giá: {self.get_giam_gia()}, thuế nhập khẩu: {self.thue_nhap_khau()}")

    def __str__(self):
        return f"Sản phẩm: {self.get_ten()} có giá: {self.get_gia()} và được giảm giá: {self.get_giam_gia()}, thuế nhập khẩu: {self.thue_nhap_khau()}"

