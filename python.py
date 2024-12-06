a=int(input("enter the 1 number="))
b=int(input("enter the 2 number="))
i=int(input("select the operation to be perfomed="))
if i==1:
       print("addition")
       c=a+b
       print(c)
if i==2:
        print("subtraction")
        c=a-b
        print(c)
if i==3:
        print("multiplication")
        c=a*b
        print(c)
if i==4:
        if a==0:
         print ("operation cannot be performed")      
        if b==0:
         print("operation cannot be performed")
        else:
         print("division")
        c=a/b
        print(c)
if i==5:
        print("stop")
  