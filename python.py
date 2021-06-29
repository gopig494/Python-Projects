#Linear Search and how the in keyword internally works
a=[10,20,3,0,1]
no=0
count=0
for i in a:
	count+=1
	if i==no:
		print("True")
		break
	elif count==len(a):
		print("false")
		
#binary search
a=[2,50,100,101,120,150]#the list must be in assending order
no=150
min=0
max=len(a)-1
#avg=(min+max)//2
while min<=max:
	avg=(min+max)//2
	if no==a[avg]:
		print("True at index of :",avg)
		break
	elif no<a[avg]:
		max=avg-1
	else:
		if no>a[avg]:
			min=avg+1
else:
	print("false")
	
#list alising
l1=[1,2,3,4,5,6]
l2=l1
print(id(l1))
print(id(l2))
l1[5]=200
print(l1)
print(l2)

#List cloning
l1=[1,2,3,4,5,6]
l2=l1[:]
print(id(l1))
print(id(l2))
l1[5]=200
print(l1)
print(l2)

l1=[1,2,3,4,5,6]
l2=l1.copy()
print(id(l1))
print(id(l2))
l1[5]=200
print(l1)
print(l2)

#comparison in List
#1
l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5,6]
print(l1==l2)
l1=[1,2,3,4,5,6,0]
l2=[1,2,3,4,5,6]
print(l1>l2)
l1=[2]
l2=[1,2,3,4,5,6]
print(l1>l2)

#2
l1=["a",'b','c','d']
l2=['a','b','c','d']
print(l1==l2)
l1=['e']
l2=['a','b','c','d']
print(l1>l2)
l1=['a','b','c','d','e']
l2=['a','b','c','d']
print(l1>l2)

#3
l1=['zen','fun']
l2=['apple','orange','banana']
print(l1==l2)
l1=['apple']
l2=['apple','orange','banana']
print(l1>l2)
l1=['z']
l2=['yellow','green']
print(l1>l2)

#list comprehension
#1
l=[i for i in range(0,20)]
print(l)

#2
a=1,2,3,45,5,6,6
l=[i for i in a]
print(l)

#3
a="gopi","apple","fb","insta","python"
l=[i for i in a]
print(l)

#4
l1=['a','b','c','d','e']
l=[i for i in l1]
print(l)

#5
a=['gopi','mugil','insta']
l=[i for i in a if 'p' in i]
print(l))

#6
a=['gopi','mugil','insta']
l=[i*3 for i in a if 'p' in i]
print(l)

#List searching
l=['gopi','python','java']
inr=eval(input("Enter the data:  "))
for i in l:
	if i[0]==inr:
		print("present",i)
	elif i[len(i)-1]==inr:
		print("present",i)
else:
	print("not present")
	
#Converting str into list
strn="we can do it"
l=[]
for i in strn:
	l.append(i)
print(l)

strn="we can do it"
li=list(strn)
print(li)

strn="we can do it"
l=[a for a in strn]
print(l)

#ex:1 colum into row and row into coloum
li=[[10,20,30],
	[40,50,60],
	[70,80,90]
   ]
i=0
j=0
l1=[]
while i<len(li):
	if j<len(li):
		l1.append(li[j][i])
		j+=1
	else:
		print(l1)
		print()
		l1.clear()
		i+=1
		j=0


