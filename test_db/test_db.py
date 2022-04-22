import sqlite3
import pandas as pd
from tqdm import tqdm
filepath = "/home/chy/workspace/trajectory-predictor/240test.db.txt"
db_name = "240_test_with_240dpi.db"
# filepath = "/home/chy/workspace/trajectory-predictor/240test_mm.db.txt"
# db_name = "240_test_mm.db"
points = open(filepath, 'r').readlines()
con = sqlite3.connect(db_name)
cur = con.cursor()
# create_table_sql = "CREATE TABLE estimate_date (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, points TEXT, historyPoints TEXT, expected_results TEXT,  recognition_results TEXT, handwriting_version INTEGER NOT NULL);"
create_table_sql = 'CREATE TABLE `estimate_date` (`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, `points` TEXT, `historyPoints` TEXT, `picture` TEXT, `expected_results` TEXT, `difficulty` INTEGER, `back_test_results` INTEGER, `recognition_results` TEXT, `model` INTEGER, `language` TEXT, `back_test_time` TEXT, `recognition_time` INTEGER, `handwriting_version` INTEGER NOT NULL, `engine_version` TEXT, `device_name` TEXT, `device_system` TEXT, `resolving_power` TEXT, `dpi` REAL, `dpiF` REAL, `dpiX` REAL, `dpiY` REAL, `status` INTEGER, `mark_time` TEXT, `ade` REAL, `aae` REAL, `mse` REAL);'
cur.execute(create_table_sql)
con.commit()
cur = con.cursor()
header = ['id', 'points', 'historyPoints', 'picture', 'expected_results',
       'difficulty', 'back_test_results', 'recognition_results', 'model',
       'language', 'back_test_time', 'recognition_time', 'handwriting_version',
       'engine_version', 'device_name', 'device_system', 'resolving_power',
       'dpi', 'dpiF', 'dpiX', 'dpiY', 'status', 'mark_time', 'ade', 'aae',
       'mse']
features = ','.join(header)
feature_values = ','.join(['?'] * len(header))
insert_data_sql = f"INSERT into estimate_date VALUES ({feature_values});"
print(insert_data_sql)
insert_points = ""
num_split = 2
idx = 1
for line in tqdm(points):
    if line == '0\n':
        num_split -= 1
    insert_points = insert_points + line
    if num_split == 0:
        data_values = (idx, insert_points, insert_points, 'picture', '',
        1, 1, '', 1,
        'language', 'back_test_time', 1, 1,
        'engine_version', 'device_name', 'device_system', 'resolving_power',
        240, 240, 240, 240, 1, 'mark_time', 0, 0,
        0)
        cur.execute(insert_data_sql, data_values)
        insert_points = ""
        num_split = 2
        idx += 1
        con.commit()

data_values = (idx, insert_points, insert_points, 'picture', '',
1, '', '', 1,
'language', 'back_test_time', 1, 1,
'engine_version', 'device_name', 'device_system', 'resolving_power',
240, 240, 240, 240, 1, 'mark_time', 0, 0,
0)
cur.execute(insert_data_sql, data_values)
con.commit()
