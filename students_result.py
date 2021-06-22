class details:
	def __init__(self,Regno,name,Class,section,mark,result):
		self.RegisterNo=Regno
		self.Name=name
		self.Class=Class
		self.Section=section
		self.Mark=mark
		self.Result=result
	def student(self):
		print('RegisterNo :',self.RegisterNo)
		print('Name :',self.Name)
		print('Class :',self.Class)
		print('Section :',self.Section)
		print('Mark :',self.Mark)
		print('Result :',self.Result)
Raju=details(622614114001,'Raju','10th Std','A-Section','400','Pass')
Gopal=details(622614114002,'Gopal','10th Std','B-Section','150','Fail')
Ramya=details(622614114003,'Ramya','10th Std','C-Section','350','Pass')
Ranjith=details(622614114004,'Ranjith','10th Std','B-Section','499','Pass')
Indian=details(622614114005,'Indian','10th Std','A-Section','412','Pass')
Tamilan=details(622614114006,'Tamilan','10th Std','C-Section','298','Pass')
Karthic=details(622614114007,'Karthic','10th Std','A-Section','488','Pass')
Mani=details(622614114008,'Mani','10th Std','A-Section','80','Fail')
Salman=details(622614114009,'Salman','10th Std','C-Section','102','Fail')
Khan=details(622614114010,'Khan','10th Std','C-Section','170','Fail')
F='Y'
while F.upper()=='Y':
	while True:
		a=input("Enter the Student Name For View the Result  :")	
		b=a.title()
		try:
			a=globals()[b]
		except KeyError:
			print("The Name is Not Available On The List, Please Type correct Name Below ")
			continue
		except:
			print("Somthing Went Wrong Please Try Again")
			break
		a.student()
		while True:
			f=input("Press Y to continue and N to exit  :")
			if f.upper()=='Y':
				F=f
			elif f.upper()=='N':
				F=f
				print("Exit")
			else:
				print("You Entered Wrong Key Please Enter Correct Key")
				continue
			break
		break

		
