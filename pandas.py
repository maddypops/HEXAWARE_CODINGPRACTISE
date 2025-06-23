import openpyxl
import pandas as pd
data = {'name':['tom','nick','krish','jack'],'age':[23,45,58,78]}
df = pd.DataFrame(data)
print(df)
df.to_excel(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\hexaware.xlsx",index=False)
df = pd.read_excel(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\hexaware.xlsx")
print(df)