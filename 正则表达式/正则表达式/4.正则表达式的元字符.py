import re



print("---------------匹配单个字符和数字---------")
r'''
.    匹配换行符以外的任意字符
[0123456789]  表示匹配方括号中所有所包含的任意一个字符
[sunck] 表示匹配"s" "u" "n" "c" "k" 中任何一个字符
[a-z]   表示匹配任意小写字母
[A-Z]   表示匹配任意大写字母
[0-9]   表示匹配任意数字  类似：[0123456789] 
[0-9a-zA-Z] 表示匹配任意数字和字母 
[0-9a-zA-Z_] 表示匹配任何数字和字母和下划线
[^sunck] 表示匹配除了sunck这几个字母以外的所有字符，中括号中的^称为 脱字符 表示不匹配集合中的字符
[^0-9] 匹配所有的非数字字符
\d     匹配所有的数字 效果同：[0-9]
\D     匹配所有非数字字符，效果同 [^0-9]
\w     匹配数字字母和下划线 效果同：[0-9a-zA-Z_]
\W     匹配非字母数字下划线 效果同：[^0-9a-zA-Z_]
\s     匹配任意的空白符（空格 换行 换页 制表 回车） 效果同： [ \f\n\r\t]
\S     匹配任意的非空白符 效果同 [^ \f\n\r\t]


'''
print(re.findall("\S","_sunck is 6a go2od"))

print("----------锚点字符（边界字符）-------------")

'''
^   行首匹配，和[]里面^的不一样
$   行尾匹配 
\A  匹配字符串开始，它和^的区别是，\A 只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z  匹配字符串结束，它和$的区别是，\Z 只匹配整个字符串的尾部，即使在re.M模式下也不会匹配它行的行尾

\b  匹配一个单词的边界，也就是指单词和空格间的位置
    "er\b" 可以匹配 never 不可以匹配 verve
\B  匹配非单词的边界，
    "er\B" 可以匹配 nerve 不可以匹配 never
'''
print(re.search("^sunck","sunck is a good man"))
#print(re.search("man$","sunck is a good man"))

print(re.findall("\Asunck","sunck is a good man \nsunck is a nice man",re.M))
print(re.findall("^sunck","sunck is a good man \nsunck is a nice man",re.M))

print(re.findall("man\Z","sunck is a good man\nsunck is a nice man",re.M))
print(re.findall("man$","sunck is a good man\nsunck is a nice man",re.M))


print(re.search(r"er\b","never "))
print(re.search(r"er\b","nerve"))
print(re.search(r"er\B","never"))
print(re.search(r"er\B","nerve"))

print("-------------多个字符----------------")

'''
说明：下方的 x、y、z 均为假设的普通字符，不是正则表达式的元字符 n m 为非负整数
（xyz） 匹配小括号内的 xyz（作为一个整体去匹配）
x?     匹配0个或者1个x
x*     匹配0个或者任意多个x （.* 表示匹配0个或者任意多个字符（换行符除外））
x+     匹配至少一个x 
x{n}   匹配确定的n个x（n是一个非负整数）
x{n,}  匹配至少n个x
x{n,m} 匹配至少n个最多m个x 注意：n<=m
x|y    |表示或 匹配的是 x或者y
'''

print(re.findall(r"(sunck)","sunck is a good man,sunck is a nice man"))
print(re.findall(r"a?","aaa"))#非贪婪匹配 尽可能少的匹配
print(re.findall(r"a*","aaabaa"))#贪婪匹配 尽可能多的匹配
print(re.findall(r".*","aaabaa"))#贪婪匹配 尽可能多的匹配
print(re.findall(r"a+","aaabaaaaaa"))#贪婪匹配 尽可能多的匹配
print(re.findall(r"a{3}","aaabaaaaa"))#贪婪匹配 尽可能多的匹
print(re.findall(r"a{3,}","aaabaaaaa"))#贪婪匹配 尽可能多的匹，
print(re.findall(r"a{3,6}","aaaabaaa"))#贪婪匹配 尽可能多的匹
print(re.findall(r"((s|S)unck)","sunck-SuNck"))#贪婪匹配 尽可能多的匹

#需求：提取 sunck…………man，
str = "sunck is a  good man  sunck is a nice man sunck is a very handsome man"
print(re.findall(r"(^sunck.*man$)",str))


print("-----------特殊-------------")
'''
*？  +？  ？？ 最小匹配 通常都是尽可能多的匹配，我们可以使用这种方式解决贪婪匹配
(?:x)   类似我们以前所讲的（xyz），但是不表示是一个组

'''
print(re.findall(r"(sunck.*?man)",str))

#注释：/*  part1 */      /*   part2  */

print(re.findall(r"//*.*?/*/",r"/*  part1 */      /*   part2  */"))

