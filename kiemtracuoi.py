danh_sach_sv = [
    {
        "ma_sv": "SV001",
        "ten_sv": "Nguyen Van A",
        "toan": 8.5,
        "ly": 7.0,
        "hoa": 9.0,
        "dtb": 8.17,
        "xep_loai": "Giỏi"
    },
    {
        "ma_sv": "SV002",
        "ten_sv": "Tran Thi B",
        "toan": 7.0,
        "ly": 7.5,
        "hoa": 8.0,
        "dtb": 7.5,
        "xep_loai": "Khá"
    },
    {
        "ma_sv": "SV003",
        "ten_sv": "Le Van C",
        "toan": 5.0,
        "ly": 6.0,
        "hoa": 5.5,
        "dtb": 5.5,
        "xep_loai": "Trung bình"
    }
]
def hien_thi_danh_sach():
    if len(danh_sach_sv) == 0:
        print("Danh sách sinh viên hiện đang rỗng!")
        return

    print("-" * 85)
    print("Mã SV | Họ và tên            | Toán  | Lý    | Hóa   | ĐTB   | Xếp loại")
    print("-" * 85)
    for sv in danh_sach_sv:
        print(sv["ma_sv"].ljust(6) + " | " + 
              sv["ten_sv"].ljust(20) + " | " + 
              str(sv["toan"]).ljust(5) + " | " + 
              str(sv["ly"]).ljust(5) + " | " + 
              str(sv["hoa"]).ljust(5) + " | " + 
              str(sv["dtb"]).ljust(5) + " | " + 
              sv["xep_loai"])
    print("-" * 85)

def tiep_nhan_sinh_vien():
    while True:
        ma_sv = input("Nhập mã sinh viên: ").strip()
        if ma_sv == "":
            print("Mã sinh viên không được để rỗng!")
            continue

        trung_ma = False
        for sv in danh_sach_sv:
            if sv["ma_sv"] == ma_sv:
                trung_ma = True
                break
        if trung_ma:
            print("Mã sinh viên này đã tồn tại! Vui lòng nhập mã khác.")
            continue
        break

    while True:
        ten_sv = input("Nhập họ và tên sinh viên: ").strip()
        if ten_sv == "":
            print("Tên sinh viên không được để rỗng!")
            continue
        break

    
def menu():
    while True:
        print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Tiếp nhận sinh viên mới")
        print("3. Cập nhật kết quả học tập")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Thống kê điểm trung bình")
        print("7. Thoát")

        choice = input("Mời bạn chọn chức năng (1-7): ").strip()
        match choice :
            case "6" :
                print(tinh_dtb_va_xep_loai(9,9,9))
            case _:
                print("yeu cau nhap lai")
             case "1" :
                  
    
menu()

