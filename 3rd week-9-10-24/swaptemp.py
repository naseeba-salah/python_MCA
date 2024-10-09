lst=['1','2','3','4','5']
leng=len(lst)
temp=lst[0]
lst[0]=lst[leng-1]
lst[leng-1]=temp
print(lst)
