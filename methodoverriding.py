'''
what is polymorphism?
poly---> many
morphism---> forms
same methods/operators will behave differenty

example:
print(5+3) #8
print("hello"+"world") #helloworld

same operator
      |
but diff behaviours

types of polymorphism
1. compile time polymorphism
2. run time polymorphism

compile time---- method overloding
   # no method overloding in python

Method overloading:
same method names 
       +
 diff parameters

   *args---> variable length arguments 
   #java ---> add(int,int)
        ---> add(int,int,int)  
   
   python approach:
   class Calculator:
      def add(self,a,b,c=0):
          print(a+b+c)
c1=Calculator
c1.add(10,20)
c1.add(10,20,30)

   '''
class Calucalator:
      def add(self,a,b,c=0):
         print(a+b+c)
c1=Calucalator()
c1.add(10,20)
c1.add(10,20,30)

#run timepolymorphism
# ---> method overriding

class Bird:
     def fly(self):
          print("Bird Flying")
class Eagle(Bird):
     def fly(self):
          print("Eagle is flying")
e1 =Eagle()
e1.fly()