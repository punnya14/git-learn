#s="Hello world from python"[::-1]
#print(s)
#s=str(dict.fromkeys(s))
#print(s)
#s=("Hello world from python")
#new=" "
#for i in s:
#    if i not in new:
 #       new+=i
#print(new)
s="Hello world from python"
p={}
for i in s:
    if i.isalpha():
        p[i]=p.get(i,0)+1
print(p)