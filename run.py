#!/usr/bin/env python3.8
import random
from user import User

def main():
    print("Welcome to Password Locker")
    print('\n')
    print("Select a short code to navigate through:To create a new user use 'nu' To login to your account 'lg' or 'ex' to exit")
    short_code = input().lower()
    print('\n')

    if short_code == 'nu':
        print('Create Username')
        created_user_name = input()

        print('Create Password')
        created_user_password = input()

        print('Confirm Password')
        confirm_password = input()


        while confirm_password != created_user_password:
            print("Invalid,Password did not match")
            print("Enter your password")
            created_user_password = input()
            print("Confirm your password")
            confirm_password = input()

        else:
            print(f"Congratulations {created_user_name}! account created successfully ")
            print('\n')
            print("Proceed to login")
            print("Username")
            entered_username = input()
            print("Enter password")
            entered_password = input()

        while entered_username != created_user_name or entered_password != created_user_password:
            print("Invalid username or password")
            print("username")
            entered_username = input()
            print("Your Password")
            entered_password = input()

        else:
            print(f"Welcome {entered_username} to your account")
            print('\n')
    elif short_code == 'lg':
        print("Welcome")
        print("Enter your User name")
        default_user_name = input()


        print("Enter password")
        default_user_password = input()
        print('\n')
        while default_user_name != 'testuser' or default_user_password != '0000':
            print("Wrong Username or Password. Username 'testuser' and password '0000'")
            print("Enter user name")
            default_user_name = input()

            print("Enter password")
            default_user_password = input()
            print('\n')

        else:
            print("Login Successfully")
            print('\n')
            print('\n')

    elif short_code == 'ex':
        exit() 
    else:
        print("Enter valid code to Continue")

if __name__ == '__main__':
    main()





