import math
from datetime import datetime
lich_su_pheptinh = []

def tinh_toan_co_ban():
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b if b != 0 else "Không thể chia cho 0"
    print("Tổng của hai số:", tong)
    print("Hiệu của hai số:", hieu)
    print("Tích của hai số:", tich)
    print("Thương của hai số:", thuong)
    lich_su_pheptinh.append(f"Cơ bản: {a}, {b} → +, -, *, /")

def luy_thua():
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    kq = a ** b
    print("Lũy thừa:", kq)
    lich_su_pheptinh.append(f"Lũy thừa: {a}^{b} = {kq}")

def can_bac_hai():
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    print("Căn bậc hai của số thứ nhất:", math.sqrt(a))
    print("Căn bậc hai của số thứ hai:", math.sqrt(b))
    lich_su_pheptinh.append(f"Căn bậc hai: √{a}, √{b}")

def ham_luong_giac():
    a = math.radians(float(input("Nhập góc thứ nhất (độ): ")))
    b = math.radians(float(input("Nhập góc thứ hai (độ): ")))
    print(f"sin({math.degrees(a)}°) = {math.sin(a)}")
    print(f"cos({math.degrees(a)}°) = {math.cos(a)}")
    print(f"tan({math.degrees(a)}°) = {math.tan(a)}")
    print(f"sin({math.degrees(b)}°) = {math.sin(b)}")
    print(f"cos({math.degrees(b)}°) = {math.cos(b)}")
    print(f"tan({math.degrees(b)}°) = {math.tan(b)}")
    lich_su_pheptinh.append("Hàm lượng giác: sin, cos, tan")

def logarit():
    a = float(input("Nhập số thứ nhất: ")) 
    b = float(input("Nhập cơ số tùy chọn: "))
    if a <= 0:
        print("Lỗi: Số phải lớn hơn 0.")
        return
    print("Log cơ số 10:", math.log10(a))
    print("Log tự nhiên (ln):", math.log(a))
    if b > 0 and b != 1:
        print(f"Log cơ số {b}:", math.log(a, b))
    else:
        print("Cơ số không hợp lệ.")
    lich_su_pheptinh.append(f"Logarit: a={a}, b={b}")

def giai_pt_bac_nhat():
    a = float(input("Nhập hệ số a (a khác 0): "))
    b = float(input("Nhập hệ số b: "))
    if a != 0:  
        x = -b / a
        print("Nghiệm của phương trình là x =", x)
        lich_su_pheptinh.append(f"PT bậc nhất: {a}x + {b} = 0 → x={x}")
    else:
        print("Lỗi: Hệ số 'a' phải khác 0.")

def giai_pt_bac_hai():
    a = float(input("Nhập hệ số a (a khác 0): "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    if a == 0:
        print("Lỗi: Hệ số 'a' phải khác 0.")
        return
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm.")
        lich_su_pheptinh.append(f"PT bậc hai: vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
        lich_su_pheptinh.append(f"PT bậc hai: nghiệm kép x={x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
        lich_su_pheptinh.append(f"PT bậc hai: x1={x1}, x2={x2}")

def xem_lich_su():
    if not lich_su_pheptinh:
        print("Chưa có phép tính nào được thực hiện.")
    else:
        print("---- LỊCH SỬ PHÉP TÍNH ----")
        for i, item in enumerate(lich_su_pheptinh, start=1):
            print(f"{i}. {item}")

def xem_thoi_gian():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Thời gian hiện tại:", now)
