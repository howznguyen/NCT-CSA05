# Buổi 5 - Tìm hiểu về Database - MySQL

## Database

### Database là gì ?

Database (cơ sở dữ liệu) là một tập hợp những data (dữ liệu) có liên quan với nhau .  Database được duy trì dưới dạng một tập hợp các tập tin trong hệ điều hành hay được lưu trữ trong các hệ quản trị cơ sở dữ liệu.  (Theo Wikipedia)

Những database điển hình là danh sách học sinh trong lớp, bảng chấm công nhân viên, danh sách kiểm kê hàng hoá,…

### Các loại database

Có 2 loại database cơ bản:
SQL (Structured Query Language) và NoSQL (Not Only SQL).

- SQL là viết tắt của Structured Query Language, nghĩa là ngôn ngữ truy vấn dữ liệu. Có thể coi SQL là ngôn ngữ chung mà bất cứ hệ thống cơ sở dữ liệu quan hệ (RDBMS) nào cũng phải đáp ứng, điển hình như: Oracle Database, SQL Server, MySQL…

- Cơ sở dữ liệu NoSQL là một Hệ thống quản lý dữ liệu không quan hệ (non-relational Data Management System) có lược đồ (schema) linh hoạt. Nó dễ mở rộng. Mục đích chính của việc sử dụng cơ sở dữ liệu NoSQL là dành cho các kho dữ liệu phân tán với nhu cầu lưu trữ dữ liệu lớn. NoSQL được sử dụng cho Dữ liệu lớn và ứng dụng web thời gian thực. Chẳng hạn các công ty như Twitter, Facebook và Google thu thập hàng terabyte dữ liệu người dùng mỗi ngày.

## Thực hành sử dụng SQL - MySQL

- Website SQL Online: [https://sqliteonline.com/](https://sqliteonline.com/)

### Các kiểu dữ liệu trong MySQL

Số nguyên:

- INT  (Không cần số lượng)
- BIGINT  (Không cần số lượng)

Số thực:

- FLOAT  (Không cần số lượng)
- DOUBLE  (Không cần số lượng)

Ngày tháng:

- DATE  (Không cần số lượng)
- DATETIME  (Không cần số lượng)

Chuỗi:

- VARCHAR  (Cần số lượng)
- TEXT  (Không cần số lượng)

### Tạo bảng trong MySQL

Cấu trúc
```
CREATE TABLE <TenBang> (
    <TenCot> <KieuDuLieu>,
    ...
)
```

Ví dụ:
```
CREATE TABLE HocSinh (
    MaHocSinh VARCHAR(10),
    HoTen VARCHAR(50),
    DiaChi VARCHAR(100),
    NgaySinh DATE,
    GioiTinh VARCHAR(10),
    Lop VARCHAR(10)
)
```



### Thêm/xoá cột trong bảng đã tồn tại trong MySQL

#### Thêm cột

Cấu trúc
```
ALTER TABLE <TenBang>
ADD COLUMN <TenCot> <KieuDuLieu>
```

#### Xoá cột

Cấu trúc
```
ALTER TABLE <TenBang>
DROP COLUMN <TenCot>
```

#### Thêm hoặc xoá nhiều cột

Cấu trúc
```
ALTER TABLE <TenBang>
ADD COLUMN <TenCot> <KieuDuLieu>,
ADD COLUMN <TenCot> <KieuDuLieu>,
...
DROP COLUMN <TenCot>,
DROP COLUMN <TenCot>,
```

Ví dụ:
```
ALTER TABLE HocSinh
ADD COLUMN Truong VARCHAR(50),
DROP COLUMN Lop;
```

### Thêm dữ liệu vào bảng trong MySQL


Cấu trúc
```
INSERT INTO <TenBang>  ( <TenCot>, <TenCot>, ...)
VALUES 
(<DuLieu>, <DuLieu>, ...),
(<DuLieu>, <DuLieu>, ...),
...
```

Ví dụ:
```
INSERT INTO HocSinh (MaHocSinh, HoTen, DiaChi, NgaySinh, GioiTinh, Truong)
VALUES 
('HS001', 'Nguyễn Văn A', 'Hà Nội', '1995-01-01', 'Nam', 'Võ Nguyên Giáp'),
('HS002', 'Nguyễn Văn B', 'Hà Nội', '1995-01-01', 'Nam', 'Võ Nguyên Giáp'),
('HS003', 'Nguyễn Văn C', 'Hà Nội', '1995-01-01', 'Nam', 'Võ Nguyên Giáp'),
('HS004', 'Nguyễn Văn D', 'Hà Nội', '1995-01-01', 'Nam', 'Võ Nguyên Giáp');


INSERT INTO HocSinh
VALUES 
('HS001', 'Nguyễn Văn A', 'Hà Nội', '1995-01-01', 'Nam', 'Võ Nguyên Giáp'),
('HS002', 'Nguyễn Văn B', 'Hà Nội', '1995-01-01', 'Nam', 'Võ Nguyên Giáp'),
('HS003', 'Nguyễn Văn C', 'Hà Nội', '1995-01-01', 'Nam', 'Võ Nguyên Giáp'),
('HS004', 'Nguyễn Văn D', 'Hà Nội', '1995-01-01', 'Nam', 'Võ Nguyên Giáp');

```

## Bài Tập Về Nhà

![https://i.imgur.com/1fwTg7P.png](https://i.imgur.com/1fwTg7P.png)

Trên đây là một sơ đồ của các bảng cần được chuyển thành MySQL:

- Hãy tạo ra các bảng này trong MySQL ( Sử dụng các kiểu dữ liệu cho từng cột sao cho hợp lý).
- Thêm 10 dòng dữ liệu vào các bảng.

**Lưu Ý:** File bài tập sẽ lưu code vào file SQL và push lên repository bài tập của các bạn.
