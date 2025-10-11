class ChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def nhap_chu_nhat(self):
        self.dai = float(input("Nhập chiều dài: "))
        self.rong = float(input("Nhập chiều rộng: "))

    def dien_tich(self):
        return self.dai * self.rong

    def chu_vi(self):
        return (self.dai + self.rong) * 2

    def xuat_thong_tin(self):
        print(f"Hình chữ nhật")
        print(f"Chiều dài: {self.dai}, Chiều rộng: {self.rong}")
        print(f"Diện tích: {self.dien_tich()}, Chu vi: {self.chu_vi()}")

class HinhVuong(ChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

    def nhap_hinh_vuong(self):
        self.canh = float(input("Nhập độ dài cạnh hình vuông: "))
    def dien_tich(self):
        return self.canh * self.canh
    def chu_vi(self):
        return self.canh * 4

    def xuat_thong_tin(self):
        print(f"Hình vuông")
        print(f"Cạnh: {self.canh}")
        print(f"Diện tích: {self.dien_tich()}, Chu vi: {self.chu_vi()}")