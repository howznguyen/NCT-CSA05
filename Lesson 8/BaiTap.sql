CREATE TABLE `BOOK` (
  `IDBOOK` bigint PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `IDCATEGORY` varchar(50),
  `TITLE` varchar(255) NOT NULL,
  `AUTHOR` varchar(50) NOT NULL,
  `PRICE` float NOT NULL,
  `DESCRIPTION` text NOT NULL
);

CREATE TABLE `CATEGORY` (
  `IDCATEGORY` varchar(50) PRIMARY KEY NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `DESCRIPTION` text NOT NULL
);

CREATE TABLE `INVOICE` (
  `IDINVOICE` bigint PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `TOTAL` float,
  `CREATEDATE` datetime
);

CREATE TABLE `DETAILINVOICE` (
  `IDDETAILINVOICE` bigint PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `IDINVOICE` bigint,
  `IDBOOK` bigint,
  `AMOUNT` bigint
);


INSERT INTO CATEGORY VALUES 
('C001', 'Tiểu thuyết', 'Tiểu thuyết'),
('C002', 'Truyện ngắn', 'Truyện ngắn'),
('C003', 'Truyện dài', 'Truyện dài'),
('C004', 'Truyện tranh', 'Truyện tranh'),
('C005', 'Khoa học', 'Khoa học'),
('C006', 'Văn học', 'Văn học'),
('C007', 'Tâm lý', 'Tâm lý'),
('C008', 'Kinh doanh', 'Kinh doanh'),
('C009', 'Kỹ năng', 'Kỹ năng'),
('C010', 'Lịch sử', 'Lịch sử'),
('C011', 'Văn nghệ', 'Văn nghệ'),
('C012', 'Thể thao', 'Thể thao'),
('C013', 'Giải trí', 'Giải trí');

INSERT INTO BOOK VALUES
(1, 'C001', 'Không gia đình', 'Hector Malot', 140000, ''),
(2, 'C001', 'Người nhà nghèo', 'Hector Malot', 180000, ''),
(3, 'C005', 'Vũ trụ diệu kỳ (Phần 1)', 'Abert Einstein', 75000, ''),
(4, 'C005', 'Vũ trụ diệu kỳ (Phần 2)', 'Abert Einstein', 75000, ''),
(5, 'C005', 'Vũ trụ diệu kỳ (Phần 3)', 'Abert Einstein', 75000, ''),
(6, 'C008', 'Mãnh lực đồng tiền', 'Lý Thông', 35000, ''),
(7, 'C009', 'Kỹ năng leo núi cơ bản', 'Trình Trình', 58000, ''),
(8, 'C010', 'Chiến thắng Điện Biên Phủ', 'Trần Lượng',46000,'');

INSERT INTO INVOICE VALUES
(1, 0, '2020-01-01 00:00:00'),
(2, 0, '2021-12-05 00:00:00'),
(3, 0, '2021-05-01 00:00:00'),
(4, 0, '2021-09-17 00:00:00'),
(5, 0, '2021-12-25 00:00:00'),
(6, 0, '2021-12-18 00:00:00'),
(7, 0, '2021-12-09 00:00:00'),
(8, 0, '2021-12-07 00:00:00');

INSERT INTO DETAILINVOICE VALUES
(1, 1, 1, 1),
(2, 1, 2, 1),
(3, 1, 3, 2),
(8, 1, 8, 1),
(9, 2, 1, 1),
(10, 2, 2, 1),
(11, 2, 3, 1),
(14, 2, 6, 1),
(15, 2, 7, 4),
(17, 3, 1, 6),
(18, 3, 2, 4),
(19, 3, 3, 6),
(20, 3, 4, 1),
(21, 3, 5, 3),
(22, 3, 6, 1),
(29, 4, 5, 2),
(34, 5, 2, 1),
(35, 5, 3, 4),
(36, 5, 4, 1),
(37, 5, 5, 2),
(40, 5, 8, 1),
(41, 6, 1, 7),
(47, 6, 7, 1),
(48, 6, 8, 1),
(49, 7, 1, 5),
(50, 7, 2, 1),
(51, 7, 3, 7),
(54, 7, 6, 1),
(55, 7, 7, 1),
(56, 7, 8, 5),
(57, 8, 1, 1),
(61, 8, 5, 2),
(62, 8, 6, 5),
(63, 8, 7, 7),
(64, 8, 8, 1);