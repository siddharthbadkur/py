# class A: 
#     def __init__(self,name,surname,categorry,marriedstatus):
#         self.name=name
#         self.surname=surname
#         self.categorry=categorry
#         self.marriedstatus=marriedstatus
                 
#     def show(self):
#         print('my name is=',self.name)
#         print('my surnamne is=',self.surname)
#         print('my csṭegory is=',self.categorry)
#         print('my married status is=',self.marriedstatus)
# obj=A('siddharth','badkur','obc','null')
# obs=A('arun','patel','obc','null')
# obj.show()
# obs.show()
# print(obj.name)
# print(obs.name)
# a=1
# b=2
# sum=0
# def add():
#     print('from a add function',a)
# def addition():
#     print('from a function ',b)
# add()
# addition()
# a=1
# def great():
#     a=2
#     print('value comes from global',a)
 
#     print('value comes from built-in global ',globals()['a'])    
    
# great()
#write a code of a caculater
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divid(x,y):
    return x/y
while True:
    print('please select your operation ')
    print("1.add\n,2.subtract\n,3.multiply\n,4.divide\n,5.off\n")
    n=int(input('enter your choice'))    
    a=int(input('enter your a number'))
    b=int(input('enter your b number'))

if n==1:
    print(a,'+',b,'=',add(a,b))
elif n==2:
    print(a,'-',b,'=',subtract(a,b))
     
elif n==3:
    print(a,'*',b,'=',multiply,(a,b))
elif n==4:
    print(a,'/',b,'=',divide(a,b))  
elif n==5:
    Break
else:
     print('enter you invalid choice')
add(a,b)
subtract(a,b)
multiply(a,b)
divide(a,b)              


          
          


