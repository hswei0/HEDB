# 下載資料檔

import pandas as pd
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import re


# 專案路徑
# TODO: 之後調整
projRoot = Path(__file__).parents[2]
root_rawdata = projRoot.joinpath('data/raw')

# 資料種類
dtcategory = ['學生類', '教職類', '研究類', '校務類', '財務類']


dturl = 'https://udb.moe.edu.tw/udata/DetailReportList/'
dturls = [dturl + c for c in dtcategory]

# 檔案下載連結
apdx = []

for dturl in dturls:
    r = requests.get(dturl)
    soup = BeautifulSoup(r.text)
    s1 = soup.find_all(attrs={'headers': 'csv'})
    apdx0 = [ss.find('a').get('href') for ss in s1]
    apdx.extend(apdx0)

# 下載檔案

for url in apdx:
    pattern = r'file/(.+)\.\s?[\u4e00-\u9fa5]'  # 中文字前面
    # 有的還有空格
    # 表單名稱
    dtnm = re.search(pattern, url).group(1)
    print(url)
    response = requests.get('https://udb.moe.edu.tw/' + url)
    fpth = root_rawdata.joinpath(dtnm + '.csv')

    with open(fpth, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    print('Please source this file')
