import operator

f=open('Testsource','r')
s=f.read()  #Storing the contents of the file
f.close()    #closing the file
s1=s.upper()  #converting all the characters to upper case
s2=s1.split(" ")  #splitting them to remove empty spaces
s3=''
for i in s2:    #concating all the elements in the list
    s3=s3+i
print(s3)
#Now getting the count of each character with help of dictionary
dict1={}  #Blank
for i in s3:
    if(i in dict1):
        dict1[i]+=1
    else:
        dict1[i]=1
dict2=sorted_d = sorted(dict1.items(), key=operator.itemgetter(1))
print(dict2)
#Write the contents of dictionary
f1=open('TestDestination','w')
for key,value in dict1.items():
    f1.write('%s:%s\n' % (key, value))
f1.close()
