#读取ip字符串集
def read_file_as_str():
    file_path = "test.txt"
    all_the_text = open(file_path).read()
    return all_the_text

if __name__ == "__main__":
    strs = str(read_file_as_str())
    for i in range(0, len(strs)):
        print(strs[i])


