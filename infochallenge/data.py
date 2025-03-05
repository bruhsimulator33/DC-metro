import pandas as pd
# june5=pd.read_csv ('June_05_2024.csv')
# june15=pd.read_csv ('June_05_2024.csv')
# print(june5)
# print(june15)
# summeravg= pd.merge(june5,june15,on='Station Name')
# print(summeravg)

summer = pd.read_csv('tabsep.csv', delimiter="\t", encoding='utf16')
print(summer)
