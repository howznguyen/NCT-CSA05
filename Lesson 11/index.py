import pandas as pd
import numpy
# df = pd.read_csv('data.csv')
# print(df)
# df['GioiTinh'] = df['GioiTinh'].replace('Male', 'Nam')
# df['GioiTinh'] = df['GioiTinh'].replace('Female', 'Nữ')
# print(df)

# df = pd.read_csv('data_err.csv')
# # print(df["DiemToan"])
# df['DiemToan'] = df['DiemToan'].replace("Bon",-1)
# print(df["DiemToan"])

# import pandas as pd
df = pd.read_csv('data.csv')
line = {'STT': 20,'Ten': 'Nguyen Van A', 'GioiTinh': 'Nam', 'NgaySinh': '2000-01-01', 'DiemToan': 5, 'DiemLy': 6, 'DiemHoa' : 7}
df = df.append(line, ignore_index=True)
print(df.info())


# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df)
# df = df.drop(4)
# print(df)