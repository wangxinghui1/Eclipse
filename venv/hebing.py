import pandas as pd
from pathlib import Path
#读取两个列表
d1=pd.read_excel('/Users/wangxinghui/Downloads/coASIN/brands.xlsx' )
d2=pd.read_excel('/Users/wangxinghui/Downloads/coASIN/ASINs.xlsx')
#创建容器
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
#将第二个表格加到第一个表格
c=df1.append(df2)
#打印出第三个表格
c.to_excel('/Users/wangxinghui/Downloads/coASIN/comp.xlsx')






