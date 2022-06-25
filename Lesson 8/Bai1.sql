CREATE TABLE Truong (
    MaTruong varchar(50),
  	TenTruong VARCHAR(50),
  	DiaChi VARCHAR(50)
);

# Tạo bảng học sinh
CREATE TABLE HocSinh (
    MaHocSinh VARCHAR(10),
    HoTen VARCHAR(50),
    DiaChi VARCHAR(100),
    NgaySinh DATE,
    GioiTinh VARCHAR(10),
    Truong VARCHAR(10)
);


# Thêm 10 dòng dữ liệu vào trong Table `HocSinh`
INSERT INTO HocSinh VALUES
('HS001', 'Nguyễn Văn A', 'Hà Nội', '1995-01-01', 'Nam', 'CCL'),
('HS002', 'Nguyễn Văn B', 'Hà Nội', '1995-01-01', 'Nam', 'PDG'),
('HS003', 'Nguyễn Văn C', 'Hà Nội', '1995-01-01', 'Nam', 'NH'),
('HS004', 'Nguyễn Văn D', 'Hà Nội', '1995-01-01', 'Nam', 'NVT'),
('HS005', 'Nguyễn Văn E', 'Hà Nội', '1995-01-01', 'Nam', 'NVT'),
('HS006', 'Nguyễn Văn F', 'Hà Nội', '1995-01-01', 'Nam', 'NVT'),
('HS007', 'Nguyễn Văn G', 'Hà Nội', '1995-01-01', 'Nam', 'NVT'),
('HS008', 'Nguyễn Văn H', 'Hà Nội', '1995-01-01', 'Nam', 'NVT'),
('HS009', 'Nguyễn Văn I', 'Hà Nội', '1995-01-01', 'Nam', 'NVT'),
('HS010', 'Nguyễn Văn J', 'Hà Nội', '1995-01-01', 'Nam', 'NVT');