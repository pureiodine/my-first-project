class Person:
    def __init__(self,name,age,payment,**kwargs):
        self._name=name
        self._age=age
        self._payment=payment
        super().__init__(**kwargs)
    @property
    def age(self):
        return self._age #get setter

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError(" Too small")
        self._age =age #set setter

    def promotion(self,rise):
        if rise<=0 or rise>10000:
            return "error" 
        else:
            self._payment=self._payment+rise  
            return self._payment
    def __str__(self):
        return f"{self._name} is {self._age} years old"
Cathy=Person("Cathy",22,3000)
print(f"{Cathy._name}'s payment is {Cathy._payment} euros")
print(Cathy)
result=Cathy.promotion(100)
print(f"After promotion: {result} euros")       
print(f"Cathy's current payment: {Cathy._payment} euros") 
class Special1(Person):
    def __init__(self,name,age,payment,job,**kwargs):
        super().__init__(name,age,payment,**kwargs)
        self._job=job
Sue=Special1("Sue",20,2000,"civil engineering")
class Special2(Person):
    def __init__(self,name,age,payment,temp,**kwargs):
        super().__init__(name,age,payment,**kwargs)
        self._temp=temp
Jack=Special2("Jack",20,40,True)
class Special(Special1,Special2):
    def __init__(self,name,age,payment,job,temp,bonus):
        super().__init__(name,age,payment,job=job,temp=temp)
        self._bonus=bonus
Jeff=Special("Jeff",29,4000,"electric engineering",False,True)
print(Sue._name)
print(Sue._age)
print(Sue._payment)
print(Sue._job)
print(Sue)
print(Jack)
print(Jeff)
print(Special.__mro__)
print(isinstance(Sue, Person))   # True
print(issubclass(Person, Special1)) # False
print(Cathy.age) #. 判断 getter
Cathy.age = 28
print(Cathy.age)
print(Cathy._age)#判断setter
print(Jeff._name)
print(Jeff._age)
print(Jeff._payment)
print(Jeff._job)
print(Jeff._temp)
print(Jeff._bonus)

class Animal:
    def __init__(self,name,width,height):
        self._name=name
        self._width=width
        self._height=height
    def __str__(self):
        return f"{self._name},is {self._width}cm and {self._height}cm "
class Carnivore(Animal):
    def __init__(self,name,width,height,habitat):
        super().__init__(name,width,height)
        self._habitat=habitat
    def __str__(self):
        return f"{self._name},is {self._width}cm and {self._height}cm, live in {self._habitat}"
a1=Animal("zebra",150,180)
c1=Carnivore("lion",200,250,"Africa")
print(a1)
print(c1)
