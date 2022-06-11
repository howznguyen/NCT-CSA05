# Bài 6 - Truy Xuất Dữ Liệu trong SQL


## Truy Xuất Dữ Liệu trong SQL

- Format câu truy vấn:
```
SELECT <columns>
FROM <table>
[WHERE <condition> <AND|OR> <condition> ....] # <condition> : <column> <operator> <value>
....
[ORDER BY <column> [ASC|DESC], ...] # ASC: tăng dần, DESC: giảm dần
[LIMIT <number>]
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

### IN
Cấu trúc:
```
<column> IN (<value>, <value>, ...)
```
Ví dụ:
```
SELECT *
FROM customers
WHERE WORKING_AREA IN('Mumbai','New York')
AND ...;
```

### BETWEEN (số, ngày tháng)
Cấu trúc
```
<column> BETWEEN <value1> AND <value2>
value1 < value2
```
Ví dụ:
```
SELECT *
FROM customers
WHERE SALARY BETWEEN 5000 AND 10000
```
### LIKE (string)
Cấu trúc:
```
<column> LIKE <value> 
```
Trong đó: <value> là một chuỗi.

Ví dụ:
```
SELECT *
FROM customers
WHERE NAME LIKE '%John%';
```

### NOT
Cấu trúc:
```
NOT ( <condition> )
<condition> NOT [ LIKE <value> | IN (<value>, <value>, ...) | BETWEEN <value1> AND <value2> ]
```
### AS
- Sử dụng sau lệnh SELECT:
Cấu trúc:
```
<column> AS <alias>
```

## Bài Tập Thực Hành
[Bài Tập Thực Hành](./BAITAPTHUCHANH.md)