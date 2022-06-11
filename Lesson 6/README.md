# Bài 6 - Truy Xuất Dữ Liệu trong SQL


## Truy Xuất Dữ Liệu trong SQL

- Format câu truy vấn:
```
SELECT <columns>
FROM <table>
[WHERE <condition> <AND|OR> <condition> ....] # <condition> : <column> <operator> <value>
```



```
-- Cấu trúc cơ bản truy xuất
SELECT <columns> FROM <table>

-- Lấy tất cả cột trong bảng
SELECT * FROM <table>
```

Ví dụ:
```
SELECT MaHocSinh,HoTen FROM HocSinh;
```

- Thực hành 1: Lấy Họ tên và giới tính trong bảng Học Sinh
```
SELECT HoTen,GioiTinh FROM HocSinh;
```

-- Điều kiện trong truy vấn SQL:
Ví dụ:
```
SELECT *
FROM HocSinh
WHERE Truong = 'Nguyễn Văn Trọng';
```

## Bài Tập Thực Hành
[Bài Tập Thực Hành](./BAITAPTHUCHANH.md)