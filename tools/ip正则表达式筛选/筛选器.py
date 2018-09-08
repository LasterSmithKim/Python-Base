import collections
import re

#读取ip字符串集
def read_file_as_str():
    file_path = "ip.txt"
    all_the_text = open(file_path).read()
    return all_the_text

if __name__ == "__main__":
    #获取文档字符串
    str = str(read_file_as_str())
    # 查找所有的IP号码
    pat = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    re_ip = re.compile(pat)
    ipLists = re_ip.findall(str)
    dic = collections.Counter(ipLists)
    dic = sorted(dic.items(), key = lambda item:item[1],reverse = True) #修改为值降序列表
    for i in dic:
        print(i[0],i[1])