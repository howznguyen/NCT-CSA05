# Bài 7 - Truy Xuất Dữ Liệu (Nâng Cao) trong SQL


## File SQL Countries.sql
[countries.sql](./countries.sql)

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


### SUM(), MAX(), MIN(), COUNT(), AVG()

Cấu trúc:
```
SELECT [MIN(<column>)||MAX(<column>)||SUM(<column>)||COUNT(<column>)||AVG(<column>)]
```

### HAVING

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