#To create a file

f=open("Mydoc.txt",'x')

f.close()




#To write a content into file & create a file if file not found

f = open("Mydoc.txt",'w')

f.write("This is a document")

f.close()



# To read content from file

f=open("Mydoc.txt",'r')

#print(f.read()) #will read whole file
print(f.read(6)) #will read upto 6th character

f.close()


# To read content line from file

f=open("Mydoc.txt",'r')

print(f.readline())

f.close()


#To add content into file

f = open("Mydoc.txt",'a')

f.write("\nThis is a document2")

f.close()


#To delete a file
import os
os.remove("Mydoc.txt")
#os.rmdir('Asd')
