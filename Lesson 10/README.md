# Truy Xuất Dữ Liệu Bằng Pandas Trong Python


### Truy xuất cột của Dataframe

Lấy theo dạng tên cột:

```
import pandas as pd


## DataFrame
df = pd.read_csv('data1.csv')

## Get Column in DataFrame
print(df['GioiTinh'])
```

### Truy xuất dòng trong một cột trong DataFrame

```
import pandas as pd


## DataFrame
df = pd.read_csv('data1.csv')

## Get Column in DataFrame
print(df['GioiTinh'][8])
```

### Boolean Indexing
Kiểm tra dữ liệu theo điều kiện

```
import pandas as pd
df = pd.read_csv('data1.csv')
print(df['GioiTinh'][df['GioiTinh'] == 'Nam'])
```

### Hàm Loc truy xuất dữ liệu theo điều kiện

Tham khảo: (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)[https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html]

```
import pandas as pd
df = pd.read_csv('data1.csv')
print(df.loc[df['GioiTinh'] == 'Nam'])
```

### Hàm iLoc truy xuất dữ liệu theo điều kiện

Tham khảo: (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)[https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html]

```
import pandas as pd
df = pd.read_csv('data1.csv')
print(df.iloc[[0,1]])
```

## Bài Tập Thực Hành
Sử dụng csv của bài tập về nhà trước để làm như sau:
+ Truy xuất 1 cột của DataFrame
+ Truy xuất 1 dòng trong cột của DataFrame
+ Tạo một cột trung bình môn từ dữ có trong csv
+ Tìm kiếm dữ liệu theo điều kiện
    + Các học sinh là Nam
    + Các học sinh là Nữ
    + Điểm Toán lớn hơn 8
    + Điểm Hoá + Điểm Lý chia 2 phải lớn hơn 5