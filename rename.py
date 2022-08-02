import glob
import os
import re


downloadDir = '/Users/satoshiaoki/works/kurukuru/kuru-chan-backup/download__'

# files = glob.glob("./capture/groups/*")
files = glob.glob("./download__/*")
for i, file in enumerate(files):
    
    # 2番目の連番を取得
    # replaceName = file.replace('詳しくはこちらをクリック', '')
    # os.rename(file,replaceName)

    # 「_」で
    filename = os.path.basename(file)
    splitArr = filename.split('_')
    newNum = int(splitArr[0]) + 23
    newfilename = str(newNum) + '_' + splitArr[1]
    # print(newNum)

    os.rename(file, downloadDir + '/' + newfilename)
    
    # changeTargetNumber = re.findall('', file)
    # num = str(int(changeTargetNumber[0]) % 30)
    # replaceStr = re.sub('([0-9]+_)([0-9]+)_',"\\1" + num + "_", file)
    # print("元：" , file)
    # print (replaceStr)
    