firstfile = open('particle_2 - Copy.txt','r')
secondfile = open('second1.txt','w')
counter =0
content = firstfile.read()
CoList = content.split("\n")

cont = firstfile.readlines()
type(cont)


for i in CoList:
    if i:
        counter+=1
print("Number of lines in file",counter)

print ("number of line , second method",len(cont))

for h in range(0, len(cont)):

    if (h < counter//4):
        print("yay")
        secondfile.write(cont(h))


##for j,line in enumerate(firstfile):
#    if j < counter//4:
#        secondfile.write(line)

#print (counter//4)
#counter2 =0

#for k in range(counter):
#    counter2 +=1
