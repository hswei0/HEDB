"""產製 Stage1 Dataset"""
import re
from pathlib import Path
import pandas as pd
from ydata_profiling import ProfileReport


projRoot = Path.cwd()
root_stage1 = projRoot.joinpath('data/stage1')
root_stage1.mkdir(exist_ok=True)
root_rawdata = projRoot.joinpath('data/raw')


def RawDesc(select_type=None):
    """生成原始資料描述統計報告

    Args:
        select_type (list, optional): 欲輸出的類別—['校', '財', '教', '學', '研']. Defaults to ['all'].
        HTML檔案輸出至`report/desc/raw`
    """

    if select_type is None:
        select_type = ['all']

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


def import_data(dt_path):
    """匯入原始資料

    Args:
        dt_path (str or path): 原始資料檔所屬資料夾路徑，常用設定為`data/raw`

    Returns:
        DataFrame: 代碼設定為文字，`...`、`無`設定為遺漏值
    """
    df = pd.read_csv(dt_path,
                     dtype={'學校統計處代碼': 'string', '系所代碼': 'string'},
                     na_values=['...', '無']
                     )
    return df


def RoctoCE(dataframe):
    """年度相關欄位轉成西元年

    Args:
        dataframe (DataFrame): 欲處理之資料

    Returns:
        DataFrame: 年度欄位轉換為西元年
    """
    flt = dataframe.columns[dataframe.columns.str.contains('年度$')]
    dataframe[flt] = dataframe[flt].apply(lambda yr: yr + 1911)
    return dataframe


def export_data(dataframe, stage1_path):
    """處理後之stage1 data 輸出

    Args:
        dataframe (DataFrame): 欲輸出之資料
        stage1_path (str or path): 輸出檔案欲儲存之路徑
    """
    dataframe.to_csv(stage1_path, index=False, encoding='utf8')
    print(f'{stage1_path} 輸出成功～')


def dataPipeline(dataset_names):
    """Stage1 資料清理流程

    Args:
        dataset_names (list): 預處理資料之路徑。以 list 型態輸入所有要處理的資料檔案路徑
    """
    for fnm in dataset_names:
        tbnm = fnm
        pth = root_rawdata.joinpath(tbnm)
        df = import_data(pth)
        df = df.pipe(RoctoCE)
        outpath = root_stage1.joinpath(tbnm)
        export_data(df, outpath)


if __name__ == "__main__":

    # 產生原始資料檢誤內容
    # RawDesc()

    dfs = [re.search(r'.+raw/(.+)', str(f)).group(1)
           for f in root_rawdata.rglob('*.csv')]
    dataPipeline(dfs)
