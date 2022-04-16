f = open("mytext2.txt", "r")
sum = 0
for x in f:
    if x != '':
       sum += float(x)

print("Summary of sales = " , sum)
f.close()
