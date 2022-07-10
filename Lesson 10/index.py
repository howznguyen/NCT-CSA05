import pandas as pd
df = pd.read_csv('data1.csv')
df["DiemToan"] = pd.to_numeric(df["DiemToan"])
df["DiemLy"] = pd.to_numeric(df["DiemLy"])
df["DiemHoa"] = pd.to_numeric(df["DiemHoa"])

df["DiemTrungBinh"] = (df["DiemToan"] + df["DiemLy"] + df["DiemHoa"]) / 3


df.to_csv("data_new.csv")
print(df)