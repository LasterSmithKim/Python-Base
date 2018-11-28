from pypinyin import pinyin, lazy_pinyin, Style
import os

def read_file_as_str():
    file_path = os.path.join('base-1.txt')
    all_the_text = open(file_path).read()
    return all_the_text

if __name__ == "__main__":
    strs = str(read_file_as_str()).replace("\n","")
    list = []
    for i in strs:
        list.append(i)
    list = set(list)


    for i in list:
        for j in list:
            file = os.path.join('base-2.txt')
            with open(file, 'a+') as f:
                f.write("金"+i+j+'\n')



