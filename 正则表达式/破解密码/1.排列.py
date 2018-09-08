import itertools

#排列：从n个元素中取出m个元素，按一定的顺序排成一列
#当 n=m 时，成为 n的全排列
#排列的多少种可能，  n！ /

mylist = list(itertools.permutations([1,2,3,4,5,6,7,8,9,0],6))
print(mylist)
print(len(mylist))
