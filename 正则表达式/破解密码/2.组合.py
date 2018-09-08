#从m个不同的元素取出n个元素为一组，叫做从 m个不同元素中取出n个元素的进行组合


import itertools

mylist = list(itertools.combinations([1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f"],6))
print(mylist)
print(len(mylist))