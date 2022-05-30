#files = open("file.txt", "r")
files = open("file.txt", "a+")
#print(files.readable())
#print(files.readline()) reads first line
#print(files.readline()) reads second line
#print(files.readlines()) reads all lines in file
#print(files.read()) reads file as your write it
print(files.write("\nAli"))
for lista in files.readlines():
    print(lista)

files.close()