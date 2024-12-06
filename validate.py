x=input("enter your name=")
y=x.isalnum()
if y==True:
   print("validated")
if y==False:
   print("non validated")
if len(x)<6:
   print("length too short")
if len(x)>15:
   print("length exceeded")