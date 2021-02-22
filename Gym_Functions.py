import json
user=[]
class Login():
	def __init__(self,full_name,phone_no):
		global user
		print('\n==========LOGIN PANEL==========')
		with open('user_accounts.json', 'r+',encoding="utf8") as user_accounts:
			users = json.load(user_accounts)
			if full_name not in users.keys():
				print("An account of that name doesn't exist.\nPlease create an account first. \n")
				return
			elif full_name in users.keys():
				if users[full_name][2] != phone_no:
					print("Your phone num is incorrect.\nPlease enter the correct phone num and try again.")
					return
				elif users[full_name][2] == phone_no:
					print("You have successfully logged in as a ",users[full_name][-1])
					print("\n")
					user.append(full_name)
					user.append(users[full_name][-1])
			if users[full_name][-1] == "MEMBER":
				while 1:
					print("Welcome you are a member ..Your available options are \n")
					print("1.VIEW PROFILE")
					print("2.YOUR REGIMEN")
					print("3.EXIT \n")
					inp=int(input("Enter your choice is : "))
					if inp==1:
						print("Your details is : \n")
						print(" Your name is : {} \n Your age is : {} \n Your Gender is : {} \n Your phone num is : {} \n Your email is : {} \n Your bmi is : {} \n Your subscription Moths is : {} \n You are a {} \n".format(user[0],users[full_name][0],users[full_name][1],users[full_name][2],users[full_name][3],users[full_name][4],users[full_name][5],users[full_name][6]))
						print("\n")
					elif inp==2:
						with open('Regimens.json', 'r+',encoding="utf8") as Regimens:
							task = json.load(Regimens)
							val=users[full_name][4]
							val=float(val)
							key=None
							if val<=18.5:
								key="<=18.5"
							elif val<=25:
								key="<=25"
							elif val<=30:
								key="<=30"
							elif val>30:
								key=">30"
							else:
								prnt("Condition Not matches in availvable regimens \n")
								return
							if key in task.keys():
								nam=key
							print(" your bmi condition is {} \n your Regimen is \n Monday : {} \n Tuesday : {} \n Wednesday : {} \n Thusrsday : {} \n Friday : {} \n Saturday : {} \n Sunday : {} \n".format(nam,task[key]["Mon"],task[key]["Tue"],task[key]["Wed"],task[key]["Thu"],task[key]["Fri"],task[key]["Sat"],task[key]["Sun"]))
							print("\n")
					elif inp==3:
						break
					else:
						print("choose correct option")
			elif users[full_name][-1] == "ADMIN":
				while 1:
					print("Welcome you are a admin..Your available options are \n")
					print("1.CREATE A MEMBER")
					print("2.VIEW MEMBER")
					print("3.DELETE MEMBER")
					print("4.UPDATE MEMBER")
					print("5.CREATE REGIMEN")
					print("6.VIEW REGIMEN")
					print("7.DELETE REGIMEN")
					print("8.UPDATE REGIMEN")
					print("9.EXIT \n")
					inp=int(input("Enter your choice is : "))
					if inp==1:
						full_name=input("Enter member name is : ")
						if full_name in users.keys():
							print("An account of this Username already exists. ")
						else:
							age=input("member Age is : ")
							gender=input("member Gender is : ")
							phone_no=input("member Mobile Number is : ")
							email=input("member Email is : ")
							bmi=input("member BMI is : ")
							subscription=input("subcription in months 1,2,3,6 or 12 : ")
							users[full_name] = [age,gender,phone_no,email,bmi,subscription,"MEMBER"]
							user_accounts.seek(0)
							json.dump(users, user_accounts)
							user_accounts.truncate()
							print("Account created for memebr successfully \n")
					elif inp==2:
						phone_no=input("Enter phone num is : ")
						for i in users.keys():
							if users[i][2]==phone_no:
								if users[i][-1]=="MEMBER":
									print("Member details is : \n")
									print(" Member name is : {} \n Member age is : {} \n Member Gender is : {} \n Member phone num is : {} \n Member email is : {} \n Member bmi is : {} \n Member subscription Moths is : {} \n".format(i,users[i][0],users[i][1],users[i][2],users[i][3],users[i][4],users[i][5],users[i][6]))
									print("\n")
									break
								elif users[i][-1]=="ADMIN":
									print("Admin details is : \n")
									print(" Admin name is : {} \n Admin age is : {} \n Admin Gender is : {} \n Admin phone num is : {} \n Admin email is : {} \n".format(i,users[i][0],users[i][1],users[i][2],users[i][3]))
									print("\n")
									break
						else:
							print("User does not exists \n")
					elif inp==3:
						full_name=input("Enter name of the member is : ")
						phone_no=input("Enter phone no of the member is : ")
						if full_name in users.keys() and users[full_name][2]==phone_no:
							if users[full_name][-1]=="MEMBER":
								for i in users.keys():
									if i==full_name:
										users.pop(i)
										user_accounts.seek(0)
										json.dump(users, user_accounts)
										user_accounts.truncate()
										print("member deleted successfully \n")
										break
							elif users[full_name][-1]=="ADMIN":
								print("you can't delete admin profile..u can only delete member profile \n")
						elif full_name not in users.keys():
							print("User Does not exists  \n")
						else:
							print("Enter phone num correctly \n")
					elif inp==4:
						full_name=input("Enter name of the member is : ")
						phone_no=input("Enter phone no of the member is : ")
						if full_name not in users.keys():
							print("User Does not exists  \n")
						elif full_name in users.keys() and users[full_name][2]==phone_no and users[full_name][-1]=="ADMIN":
							print(" What do u want to update \n 0.age \n 1.gender \n 2.phone \n 3.mail \n ")
							val=int(input("Enter option is : "))
							updated_val=input("Enter updates value is :")
							users[full_name][val]=updated_val
							user_accounts.seek(0)
							json.dump(users, user_accounts)
							user_accounts.truncate()
							print("Updated successfully \n")
						elif full_name in users.keys() and users[full_name][2]==phone_no and users[full_name][-1]=="MEMBER":
							print(" What do u want to update  \n 0.age \n 1.gender \n 2.phone \n 3.mail \n 4.bmi \n 5.subscripton  ")
							val=int(input("Enter option is : "))
							updated_val=input("Enter updates value is :")
							users[full_name][val]=updated_val
							user_accounts.seek(0)
							json.dump(users, user_accounts)
							user_accounts.truncate()
							print("Updated successfully \n")
						else:
							print("Enter phone num correctly \n")
					elif inp==5:
						with open('Regimens.json', 'r+',encoding="utf8") as Regimens:
							task = json.load(Regimens)
							condition=input("Enter bmi condition is like <18 , <20 : ")
							if condition in task.keys():
								print("This condition is already exists...Update if u want\n")
							else:
								Mon=input("Monday Excercise is : ")
								Tue=input("Tuesday Excercise is : ")
								Wed=input("Wednesday Excercise is : ")
								Thu=input("Thursady Excercise is : ")
								Fri=input("Friday Excercise is : ")
								Sat=input("Saturday Excercise is : ")
								Sun=input("Sunday Excercise is : ")
								task[condition] = {'Mon':Mon,'Tue':Tue,'Wed':Wed,'Thu':Thu,'Fri':Fri,'Sat':Sat,'Sun':Sun}
								Regimens.seek(0)
								json.dump(task, Regimens)
								Regimens.truncate()
								print("Regimen created successfully \n")
					elif inp==6:
						with open('Regimens.json', 'r+',encoding="utf8") as Regimens:
							task = json.load(Regimens)
							condition=input("Enter bmi condition is like <30 , <18 : ")
							if condition in task.keys():
								print(" bmi condition is {} \n Regimen created for this condition is \n Monday : {} \n Tuesday : {} \n Wednesday : {} \n Thusrsday : {} \n Friday : {} \n Saturday : {} \n Sunday : {} \n".format(condition,task[condition]["Mon"],task[condition]["Tue"],task[condition]["Wed"],task[condition]["Thu"],task[condition]["Fri"],task[condition]["Sat"],task[condition]["Sun"]))
								print("\n")
							else:
								print("condition does not exists \n")
					elif inp==7:
						with open('Regimens.json', 'r+',encoding="utf8") as Regimens:
							task = json.load(Regimens)
							condition=input("Enter bmi condition is like <30 , <18 : ")
							if condition in task.keys():
								task.pop(condition)
								Regimens.seek(0)
								json.dump(task, Regimens)
								Regimens.truncate()
								print("Regiment deleted successfully")
								print("\n")
							else:
								print("condition does not exists \n")
					elif inp==8:
						with open('Regimens.json', 'r+',encoding="utf8") as Regimens:
							task = json.load(Regimens)
							condition=input("Enter bmi condition is like <30 , <18 : ")
							if condition not in task.keys():
								print("condition does not exist")
							elif condition in task.keys():
								print("which u want to be update ? \n")
								print(" Mon\n Tue \n Wed \n Thu \n Fri \n Sat \n Sun \n")
								val=input("Enter option is : ")
								updated_val=input("Enter updated value is : ")
								if val in task[condition].keys():
									task[condition][val]=updated_val
									Regimens.seek(0)
									json.dump(task, Regimens)
									Regimens.truncate()
									print("Regiment Updated successfully")
								else:
									print("Enter correctly")
					elif inp==9:
						break
					else:
						print("choose correct option \n")
						
class Logout():
	def __init__(self):
		global user
		if len(user) == 0:
			print("you are already logged out")
		else:
			user=[]
			print("you are successfully logged out")
