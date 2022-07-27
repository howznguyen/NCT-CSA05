import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#2
df  = pd.read_csv("data.csv")
y  = df.groupby(("DiemToan")("DiemLy")("DiemHoa"))[["DiemToan"]["DiemLy"]["DiemHoa"]].sum()/3
if  y  >= 8:
    a = y.count()

if  y  >= 6.5 and y < 8:
    b = y.count()

if  y  >= 4 and y  < 6.5:
    c = y.count()

if  y < 4:
    d = y.count()

plt.pie(a, b, c, d)
plt.show()

# df = pd.read_csv("data.csv")
# gender = df.groupby("GioiTinh")["GioiTinh"].count()
# print(gender)
# plt.pie(gender, labels=gender.index)
# plt.show()



# xpoints = [1, 9 , 8 ,2,6, 8]
# ypoints = [8, 6 , 8 ,4, 8, 6]

# plt.plot(xpoints, ypoints)
# plt.show()