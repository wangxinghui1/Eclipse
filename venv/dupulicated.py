import pandas as pd
d2=pd.read_excel('/Users/wangxinghui/Downloads/coASIN/comp.xlsx')
#创建容器
c=pd.DataFrame(d2)
#判断是否有重复
l=c[c.duplicated(subset='ASIN',keep='first')]
l.to_excel('/Users/wangxinghui/Downloads/coASIN/comp1.xlsx')