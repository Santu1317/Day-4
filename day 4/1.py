'''import sys
def Next_smallest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(Next_smallest_palindrome(99))
print(Next_smallest_palindrome(1221))'''
#------------------------------------------------

'''def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    p=patient_medical_speciality_list.count('p')
    o=patient_medical_speciality_list.count('o')
    e=patient_medical_speciality_list.count('e')
    if p>e and p>o:
        speciality=medical_speciality['p']
    elif e>o:
        speciality=medical_speciality['e']
    else:
        speciality=medical_speciality['o']
    return speciality
patient_medical_speciality_list=[301,'p',302,'p',305,'p',401,'e',656,'e']
medical_speciality={"p":"pediatrics","o":"orthopedics","e":"ent"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)'''
#-------------------------------------------------------------------------------------------

'''s1=input()
s2=input()
s3=s1.replace(" ",'')
s4=s2.replace(" ",'')
a=[]
b=[]
c=[]
for i in s3:
    a.append(i)
for i in s4:
    b.append(i)
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
d=''
for i in c:
    d+=i
print(d)'''
#------------------------------------------------

'''class example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())'''
#------------------------------------

'''class example:
    def __init_(self,num):
        self.num=num1
    def set_num(self,num2):
        self.num=num21
    def get_num(self):
        return self.num
obj=example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())'''
#--------------------------------------

'''class customer:
    def __init__(self):
        cust_id=100
c1=customer()
print(c1.cust_id)'''
#-------------------------------------

'''class customer:
    def __init__(self,id):
        id=100
c1=customer(200)
print(c1.id)'''
#------------------------------------

'''class customer:
    def __init__(self,id):
        self.id=100
c1=customer(200)
print(c1.id)'''
#-------------------------------------

'''class customer:
    def __init__(self):
        self.cust_id=100
c1=customer()
print(c1.cust_id)'''
#-----------------------------------------

'''class customer:
    def __init__(self,id):
        self.id=100
c1=customer(200)
print(c1.id)
class customer:
    def __init__(self,id):
        self.id=id'''
#-------------------------------------

'''class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="head first programming"
your_fav=Book()
your_fav.title="learn python"
my_fav.title="learning python"
print("my favorite is",my_fav.title)
print("your's is",your_fav.title)'''
#------------------------------------------

'''class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=shoe(1000,"canvas")
print(s1)
print(s1.price,s1.material)'''
#--------------------------------------------

'''class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=shoe(1000,"canvas")
print("the unique id of the object",id(s1))'''
#---------------------------------------------------

'''class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "shoe with price:"+str(self.price)+"and material:"+self.material
s1=shoe(1000,"canvas")
print(s1)'''
#-------------------------------------------------------------------------------------

'''class mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("displaying details")
    def purchase(self):
        self.display()
        print("calculating price")
mobile().purchase()
mobile().purchase()
m1=mobile()
print(m1)
m2=mobile()
print(m2)
m1=m2'''
#--------------------------------------------

'''class mobile:
    def __init__(self,brand,price):
        self.price=price
        self.brand=brand
        self.total_price=None
    def purchase(self):
        if self.brand=="apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print("total price of",self.brand,"mobile is",self.total_price)
    def amount_returned(self):
        return(self.price-self.total_price)
mob1=mobile("apple",20000)
mob2=mobile("samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())'''
#-------------------------------------------------------------------------------

'''class customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount<1000 and amount>0:
            self.wallet_balance+=amount
    def show_balance(self):
        print("the balance is",self.wallet_balance)
c1=customer(100,"santu",20,1000)
c1.update_balance(500)
c1.show_balance()'''
#-----------------------------------------------------------------------

'''class customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def set_balance(self,amount):
        if amount<50000 and amount>0:
            self.__wallet_balance+=amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=customer(100,"santu",20,1000)
print(c1.get_wallet_balance())
c1.set_balance(5000)
print(c1.get_wallet_balance())'''
#--------------------------------------------------------------------

'''class dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=dam("abc dam",3.5)
print("dam name:",dam1.name)
print("dam length",dam1.get_length())'''
#----------------------------------------------

