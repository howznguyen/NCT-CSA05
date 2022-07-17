# Truy Xuất Dữ Liệu Bằng Pandas Trong Python


## Replace DataFrame
Sử dụng DataFrame.replace () trong pandas, bạn có thể thay thế các hàng đã chọn bằng các giá trị khác.


Ví dụ:

```
import pandas as pd
df = pd.read_csv('data.csv')
df['GioiTinh'] = df['GioiTinh'].replace('Male', 'Nam')
df['GioiTinh'] = df['GioiTinh'].replace('Female', 'Nữ')
```


## at, iat 
Truy xuất dữ liệu trong DataFrame theo vị trí của dòng và cột

Ví dụ:
```
import pandas as pd
df = pd.read_csv('data.csv')
print(df.iat[4,3])
print(df.at[4,'GioiTinh'])
```

## append
Thêm dòng dữ liệu vào DataFrame

Ví dụ
```
import pandas as pd
df = pd.read_csv('data.csv')
line = {'STT': 20,'Ten': 'Nguyen Van A', 'GioiTinh': 'Nam', 'NgaySinh': '2000-01-01', 'DiemToan': 5, 'DiemLy': 6, 'DiemHoa' : 7}
df = df.append(line, ignore_index=True)
print(df.info())
```

## drop
Xóa dòng dữ liệu trong DataFrame

Ví dụ:
```
import pandas as pd
df = pd.read_csv('data.csv')
df.drop(4)
```

## Bài tập thực hành:
1. Thay đổi giá trị của 'Nam' và 'Nữ' thành 0 và 1.
2. Thêm 10 dòng dữ liệu vào DataFrame.
3. Xoá 3 từ dòng 5 đến dòng 8 của DataFrame.