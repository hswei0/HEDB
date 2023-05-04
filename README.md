HEDB
====

大專校庫資料整理方案

Instructions
------------

### Commit Message 規範

- 寫下「為什麼」你要作這樣的異動，而不是單單只記錄下你做了「什麼」異動。Commit Message 最好兼俱 Why 及 What，讓日後進行維護人員更快進入狀況。
- 獨立 Commit 每個不同意義的異動，這樣 commit 訊息才會跟異動的程式碼有關聯。

格式說明

![Commit Message 規範範例解析](https://4.bp.blogspot.com/-HdNhJQb0D94/XMvqErOYGLI/AAAAAAAAAQ8/FQiuZsG7TT0WcQ8Q4zcccHCsuBOEDrouACLcBGAs/s1600/222.png)

Header

* **type** 代表 commit 的類別：feat, fix, docs, style, refactor, test, chore，**必要欄位**。
  * Type 是用來告訴進行 Code Review 的人應該以什麼態度來檢視 Commit 內容
  * 依NERDA資料庫工作性質調整後的type list:
    * feat: 新增/修改功能 (feature)。
    * fix: 修補 bug (bug fix)。
    * docs: 文件 (documentation)。
    * style: 格式 (不影響程式碼運行的變動 white-space, formatting, missing semi colons, etc)。
    * refactor: 重構 (既不是新增功能，也不是修補 bug 的程式碼變動)。
    * revert: 撤銷回覆先前的 commit 例如：revert: type(scope): subject (回覆版本：xxxx)。
* **scope** 代表 commit 影響的範圍，例如資料庫、控制層、模板層等等，視專案不同而不同，為可選欄位。
* **subject** 代表此 commit 的簡短描述，不要超過 50 個字元，結尾不要加句號，為必要欄位。

#### Body

本次 Commit 的詳細描述，可以分成多行，每一行不要超過 72 個字元。
說明程式碼變動的項目與原因，還有與先前行為的對比。

#### Footer

填寫任務編號（如果有的話）

BREAKING CHANGE（可忽略），記錄不兼容的變動，以 BREAKING CHANGE: 開頭，後面是對變動的描述、以及變動原因和遷移方法

### 訊息模板

以 NERDA資料庫業務內容設計

```
feat: 新增20XX年資料

    目標：
    - 加入新年度資料
    - 修改使用說明

    調整項目：
    1. tb1新增欄位1
	2. airtable 上的說明更新

issue #110


```

Project Organization
--------------------

    ├── LICENSE
    ├── README.md    <- The top-level README for developers using this project.
    ├── data.dvc       <- Keeps the data versioned.
    ├── man.dvc       <- Keeps the manual versioned.
    ├── data
    │   ├── stage1       <- The datasets for analyse.
    │   └── raw            <- The original data.
    │
    ├── man
    │   ├── raw           <- 原始資料使用說明(codebook)
    │   └── release     <- 人工調整後之資料使用說明(codebook)
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short`-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures                 <- Generated graphics and figures to be used in reporting
    │   └── metrics.txt             <- Relevant metrics after evaluating the model.
    │   └── training_metrics.txt    <- Relevant metrics from training the model.
    │
    ├── Pipfile   <- The requirements file for reproducing the analysis environment
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── __init__.py
    │   │   └── make_dataset.py
    │   │
    │   ├── models         <- 建立分析指標
    │   │   ├──__init__.py
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       ├── __init__.py
    │       └── visualize.py

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
