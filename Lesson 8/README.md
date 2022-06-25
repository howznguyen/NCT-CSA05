# Bài 8

# Kiến thức
### JOIN (Liên Kết Bảng)
Dùng để liên kết các bảng trong SQL.

Cú Pháp:
```
SELECT <columns>
FROM <table1>
JOIN <table2> ON <condition>
```

Ví dụ:
```
SELECT *
FROM HocSinh
JOIN Truong ON HocSinh.Truong = Truong.MaTruong
```

### ALIAS for Table
Rút gọn tên bảng trong SQL.

Cú pháp:
```
SELECT <columns>
FROM <table> <alias>
```

### UNION

Cú pháp:
```
SELECT <columns>
FROM <table1>
....
UNION
SELECT <columns>
FROM <table2>
....
```

Ví dụ:
```
SELECT *
FROM HocSinh
WHERE Truong = 'CCL'
UNION
SELECT *
FROM HocSinh
WHERE Truong = 'NH'
```

## Bài tập thực hành

Tạo các bảng như trong hình dưới và tạo dữ liệu cho từng bảng

![](https://i.imgur.com/SDRh2qL.png)