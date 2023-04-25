
import pandas as pd
from pathlib import Path
import re
import os

# 製作codebook
colnm = ['欄位名稱(中)', '原始欄位名稱', '資料表名稱', '資料層級', '欄位名稱(英)', '中文值標籤',
         '序號', '型態', '簡易說明', '資料變動說明', '本單位新增', '資料涵蓋學年度']

projRoot = Path(__file__).parents[2]
root_manraw = projRoot.joinpath('man/raw')
# change cwd
os.chdir(root_manraw)
root_rawdata = projRoot.joinpath('data/raw')
# filepaths = sorted(root_rawdata.rglob('學*.csv'))
filepaths = sorted(root_rawdata.rglob('*.csv'))
for flp in filepaths:
    cdb = pd.DataFrame(columns=colnm)
    dt = pd.read_csv(flp, na_values=['...'])
    # 固定內容欄位
    try:
        cdb['原始欄位名稱'] = dt.columns
        cdb['序號'] = cdb.index + 1  # 由1開始
        cdb['型態'] = dt.dtypes.tolist()
        pattern = re.compile(r'raw/(.+)\.csv')  # 中文字前面
        filename = re.search(pattern, str(flp)).group(1)
        cdb['資料表名稱'] = filename
        if '學年度' in dt.columns:
            cdb['資料涵蓋學年度'] = ' ;'.join(dt['學年度'].unique().astype(str).tolist())
        elif '查核年度' in dt.columns:
            print(f'資料表無「學年度」欄位，以「查核年度」替代：/n {filename}')
            cdb['資料涵蓋學年度'] = ' ;'.join(
                dt['查核年度'].unique().astype(str).tolist())
        else:
            print(f'資料表無「學年度」欄位，以「年度」替代：/n {filename}')
            cdb['資料涵蓋學年度'] = ' ;'.join(dt['年度'].unique().astype(str).tolist())

        cdb['本單位新增'] = False
    except Exception as e:
        print(f'{filename} 發生錯誤')
        print(f"An exception occurred: {e}")
    cdb.to_csv(filename + '.csv', index=False)
