import configparser
import os
import urllib
import urllib.request
import ssl
import time
import json
import numpy

print("======= AU Check Program (start) =======", flush=True)

config = configparser.ConfigParser()

#讀取 ini檔
config.read('ServerList.ini')

#設定一個新的空陣列
ServerUrlList = []

#將 section 為 ApexOneServerList 下的 value 給放進 ServerUrlList 的陣列中
if config.has_section('ApexOneServerList') == True:
    data_points = config.options('ApexOneServerList')

    for var in data_points:
        ServerUrlList.append(config.get('ApexOneServerList', var))

# print(ServerUrlList)

# 要設定 ssl certificate的部分，由 default 改成 unverified
ssl._create_default_https_context = ssl._create_unverified_context

# 得到 ini 檔中，url的數量(==陣列長度)
ServerUrlListlength = len(ServerUrlList)

# 將 Server 的 url list 進行 split，只保留 Server 的 domain Name，並將其放入新的陣列

ServerNameArray = []

for i in range(ServerUrlListlength):
    ServerNameSplit = ServerUrlList[i].split('/')
    ServerName = ServerNameSplit[2]
    # print("Server Name is : " + ServerName)

    ServerNameArray.append(ServerName)

# 使用urlretrieve下載ini檔
for i in range(ServerUrlListlength):
    try:
        urllib.request.urlretrieve(ServerUrlList[i], str(i+1) + "_server.ini")
    except:
        print(ServerNameArray[i] + " unable to download server.ini")


StoreServerAndPatternInfo = []
ServerInfoStr = []

for i in range(ServerUrlListlength):

    fileName = str(i+1) + "_server.ini"

    if os.path.isfile(fileName):
        fp = open(fileName)

        config_p = configparser.ConfigParser()

        config_p.readfp(fp)
        print(fileName)

        # Config_Virus_Pattern = config['PATTERN']['P.4']
        # Config_SmartScanVirus_Pattern = config['PATTERN']['P.48020000']

        if config_p.has_option('PATTERN','P.4') == True:
            VirusPatternTempStr = config_p['PATTERN']['P.4']
            VirusPatternStrArray = VirusPatternTempStr.split(',')
            VirusPatternStr = VirusPatternStrArray[1].strip(" ")
            VirusPattern = VirusPatternStr[0:2] + "." + VirusPatternStr[2:5] + "." + VirusPatternStr[5:]
        else:
            VirusPattern = "Check Conventional Pattern Failed"
            print("Check Conventional Pattern Failed")

        # print("======= AU Check (Virus Pattern) ======= \r\n")
        # print("Virus Pattern is : " + VirusPattern)

        if config_p.has_option('PATTERN','P.48020000') == True:
            SmartScanVirusPatternTempStr = config_p['PATTERN']['P.48020000']
            SmartScanVirusPatternStrArray = SmartScanVirusPatternTempStr.split(',')
            SmartScanVirusPatternStr = SmartScanVirusPatternStrArray[1].strip(" ")
            SmartScanVirusPattern = SmartScanVirusPatternStr[0:2] + "." + SmartScanVirusPatternStr[2:5] + "." + SmartScanVirusPatternStr[5:]
        else:
            SmartScanVirusPattern = "Check Smart Scan Pattern Failed"
            print("Check Smart Scan Pattern Failed")
            

        
            
        # print("======= AU Check (Smart Scan Virus Pattern) ======= \r\n")
        # print("Smart Scan Virus Pattern is : " + SmartScanVirusPattern)

        ServerInfoStr.append(ServerNameArray[i])
        ServerInfoStr.append(VirusPattern)
        ServerInfoStr.append(SmartScanVirusPattern)
        fp.close()
        time.sleep(1)
    else:
        ServerInfoStr.append(ServerNameArray[i])
        ServerInfoStr.append("can't download server.ini")
        ServerInfoStr.append("can't download server.ini")
        time.sleep(1)

StoreServerAndPatternInfo.append(ServerInfoStr)
print(StoreServerAndPatternInfo)

StoreServerAndPatternInfoArr = numpy.array(StoreServerAndPatternInfo).flatten()

StoreServerAndPatternInfoLength = len(StoreServerAndPatternInfoArr)

# print(StoreServerAndPatternInfoArr)
# print(StoreServerAndPatternInfoLength)

text1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./bootstrap4/css/bootstrap.min.css">
    <title>Virus Pattern / Smart Scan Virus Pattern Check</title>
</head>
<body>

    <div class="container-fluid">
        <div class="row text-center">
            <div class="col-1"></div>
            <div class="col-8">
                <table class="table table-striped">
                    <thead>
                      <tr>
                        <th scope="col">Server Name</th>
                        <th scope="col">Conventional Virus Pattern</th>
                        <th scope="col">Smart Scan Virus Pattern</th>
                      </tr>
                    </thead>
                    <tbody>
'''

text2 = ''

for i in range(0, StoreServerAndPatternInfoLength, 3):
    text2TempStr = '<tr><td>' + StoreServerAndPatternInfoArr[i] + '</td><td>' + StoreServerAndPatternInfoArr[i+1] + '</td><td>' + StoreServerAndPatternInfoArr[i+2] + '</td><tr>'
    text2 += text2TempStr


text3 = '''
</tbody>
                  </table>
            </div>
            <div class="col-1"></div>
        </div>
    </div>

    <script src="./jquery-3.3.1.slim.min.js"></script>
    <script src="./bootstrap4/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

file = open('AU_Check_Result.html', 'w')

file.write(text1)
file.write(text2)
file.write(text3)

file.close()

print("======= AU Check Program (end) =======", flush=True)




