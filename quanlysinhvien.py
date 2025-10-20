from sinhvienpoly import *
class Quanlysinhvien:
    def __init__(self):
        self.dssv = []

    def tao_sv_moi(self):
        print("\nNhập thông tin sinh viên mới")
        ten = input("Họ và Tên: ").strip()
        nganh = input("Nhập ngành học: ").strip().lower()   
        while True:
            try:
                diem = float(input("Nhập vào điểm: "))
                if 0 <= diem <= 10:
                    break
                else:
                    print("Nhập điểm từ 0 đến 10.")
            except ValueError:
                print("Nhập số đừng nhập chữ.")
        sinh_vien_moi = SinhVienPoly(ten, nganh)
        sinh_vien_moi.set_diem(diem)
        print("Đã thêm sinh viên mới.")
        return sinh_vien_moi
    def them_sinh_vien(self):
        self.dssv.append(self.tao_sv_moi())
    def xuat_danh_sach_sinh_vien(self):
        if not self.dssv:
            print("\nHãy nhập sinh viên.")
            return
        print("\nDanh sách sinh viên")
        for i, sv in enumerate(self.dssv, start=1):
            print(f"Sinh viên thứ {i}:", end=" ")
            sv.xuat_sv()
    def sinh_vien_gioi(self):
        sv_gioi = [sv for sv in self.dssv if sv.get_hoc_luc() == "Giỏi"]
        if not sv_gioi:
            print("\nKhông có sinh viên nào đạt học lực giỏi.")
            return           
        print("\nDanh sách sinh viên giỏi")
        for i, sv in enumerate(self.sv_gioi, start=1):
            print(f"Sinh viên thứ {i}:", end=" ")
            sv.xuat_sv()
    def sap_xep_theo_diem(self):
        if not self.dssv:
            print("\nChưa có sinh viên, không thể sắp xếp.")
            return
        self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
        print("\nDanh sách sinh viên đã sắp xếp.")
        self.xuat_danh_sach_sinh_vien()