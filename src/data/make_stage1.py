"""產製 Stage1 Dataset"""
import re
from pathlib import Path
import pandas as pd
from ydata_profiling import ProfileReport


class Stage1Data():
    """生成資料清理後的檔案 (Stage1)
    """

    def __init__(self, projectRoot):
        self.projRoot = projectRoot
        self.rootRawData = self.projRoot.joinpath('data/raw')
        self.rootStage1 = self.projRoot.joinpath('data/stage1')
        self.rootStage1.mkdir(parents=True, exist_ok=True)

        # all datasets
        self.dataNames = [re.search(r'.+raw/(.+)', str(f)).group(1)
                          for f in self.rootRawData.rglob('*.csv')
                          ]

    def raw_desc(self,
                 select_type=None
                 ):
        """生成原始資料描述統計報告
        Args:
            select_type (list, optional): 欲輸出的類別—['校', '財', '教', '學', '研']. Defaults to ['all'].
            HTML檔案輸出至`report/desc/raw`
        """

        if select_type is None:
            select_type = ['all']

        root_rawDesc = self.projRoot.joinpath('reports/desc/raw')
        print(root_rawDesc)
        root_rawDesc.mkdir(exist_ok=True, parents=True)

        if select_type == ['all']:
            pattern = '*.csv'
        else:
            characters = ''.join(select_type)
            pattern = f'[{characters}]*.csv'

        filepaths = sorted(self.rootRawData.rglob(pattern))

        for fpth in filepaths:
            df = pd.read_csv(fpth,
                             dtype={'學校統計處代碼': 'string', '系所代碼': 'string'}
                             )
            fnm = fpth.stem
            profile = ProfileReport(df,
                                    title=f"{fnm} 原始資料描述統計報告",
                                    minimal=True)
            print(f'輸出{fnm}')
            # TODO: 暫時無法解決中文字輸出問題，可能得等套件更新
            profile.to_file(root_rawDesc.joinpath(f'{fnm}.html'))

    @staticmethod
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
    
    def

    def toStage1_pipeline(self):

        for fnm in self.dataNames:
            # import raw dataset
            pth = self.rootRawData.joinpath(fnm)
            df = pd.read_csv(pth,
                             dtype={'學校統計處代碼': 'string', '系所代碼': 'string'},
                             na_values=['...', '無']
                             )
            # 西元年轉換
            df = df.pipe(self.RoctoCE)

            # 檔案輸出
            df.to_csv(self.rootStage1.joinpath(fnm),
                      index=False,
                      encoding='utf8'
                      )
            print(f'{fnm} 輸出成功～')


if __name__ == "__main__":

    projRoot = Path.cwd()
    st1 = Stage1Data(projRoot)

    # 輸出 raw data 檢誤報告
    st1.raw_desc()

    # 輸出 stage1 資料
    st1.toStage1_pipeline()
