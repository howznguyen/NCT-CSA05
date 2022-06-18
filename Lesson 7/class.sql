CREATE TABLE `class` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `hoten` TEXT,
    `lop` TEXT,
    `namsinh` TEXT,
    `gioitinh` TEXT,
    `monhoc` TEXT,
    `diem` FLOAT,
    `xeploai` TEXT,
    PRIMARY KEY (`id`)
);


INSERT INTO `class` (hoten, lop, namsinh, gioitinh, monhoc, diem, xeploai) 
VALUES 
('Nguyen Van A', '12A', '2000', 'Nam', 'Toan', 8, NULL),
('Nguyen Van B', '12A', '2001', 'Nam', 'Toan', 9, NULL),
('Nguyen Van C', '12B', '2002', 'Nam', 'Toan', 9.5, NULL),
('Nguyen Van A', '12A', '2000', 'Nam', 'Ly', 6, NULL),
('Nguyen Van B', '12A', '2001', 'Nam', 'Ly', 7, NULL),
('Nguyen Van C', '12B', '2002', 'Nam', 'Ly', 8.5, NULL),
('Nguyen Van A', '12A', '2000', 'Nam', 'Hoa', 5, NULL),
('Nguyen Van B', '12A', '2001', 'Nam', 'Hoa', 8, NULL),
('Nguyen Van C', '12B', '2002', 'Nam', 'Hoa', 6, NULL),
('Nguyen Van A', '12A', '2000', 'Nam', 'Anh', 3, NULL),
('Nguyen Van B', '12A', '2001', 'Nam', 'Ly', 5, NULL),
('Nguyen Van C', '12B', '2002', 'Nam', 'Ly', 7.5, NULL);