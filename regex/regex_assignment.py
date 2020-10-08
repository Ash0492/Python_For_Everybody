import re
fh = open('regex_sum_1006098.txt')
numlist = list()

for line in fh:
    y = re.findall('[0-9]+',line)
    numlist = numlist+y
listy = [int(i) for i in numlist]
print(sum(listy))
