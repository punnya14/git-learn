"""
l={1,2,3,4,5}
p={}
for i in l:
    l={}
    a=i*2
    l[i]=a
    p.update(l)
    print(l)

"""
'''
l={1,2,3,4,5}
x={a:(lambda y:y*2)(a)for a in l}
print (x)
'''
""""
price=[15,25,10,30,50]
a=[i for i in price if i<20]
print(a)
"""
""""
customers={'Rahul','Antony','Salman','Arun','Kiran'}
a=[i for i in customers if "A" in i[0]]
print(a)
"""
""""
employees={'Antony':55000,'Susan':45000,'Kiran':60000}
a={k:"high"if n>50000 else "low" for k,n in employees.items()}
print(a)
"""
words=['apple','banana','apple','orange','banana','apple']
p=[i:words.count(i) for i in words]
print[p]