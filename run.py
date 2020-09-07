#!/usr/bin/env python3.8
import random
from user import User
from user import Credentials

def save_credentials(user):
    user.save_created_credential()

def create_credentials(username, password):
    new_credential = User(username, password)
    return new_credential

def save_existing_credential(user):
    user.save_existing_credential_accounts()

def view_various_accounts():
    return User.view_my_various_credential_accounts()

def delete_existing_credential(user):
    user.delete_credential_account()
    

def main():
    while True:
        print('-'*80)
        print("Welcome to Password Locker")
        print('\n')
        print("Select a short code to navigate through:")
        print('\n')
        print("nu => To create a new user use")
        print("lg => To login to your account")
        print("aea => add existing account credentials")
        print("vac => view all accounts")
        print("dc => delete credentials")
        print("ex => to exit")
        print('-'*40)
        short_code = input().lower()
        print('\n')
       

        if short_code == 'nu':
            print('Create Username')
            created_user_name = input()
            print('-'*40)

            print('Create Password')
            created_user_password = input()

            print('Confirm Password')
            confirm_password = input()

            save_credentials(create_credentials(created_user_name, created_user_password))
            print ('\n')
            print(f"Existing Credentials {created_user_name} {created_user_password} {confirm_password} added")
            print ('\n')
            print('-'*40)
            


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
                print('-'*40)

            while entered_username != created_user_name or entered_password != created_user_password:
                print("Invalid username or password")
                print("username")
                entered_username = input()
                print("Your Password")
                entered_password = input()

            else:
                print(f"Welcome {entered_username} to your account")
                print('\n')
                print('-'*40)
                
        elif short_code == 'lg':
            print("Welcome")
            print("Enter your User name")
            default_user_name = input()


            print("Enter password")
            default_user_password = input()
            print('\n')
            print('-'*40)
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
                print('-'*40)

        elif short_code == 'vac':

            if view_various_accounts():
                print("Here is a list of all your Accounts")
                print('\n')

                for user in view_various_accounts():
                        print(f"{user.username} {user.password}")
                        username = " "
                        password = " "

                print('\n')
            else:
                print('\n')
                print("You don't seem to have any accounts saved yet")
                print('\n')
                print('-'*40)

        
        elif short_code == 'aea':
            print("Add existing username")
            existing_username = input()

            print("Input it's password")
            epassword = input()

            save_existing_credential(create_credentials(existing_username, epassword))
            print ('\n')
            print(f"Existing Credentials {existing_username} {epassword} added")
            print ('\n')
            print('-'*40)

        elif short_code == 'dc':
           delete_existing_credential(user)
           print("Credential deleted")
           print('-'*40)

        elif short_code == 'ex':
            print("Bye see you")
            break
            print('-'*40)
        

        else:
            print("Enter valid code to Continue")

    
if __name__ == '__main__':
    main()





