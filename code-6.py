# file=open("demo.txt","w")
# file.close()
file=open("demo.txt","r")
content=file.read()
print(content)
file.close()
file=open("demo.txt","a")
file.write("these are vegetables")
file.close()
file=open("demo.txt","r")
content=file.read()
print(content)
file.close()