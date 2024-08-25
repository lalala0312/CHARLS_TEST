import pandas as pd
import sqlite3
#
# # 读取 .dta 文件
# df = pd.read_stata('2020/Family_Information.dta')
#
# # 连接到 SQLite 数据库（如果数据库不存在，将自动创建）
# conn = sqlite3.connect('my_database.db')
#
# # 将数据存入 SQLite 数据库，指定表名
# df.to_sql('Family_Information', conn, if_exists='replace', index=False)
#
# # 关闭数据库连接
# conn.close()
#
# print("Data has been successfully stored in the SQLite database.")


# 读取 .dta 文件
df = pd.read_stata('2020/Health_Status_and_Functioning.dta')

# 获取数据条目数量
num_rows = len(df)

print(f"Total number of rows: {num_rows}")