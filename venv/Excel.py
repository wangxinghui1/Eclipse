import pandas as pd
from pathlib import Path
#选择合并路径
EX_dir=Path("C:\Ex")
#利用glob方法获取所有Excel list
ex_files=EX_dir.glob('*.xlsx')
#创建pandas表格容器dataFrame
df=pd.DataFrame()
#遍历Excel文件，读取表格数据添加到pandas中
for xlsx in ex_files:
   data=pd.read_excel(xlsx,)
   #不断的读取并添加数据
   df=df.append(data)
#将所有数据写入到新的数据中去
df.to_excel(EX_dir,"OB.xlsx")
