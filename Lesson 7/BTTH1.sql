# CÂU 1
# Tính trung bình điểm của tất cả các môn học.
SELECT monhoc, AVG(diem) as diemtrungbinh
FROM class
GROUP BY monhoc

# CÂU 2
# Tính tổng học sinh trong từng lớp.
SELECT DISTINCT lop, COUNT(*) as siso
FROM class
GROUP BY lop, hoten

# CÂU 3
# Tính học sinh giỏi môn lý nhất trong lớp.
## TH cho toàn trường
SELECT hoten, lop, diem
FROM class
WHERE monhoc = 'Ly'
ORDER BY diem DESC
LIMIT 1

## TH Từng lớp
SELECT lop, MAX(diem) AS diemcaonhat
FROM class
WHERE monhoc = "Ly"
GROUP BY lop

# CÂU 4
# Tính học sinh giỏi môn hóa nhất trong lớp.
## TH cho toàn trường
SELECT hoten, lop, diem
FROM class
WHERE monhoc = 'Hoa'
ORDER BY diem DESC
LIMIT 1

## TH Từng lớp
SELECT lop, MAX(diem) AS diemcaonhat
FROM class
WHERE monhoc = "Hoa"
GROUP BY lop