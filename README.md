# 大專校務資訊公開平臺

## 資料簡介

本專案原始資料取自教育部建置之[大專校院校務資訊公開平臺](https://udb.moe.edu.tw/)，資料類型涵蓋—學生類、教職類、研究類、校務類、財務類、教育統計等。取得原始資料後，進行初步資料處理釋出可供分析使用之資料，後續再依據研究需求建構相關分析指標。

## 資料使用說明

### 資料取得

本專案之資料公開釋出於 Dagshub 檔案託管平台，資料處理過程之原始碼與釋出資料版本控制紀錄分別以 git 和 dvc 進行管理並開源分享，可自行下載取用。
提供之資料可分為四種使用情境：

- 原始資料檔 (raw)：自公開平臺下載之原始資料，僅作為備份使用，無額外處理。
- 資料分析用 (stage1)：對原始資料之欄位格式進行調整、遺漏值設定、encoding 統一使用 `utf8`、年份相關欄位轉為西元制，並依據原始表單名稱個別儲存。
- 研究專案分析用 (stage2)：依個別研究專案之目的建構之研究資料，可能涉及跨表單合併、欄位運算、模型建構等行為。可供相關領域研究者參考使用。
- 常用評量指標 (index)： 本專案參考過去研究、評估報告常使用到的研究指標，依照定義加以建構之評量指標，可併入分析資料使用。

以上各類型資料皆存於專案的 data 資料夾內，可以分別下載，或是參考下方「快速使用」的介紹， `clone` 整個專案來使用。

#### 快速使用

以下說明將會使用 git 和 python 來介紹，請先行安裝和設定。

首先，透過 git 下載專案：

```
git clone https://github.com/hswei0/HEDB.git
```

下載 dvc 和 dagshub 套件，並記得將工作路徑轉換到專案的資料夾

```
pip install dagshub
pip install dvc
```

最後，透過 `dvc pull` 提取資料

```
dvc pull -q -r origin
```

操作完畢後，資料檔會儲存於本機專案資料夾的 data 資料夾中，並依前段使用情境的分類，存於各資料夾中，可依需求直接使用。

### 欄位說明

以下為校務資訊公開平台上的資料類別以及所有資料表：

|                                   研究類                                   |                                        校務類                                        |                          財務類                          |                                    教職類                                    |                               學生類                               |
| :-------------------------------------------------------------------------: | :----------------------------------------------------------------------------------: | :-------------------------------------------------------: | :--------------------------------------------------------------------------: | :-----------------------------------------------------------------: |
|   研1.學校承接各單位資助「各類計畫經費」及其每師平均承接金額-以「校」統計   |            校1-1.本國籍日間學士班以下學費、雜費收費基準-以「系(所)」統計            |  財1-1.國立學校可用資金、本年度現金增減情形-以「校」統計  |                      教1-1.專任教師數-以「系(所)」統計                      |             學1-1.正式學籍在學學生人數-以「系(所)」統計             |
| 研2.學校承接各單位資助「產學合作」計畫經費及其每師平均承接金額-以「校」統計 | 校1-2.日間學士班以下學費、雜費收費基準-以「學院」統計 (111學年度起改以校1-3呈現公布) |     財1-2.國立學校學雜費收入占總收入比率-以「校」統計     |                        教1-2.專任教師數-以「校」統計                        |         學1-2.正式學籍在學學生人數-以「校(含學制班別)」統計         |
|               研3.學校申請專利、新品種及授權件數-以「校」統計               |                校1-3.日間學士班以下學費、雜費收費基準-以「學院」統計                |        財1-3.國立學校負債占總資產比率-以「校」統計        |                   教1-3.專任教師數-以「校(編制內外)」統計                   |     學2-1.畢業生數及其取得輔系、雙主修資格人數-以「系(所)」統計     |
|              研4.學校各種智慧財產權衍生運用總金額-以「校」統計              |            校2.日間學士班以下專業必、選修實際開設學分數-以「系(所)」統計            |              財1-4.國立學校財務報表公告網址              |              教1-4.專任教師數-以「校(編制內外、年齡組別)」統計              | 學2-2.畢業生數及其取得輔系、雙主修資格人數-以「校(含學制班別)」統計 |
|   研5.專任教師獲資助「學術研究」計畫經費及其每師平均承接金額-以「校」統計   |                   校3.日間學士班以下畢業學分結構-以「系(所)」統計                   |          財1-5.國立學校財務相關比率-以「校」統計          |               教1-5.專任教師數-以「校(編制內外、學位別)」統計               |       學2-3.畢業授予學位之中英文名稱及人數表-以「系(所)」統計       |
|                        研6.學校衍生企業-以「校」統計                        |         校4.日間學士班以下學校課程授課人數及其比率-以「校(含學制班別)」統計         | 財1-6.查核國立各校財務狀況結果及追蹤辦理情形-以「校」統計 |                      教2-1.兼任教師數-以「系(所)」統計                      |           學2-4.畢業碩、博士學位論文資料-以「系(所)」統計           |
|                   研7.學校合作企業新事業部門-以「校」統計                   |                             校5.圖書館統計-以「校」統計                             |  財2-1.私立學校可用資金、本學年現金增減情形-以「校」統計  |                        教2-2.兼任教師數-以「校」統計                        |       學2-5.畢業碩、博士學位論文資料-以「校(含學制班別)」統計       |
|                                                                            |             校6.近3學年度學校購買圖書資料費及其每生平均經費-以「校」統計             |     財2-2.私立學校學雜費收入占總收入比率-以「校」統計     |                    教3-1.外籍專任教師數-以「系(所)」統計                    |           學3-1.境外學位生數及其在學比率-以「系(所)」統計           |
|                                                                            |                           校7.校舍及校地面積-以「校」統計                           |        財2-3.私立學校負債占總資產比率-以「校」統計        |                      教3-2.外籍專任教師數-以「校」統計                      |            學3-2.外國學生數及其在學比率-以「系(所)」統計            |
|                                                                            |                      校8.提供學生住宿人數及其比率-以「校」統計                      |              財2-4.私立學校財務報表公告網址              |                 教4-1.專任教師每週授課時數-以「系(所)」統計                 |          學3-3.僑生、港澳生數及其在學比率-以「系(所)」統計          |
|                                                                            |                   校9.提供一年級學生住宿人數及其比率-以「校」統計                   |          財2-5.私立學校財務相關比率-以「校」統計          |                   教4-2.專任教師每週授課時數-以「校」統計                   |       學3-4.大陸地區來臺學位生數及其在學比率-以「系(所)」統計       |
|                                                                            |            校10.獲弱勢學生助學計畫補助之受惠學生人數及其比率-以「校」統計            |          財2-6.私立學校各項收入情形-以「校」統計          |                       教5.日間學制生師比-以「校」統計                       |                 學3-5.畢業境外生數-以「系(所)」統計                 |
|                                                                            |                校11.學校以「自籌經費」提供學生之助學金額-以「校」統計                |        財2-7.私立學校各項經常支出情形-以「校」統計        |                 教6.近3學年度專任教師數增減比率-以「校」統計                 |             學3-6.畢業境外生數-以「校(含學制班別)」統計             |
|                                                                            |                           校12.學雜費減免人數-以「校」統計                           |        財2-8.私立學校各項資本支出情形-以「校」統計        |              教7.專任教師升等通過人數及其通過比率-以「校」統計              |    學3-7.境外學位生數(依身分類別呈現)- 以「校(含學制班別)」統計    |
|                                                                            |              校13.私立學校法人董事、監察人名單及其任期資訊-以「校」統計              | 財2-9.查核私立各校財務狀況結果及追蹤辦理情形-以「校」統計 |                     教8.專、兼任輔導人員數-以「校」統計                     |    學4.日間學士班以下申請延長修業年限之延修生數-以「系(所)」統計    |
|                                                                            |                  校14.學校課程、採購及校務資訊公開網址-以「校」統計                  |        財2-10.私立學校收支餘絀情形表-以「校」統計        | 教9. 私立學校編制內專任教師平均支給數額與公立學校支給數額比較表-以「校」統計 |        學5.日間學制本國學生出國進修交流人數-以「系(所)」統計        |
|                                                                            |             校15.學校開設全外語授課之院、系所、學位學程-以「系(所)」統計             |        財2-11.私立學校財務比率及燈號-以「校」統計        |    教10. 編制外專任教師平均支給數額與公立學校支給數額比較表-以「校」統計    |                學6.修讀校際選課人次-以「系(所)」統計                |
|                                                                            |         校16.私立學校校長、董事會成員之配偶及三親等任職學校人數-以「校」統計         |                                                          |                 教11. 編制外專任教師數及其比率-以「校」統計                 |                  學7.修讀輔系人次-以「系(所)」統計                  |
|                                                                            |                                                                                      |                                                          |             教12. 學校學術主管不符合聘任資格統計表-以「校」統計             |                 學8.修讀雙主修人次-以「系(所)」統計                 |
|                                                                            |                                                                                      |                                                          |                   教13.私立學校兼任教師鐘點費-以「校」統計                   |               學9.學校雙聯合作案件數-以「系(所)」統計               |
|                                                                            |                                                                                      |                                                          |         教14.公立學校、政府機關(構)退休再任私立學校人數-以「校」統計         |          學10.日間學制修讀雙聯學制學生數-以「系(所)」統計          |
|                                                                            |                                                                                      |                                                          |                      教15.兼任教師聘任情形-以「校」統計                      |           學11.學校辦理國際合作與交流資料表-以「校」統計           |
|                                                                            |                                                                                      |                                                          |                    教16.兼任教師不予再聘理由-以「校」統計                    |            學12-1.新生(含境外生)註冊率-以「系(所)」統計            |
|                                                                            |                                                                                      |                                                          |                教17.私立學校調整學術研究加給情形-以「校」統計                |        學12-2.新生(含境外生)註冊率-以「校(含學制班別)」統計        |
|                                                                            |                                                                                      |                                                          |                  教18.私立學校積欠教師薪資情形-以「校」統計                  |              學12-3.新生(含境外生)註冊率-以「校」統計              |
|                                                                            |                                                                                      |                                                          |                    教19.專任教師基本授課時數-以「校」統計                    |         學13-1.於學年底處於休學狀態之人數-以「系(所)」統計         |
|                                                                            |                                                                                      |                                                          |  教20-1.專任教師實際授課時數大於規定職級之基本授課時數情形-以「系(所)」統計  |     學13-2.於學年底處於休學狀態之人數-以「校(含學制班別)」統計     |
|                                                                            |                                                                                      |                                                          |    教20-2.專任教師實際授課時數大於規定職級之基本授課時數情形-以「校」統計    |                  學14-1.退學人數-以「系(所)」統計                  |
|                                                                            |                                                                                      |                                                          |               教21-1.專任教師減授授課時數情形-以「系(所)」統計               |              學14-2.退學人數-以「校(含學制班別)」統計              |
|                                                                            |                                                                                      |                                                          |                 教21-2.專任教師減授授課時數情形-以「校」統計                 |   學15.在學學生參與競賽、論文出版等成效-以「校(含學制班別)」統計   |
|                                                                            |                                                                                      |                                                          |                                                                              |         學16.學士班以下就學穩定率-以「校(含學制班別)」統計         |
|                                                                            |                                                                                      |                                                          |                                                                              |          學17.獎助生及勞僱型學生兼任助理人數-以「校」統計          |
|                                                                            |                                                                                      |                                                          |                                                                              |           學18.學校執行工讀及生活助學金情形-以「校」統計           |
|                                                                            |                                                                                      |                                                          |                                                                              |        學19.兼任助理平均每月支給金額人數統計表-以「校」統計        |
|                                                                            |                                                                                      |                                                          |                                                                              |                 學20.學生實習情形-以「系(所)」統計                 |
|                                                                            |                                                                                      |                                                          |                                                                              |            學21.學生實習機構及權益保障-以「系(所)」統計            |

#### 欄位檢視與資料探索

若欲細看本專案整理過後 (stage1) 各資料表的欄位內容與描述統計結果，可於 dagshub 網頁點選 [notebooks/explore-data.ipynb](https://dagshub.com/hsuwei/HEDB/src/beta-release/notebooks) 檔案，開啟後點擊右上角 `Open in Colab`，便可開啟 google colab ，執行完環境設定語法後，即可線上進行資料檢視與相關分析，相關檔案則會存於個人google drive。

### 檔案架構

    ├── LICENSE
    ├── README.md    <- 專案說明文件
    ├── data.dvc       <- data 版控工具
    ├── man.dvc       <- manual 版控工具
    ├── data
    │   ├── raw        <- The original data.
    │   ├── stage1     <- The datasets for analyse.
    │   ├── stage2     <- The data for research.
    │   └── index      <- 校務分析指標
    │
    ├── man
    │   ├── raw           <- 原始資料使用說明(codebook)
    │   └── release       <- 人工調整後之資料使用說明(codebook)
    │
    ├── notebooks      <- Jupyter notebooks 主要為資料探勘和初步分析
    │
    ├── references     <- 相關規定和參考文件
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── desc           <- 描述性資料分析
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── pyproject.toml     <- The requirements file for reproducing the analysis environment (`poetry`)
    │
    ├── src                    <- Source code for use in this project.
    │   ├── __init__.py          <- Makes src a Python module
    │   │
    │   ├── data                 <- Scripts to download or generate data
    │   │   ├── __init__.py
    │   │   ├── download_data.py   <- 下載原始資料
    │   │   ├── gen_codebook.py    <- 產生 codebook
    │   │   └── make_stage1.py     <- stage1 資料處理與輸出
    │   │
    │   ├── models         <- 建立分析指標
    │   │   ├──__init__.py
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       ├── __init__.py
    │       └── visualize.py
