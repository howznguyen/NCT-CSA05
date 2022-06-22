# Bài 7 - Truy Xuất Dữ Liệu (Nâng Cao) trong SQL


## File SQL trong bài
[countries.sql](./countries.sql)
[class.sql](./class.sql)

## Truy Xuất Dữ Liệu trong SQL

- Format câu truy vấn:
```
SELECT <columns>
FROM <table>
[WHERE <condition> <AND|OR> <condition> ....] # <condition> : <column> <operator> <value>
[GROUP BY <column>, ...]
[HAVING <condition> <AND|OR> <condition> ....]
[ORDER BY <column> [ASC|DESC], ...] # ASC: tăng dần, DESC: giảm dần
[LIMIT <number>]
```
### GROUP BY
Mệnh đề GROUP BY trong SQL cho phép bạn sắp xếp các hàng của truy vấn theo nhóm. Các nhóm được xác định bởi các cột mà bạn chỉ định trong mệnh đề GROUP BY. Thông thường, GROUP BY được sử dụng để tính tổng theo điều kiện, đếm bản ghi thỏa mãn điều kiện nào đó hoặc tìm dữ liệu MIN, MAX.


Cấu trúc:
```
GROUP BY <column>, ...
```

Ví dụ:
```
GROUP BY country_code, country_name
```


### SUM(), MAX(), MIN(), COUNT(), AVG()

Cấu trúc:
```
SELECT [MIN(<column>)||MAX(<column>)||SUM(<column>)||COUNT(<column>)||AVG(<column>)]
```

Ví dụ:
```
SELECT SUM(population)
```

### HAVING
Mệnh đề HAVING được dùng kết hợp với mệnh đề GROUP BY trong SQL để giới hạn nhóm các hàng trả về, chỉ khi điều kiện được được đáp ứng là TRUE.

Cấu trúc:
```
HAVING <condition> <AND|OR> <condition> ....
```

Ví dụ:
```
HAVING AVG(diem) > 7
```

### Bài tập thực hành

#### Bài 1
Dùng file Class: [class.sql](./class.sql)

Câu hỏi:
- Tính trung bình điểm của tất cả các môn học.
- Tính tổng học sinh trong trừng lớp.
- Tính học sinh giỏi môn lý nhất trong lớp.
- Tính học sinh giỏi môn hóa nhất trong lớp.

Đáp án: [BTTH1.sql](./BTTH1.sql)

### Bài Tập Về Nhà
Dùng file Class: [countries.sql](./countries.sql)

Câu hỏi:
- Tính số lượng nước nằm trong 1 `region`
- Tính số lượng `subregion` nằm trong 1 `region`
- Hiển thị tên các nước dưới nam bán cầu
- Số lượng các đồng tiền được sử dụng trong 1 `region`
- Hiển thị tên các nước có kinh độ từ -20 đến 61
- Hiển thị tên các `subregion` có kinh độ từ -20 đến 61