from pypinyin import pinyin, lazy_pinyin, Style
import os
import subprocess


def read_file_as_str():
    file_path = os.path.join('basedata.txt')
    all_the_text = open(file_path).read()
    return all_the_text
def style3(ming):
    pinyinstr = str(pinyin(ming,style=Style.TONE3)[0][0])
    if "4" in pinyinstr:
        return 4
    elif '3' in pinyinstr:
        return 3
    elif '2' in pinyinstr:
        return 2
    elif '1' in pinyinstr:
        return 1
    else:
        return 0

if __name__ == "__main__":
    strs = str(read_file_as_str())
    count = 0
    num = len(strs)*len(strs)
    for j in range(0, len(strs)):
        for i in range(0, len(strs)):
            ming1 = strs[j][0]
            ming2 = strs[i][0]
            datastr = (ming1+ming2)
            #写入文件
            file = os.path.join('to-data2.txt')
            with open(file, 'a+') as f:
                f.write(datastr + '\n')
            #显示写入进度
            count += 1
            print(str(round((count/num)*100,2)) +str("%"))




