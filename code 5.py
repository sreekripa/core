# try:
#     def division(a,b):
#         c=a/b
#         print(c)
#     x=int(input("enter the first number"))
#     y=int(input("enter the second number"))
#     division(x,y)
# except:
#     print("sorry,you enter zero")
def division(a,b):
    try:
        c = a / b
        print(c)

    except:
        print("sorry, you enter zero")

x = int(input("enter the first number"))
y = int(input("enter the second number"))
division(x, y)





