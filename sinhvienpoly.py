class SinhVienPoly:
    def __init__(self, ten_sinh_vien:str, nganh_hoc:str):
        self.ten_sinh_vien = ten_sinh_vien
        self.nganh_hoc = nganh_hoc
    def nhap_thong_tin(self):
        self.ten_sinh_vien = input("Mời nhập tên: ")
        self.nganh_hoc = input("Nhập ngành học:")
        self.diem = float(input("Mời nhập điểm:"))
    def xuat_sv(self):
        print(f"Tên sinh viên: {self.ten_sinh_vien}, Ngành học: {self.nganh_hoc}, Điểm: {self.get_diem()}, Học lực: {self.get_hoc_luc()}")
    def set_diem(self, diem):
        self.diem = diem
    def get_diem(self):
        return self.diem
    def set_hoc_luc(self, hoc_luc):
        self.hoc_luc = hoc_luc
    def get_hoc_luc(self):
        diem = self.get_diem()
        
        if diem >= 9 and diem <= 10:
            return "Xuất sắc"
        elif diem >= 8:
            return "Giỏi"
        elif diem >= 7:
            return "Khá"
        elif diem >= 5:
            return "Trung bình"
        else:
            return "Chưa đạt"
    def xuat_thong_tin(self):
        print(f"{self.ten_sinh_vien: <20}, {self.nganh_hoc: <10}, {self.get_diem(): 10}, {self.get_hoc_luc(): 10}")
    def __str__(self):
        return f"{self.ten_sinh_vien:}, {self.nganh_hoc: }, {self.get_diem(): }, {self.get_hoc_luc(): }"
class SinhVienIT(SinhVienPoly):
    def __init__(self, ten_sinh_vien:str, nganh_hoc:str, java, html, css):
        super().__init__(ten_sinh_vien, nganh_hoc)
        self.java = java
        self.html = html
        self.css = css
    def nhap_thong_tin(self):
        super().nhap_thong_tin()
        self.java = float(input("Điểm Java: "))
        self.html = float(input("Điểm HTML: "))
        self.css = float(input("Điểm CSS: "))
    def get_diem(self):
        return (self.java * 2 + self.html + self.css) / 4
    def xuat_sv(self):
        print(f"Tên sinh viên: {self.ten_sinh_vien}, Ngành học: {self.nganh_hoc}, Điểm: {self.get_diem()}, Học lực: {self.get_hoc_luc()}")
class SinhVienBiz(SinhVienPoly):
    def __init__(self, ten_sinh_vien, nganh_hoc, marketing, sales):
        super().__init__(ten_sinh_vien, nganh_hoc)
        self.marketing = marketing
        self.sales = sales
    def nhap_thong_tin(self):
        super().nhap_thong_tin()
        self.marketing = float(input("Điểm Marketing: "))
        self.sales = float(input("Điểm Sales: "))
    def get_diem(self):
        return (self.marketing + self.sales) / 2
    def xuat_sv(self):
        print(f"Tên sinh viên: {self.ten_sinh_vien}, Ngành học: {self.nganh_hoc}, Điểm: {self.get_diem()}, Học lực: {self.get_hoc_luc()}")