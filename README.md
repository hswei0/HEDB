# 大專校務資訊公開平臺

## 資料簡介

本專案原始資料取自教育部建置之[大專校院校務資訊公開平臺]，資料類型涵蓋—學生類、教職類、研究類、校務類、財務類、教育統計等。[^資訊分類簡介] 取得原始資料後，進行初步資料處理釋出可供分析使用之資料，後續再依據研究需求建構相關分析指標。

[^資訊分類簡介]: 資訊分類詳情請見[網頁](https://udb.moe.edu.tw/udata/Introduction)。

<!--links-->
[大專校院校務資訊公開平臺]: https://udb.moe.edu.tw/udata/Index

## 資料使用說明

### 資料取得

本專案之資料公開釋出於 [Dagshub] 檔案託管平台，資料處理過程之原始碼與釋出資料版本控制紀錄分別以 git 和 dvc 進行管理並開源分享，可自行下載取用。
提供之資料可分為四種使用情境：

- 原始資料檔 (raw)：自公開平臺下載之原始資料，僅作為備份使用，無額外處理。
- 資料分析用 (stage1)：對原始資料之欄位格式進行調整、遺漏值設定、encoding 統一使用`utf8`、年份相關欄位轉為西元制，並依據原始表單名稱個別儲存。
- 研究專案分析用 (stage2)：依個別研究專案之目的建構之研究資料，可能涉及跨表單合併、欄位運算、模型建構等行為。可供相關領域研究者參考使用。
- 常用評量指標 (index)： 本專案參考過去研究、評估報告常使用到的研究指標，依照定義加以建構之評量指標，可併入分析資料使用。

以上各類型資料皆存於 Dagshub 之專案的 [data] 頁面中對應的資料夾內，可以分別下載，或是參考 dvc 的使用分法， `clone` 整個專案來使用。

### 欄位說明

以下為原始檔案之欄位內容，可透過 filter 等功能進一步檢視。

<iframe class="airtable-embed" src="https://airtable.com/embed/shrRLLPnxhHDN40kA?backgroundColor=purple&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>

<!--links-->
[Dagshub]: https://dagshub.com/hsuwei/HEDB
[data]: https://dagshub.com/hsuwei/HEDB/src/master/data

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


