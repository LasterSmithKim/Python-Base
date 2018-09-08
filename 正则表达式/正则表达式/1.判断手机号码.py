
'''
给你一串字符串，判断这是否是手机号码？

'''
import re
def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] != "39" and str[1:3] != "35":
        return False
    for i in range(3,11):
        if str[i] < "0" or  str[i] > "9":
            return False
    return True

def checkPhone2(str):
    #13905106399
    pat = r"^1(([3578]\d)|(47))\d{8}$"
    res = re.findall(pat,str)
    print(res)


def checkPhone3(str):
    #13905106399
    pat = r"(1(([3578]\d)|(47))\d{8})"
    res = re.findall(pat,str)
    return res

print(checkPhone2("13500101234"))
print(checkPhone2("135051012234"))
print(checkPhone2("135a5101234"))
print(checkPhone2("135035101234"))
print(checkPhone2("1350101234"))
print(checkPhone2("14755101234"))
print(checkPhone2("135205101234"))
print(checkPhone2("1350a5101234"))
print(checkPhone2("13505s101234"))

print(checkPhone3("13500101234af15905101331fdsa14711111111sfsd13711111111a"))

