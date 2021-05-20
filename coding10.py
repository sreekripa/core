class computer:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getspecs(self):
        self.name=input("Enter the computer name")
        self.price=input("enter the price")
    def displayspecs(self):
         print("computer name:",self.name,"\n","price:",self.price)
class desktop(computer):
    def __init__(self,model):
        self.model=model
    def fun1(self):
        self.model=input("enter the desktop model")
    def get1(self):
        print("desktop model:",self.model)
class laptop(desktop):
    def __init__(self,weight):
        self.weight=weight
    def fun2(self):
        self.weight=input("enter the laptop weight")
    def get2(self):
        print("laptop weight:",self.weight)
obj=laptop('')
obj.getspecs()
obj.displayspecs()
obj.fun1()
obj.get1()
obj.fun2()
obj.get2()
print("display the class:COMPUTER")
obj=computer('','')
obj.getspecs()
obj.displayspecs()
print("display the class:DESKTOP ")
obj=desktop("")
obj.fun1()
obj.get1()




