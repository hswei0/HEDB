
import pandas as pd
import numpy as np
from pathlib import Path
import re
import os


# Filepaths to stage 1 data
projRoot = Path.cwd().parents[1]
print(projRoot)
path_stage1 = projRoot.joinpath('data/stage1')
filepaths_s1 = sorted(path_stage1.rglob('[教學]*.csv'))


# TODO: note 轉為docstring
# Stage2: Aggregate to school-year data (on school level)

# creating stage2 folder
path_stage2 = projRoot.joinpath('data/stage2')
path_stage2.mkdir(exist_ok=True, parents=True)
file = filepaths_s1[0]

# 2-1 long to wide on '學期' (by '學年度' and '學校統計處代碼')
# TODO: 切分成不同的function來維護
# TODO: 建一個class來執行校層級資料創建功能


class SchoolStat():

    def __init__(self):
       
       
    def get_data(self):
        df = pd.read_csv(file, 
                         dtype={'學校統計處代碼': 'string', '系所代碼': 'string'}
                         )


# for file in filepaths_s1:
df = pd.read_csv(file,
                 dtype={'學校統計處代碼': 'string', '系所代碼': 'string'}
                 )
# df[['學年度', '學校統計處代碼']] = df[['學年度', '學校統計處代碼']].astype('object')
# 平均、百分比等資訊等aggregate之後再重新計算
cols_to_drop = [col for col in df.columns if ('%' in col) or (
    '平均' in col)]
df = df.drop(cols_to_drop, axis=1)
print(f'drop columns: {cols_to_drop}')
# 刪除休退學統計表
# 目前休退學人數統計表各自「以「系(所)」」為單位的表，人數加總不一致，所以刪掉
if ('休學' in f'{file}') or ('退學' in f'{file}'):
    dropcol = '在學學生數'
    df = df.drop([dropcol], axis=1)
    print(f'drop {dropcol}')

if ('學制班別' in list(df.columns)) and ('日間/進修' not in list(df.columns)):
    fltr = ['學士班(日間)', '五專', '二專(日間)']
    df = df[df['學制班別'].isin(fltr)]
elif ('學制班別' in list(df.columns)) and ('日間/進修' in list(df.columns)):
    fltr = ['二年制大學(二技)', '二專', '五專', '學士班(含四技)']
    df = df[df['日間/進修'].isin(['日間']) &
            df['學制班別'].isin(fltr)]

numeric_cols = [numcol for numcol in df.select_dtypes(include=['int', 'float']).columns
                if numcol not in ['學期', '系所代碼']]

# 有分1、2學期的資料表，依學期做long 轉wide
if ('學期' in list(df.columns)) and (numeric_cols != []):
    df = df.groupby(['學年度', '學校統計處代碼', '學期'])[numeric_cols].agg(
        lambda x: np.nan if np.all(pd.isna(x)) else x.sum())
    df.reset_index(inplace=True)
    df = df.pivot(index=['學年度', '學校統計處代碼'],
                  columns='學期', values=numeric_cols)
    df.columns = [f"{col[0]}_{col[1]}" for col in df.columns]
    df.reset_index(inplace=True)
# 如果整張表都沒有數值變項，就先不採用（跟指標較無關，或再想辦法呈現）
elif numeric_cols == []:
    filepaths_s1.remove(file)
    print('not in use: ' + f'{file.name}')
# continue
# 「以學年底狀態統計」的表，視作是第2學期的數據，變項名稱加上後綴'_2'
elif '學年底' in f'{file}':
    df = df.rename(columns={col: col+'_2' for col in df[numeric_cols]})

numeric_cols = [numcol for numcol in df.select_dtypes(include=['int', 'float']).columns
                if numcol not in ['學期', '系所代碼']]
# aggregate to school level
df = df.groupby(['學年度', '學校統計處代碼'])[numeric_cols].agg(
    lambda x: np.nan if np.all(pd.isna(x)) else x.sum())
df.reset_index(inplace=True)
csv_filename = f'{path_stage2}/{file.name}'
df.to_csv(csv_filename, index=False)


# Filepaths to stage 2 data
filepaths_s2 = sorted(path_stage2.rglob('[教學]*.csv'))


# Stage3: All stage2 datasets merged
dfs = {}
for file in filepaths_s2:
    dfs[file.name] = pd.read_csv(file)
    dfs[file.name][['學年度', '學校統計處代碼']] = dfs[file.name][[
        '學年度', '學校統計處代碼']].astype('string')  # merge的時候，校統計處代碼要先統一長度
    dfs[file.name]['學校統計處代碼'] = dfs[file.name]['學校統計處代碼'].str.zfill(4)
    dfs[file.name]['學年度'] = dfs[file.name]['學年度'].str.zfill(3)
# merge all
keys = list(dfs.keys())
merged_df = dfs[keys[0]]
for i in range(1, len(keys)):
    merged_df = pd.merge(merged_df, dfs[keys[i]], how='outer')

# creating stage3 folder
path_stage3 = projRoot.joinpath('data/stage3')
path_stage3.mkdir(exist_ok=True)

csv_filename = f'{path_stage3}/學教_merged.csv'
merged_df.to_csv(csv_filename, index=False)
