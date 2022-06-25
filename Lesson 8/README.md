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

Câu hỏi:
- Xuất danh sách của 1 hoá đơn bất kì.
```
SELECT TITLE, AUTHOR, PRICE, AMOUNT, PRICE * AMOUNT AS 'TOTAL'
FROM DETAILINVOICE DI
JOIN BOOK B ON DI.IDBOOK = B.IDBOOK
WHERE idinvoice = 1
```

- Xuất danh sách các hoá đơn có tên sách là 'Không gia đình'.
```
SELECT DI.IDINVOICE ,TITLE, AUTHOR, PRICE, AMOUNT, PRICE * AMOUNT AS 'TOTAL'
FROM DETAILINVOICE DI
JOIN BOOK B ON DI.IDBOOK = B.IDBOOK
WHERE TITLE = 'Không gia đình'
```

- Xuất danh sách các hoá đơn có sách giá trị từ 100000 đến 200000.
```
SELECT DI.IDINVOICE 
FROM DETAILINVOICE DI
JOIN BOOK B ON DI.IDBOOK = B.IDBOOK
WHERE PRICE BETWEEN 100000 AND 200000
GROUP BY IDINVOICE
```

## Bài tập về nhà
Sử dụng cấu trúc SQL sau:
[BaiTap.sql](./BaiTap.sql)

Câu hỏi:
- Tính tổng số lượng sách của các hoá đơn.
- Tính tổng tiền của các hoá đơn.
- Tính các hoá đơn có sách có chủ đề là 'Khoa học' hoặc 'Văn học'.
- Tính số lượng sách đã được mua nhiều nhất trong năm 2021.
- Thêm 1 dòng Chi tiết hoá đơn vào 1 Hoá đơn có sẵn và cập nhật lại tổng tiền của hoá đơn đó.