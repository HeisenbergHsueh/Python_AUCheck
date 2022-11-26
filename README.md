# python工具開發-偵測防毒伺服器運行狀態

## 使用情境說明 : 

### 公家機關的客戶方早期的防毒伺服器是各縣市局處自行架構，而客戶在這幾年面臨著資訊部門的轉型，需要對資安架構有著更進一步控制之際，他們才發現說，他們竟然不清楚目前全台灣他們所擁有的防毒伺服器的數量以及位置，因此請我公司協助撰寫此工具，幫助他們確認2件事情

### 1 : 找出座落於全台灣的防毒伺服器目前是否仍在運行

### 2 : 若確定有在運行，目前防毒伺服器的病毒碼版本為何?

## 架構邏輯說明

### Step 1 : 首先，會準備一份名為ServerList.ini的檔案給user，而由於每一台防毒server都可以透過url去下載該台防毒server的設定檔(設定檔名為 : server.ini)，因此需要請user把下載server.ini的url放到ServerList.ini中，如下圖

<img style="width: 600px;" src=https://i.imgur.com/fxKMQZO.png />

### Step 2 : 接著執行以python撰寫好的程式-AUCheck.exe，此程式便會去讀取此ServerList.ini中，user所放入的url，逐條去讀取並嘗試透過url下載server.ini，當server.ini成功下載下來，即代表此台防毒server目前仍處於運行狀態，如下圖

<img style="width: 600px;" src=https://i.imgur.com/3tZFcmw.png />

### Step 3 : 接著AUCheck.exe會去查詢server.ini文件中關於病毒碼目前版本的訊息，如下圖，由於病毒碼版本的形式共有2種，因此需要透過查詢ini的key value的方式，分別得到下圖中的P.2、P.48020000的value

<img style="width: 600px;" src=https://i.imgur.com/znhpgmq.png />

### Step 4 : 讀取完之後，AUCheck.exe會生成一份HTML檔，將結果呈現於HTML檔中，方便user查看，如下圖

<img style="width: 600px;" src=https://i.imgur.com/yyuweJP.png />

## 貢獻

### AUCheck.exe成功幫助客戶在10分鐘之內，釐清楚全台灣目前有幾台server是正常運作、幾台已經掛掉、幾台的版本需要更新，依照客戶所言，若是以人力下去一台一台找主機，恐怕需要花費至少2週