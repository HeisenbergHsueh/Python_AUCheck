import configparser
import urllib.request
import os

# urllib.request.urlretrieve("https://osce14-p.activeupdate.trendmicro.com/activeupdate", "1_server.ini")

config = configparser.ConfigParser()

#讀取 ini檔
if os.path.isfile('server.ini'):
    config.read('server.ini')

    chekcNum = config.has_option('PATTERN','P.4')

    print(str(chekcNum))

if os.path.isfile('2_server.ini'):
    config.read('2_server.ini')

    chekcNum = config.has_option('PATTERN','P.4')

    print(str(chekcNum))



    # if config.has_option('PATTERN','P.4'):
    #     VirusPatternTempStr = config['PATTERN']['P.4']
    #     VirusPatternStrArray = VirusPatternTempStr.split(',')
    #     VirusPatternStr = VirusPatternStrArray[1].strip(" ")
    #     VirusPattern = VirusPatternStr[0:2] + "." + VirusPatternStr[2:5] + "." + VirusPatternStr[5:]
    #     print(VirusPattern)
    # else:
    #     print("Check Conventional Pattern Fail")

    # try:
    #     VirusPatternTempStr = config['PATTERN']['P.4']
    #     VirusPatternStrArray = VirusPatternTempStr.split(',')
    #     VirusPatternStr = VirusPatternStrArray[1].strip(" ")
    #     VirusPattern = VirusPatternStr[0:2] + "." + VirusPatternStr[2:5] + "." + VirusPatternStr[5:]
    #     print(VirusPattern)
    # except:
    #     print("Check Pattern Fail")
