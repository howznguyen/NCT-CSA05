import pandas as pd

# DataFrame
# df = pd.read_csv('./AgeDataset.csv')

# print(df.info())

# DataFrame là một tập hợp các Series
# Series là một tập hợp dữ liệu có trong một cột

# sr1 = pd.Series([1, 2, 3, 4, 5])
# sr2 = pd.Series(['Duy','A','B','C','D'])

# df = pd.DataFrame()

# df['STT'] = sr1
# df['Ten'] = sr2

##
data = {
    'STT': pd.Series([1,2,3]),
    'Ten': pd.Series(['A','B','C'])
}
df = pd.DataFrame(data)

df.to_csv('Data.csv')
