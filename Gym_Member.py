import json
class Member():
	def __init__(self,full_name,age,gender,phone_no,email,bmi,subscription):
		with open('user_accounts.json', 'r+',encoding="utf8") as user_accounts:
			users = json.load(user_accounts)
			self.full_name=full_name
			self.age=age
			self.gender=gender
			self.phone_no=phone_no
			self.email=email
			self.bmi=bmi
			self.subscription=subscription
			if full_name in users.keys():
				print("An account of this Username already exists.\nPlease Login insted.")
			else:
				users[full_name] = [age,gender,phone_no,email,bmi,subscription,"MEMBER"]
				user_accounts.seek(0)
				json.dump(users, user_accounts)
				user_accounts.truncate()
				print("Account created for memebr successfully \n")
class Super_User():
	def __init__(self,full_name,age,gender,phone_no,email):
		with open('user_accounts.json', 'r+',encoding="utf8") as user_accounts:
			users = json.load(user_accounts)
			self.full_name=full_name
			self.age=age
			self.gender=gender
			self.phone_no=phone_no
			self.email=email
			if full_name in users.keys():
				print("An account of this Username already exists.\nPlease enter the login panel.  \n")
			else:
				users[full_name] = [age,gender,phone_no,email,"ADMIN"]
				user_accounts.seek(0)
				json.dump(users, user_accounts)
				user_accounts.truncate()
				print("Account created for Admin successfully! \n")

