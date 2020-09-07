import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User('Wycliffe','Ronoh')

    def test_init(self):
        
        self.assertEqual(self.new_user.username,'Wycliffe')
        self.assertEqual(self.new_user.password,'Ronoh')
        
    def test_save_user(self):
        
        self.new_user.save_created_credential() 
        self.assertEqual(len(User.user_list),1)  

    def test_save_multiple_user(self):
        self.new_user.save_created_credential()
        test_user = User("Test","user") 
        test_user.save_created_credential()
        self.assertEqual(len(User.user_list),2)

    def tearDown(self):
        
        User.user_list = []

    def delete_user(self):

        User.user_list.remove(self)

    
    def test_delete_contact(self):
        
        self.new_user.save_created_credential()
        test_user = User("Test","user")
        test_user.save_created_credential()

        self.new_user.delete_credential_account()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_username(self):
        
        self.new_user.save_created_credential()
        test_user = User("Test","user")
        test_user.save_created_credential()

        found_user = User.view_my_various_credential_accounts("Test")

        self.assertEqual(found_user.username,test_user.username)
if __name__ == '__main__':
    unittest.main()