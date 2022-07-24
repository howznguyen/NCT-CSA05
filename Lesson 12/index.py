import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



df = pd.read_csv("data.csv")
gender = df.groupby("GioiTinh")["GioiTinh"].count()
print(gender)
plt.pie(gender, labels=gender.index)
plt.show()



# xpoints = [1, 9 , 8 ,2,6, 8]
# ypoints = [8, 6 , 8 ,4, 8, 6]

# plt.plot(xpoints, ypoints)
# plt.show()