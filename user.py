class User:
    user_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def save_created_credential(self):
        User.user_list.append(self)

    def save_existing_credential_accounts(self):
        User.user_list.append(self)

    @classmethod
    def view_my_various_credential_accounts(cls,username):
        for user in cls.user_list:
            if user.username == username:
                return user

    def delete_credential_account(self):
        User.user_list.remove(self)

class Credentials:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_existing_credential_accounts(self):
        User.user_list.append(self)

    @classmethod
    def view_my_various_credential_accounts(cls,username):
        for user in cls.user_list:
            if user.username == username:
                return cls.user_list

    def delete_credential_account(self):
        User.user_list.remove(self)


    
