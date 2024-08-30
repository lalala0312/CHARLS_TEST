import pandas as pd
import os
import sqlite3


folder_path = '2020/'
conn = sqlite3.connect('my_database.db')
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('zip'):
            continue
        file_path = root + file
        data_read = pd.read_stata(file_path)
        data_read.to_sql(file[:-4], conn, if_exists='replace', index=False)
        print(file[:-4])
        print("Data has been successfully stored in the SQLite database.")
conn.close()
print("ALL ready")


# # 读取 .dta 文件
# df = pd.read_stata('2020/Health_Status_and_Functioning.dta')
#
# # 获取数据条目数量
# num_rows = len(df)
#
# print(f"Total number of rows: {num_rows}")