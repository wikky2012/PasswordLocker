class User:
    user_list = []
    def save_created_credential(self):
        User.user_list.append(self)
        
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_existing_credential_accounts(self):
        User.user_list.append(self)

    @classmethod
    def view_my_various_credential_accounts(cls):
        return cls.user_list

    def delete_credential_account(self):
        User.user_list.remove(self)


    
