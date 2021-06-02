import re 

choose='y'

while choose.upper()=='Y':

	while True:
		inp=input("Enter The Path Of The Document   : ")
		try:
			loc=open(inp,"r")  #/home/gopi/Desktop/mocinterview.docx
		except FileNotFoundError:
			print("File Not Fount PLease Enter The Correct Path  :")
			continue
		break

	read=loc.read()
	var=read

	def fun(no):
		stru=re.compile(r'((91)[6-9][0-9]{4})-([0-9]{5})')
		res=stru.search(no)
		return res
	res=fun(var)
	p1=res.group(1)
	p2=res.group(3)
	print(p1+p2)
	p1=str(p1+p2)
	s=open("/home/gopi/Desktop/write.docx","r+")
	s.write(p1)
	
	while True:
		a=input("Enter 'y' to continue and 'n' to exit  : ")
		if a.upper() !='Y' and a.upper() !='N':
			continue 
		else:
			choose=a
			break 
			
