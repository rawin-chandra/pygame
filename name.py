name = []
print("Enter 10 names")
for i in range(10):
    x = input("Enter name : ")
    name.append(x)

f = open("name.txt", "w")
for x in name:
    f.write(x)
    f.write("\r\n")
'''
   for i in range(10):
       f.write(name[i])
'''
f.close()
