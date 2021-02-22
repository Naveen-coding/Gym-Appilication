import Gym_Member
import Gym_Functions
if __name__ == "__main__":
	while 1:
		print('\n=========WELCOME TO GYM ==========')
		print('-----------------------------------------')
		print('1. NEW MMBER REGISTRATION')
		print("2. NEW SUPER USER REGISTRATION")
		print("3. LOGIN")
		print("4. LOGOUT")
		print("5. EXIT")
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			full_name=input("Enter your name is : ")
			age=input("your Age is : ")
			gender=input("your Gender is : ")
			phone_no=input("your Mobile Number is : ")
			email=input("your Email is : ")
			bmi=input("your BMI is : ")
			subscription=input("How many months subcription u want 1,3,6 or 12 : ")
			Gym_Member.Member(full_name,age,gender,phone_no,email,bmi,subscription)
		elif choice == 2:
			full_name=input("Enter your name is : ")
			age=input("your Age is : ")
			gender=input("your Gender is : ")
			phone_no=input("your Mobile Number is : ")
			email=input("your Email is : ")
			Gym_Member.Super_User(full_name,age,gender,phone_no,email)
		elif choice == 3:
			if Gym_Functions.user==[]:
				full_name=input("Enter your full name is : ")
				phone_no=input("Enter your phone no is : ")
				Gym_Functions.Login(full_name,phone_no)
			else:
				print("Already {} is logged in ..pls logout first if u want continue with another Login.\n".format(Gym_Functions.user[0]))
		elif choice == 4:
			Gym_Functions.Logout()
		elif choice == 5:
			print("Thank u ....")
			break;
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
