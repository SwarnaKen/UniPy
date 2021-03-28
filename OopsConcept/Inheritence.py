class Base:
    name="Swarna"
    def baseMethod(self):
        print("I am in Baseclass")

class Child(Base):
    company="Kenric"
    def childMethod(self):
        print("I am in Childclass")

c=Child()
c.childMethod()
c.baseMethod()
print(c.name)
print(c.company)


