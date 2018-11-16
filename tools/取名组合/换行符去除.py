from pypinyin import pinyin, lazy_pinyin, Style
import os
from crawlerbm8 import cooking

def read_file_as_str():
    file_path = os.path.join('bak.txt')
    all_the_text = open(file_path).read()
    return all_the_text

if __name__ == "__main__":
    strs = str(read_file_as_str()).replace("\n","")
    print(strs)