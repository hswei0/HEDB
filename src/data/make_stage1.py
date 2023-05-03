from pathlib import Path
import pandas as pd
from ydata_profiling import ProfileReport
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager


# 製作 Stage 1 datasets

projRoot = Path.cwd().parents[1]
root_stage1 = projRoot.joinpath('data/stage1')
root_stage1.mkdir(exist_ok=True)
root_rawdata = projRoot.joinpath('data/raw')


# 產製原始資料描述統計報告


def genRawDesc(select_type=['all']):
    """_summary_

    :param select_type: _description_, defaults to ['all']
    :type select_type: list, optional
    """

    root_rawDesc = projRoot.joinpath('reports/desc/raw')
    root_rawDesc.mkdir(exist_ok=True, parents=True)

    if select_type == ['all']:
        pattern = '*.csv'
    else:
        characters = ''.join(select_type)
        pattern = f'[{characters}]*.csv'

    filepaths = sorted(root_rawdata.rglob(pattern))

    for fpth in filepaths:
        df = pd.read_csv(fpth,
                         dtype={'學校統計處代碼': 'string', '系所代碼': 'string'}
                         )
        fnm = fpth.stem
        profile = ProfileReport(df,
                                title=f"{fnm} 原始資料描述統計報告",
                                minimal=True)
        # 輸出速度有影響
        print(f'輸出{fnm}')
        # TODO: 暫時無法解決中文字輸出問題，可能得等套件更新
        profile.to_file(root_rawDesc.joinpath(f'{fnm}.html'))
