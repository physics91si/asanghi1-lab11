#!/anaconda/bin/python

import string 
a=string.ascii_lowercase
b=a[0:10]
tenAlphas= [char for char in b]
print(tenAlphas)
tenAlphasMinsSixth=[char for char in b if char !="f"]
print(tenAlphasMinsSixth) 
repeatedMinsSixth=[i*j for j in b for i in range(1,4)]
print(repeatedMinsSixth)
gridRepeated=[[char,char*2,char*3] for char in tenAlphasMinsSixth]
print(gridRepeated)
