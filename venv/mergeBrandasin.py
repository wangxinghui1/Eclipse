import pandas as pd
d1=pd.read_excel('/Users/wangxinghui/Downloads/SEProduct/A1b.xlsx')
d2=pd.read_excel('/Users/wangxinghui/Downloads/SEProduct/findresult.xlsx')
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
index=df1['ASIN'].isin(df2['ASIN'])
outfile=df1[index]
outfile.to_excel('/Users/wangxinghui/Downloads/SEProduct/outfile.xlsx',index=False,encoding='gbk')