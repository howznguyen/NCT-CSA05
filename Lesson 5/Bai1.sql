# Tạo bảng học sinh
CREATE TABLE HocSinh (
    MaHocSinh VARCHAR(10),
    HoTen VARCHAR(50),
    DiaChi VARCHAR(100),
    NgaySinh DATE,
    GioiTinh VARCHAR(10),
    Lop VARCHAR(10)
);

# Thêm cột `Truong` và xoá cột `Lop`
ALTER TABLE HocSinh
ADD COLUMN Truong VARCHAR(50),
DROP COLUMN Lop;

# Thêm 10 dòng dữ liệu vào trong Table `HocSinh`
INSERT INTO HocSinh VALUES
('HS001', 'Nguyễn Văn A', 'Hà Nội', '1995-01-01', 'Nam', 'Cù Chính Lan'),
('HS002', 'Nguyễn Văn B', 'Hà Nội', '1995-01-01', 'Nam', 'Phan Đình Giót'),
('HS003', 'Nguyễn Văn C', 'Hà Nội', '1995-01-01', 'Nam', 'Nguyễn Huệ'),
('HS004', 'Nguyễn Văn D', 'Hà Nội', '1995-01-01', 'Nam', 'Nguyễn Văn Trọng'),
('HS005', 'Nguyễn Văn E', 'Hà Nội', '1995-01-01', 'Nam', 'Nguyễn Văn Trọng'),
('HS006', 'Nguyễn Văn F', 'Hà Nội', '1995-01-01', 'Nam', 'Nguyễn Văn Trọng'),
('HS007', 'Nguyễn Văn G', 'Hà Nội', '1995-01-01', 'Nam', 'Nguyễn Văn Trọng'),
('HS008', 'Nguyễn Văn H', 'Hà Nội', '1995-01-01', 'Nam', 'Nguyễn Văn Trọng'),
('HS009', 'Nguyễn Văn I', 'Hà Nội', '1995-01-01', 'Nam', 'Nguyễn Văn Trọng'),
('HS010', 'Nguyễn Văn J', 'Hà Nội', '1995-01-01', 'Nam', 'Nguyễn Văn Trọng');