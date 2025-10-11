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
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.giam_gia = giam_gia
        
    def thue_nhap_khau(self):
        return self.gia * 0.1
    
    def nhap_sp(self):
        self.ten_san_pham = input("Tên sản phẩm: ")
        self.gia = float(input("Giá: "))
        self.giam_gia = float(input("Giảm giá: "))
        
    def set_ten(self, ten_san_pham):
        self.ten_san_pham = ten_san_pham
        
    def get_ten(self):
        return self.ten_san_pham
    
    def set_gia(self, gia):
        self.gia = gia
        
    def get_gia(self):
        return self.gia
    
    def xuat_tt_sp(self):
        print(f"Sản phẩm: {self.ten_san_pham} có giá: {self.gia} và được giảm giá: {self.giam_gia}, thuế nhập khẩu: {self.thue_nhap_khau()}")
        
    def __str__(self):
        return f"Sản phẩm: {self.ten_san_pham} có giá: {self.gia} và được giảm giá: {self.giam_gia}, thuế nhập khẩu: {self.thue_nhap_khau()}"
    
    