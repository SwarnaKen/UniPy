class Base:
    name="Swarna" #properties
    def baseMethod(self): #Methods
        print("I am in Baseclass")
    def getname(self):
        return self.name

class Child(Base): #class
    company="Kenric"
    def childMethod(self):
        print("I am in Childclass")
   # def getcompany(self):

c=Child() #Object/ instance 
c.childMethod()
c.baseMethod()

print(c.name)
print(c.company)
print(c.getname())

