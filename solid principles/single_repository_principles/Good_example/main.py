from User import User
from UserRepository import UserRepository

user1 = User("Akshat chawla",'akshat@aonetech.in', 27)
userRepo1 = UserRepository('aonetech', 'aonetechdev', 'password')

user1.get_user_info()
userRepo1.add_to_database(user1)