# Phân Tích Dữ Liệu Bằng Pandas Trong Python


## Pandas là gì ?

Pandas là một thư viện Python cung cấp các cấu trúc dữ liệu nhanh, mạnh mẽ, linh hoạt và mang hàm ý. Tên thư viện được bắt nguồn từ panel data (bảng dữ liệu). Pandas được thiết kế để làm việc dễ dàng và trực quan với dữ liệu có cấu trúc (dạng bảng, đa chiều, có tiềm năng không đồng nhất) và dữ liệu chuỗi thời gian.

## Cách Cài Đặt Pandas

```
pip install pandas
```

## Những hàm thông dụng

## read_csv()
Đọc dữ liệu từ tập tin csv

```
import pandas as pd
df = pd.read_csv('data.csv')
```

## read_excel()
Đọc dữ liệu từ tập tin excel

```
import pandas as pd
df = pd.read_excel('data.xlsx')
```

## head(<so>)
Lấy <so> dòng dữ liệu đầu tiên. Mặc định là 5 dòng.

```
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
```

## info()
Lấy thông tin từng cột và dòng dữ liệu

```
import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())
```

## to_csv()
Lưu dữ liệu thành tập tin csv

```
import pandas as pd
df = pd.read_csv('data.csv')
df.to_csv('data1.csv')
```

## to_excel()
Lưu dữ liệu thành tập tin excel

```
import pandas as pd
df = pd.read_csv('data.csv')
df.to_excel('data1.xlsx')
```

## Bài Tập Thực Hành

Tạo một DataFrame là một danh sách học sinh
Trong có các cột STT,HoTen,NgaySinh,GioiTinh
Rồi sau đó lưu dữ liệu của DataFrame đó thành file 'hocsinh.csv'